#!/usr/bin/env python3
"""Two genuinely coupled material-angle states initialize the original m3 solver.

Only the design-state restart is changed. Each anchor first passes through the
original material-angle pullback. Their normalized fields and even design
parameters are extrapolated, and the original inlet cutoff is reapplied. The
actual nonlinear DN, its Jacobian, original residuals, local guards and every
acceptance gate remain unchanged. This is not a fixed-metric refinement rule.
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
import numpy as np


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def accepted_anchor(rec, path):
    if not rec.get('solver_success'):
        raise ValueError(f'Anchor prefix was not accepted: {path}')
    if not rec['config'].get('actual_nonlinear_tail'):
        raise ValueError(f'Anchor is not a genuine nonlinear coupled state: {path}')
    seam = rec.get('tail_seam', {})
    if not seam.get('tail_converged'):
        raise ValueError(f'Anchor has no accepted actual nonlinear tail: {path}')
    threshold = rec['tail_config']['solveTolerance']
    if not np.isfinite(seam.get('tail_shooting_residual', np.inf)) or seam['tail_shooting_residual'] > threshold:
        raise ValueError(f'Anchor actual tail misses its original gate: {path}')
    checks = rec.get('actual_outer_checks', [])
    if rec.get('dn_solver') == 'outer_actual_inner_affine':
        if not checks or not checks[-1]['inner_success']:
            raise ValueError(f'Anchor has no accepted actual outer check: {path}')
        if checks[-1]['actual_boundary_residual'] > rec['config']['bc_tol']:
            raise ValueError(f'Anchor actual boundary misses its original gate: {path}')


def main():
    p = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--short-bridge', type=Path, required=True)
    p.add_argument('--secant-low', type=Path, required=True)
    a, rest = p.parse_known_args()
    if '--fixed' in rest or '--preserve-restart-mesh' in rest:
        raise ValueError('This secant is a design restart, not a fixed-g or preserved-mesh refinement')
    source = a.source_topic.resolve()
    source_paths = [
        Path(__file__).resolve(), source / 'scripts/db6f-prefix-coupled.py',
        source / 'scripts/950f-prefix-adaptive-chart-bvp-v2.py',
        source / 'scripts/db6f-prefix-flat-profile.py', a.short_bridge.resolve(),
    ]
    c = module('m3_secant_original_coupler', source_paths[1])
    flat = module('m3_secant_original_flat', source_paths[3])
    flat.install(c.adaptive)
    short = module('m3_secant_original_short', a.short_bridge.resolve())
    original_install = c.adaptive.old.install_source

    def install(root):
        original_install(root)
        short.install()
    c.adaptive.old.install_source = install
    out = Path(rest[rest.index('--out-prefix') + 1])
    out.parent.mkdir(parents=True, exist_ok=True)
    runfile = out.with_name(out.name + '-secant-record.json')
    record = dict(scope=__doc__, command=[sys.executable, *sys.argv],
                  source_hashes={str(path): sha(path) for path in source_paths})

    def save():
        runfile.write_text(json.dumps(record, indent=2) + '\n')
    save()
    base_build = c.adaptive.build_classes

    def build(chart):
        Flow, BVP = base_build(chart)
        original_restart = BVP.restart

        def restart(self, path):
            from curve_stable_prefix_bvp import load_checkpoint
            if self.fixed:
                raise ValueError('A design secant cannot be used for a fixed-g refinement')
            hi = load_checkpoint(path)
            lo = load_checkpoint(a.secant_low)
            for rec, anchor in [(hi, path), (lo, a.secant_low)]:
                accepted_anchor(rec, anchor)
                baseline = {k: v for k, v in self.cfg.items() if k != 'delta'}
                current = {k: v for k, v in rec['frozen_profile'].items() if k != 'delta'}
                if current != baseline:
                    raise ValueError('Continuation anchors change non-delta prefix design parameters')
            qh, ql = hi['actual_primary_amplitude'], lo['actual_primary_amplitude']
            if not 0 < ql < qh < self.q:
                raise ValueError('Expected 0 < actual low q < actual high q < target q')
            th, yh, ph = original_restart(self, path)
            tl, yl, pl = original_restart(self, a.secant_low)
            if not np.array_equal(th, tl):
                raise ValueError('Secant target meshes differ after original restarts')
            weight = (self.q - qh) / (qh - ql)
            even_weight = (self.q**2 - qh**2) / (qh**2 - ql**2)
            y = yh + weight * (yh - yl)
            par = ph + even_weight * (ph - pl)
            flow = self.flow(par[0])
            s, _ = self.chart(th, par[0])
            correction = self.initial(par) - y[:, 0]
            cutoff = (flow.Tu if flow.direction == 'outward' else flow.Td) / 2
            y += correction[:, None] * np.maximum(0, 1 - s / cutoff)[None, :]**3
            record['secant'] = dict(
                high=str(Path(path).resolve()), low=str(a.secant_low.resolve()),
                high_sha256=sha(path), low_sha256=sha(a.secant_low),
                high_actual_q=qh, low_actual_q=ql, target_q=self.q,
                normalized_shape_weight=weight, even_design_parameter_weight=even_weight,
                inlet_correction_linf=float(abs(correction).max()), target_nodes=len(th),
                high_modes=hi['config']['modes'], low_modes=lo['config']['modes'],
                target_modes=self.M,
                material_pullback='Each original restart performs its own old-to-new material-angle pullback',
                scope='Initial guess only; accepted anchors do not imply acceptance of this extrapolation',
            )
            save()
            print(json.dumps(dict(event='coupled_material_secant', **record['secant'])), flush=True)
            return th, y, par
        BVP.restart = restart
        return Flow, BVP
    c.adaptive.build_classes = build
    sys.argv = [sys.argv[0], '--source-root', str(source / 'repro/source-root')] + rest
    started = time.monotonic()
    try:
        c.main()
        record['wrapper_returned'] = True
    finally:
        record['seconds'] = time.monotonic() - started
        save()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Re-read every stored finite coefficient and independently replay diagnostics.

This does not repeat Newton or claim a continuous/full-frequency certificate.
It tests that the complete persisted polynomial has the reported diagnostics
and actually meets the original finite collocation and boundary tolerances.
"""
from __future__ import annotations
import argparse
import inspect
import json
import time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.interpolate import PPoly
from flint import ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_fast_jacobian import FastCompactNormalized
from fourfold_codazzi_compact_metric_branch_probe import diagnostic
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--object', type=Path, default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('preserve the original independent review')
    tick = time.monotonic()
    ctx.prec = 192
    ctx.cap = 6
    original = json.loads(args.report.read_text())
    saved = load_candidate(args.candidate)
    meta = json.loads(str(saved['metadata']))
    if (original['candidate_sha256'] != sha(args.candidate)
            or meta['object_sha256'] != sha(args.object)
            or not np.all(np.isfinite(saved['piece_coefficients']))):
        raise ValueError('the complete finite candidate identity is invalid')
    geometry, _ = load_exact_object(args.object, 512)
    body = RotationalBodyTarget(geometry)
    graft = RotationalGraftTarget(geometry, args.object)
    m = int(meta['modes'])
    system = FastCompactNormalized(geometry, m, original['angular_grid'], body, graft)
    system.alpha = float(meta['amplitude'])
    x = saved['radial_nodes']
    # The archived c is the internal PPoly representation, with its original
    # interpolation axis recorded by the producer as axis=1.
    sol = PPoly.construct_fast(saved['piece_coefficients'], x, extrapolate=True, axis=1)
    result = SimpleNamespace(x=x, sol=sol, p=np.array([float(meta['nu'])]))
    actual = diagnostic(system, result)
    exact_diagnostic_match = actual == original['diagnostics']
    y = sol(x)
    h = np.diff(x)
    col, middle, f, fmiddle = bvp.collocation_fun(system.evaluate, y, result.p, x, h)
    rms = bvp.estimate_rms_residuals(system.evaluate, sol, x, h, result.p,
                                  1.5 * col / h, fmiddle)
    qstar = 1 / np.sqrt(1 + (graft.a_endpoint / (4 * graft.omega)) ** 2)
    left, right = y[:, 0], y[:, -1]
    mean = left[m] if meta['mean_boundary'] == 'waist' else right[m]
    boundary = np.r_[left[:m], mean, left[m+1] + 1,
                     right[:m] + qstar * right[m+1:]]
    max_rms = float(np.max(rms))
    max_boundary = float(np.max(abs(boundary)))
    passed = bool(exact_diagnostic_match and actual['valid']
                  and max_rms <= original['tol']
                  and max_boundary <= original['tol'] / 100)
    output = dict(
        kind='independent_complete_saved_finite_Codazzi_candidate_review',
        passed=passed, certified=False,
        source_sha256=sha(__file__),
        inputs={str(p): sha(p) for p in (args.candidate, args.report, args.object)},
        modes=m, radial_nodes=len(x), angular_grid=original['angular_grid'],
        diagnostic_angular_grid=2*original['angular_grid'],
        every_archived_coefficient_loaded=True,
        exact_diagnostic_dictionary_match=exact_diagnostic_match,
        recomputed_diagnostics=actual,
        maximum_relative_collocation_RMS_residual=max_rms,
        maximum_boundary_residual=max_boundary,
        original_relative_tolerance=original['tol'],
        original_boundary_tolerance=original['tol']/100,
        original_reported_finite_success=original['finite_BVP_success'],
        dependencies={name: sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_compact_metric_fast_jacobian.py',
            'fourfold_codazzi_compact_metric_branch_probe.py',
            'fourfold_phase_symmetric_geometry.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py')},
        scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        wall_seconds=time.monotonic()-tick,
        scope='Complete persisted finite polynomial replay only. Full doubled-grid and radial-quarter diagnostics match, and the original finite tolerances are checked again. No nonlinear tail matching, continuous enclosure, infinite-mode PDE existence or closed surface follows.')
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print({key: output[key] for key in ('passed', 'exact_diagnostic_dictionary_match',
          'maximum_relative_collocation_RMS_residual', 'maximum_boundary_residual', 'wall_seconds')}, flush=True)


if __name__ == '__main__':
    main()

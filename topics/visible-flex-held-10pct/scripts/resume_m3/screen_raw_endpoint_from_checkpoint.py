#!/usr/bin/env python3
"""Check a new exact-circle core design using an actual raw checkpoint's controls.

This performs no BVP or tail solve.  It preserves the input's physical q and
control coefficients, changes only the explicitly listed core design settings,
and runs the original complete rho guard.  Sample maxima and the supplementary
interpolation estimate are numerical diagnostics, not interval geometry claims.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np
from couple_m3_smallcut_secant import accepted_anchor


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--control-transition', type=float, action='append')
    p.add_argument('--homotopy', type=float, default=1.)
    p.add_argument('--samples', type=int, default=32768)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.samples < 512 or not 0 <= a.homotopy <= 1:
        raise ValueError('Invalid diagnostic resolution or homotopy')
    r = json.loads(gzip.decompress(a.checkpoint.read_bytes()))
    accepted_anchor(r, a.checkpoint)
    if r.get('core_control_path') != 'raw-mean-primary-compact-v1':
        raise ValueError('Expected a completed actual raw-core checkpoint')
    if r['config']['base_mode'] != 3:
        raise ValueError('This diagnostic is for the m3 physical branch')
    q = float(r['actual_primary_amplitude'])
    c = np.asarray(r['parameters'][1:], float) * np.asarray(r['central_correction_scales'], float)
    if len(c) != r['config']['modes'] - 1:
        raise ValueError('Incomplete actual control vector')
    lib = Path(__file__).with_name('round_raw_lib')
    sys.path.insert(0, str(lib))
    from plateau_core import PlateauSupportCore
    from fixed_large_radius_core import make_core_class
    from tight_moment_interval_bounds import install
    install()
    Core = make_core_class(PlateauSupportCore)
    initial_settings = dict(r['core_round_settings'])
    if initial_settings['bimodal_eta'] != 0 or not initial_settings['lock_fundamental']:
        raise ValueError('Expected the actual eta=0, mean/primary-locked m3 path')
    widths = a.control_transition or [initial_settings['control_transition']]
    x = 2 * np.pi / 3 * np.arange(a.samples) / a.samples
    rows = []
    for width in widths:
        settings = dict(initial_settings, homotopy=a.homotopy, control_transition=width,
                        arc_nodes=4096)
        # The zero-control core is only a background for evaluating the same
        # explicitly defined complete control function if the actual guard fails.
        baseline = Core(q, np.zeros_like(c), 3, **settings)
        jets = baseline.basis.support_jets(x, 2, a.homotopy)
        support = c @ jets[0]
        curvature = c @ (jets[0] + jets[2])
        rho = 1 + q * baseline.unit_rho(x) + curvature
        bounds = baseline.basis.homotopy_rho_bounds(a.homotopy)
        second_bound = float(np.sum(abs(c) * bounds[2]))
        spacing = baseline.T / a.samples
        interpolation_remainder = spacing * spacing * second_bound / 8
        ce = baseline.basis.coefficient_evaluation_error_bounds
        ce_rho = a.homotopy * (ce[0] + ce[2])
        ce_rho += (1 - a.homotopy) * 8 * baseline.basis.fundamental_evaluation_error
        coefficient_error = float(np.sum(abs(c) * ce_rho))
        triangle = float(np.sum(abs(c) * bounds[0]))
        allowance = coefficient_error + 1e-12 * (1 + q * 8 / (1 - baseline.mean_chi) + triangle)
        row = dict(settings=settings, q=q, modes=r['config']['modes'],
                   control_support_sample_linf=float(max(abs(support))),
                   complete_control_rho_sample_linf=float(max(abs(curvature))),
                   complete_rho_sample_min=float(min(rho)),
                   complete_rho_sample_max=float(max(rho)),
                   control_rho_second_derivative_bound=second_bound,
                   control_rho_interpolation_remainder=interpolation_remainder,
                   coefficient_error_allowance=coefficient_error,
                   existing_style_value_allowance=allowance,
                   numerical_control_rho_upper=math.nextafter(float(max(abs(curvature))) +
                       interpolation_remainder + allowance, math.inf),
                   numerical_upper_scope='C2 interpolation formula and certified coefficient derivative bounds, with the existing numerical libm/evaluation allowance; not a new strict interval certificate.')
        try:
            core = Core(q, c, 3, **settings)
        except FloatingPointError as error:
            row.update(original_rho_guard_passed=False, original_rho_guard_error=str(error))
        else:
            geo = core.normal_geometry(x)
            arc = core.center + np.linspace(-core.a, core.a, 1025)
            arc_rho = core.normal_geometry(arc)['rho']
            row.update(original_rho_guard_passed=True, original_rho_lower=core.rho_lower,
                       original_rho_upper=core.rho_upper, original_guard_grid=core.positivity_grid_per_sector,
                       original_core_summary=core.summary(),
                       support_sample_min=float(min(geo['h'])), support_sample_max=float(max(geo['h'])),
                       radius_sample_min=float(np.linalg.norm(geo['F'], axis=1).min()),
                       radius_sample_max=float(np.linalg.norm(geo['F'], axis=1).max()),
                       arc_rho_defect_sample_linf=float(max(abs(arc_rho - (1 + 8 * q)))))
        rows.append(row)
        print(json.dumps({k: row.get(k) for k in (
            'settings', 'original_rho_guard_passed', 'original_rho_guard_error',
            'original_rho_lower', 'complete_control_rho_sample_linf',
            'numerical_control_rho_upper', 'complete_rho_sample_min',
            'arc_rho_defect_sample_linf')}), flush=True)
    result = dict(scope=__doc__, command=sys.argv, input=str(a.checkpoint.resolve()),
                  input_sha256=sha(a.checkpoint), input_core_settings=initial_settings,
                  physical_control_coefficients=c.tolist(), input_profile=r['frozen_profile'],
                  source_sha256={str(f.resolve()): sha(f) for f in
                      [Path(__file__), Path(__file__).with_name('couple_m3_smallcut_secant.py'),
                       *sorted(lib.glob('*.py'))]}, samples_per_sector=a.samples, rows=rows,
                  interpretation='Each row is an explicitly changed physical core initial guess. None is a coupled state, a fixed-g refinement, or a completed exact-circle construction.')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()

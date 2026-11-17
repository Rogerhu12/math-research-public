#!/usr/bin/env python3
"""Read-only primary-width probes using all actual n4 controls and its chart.

Only the baseline width/lambda is the accepted finite checkpoint. Every other
row is a new unsolved core design with those same physical coefficients.
Complete reference-lift reconstruction is checked separately from finite
Fourier tails, which are numerical diagnostics and not uniform error bounds.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def spectral_rows(fields, freq, cutoffs):
    result = {}
    for name, field in fields.items():
        coefficient = np.fft.fft(field, axis=0) / len(freq)
        magnitude = (abs(coefficient) if coefficient.ndim == 1
                     else np.linalg.norm(coefficient, axis=1))
        result[name] = {str(M): float(magnitude[freq > 4 * M + 1].sum())
                        for M in cutoffs}
        result[name]['above_N_over_4'] = float(magnitude[freq > len(freq) // 4].sum())
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-topic', 'checkpoint', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--widths', type=float, nargs='+', default=[.08, .12, .16, .24, .32])
    parser.add_argument('--lambdas', type=float, nargs='+', default=[.02, 1.])
    parser.add_argument('--samples', type=int, default=8192)
    args = parser.parse_args()
    if args.samples < 4096 or args.samples % 4:
        raise ValueError('Use a fine sample count compatible with C4')
    sys.path.insert(0, str(Path(__file__).parent))
    from refine_fixed_raw_n4 import build_seed
    from raw_fixed_core import make_core_class
    from run_large_radius_circle import ReferenceCore
    source = args.source_topic.resolve()
    sys.path[:0] = [str(source / 'notes'),
                    str(source / 'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    from curve_stable_prefix_bvp import load_checkpoint
    rec = load_checkpoint(args.checkpoint)
    M = rec['config']['modes']
    seed = build_seed(source, args.checkpoint, M, rec['config']['angular'])
    obj, par = seed['obj'], seed['par']
    obj.initial(par)
    flow = obj.flow(par[0])
    original = obj._core
    q = obj.support_amplitude
    controls = obj.pscale * par[1:]
    J = seed['core_projection_order']
    Core = make_core_class(ReferenceCore, J)
    N = args.samples
    angle = flow.angular(N)
    psi, u, du, ddu = angle[:4]
    freq = abs(np.rint(np.fft.fftfreq(N) * N).astype(int))
    basis = flow.basis(N)
    projection_samples = max(2048, 128 * M)
    projection_angle = flow.angular(projection_samples)
    projection_basis = flow.basis(projection_samples)[0]
    cutoff = [M, 24, 32, 48]
    started = time.monotonic()
    rows = []
    for lam in args.lambdas:
        for width in args.widths:
            settings = dict(seed['settings'], homotopy=lam, transition=width)
            row = dict(primary_transition=width, homotopy=lam,
                       is_accepted_checkpoint_core=(width == seed['settings']['transition']
                                                    and lam == seed['settings']['homotopy']))
            try:
                core = Core(q, controls, 4, arc_nodes=2048, **settings)
                z = core.evaluate(u)
                exact_jets = [z['F'], z['Ft'] * du[:, None],
                              z['Ftt'] * du[:, None] ** 2 + z['Ft'] * ddu[:, None]]
                perturbations = [exact_jets[k] - angle[4 + k] for k in range(3)]
                projection_core = core.evaluate(projection_angle[1])
                coefficients = flow.project(
                    (projection_core['F'] - projection_angle[4])[None, :, :],
                    projection_basis) / obj.q
                represented = [obj.q * flow.values(coefficients, B)[0] for B in basis]
                omitted = [perturbations[k] - represented[k] for k in range(3)]
                flow.exact_lift_core = core
                flow.exact_lift_initial = coefficients[:, 0]
                flow.exact_lift_cache = {}
                lifted = flow.geo(np.array([0.]), N)
                reconstruction = {name: float(abs(lifted[key][0] + represented[k]
                                                   - exact_jets[k]).max())
                                  for k, (name, key) in enumerate(
                                      [('F', 'pos'), ('F_psi', 'p1'), ('F_psipsi', 'p2')])}
                material = core.evaluate(psi)
                phi_arc = core.center + np.linspace(-core.a, core.a, 129)
                arc = core.normal_geometry(phi_arc)
                normal = np.c_[np.cos(phi_arc), np.sin(phi_arc), np.zeros_like(phi_arc)]
                radius = 1 + q * core._circle_constant
                centers = arc['F'] - radius * normal
                center = centers[len(centers) // 2]
                row.update(
                    success=True, flatten_beta=core.local_flatten_beta,
                    rho_guard_lower=core.rho_lower,
                    rho_sampled_min=core.rho_min_sample,
                    circle_radius_at_lambda_one=radius,
                    arc_rho_defect=float(abs(arc['rho'] - radius).max()),
                    arc_center_variation=float(np.linalg.norm(centers - center, axis=1).max()),
                    center_norm_sample=float(np.linalg.norm(center)),
                    candidate_centrally_symmetric_witness=(
                        float(2 * np.linalg.norm(center) * np.sin(core.a)) if lam == 1 else None),
                    minimum_actual_chart_derivative=float(du.min()),
                    maximum_actual_chart_derivative=float(du.max()),
                    original_core_difference=max(float(abs(original.evaluate(u)[name] - z[name]).max())
                                                 for name in ('F', 'Ft', 'Ftt')),
                    complete_lift_reconstruction=reconstruction,
                    retained_mode=M,
                    unrepresented_reference_jet_max={name: float(np.linalg.norm(omitted[k], axis=1).max())
                                                     for k, name in enumerate(('F', 'F_psi', 'F_psipsi'))},
                    actual_chart_spectrum=spectral_rows(
                        dict(F_perturbation=perturbations[0],
                             F_psi_perturbation=perturbations[1],
                             F_psipsi_perturbation=perturbations[2]), freq, cutoff),
                    material_spectrum=spectral_rows(dict(F_uu=material['Ftt']), freq, cutoff))
            except Exception as exc:
                row.update(success=False, error=repr(exc))
            rows.append(row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
    result = dict(scope=__doc__, command=sys.argv,
                  input_checkpoint_sha256=sha(args.checkpoint),
                  source_sha256={name: sha(Path(__file__).with_name(name)) for name in
                                 ('probe_primary_width_actual_n4.py', 'refine_fixed_raw_n4.py',
                                  'raw_fixed_core.py', 'raw_n4_free_complementary.py',
                                  'raw_n4_complementary.py', 'large_radius_local_core.py',
                                  'second_order_large_radius_core.py', 'exact_core_lift.py',
                                  'bimodal_chart_loader.py')},
                  source_modes=M, all_free_controls=len(controls),
                  raw_anchor_modes=J, actual_q=q, gauge_q=obj.q,
                  eta=seed['eta'], physical_profile=obj.cfg,
                  actual_chart_warp_e=flow.warp_e,
                  original_plateau_settings=seed['settings'], samples=N,
                  actual_inlet_projection_samples=projection_samples,
                  physical_control_sha256=hashlib.sha256(np.asarray(controls, '<f8').tobytes()).hexdigest(),
                  rows=rows, seconds=time.monotonic() - started,
                  interpretation='Candidate scalar witnesses need a complete closed family, common H, global diameter/reach and full error control. The whole core remains in the exact reference lift; a Fourier tail measures representability rather than dropped inlet data. No changed width/lambda row is an accepted BVP.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()

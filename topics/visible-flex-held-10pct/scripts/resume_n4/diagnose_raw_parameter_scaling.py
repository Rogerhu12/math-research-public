#!/usr/bin/env python3
"""Read one actual raw fixed-g state and measure its local parameter directions.

No Newton step, modified core, or acceptance test is performed. The optional
matrix output is a scratch-only reversible local coordinate transformation.
Its reported effect on sampled blocks is not a condition estimate for the
complete collocation Jacobian.
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


def matrix_report(matrix):
    matrix = np.asarray(matrix, float)
    values = np.linalg.svd(matrix, compute_uv=False)
    cols = np.linalg.norm(matrix, axis=0)
    return dict(rows=matrix.shape[0], columns=matrix.shape[1],
                singular_max=float(values[0]), singular_min=float(values[-1]),
                condition_2=float(values[0] / values[-1]),
                column_norm_min=float(cols.min()),
                column_norm_max=float(cols.max()),
                min_column=int(cols.argmin()), max_column=int(cols.argmax()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('loader', 'source-topic', 'checkpoint', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--modes', type=int, required=True)
    parser.add_argument('--angular', type=int, default=1280)
    parser.add_argument('--core-samples', type=int, default=4096)
    parser.add_argument('--transform-out', type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.loader.resolve()))
    from refine_fixed_raw_n4 import build_seed
    from exact_lift_parameter_jac import parameter_jets
    started = time.monotonic()
    seed = build_seed(args.source_topic, args.checkpoint,
                      args.modes, args.angular)
    obj, par, x, y = (seed[k] for k in ('obj', 'par', 'x', 'y'))
    obj.initial(par)
    A, B, P = obj.bc_jac(y[:, 0], y[:, -1], par)
    scales = np.r_[obj.support_amplitude, obj.pscale]
    theta = 2 * np.pi * np.arange(args.core_samples) / args.core_samples
    physical = parameter_jets(obj._core, theta)
    blocks = [np.moveaxis(value * scales[:, None, None] / obj.q, 0, -1)
              .reshape((-1, obj.M)) / np.sqrt(args.core_samples)
              for value in physical]
    core_matrix = np.vstack(blocks)
    # A = U diag(s) Vt. p = p_anchor + T z with T=V diag(1/s)
    # is an explicitly invertible affine parameter re-expression.
    _, singular, vt = np.linalg.svd(core_matrix, full_matrices=False)
    if singular[-1] <= 0:
        raise FloatingPointError('Sampled complete core parameter directions lost rank')
    transform = vt.T / singular[None, :]
    inverse = singular[:, None] * vt
    sites = np.unique(np.r_[np.linspace(0, 1, 15),
                            obj.inverse_chart(np.array([.06, .065, .07, .08]), par[0])])
    physical_s, _ = obj.chart(sites, par[0])
    from scipy.interpolate import PPoly
    cp = seed['record']
    pp = PPoly.construct_fast(np.asarray(cp['pp_coefficients']),
                             np.asarray(cp['mesh']), extrapolate=True, axis=1)
    if cp['config']['modes'] != obj.M:
        # Exact build_seed has already embedded the whole old map. Its smooth
        # coefficient interpolant only supplies read-only diagnostic sites.
        from scipy.interpolate import CubicSpline
        Y = CubicSpline(x, y, axis=1)(sites)
    else:
        Y = pp(physical_s)
    _, PJ = obj.fun_jac(sites, Y, par)
    flow_matrix = np.moveaxis(PJ, 1, -1).reshape((-1, obj.M)) / np.sqrt(len(sites))
    matrices = dict(inlet_parameter=obj._initial_jac,
                    boundary_parameter=P,
                    sampled_complete_core_H2=core_matrix,
                    sampled_parameter_flow=flow_matrix)
    rows = {name: dict(original=matrix_report(matrix),
                       transformed=matrix_report(matrix @ transform))
            for name, matrix in matrices.items()}
    rho_phi = obj._core.rho_material_jets(theta)
    result = dict(scope=__doc__, command=sys.argv,
                  source_sha256=sha(__file__), input_checkpoint_sha256=sha(args.checkpoint),
                  driver_sha256=sha(args.loader / 'refine_fixed_raw_n4.py'),
                  core_driver_sha256=sha(args.loader / 'raw_fixed_core.py'),
                  free_basis_sha256=sha(args.loader / 'raw_n4_free_complementary.py'),
                  exact_parameter_jet_sha256=sha(args.loader / 'exact_lift_parameter_jac.py'),
                  modes=obj.M, input_modes=cp['config']['modes'],
                  angular=obj.nt, core_samples=args.core_samples,
                  sampled_flow_sites=len(sites), physical_profile=obj.cfg,
                  raw_anchor_modes=seed['core_projection_order'],
                  homotopy=seed['settings']['homotopy'],
                  eta=seed['eta'], q_gauge=obj.q, actual_q=obj.support_amplitude,
                  original_correction_scale_min=float(obj.pscale.min()),
                  original_correction_scale_max=float(obj.pscale.max()),
                  physical_parameter_scale_min=float(scales.min()),
                  physical_parameter_scale_max=float(scales.max()),
                  boundary_residual_max=float(abs(obj.bc(y[:, 0], y[:, -1], par)).max()),
                  complete_boundary_matrix=matrix_report(np.hstack((A, B, P))),
                  blocks=rows, transformation=matrix_report(transform),
                  transformation_inverse_error=float(abs(inverse @ transform - np.eye(obj.M)).max()),
                  core_sampled_rho_min=float(rho_phi['rho'].min()),
                  seed_identity={key: seed['diagnostics'][key] for key in
                                 ('complete_core_identity_error', 'complete_map_projection_error')},
                  seconds=time.monotonic() - started,
                  interpretation='The complete core H2 here is the sampled quadratic norm of the full fixed-material F,F_u,F_uu parameter directions, divided by the gauge q. Boundary/flow blocks are partial Jacobian diagnostics only. The transformation has not been used in a solve.')
    if args.transform_out:
        np.savez(args.transform_out, parameter_anchor=par, transform=transform, inverse=inverse)
        result['scratch_transform_sha256'] = sha(args.transform_out)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(modes=obj.M, blocks=rows,
                          output_sha256=sha(args.out)), ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Bounded-memory image screen of a completed actual finite-tail prefix.

The saved physical PPoly, all Fourier modes and full mean height are retained.
The upper prefix and its mirror are still open. Diameter, phase Hausdorff
distances and curvature products are samples, with no continuum error bound;
they establish neither closedness, reach nor the target held displacement.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import inspect
import json
import math
from pathlib import Path
import textwrap
import time
import types
import numpy as np
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint', 'source-topic', 'port', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--radial', type=int, default=241)
    parser.add_argument('--angular', type=int, default=256)
    parser.add_argument('--height-angular', type=int, default=768)
    parser.add_argument('--phases', type=int, default=4)
    parser.add_argument('--batch', type=int, default=8)
    args = parser.parse_args()
    if (min(args.radial, args.angular, args.height_angular, args.phases) < 1
            or args.angular % 2 or not 1 <= args.batch <= 16):
        raise ValueError('Positive samples, even angle count and batch 1..16 required')
    started = time.monotonic()
    helper = HERE/'geometric-checkpoint-core-pullback.py'
    hashes = {str(p): sha(p) for p in (Path(__file__), helper, args.checkpoint, args.port)}
    spec = importlib.util.spec_from_file_location('strong_actual_geometry_pullback', helper)
    pullback = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pullback)
    saved, unused = pullback.load_saved(args.checkpoint, args.source_topic, args.port,
        angular=max(args.angular, args.height_angular))
    rec, flow = saved.rec, saved.flow
    if (not rec.get('solver_success') or rec.get('audit_pending', True)
            or not rec['config'].get('actual_nonlinear_tail') or saved.mode != 2
            or rec['physical_port_sha256'] != hashes[str(args.port)]):
        raise ValueError('An audited actual finite-tail mode-two prefix and its exact port are required')
    if rec['actual_tail']['residual'] > rec['actual_tail']['config']['solveTolerance']:
        raise ValueError('The saved actual tail did not satisfy its original residual gate')
    original = textwrap.dedent(inspect.getsource(flow.height_integral.__func__))
    if original.count('128') != 3:
        raise ValueError('Original independent mean-height batch sites changed')
    transformed = original.replace('128', str(args.batch))
    scope = {'np': np}
    exec(compile(transformed, '<bounded-original-mean-height>', 'exec'), scope)
    mean_height = types.MethodType(scope['height_integral'], flow)
    ss = np.unique(np.r_[np.linspace(0., flow.end, args.radial), flow.breaks, flow.end])
    height = mean_height(saved.sol, ss, args.height_angular, 6)
    basis, unused1, unused2 = flow.basis(args.angular)
    groups = []
    for first in range(0, len(ss), args.batch):
        sl = slice(first, first+args.batch)
        point = flow.geo(ss[sl], args.angular)['pos'] + saved.q*flow.values(saved.sol.sol(ss[sl]), basis)
        point[:, :, 2] += height[sl, None]
        groups.append(point)
    grid = np.concatenate(groups)
    opposite = np.roll(grid, args.angular//2, axis=1)
    symmetry_error = float(np.max(abs(opposite-grid*np.array([-1., -1., 1.]))))
    if symmetry_error > 1e-10*max(1., float(np.max(abs(grid)))):
        raise ValueError('The sampled half-turn symmetry required for the diameter identity failed')
    upper = grid.reshape(-1, 3)
    cloud = np.concatenate((upper, upper*np.array([1., 1., -1.])))
    radius = np.linalg.norm(cloud, axis=1)
    index = int(np.argmax(radius))
    diameter = 2.*float(radius[index])
    tree = cKDTree(cloud)
    phase_rows = []
    for phase in np.linspace(0., math.pi/2, args.phases+1)[1:]:
        c, sn = math.cos(phase), math.sin(phase)
        rotation = np.array([[c, -sn, 0.], [sn, c, 0.], [0., 0., 1.]])
        rotated = cloud@rotation.T
        forward, forward_nearest = tree.query(rotated, workers=1)
        backward, backward_nearest = cKDTree(rotated).query(cloud, workers=1)
        i, j = int(np.argmax(forward)), int(np.argmax(backward))
        distance = float(max(forward[i], backward[j]))
        phase_rows.append(dict(phase=float(phase), hausdorff_sample=distance,
            hausdorff_sample_over_D_sample=distance/diameter,
            forward_witness=rotated[i].tolist(), forward_nearest=cloud[forward_nearest[i]].tolist(),
            backward_witness=cloud[j].tolist(), backward_nearest=rotated[backward_nearest[j]].tolist()))
    core = rec['core']
    core_gap = core.get('phase_pi_over_base_mode_support_gap_lower')
    curvature = float(rec['summary']['kappa_sample'])
    result = dict(scope=__doc__, checkpoint=str(args.checkpoint), source_sha256=hashes,
        actual_primary_amplitude=float(rec['actual_primary_amplitude']),
        representation_gauge=float(saved.q), all_actual_core_coefficients=core['coefficients'],
        modes=saved.M, saved_prefix_angular=rec['config']['angular'],
        radial_samples=len(ss), angular_samples=args.angular,
        height_angular=args.height_angular, height_quadrature_order=6, batch=args.batch,
        target_cloud_points=len(cloud), sample_half_turn_error=symmetry_error,
        diameter_sample=diameter, diameter_sample_witness=cloud[index].tolist(),
        height_max_sample=float(np.max(abs(cloud[:, 2]))),
        saved_curvature_sample=curvature, saved_curvature_times_D_sample=curvature*diameter,
        reciprocal_saved_curvature_D_sample=1./(curvature*diameter),
        physical_metric_l1_sample=rec['summary']['metric_l1'],
        physical_Darboux_l1_sample=rec['summary']['darboux_l1'],
        true_tail_residual=rec['actual_tail']['residual'],
        phases=phase_rows, best_sample=max(phase_rows, key=lambda row: row['hausdorff_sample']),
        planar_core_gap_lower=core_gap,
        planar_core_gap_lower_over_D_sample=None if core_gap is None else core_gap/diameter,
        planar_core_gap_is_not_whole_surface_held=True,
        mean_height_batch_transform=dict(replacements=3, original_batch=128,
            original_sha256=hashlib.sha256(original.encode()).hexdigest(),
            transformed_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
            unchanged_quadrature_and_radial_order=True),
        closed_surface=False, continuous_reach_certificate=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('actual_primary_amplitude',
        'representation_gauge', 'diameter_sample', 'saved_curvature_times_D_sample',
        'best_sample', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Measure full-coefficient amplitude/diameter of a mirrored accepted prefix.

The physical mean uses the original postprocessor's angular/Gauss rule.
Images are compared as point sets, not by parameter displacement. The
mirrored prefix still has two boundary circles; no closed-surface held,
reach, continuous error enclosure, or rigid-motion-free distance is claimed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import inspect
import json
import math
from pathlib import Path
import textwrap
import time
from types import MethodType
import numpy as np
from scipy.spatial import cKDTree


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-topic', 'checkpoint', 'port', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--radial', type=int, default=401)
    parser.add_argument('--angular', type=int, default=512)
    parser.add_argument('--phases', type=int, default=8)
    parser.add_argument('--batch', type=int, default=8)
    parser.add_argument('--include-all-saved-nodes', action='store_true')
    args = parser.parse_args()
    if min(args.radial, args.angular, args.phases, args.batch) < 1:
        raise ValueError('Positive sample counts and batch are required')
    started = time.monotonic()
    path = Path(__file__).with_name('geometric-checkpoint-core-pullback.py')
    spec = importlib.util.spec_from_file_location('strong_amplitude_pullback', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    saved, _ = module.load_saved(args.checkpoint, args.source_topic, args.port,
                                angular=max(256, args.angular))
    if (not saved.rec['solver_success'] or saved.rec.get('audit_pending', True)
            or saved.mode != 2):
        raise ValueError('A fully processed accepted even-frequency prefix is required')
    flow = saved.flow
    original = textwrap.dedent(inspect.getsource(flow.height_integral.__func__))
    edits = [('range(0,len(flat),128)', f'range(0,len(flat),{args.batch})', 1),
             ('first:first+128', f'first:first+{args.batch}', 2)]
    transformed = original
    for old, new, count in edits:
        if transformed.count(old) != count:
            raise ValueError('Original independent mean-batch source changed')
        transformed = transformed.replace(old, new)
    scope = dict(flow.height_integral.__func__.__globals__)
    exec(compile(transformed, '<strong-amplitude-mean-batches>', 'exec'), scope)
    flow.height_integral = MethodType(scope['height_integral'], flow)
    pieces = [np.linspace(0, flow.end, args.radial), np.asarray(flow.breaks),
              np.array([0., flow.end])]
    if args.include_all_saved_nodes:
        pieces.append(saved.sol.x)
    radial = np.unique(np.concatenate(pieces))
    mean_angular = max(512, 16*(3*saved.M+1))
    mean = flow.height_integral(saved.sol, radial, mean_angular, 6)
    basis, _, _ = flow.basis(args.angular)
    upper = np.empty((len(radial), args.angular, 3))
    for first in range(0, len(radial), args.batch):
        block = slice(first, first+args.batch)
        s = radial[block]
        points = flow.geo(s, args.angular)['pos'] + saved.q*flow.values(saved.sol.sol(s), basis)
        points[:, :, 2] += mean[block, None]
        upper[block] = points
    flat = upper.reshape(-1, 3)
    cloud = np.concatenate((flat, flat*np.array([1., 1., -1.])))
    radii = np.linalg.norm(cloud, axis=1)
    imax = int(np.argmax(radii))
    diameter = 2*float(radii[imax])
    tree = cKDTree(cloud)
    rows = []
    for phase in np.linspace(0, math.pi/2, args.phases+1)[1:]:
        c, s = math.cos(phase), math.sin(phase)
        rotation = np.array([[c, -s, 0.], [s, c, 0.], [0., 0., 1.]])
        moved = cloud@rotation.T
        forward, nearest = tree.query(moved, workers=1)
        backward, back_nearest = cKDTree(moved).query(cloud, workers=1)
        i, j = int(forward.argmax()), int(backward.argmax())
        distance = float(max(forward[i], backward[j]))
        rows.append(dict(phase=float(phase), hausdorff_cloud=distance,
                         cloud_ratio=distance/diameter,
                         forward_witness=moved[i].tolist(),
                         forward_nearest=cloud[nearest[i]].tolist(),
                         backward_witness=cloud[j].tolist(),
                         backward_nearest=moved[back_nearest[j]].tolist()))
    coefficients = saved.rec['core']['coefficients']
    gap = 2*sum((Fraction(x) for x in coefficients[::2]), Fraction(0))
    witness = np.array([0., 1+sum(coefficients), 0.])
    nearest_gap, near_index = tree.query(witness)
    result = dict(scope=__doc__, checkpoint=str(args.checkpoint),
                  checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  modes=saved.M, representation_gauge=saved.q,
                  actual_primary=saved.rec['actual_primary_amplitude'],
                  original_mean_rule=dict(angular=mean_angular, Gauss_order=6,
                      independent_batch=args.batch, saved_mesh_preserved=True),
                  radial_samples=len(radial), angular_samples=args.angular,
                  all_saved_nodes_included=args.include_all_saved_nodes,
                  prefix_half_height_sample=float(np.max(abs(flat[:, 2]))),
                  prefix_radius_sample=float(np.max(np.linalg.norm(flat[:, :2], axis=1))),
                  mirrored_prefix_diameter_sample=diameter,
                  diameter_identity='For the continuous double-mirrored even-frequency prefix, central symmetry gives diam(S)=2 sup_{x in S}|x|. The supremum here is only sampled.',
                  diameter_sample_witness=cloud[imax].tolist(),
                  core_axis_support_gap=dict(numerator=str(gap.numerator),
                      denominator=str(gap.denominator), value=float(gap),
                      all_saved_coefficients_used=True),
                  core_axis_gap_over_prefix_diameter_sample=float(gap)/diameter,
                  core_axis_spatial_witness=dict(point=witness.tolist(),
                      nearest_cloud_distance=float(nearest_gap),
                      nearest=cloud[near_index].tolist()),
                  phases=rows, best=max(rows, key=lambda row:row['hausdorff_cloud']),
                  closed_candidate=False, full_tail_or_caps_included=False,
                  continuous_sampling_error_paid=False,
                  held_or_reach_completion_claim=False,
                  seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key:result[key] for key in
          ('modes', 'actual_primary', 'mirrored_prefix_diameter_sample',
           'core_axis_support_gap', 'core_axis_gap_over_prefix_diameter_sample',
           'best', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()

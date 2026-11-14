#!/usr/bin/env python3
"""Directed convex-hull bounds on every original geometry mesh rectangle.

The complete original immutable block chain is consumed. A chosen floating
separation direction is merely an exact dyadic proposal: its norm is then
proved <=1 by directed arithmetic. All vertices, the exact dyadic height
translation, pi/4 witness rotation, fourfold wrap and both reflections are
retained. This mesh certificate alone does not assert a continuous surface.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_phase_beta_bulk_box import Box, arb_box, reduce_box, square_box
from fourfold_phase_root_interval import stack
from fourfold_phase_metric_defect import record

REPORT = '49870375c7397a53b867d67ce94aa8fcd2d86a69bfe7fc3a7f482b9232d30a2e'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
KIND = 'complete_original_geometry_mesh_directed_convex_hulls_v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_sha(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == bytes((31, 139)) else raw)


def save(path, value):
    raw = (json.dumps(value, indent=2, allow_nan=False) + '\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, mtime=0)
    tmp = Path(str(path) + '.partial')
    tmp.write_bytes(raw)
    tmp.replace(path)


def angle_next(value):
    """The last angular neighbour is the true pi/2 world rotation."""
    last = stack([-value[0, 1], value[0, 0], value[0, 2]])
    return Box(np.concatenate((value.lo[1:], last.lo[None]), axis=0),
               np.concatenate((value.hi[1:], last.hi[None]), axis=0))


def shifted(value, height):
    return Box(value) + stack([Box(0.), Box(0.), Box(height)])


def witness_targets(waist, height):
    w = shifted(waist, height)
    c = arb_box(arb(2).sqrt() / 2)
    w = stack([c * (w[0] - w[1]), c * (w[0] + w[1]), w[2]])
    targets = []
    for _ in range(4):
        targets.append(w)
        targets.append(stack([w[0], w[1], -w[2]]))
        w = stack([w[1], -w[0], w[2]])
    return stack(targets)


def separating_distance(vertices, targets):
    """One proved unit-ball covector for each quad and witness image."""
    centre = np.mean(vertices.lo / 2 + vertices.hi / 2, axis=1)
    proposed_w = targets.lo / 2 + targets.hi / 2
    direction = proposed_w[None, :, :] - centre[:, None, :]
    if not np.all(np.isfinite(direction)):
        raise ValueError('nonfinite dyadic separation proposal')
    sq = reduce_box(square_box(Box(direction)), 2)
    # sqrt is only a proposal. The following directed square comparison
    # proves the actual norm inequality independently of its rounding.
    denominator = np.nextafter(np.sqrt(sq.hi), np.inf)
    denominator = np.where(sq.hi == 0., 1., denominator)
    for _ in range(8):
        bad = square_box(Box(denominator)).lo < sq.hi
        if not np.any(bad):
            break
        denominator = np.where(bad, np.nextafter(denominator, np.inf), denominator)
    if np.any(square_box(Box(denominator)).lo < sq.hi):
        raise ValueError('the proposed separating norm was not proved')
    normal = Box(direction) / Box(denominator[:, :, None])
    lower = np.full((vertices.lo.shape[0], targets.lo.shape[0]), np.inf)
    for v in range(4):
        difference = targets.reshape(1, 8, 3) - vertices[:, v, :].reshape(-1, 1, 3)
        dot = reduce_box(normal * difference, 2)
        lower = np.minimum(lower, dot.lo)
    index = np.unravel_index(np.argmin(lower), lower.shape)
    return arb(float(lower[index])).lower(), list(map(int, index))


def cell_bounds(outer, inner, targets, height):
    f0, f1 = shifted(outer[:, :3], height), shifted(inner[:, :3], height)
    n0, n1 = Box(outer[:, 3:6]), Box(inner[:, 3:6])
    F = stack([f0, angle_next(f0), f1, angle_next(f1)], 1)
    N = stack([n0, angle_next(n0), n1, angle_next(n1)], 1)
    squared = reduce_box(square_box(F), 2)
    radius = arb(float(np.max(squared.hi))).sqrt().upper()
    # Independent component hulls enclose both bilinear fields. This
    # pays all cross-vertex dot products instead of using endpoint dots.
    fbox = Box(np.min(F.lo, axis=1), np.max(F.hi, axis=1))
    nbox = Box(np.min(N.lo, axis=1), np.max(N.hi, axis=1))
    support = arb(float(np.min(reduce_box(fbox * nbox, 1).lo))).lower()
    distance, where = separating_distance(F, targets)
    zmin = arb(float(np.min(F.lo[:, :, 2]))).lower()
    return dict(vertex_radius_upper=record(radius),
                bilinear_frame_support_lower=record(support),
                convex_hull_witness_distance_lower=record(distance),
                minimum_vertex_height=record(zmin),
                distance_min_at_angle_and_target=where)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--geometry-report', type=Path, required=True)
    ap.add_argument('--geometry-blocks', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--max-blocks', type=int, default=141)
    ap.add_argument('--resume', action='store_true')
    args = ap.parse_args()
    if args.out.exists() != args.resume:
        raise FileExistsError('use a new output or explicit same-identity resume')
    start = time.monotonic()
    ctx.prec = 192
    ctx.cap = 6
    if sha(args.geometry_report) != REPORT or sha(args.candidate) != CANDIDATE:
        raise ValueError('the actual original geometry and complete candidate are required')
    original = load(args.geometry_report)
    gi = original['identity']
    if not original['complete'] or original['failure'] is not None or gi['angles'] != 512:
        raise ValueError('all original geometry blocks and angle nodes are required')
    saved = load_candidate(args.candidate)
    nodes = np.asarray(saved['radial_nodes'])
    radii = np.unique(np.r_[np.linspace(0., 25/8, int(np.ceil((25/8)/gi['max_requested_step']))+1),
                            nodes, .05, .18, .25, 3.])
    if len(radii) != 8967 or array_sha(radii) != gi['radial_grid_sha256']:
        raise ValueError('the original exact dyadic radial grid changed')
    paths = sorted(args.geometry_blocks.glob('block-*.npz'))
    if len(paths) != 141 or [x.name for x in paths] != [f'block-{i:06d}.npz' for i in range(141)]:
        raise ValueError('the complete immutable block chain is required')
    height = float(original['global_sampled_geometry']['common_world_height_translation'])
    with np.load(paths[-1], allow_pickle=False) as z:
        if int(z['indices'][-1]) != 0:
            raise ValueError('the complete final waist row is missing')
        waist = z['geometry'][-1, 0, :3].copy()
    targets = witness_targets(waist, height)
    identity = dict(source_sha256=sha(__file__), geometry_report_sha256=REPORT,
        candidate_sha256=CANDIDATE, original_chain_sha256=original['last_complete_block_sha256'],
        radial_grid_sha256=gi['radial_grid_sha256'], exact_height_translation=str(Fraction.from_float(height)),
        exact_witness='Rz(pi/4) times original dyadic waist vertex plus the exact common height translation',
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_candidate_shards.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_root_interval.py','fourfold_phase_metric_defect.py')})
    original_identity = json.dumps(gi, sort_keys=True, separators=(',', ':'), allow_nan=False)
    if args.resume:
        doc = load(args.out)
        if doc['identity'] != identity or doc['complete'] or doc['failure'] is not None:
            raise ValueError('only the same successful partial mesh consumer can resume')
        done = doc['complete_blocks']
        previous = doc['last_complete_block_sha256']
        elapsed = doc['wall_seconds']
        with np.load(paths[done-1], allow_pickle=False) as z:
            outer = z['geometry'][-1].copy()
            expected = int(z['indices'][-1]) - 1
        doc['resume_history'].append(done)
    else:
        done, previous, elapsed, outer, expected = 0, '', 0., None, 8966
        doc = dict(kind=KIND, identity=identity, complete=False, failure=None,
            complete_blocks=0, total_blocks=141, total_radial_cells=8966,
            angular_cells_per_quadrant=512, inverse_witness_images=8,
            rows=[], block_checks=[], resume_history=[], wall_seconds=0.,
            exact_original_vertices_and_translation_retained=True,
            all_four_quarter_rotations_and_both_reflections=True,
            true_fourfold_angular_wrap=True,
            directed_separating_norm_proved=True,
            radial_integration_error_included=False,
            continuous_angular_error_included=False,
            real_tail_caps_or_markers_included=False,
            nonlinear_solution_or_final_surface_geometry_proved=False)
        save(args.out, doc)
    try:
        for block in range(done, min(len(paths), done + args.max_blocks)):
            path = paths[block]
            with np.load(path, allow_pickle=False) as z:
                indices, points = z['indices'].copy(), z['geometry'].copy()
                if str(z['identity']) != original_identity or str(z['previous_block_sha256']) != previous:
                    raise ValueError('the original geometry chain or identity changed')
                if (points.shape != (len(indices), 512, 12) or
                    not np.array_equal(indices, np.arange(expected, expected-len(indices), -1)) or
                    not np.all(np.isfinite(points))):
                    raise ValueError('a complete original block is missing or nonfinite')
                for j, index in enumerate(indices):
                    index = int(index)
                    if outer is not None:
                        bounds = cell_bounds(outer, points[j], targets, height)
                        doc['rows'].append(dict(radial_index=index,
                            interval=[str(Fraction.from_float(float(radii[index]))),
                                      str(Fraction.from_float(float(radii[index+1])))],
                            **bounds))
                    outer = points[j]
                expected = int(indices[-1]) - 1
            previous = sha(path)
            doc['block_checks'].append(dict(block=block, file=path.name, sha256=previous))
            doc['complete_blocks'] = block+1
            doc['last_complete_block_sha256'] = previous
            doc['complete'] = block+1 == len(paths)
            if doc['complete']:
                if expected != -1 or len(doc['rows']) != 8966 or previous != identity['original_chain_sha256']:
                    raise ValueError('the complete original mesh was not consumed')
                from fourfold_codazzi_rotational_cap_jacobi import box_from_record
                def bounds_of(key):
                    return [box_from_record(x[key]) for x in doc['rows']]
                doc['global_mesh_bounds'] = dict(
                    vertex_radius_upper=record(max(bounds_of('vertex_radius_upper')).upper()),
                    bilinear_frame_support_lower=record(min(bounds_of('bilinear_frame_support_lower')).lower()),
                    convex_hull_witness_distance_lower=record(min(bounds_of('convex_hull_witness_distance_lower')).lower()))
            doc['wall_seconds'] = elapsed + time.monotonic() - start
            save(args.out, doc)
            print(dict(complete_blocks=block+1, total=141, radial_cells=len(doc['rows']),
                       last_radial_index=expected+1, wall_seconds=doc['wall_seconds']), flush=True)
    except Exception as error:
        doc['complete'] = False
        doc['failure'] = dict(type=type(error).__name__, message=str(error))
        doc['wall_seconds'] = elapsed + time.monotonic() - start
        save(args.out, doc)
        raise
    if doc['complete']:
        print(json.dumps(dict(complete=True, bounds=doc['global_mesh_bounds'],
                              seconds=doc['wall_seconds'])), flush=True)


if __name__ == '__main__':
    main()

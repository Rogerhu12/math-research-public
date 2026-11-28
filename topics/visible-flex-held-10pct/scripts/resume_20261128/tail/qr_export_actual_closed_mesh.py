#!/usr/bin/env python3
"""Export small meshes of a genuine lambda-one complete-prefix-QR full map, never a certificate.

The original accepted source, complete unscaled tail bundle and (when used)
actual coupled endpoint remain authoritative. Every saved mode is evaluated;
the finite mesh sampling is only a visualization of that map. Binary PLY uses
double coordinates so that a small fixed cap is not deliberately rounded to
single precision. No mesh or other reproducible array belongs in the source
repository. The held frame requires the real lambda-one circular core.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
TAIL = HERE.parent/'tail'
ANALYTIC = HERE.parent/'analytic'
sys.path[:0] = [str(TAIL), str(HERE), str(SCRIPTS/'resume_20261126'), str(ANALYTIC)]
import material_circle_phase_contract as phase_api
from qr_actual_closed_map import ActualClosedMapV2, rotation, circle
from seam_export_tail_geometry_v2 import checked, ref, sha, bind_height, validate_packet_states
from seam_cut_height_compatibility import load_packet
from seam_tail_spectrum_v2 import canonical_contract, degree_argument
from verify_complete_tail_radius_identity import require_unscaled, complete_height_bytes

LIMIT = 5_000_000
REVIEWED_MAP_SHA = '57b39a97d9d5abcd3ae7dfb17697addb67a8094efba375996ea268a44068d92b'
REVIEWED_MESH = ANALYTIC/'chord_export_actual_closed_mesh.py'
REVIEWED_MESH_SHA = '3ab5594ad5098df5db1300b7add42a2ee1bf9c44540cc9b18e11b6c36d8dde7e'


def save(path, record):
    temporary = Path(str(path)+'.tmp')
    temporary.write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def validate_actual_tail(bundle):
    """Re-execute the original packet/scope/height gates, without a solver."""
    checked(bundle['accepted_packet'])
    checked(bundle['source_port'])
    background = SCRIPTS.parent/'notes/2026-11-20-m3-m24-warm050-execution.json'
    packet, _, _, spacing, modes, _ = load_packet(
        Path(bundle['accepted_packet']['path']), Path(bundle['source_port']['path']), background)
    spectrum = checked(bundle['spectrum_contract'])
    canonical_contract(spectrum)
    if (spectrum != bundle['spectrum'] or spectrum['finite_scope'] != bundle['finite_scope']
            or validate_packet_states(packet, modes, spacing, degree_argument(spectrum)) != spectrum):
        raise ValueError('The mesh input lost the original accepted complete tail spectrum')
    identity = bundle['height_identity']
    require_unscaled(identity)
    checked(identity['reference'])
    if bind_height(packet, Path(identity['reference']['path']), identity['reference_key'],
                   identity['factor'], identity['original_arithmetic']) != identity:
        raise ValueError('The original full-height packet no longer matches its actual reference')
    return packet, modes, background


def ring_parameters(model, prefix_intervals, tail_intervals, disk_intervals):
    """One center ring, then upper rings; the lower half reverses this list."""
    ell, end = model.cylinder_half_length, model.end
    upper = [('prefix', 0.)]
    if ell:
        upper.extend(('prefix', z) for z in (ell/2, ell))
    u = np.unique(np.r_[np.linspace(0., end, prefix_intervals+1),
                        model.prefix.center_width, .75*end,
                        end-model.prefix.end_lift.width, end])
    upper.extend(('prefix', ell+float(s)) for s in u if 0 < s <= end)
    radii = np.unique(np.r_[np.geomspace(model.a, model.Rcut, tail_intervals+1),
                            model.a, float(model.cap.inner), float(model.cap.deep)])
    upper.extend(('tail', float(r)) for r in radii[::-1] if model.a < r < model.Rcut)
    disk = np.unique(np.r_[np.linspace(0., model.a, disk_intervals+1),
                           model.marker_radius, model.marker_radius/2, model.a])
    upper.extend(('tail', float(r)) for r in disk[::-1] if r > 0.)
    # A single exact topological vertex represents each pole. No duplicate
    # ring is introduced at a prefix/tail, cylinder or disk join.
    lower = [(kind, coordinate, -1) for kind, coordinate in upper[:0:-1]]
    return lower+[(kind, coordinate, 1) for kind, coordinate in upper]


def ring_positions(model, kind, coordinate, side, theta, phase):
    """Vector evaluation of the same position formulas as the frozen reader."""
    theta = np.asarray(theta, float)
    ell = model.cylinder_half_length
    if kind == 'prefix':
        s = coordinate
        if ell and s <= ell:
            points = model.prefix.core.evaluate(theta-phase)['F'].copy()
            points[:, 2] = s
        else:
            u = max(0., s-ell)
            psi = model.phase_chart.inverse(u, theta-phase)
            points = model.prefix.evaluate([u], psi)[0][0].copy()
            points[:, 2] += ell
        points = rotation(points, phase)
        points[:, 2] *= side
        return points
    radius = coordinate
    if radius <= model.a:
        points = radius*circle(theta)
        values = [model.marker(float(x), float(y))[0] for x, y in points[:, :2]]
        points[:, 2] = side*(model.Zcap+ell+np.asarray(values))
        return points
    phi = theta-phase
    actual_r, _, _ = model.target.perturbation_radius(radius)
    coefficients = model.cap.coefficients(actual_r)[0]
    points = radius*circle(phi)+model.cap.fourier(coefficients, phi)*np.asarray([1., 1., -1.])
    points[:, 2] += (model.target.zcut+model.target.mean+
                     model.background.sample(radius)['heightFromRToCut']+ell)
    points = rotation(points, phase)
    points[:, 2] *= side
    return points


def transform(points, phase, frame):
    if frame is None:
        return points
    center, curvature = frame
    # This evaluates R54's real expression. The displayed center and binary
    # coordinates are numerical evaluations, not new defining constants.
    return rotation(points, -(1-curvature)*phase)+center-rotation(center, curvature*phase)


def faces_for_rings(rings, angular):
    j = np.arange(angular, dtype=np.int32)
    jp = (j+1) % angular
    parts = [np.stack((np.zeros(angular, np.int32), 1+jp, 1+j), axis=1)]
    for ring in range(rings-1):
        a, b = 1+ring*angular+j, 1+(ring+1)*angular+j
        ap, bp = 1+ring*angular+jp, 1+(ring+1)*angular+jp
        parts.extend((np.stack((a, ap, b), axis=1), np.stack((ap, bp, b), axis=1)))
    top = 1+rings*angular
    a, ap = 1+(rings-1)*angular+j, 1+(rings-1)*angular+jp
    parts.append(np.stack((a, ap, np.full(angular, top, np.int32)), axis=1))
    faces = np.concatenate(parts)
    edges = np.concatenate((faces[:, [0, 1]], faces[:, [1, 2]], faces[:, [2, 0]]))
    unoriented = np.sort(edges, axis=1)
    unique, inverse, counts = np.unique(unoriented, axis=0, return_inverse=True, return_counts=True)
    balance = np.bincount(inverse, weights=np.where(edges[:, 0] < edges[:, 1], 1, -1))
    vertices = top+1
    if not (np.all(counts == 2) and np.all(balance == 0)
            and vertices-len(unique)+len(faces) == 2 and len(faces) == 2*vertices-4):
        raise ArithmeticError('The generated ring topology is not the declared closed oriented sphere')
    return faces, dict(vertices=vertices, faces=len(faces), edges=len(unique),
        euler_characteristic=2, every_edge_has_two_oppositely_oriented_faces=True,
        connected_by_explicit_ring_chain_and_two_pole_fans=True,
        geometric_embedding_proved=False)


def write_ply(path, vertices, faces, label):
    header = ('ply\nformat binary_little_endian 1.0\n'
        'comment Actual full-field finite-map visualization; no metric or embedding certificate\n'
        f'comment {label}\nelement vertex {len(vertices)}\n'
        'property double x\nproperty double y\nproperty double z\n'
        f'element face {len(faces)}\nproperty list uchar int vertex_indices\nend_header\n').encode()
    records = np.empty(len(faces), dtype=np.dtype([('count', 'u1'), ('vertices', '<i4', (3,))]))
    records['count'] = 3
    records['vertices'] = faces
    size = len(header)+vertices.size*8+records.nbytes
    if not size < LIMIT:
        raise ValueError(f'The requested complete mesh is {size} bytes; use a coarser visualization grid')
    with path.open('xb') as stream:
        stream.write(header)
        stream.write(np.asarray(vertices, dtype='<f8').tobytes())
        stream.write(records.tobytes())
    if path.stat().st_size != size:
        raise IOError('The mesh file length differs from its complete data contract')
    return dict(**ref(path), bytes=size, coordinates='binary-little-endian-float64',
                triangles='binary-little-endian-uint8-count-plus-int32-indices')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run', 'geometry-bundle', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--coupling-summary', type=Path, required=True)
    parser.add_argument('--frame', choices=('held', 'phase'), default='held')
    parser.add_argument('--cylinder-half-length', type=float, choices=(.0025, .005), default=.0025)
    parser.add_argument('--angular', type=int, default=256)
    parser.add_argument('--prefix-intervals', type=int, default=56)
    parser.add_argument('--tail-intervals', type=int, default=28)
    parser.add_argument('--disk-intervals', type=int, default=8)
    parser.add_argument('--times', nargs='+', default=['0', '1/4', '1/2', '3/4', '1'])
    parser.add_argument('--cut-width', type=float, default=.04)
    parser.add_argument('--phase-end', type=Q, required=True)
    parser.add_argument('--held-width', type=Q, default=Q(27,50))
    args = parser.parse_args()
    phase_end, held_width = args.phase_end, args.held_width
    if phase_end <= 0 or held_width <= 0:
        raise ValueError('Use positive exact phase-end and held-width')
    if sha(REVIEWED_MESH) != REVIEWED_MESH_SHA:
        raise ValueError('The inherited full spectrum/topology mesh source changed')
    out = args.outdir.resolve()
    repo = SCRIPTS.parents[2]
    if out == repo or repo in out.parents:
        raise ValueError('Reproducible meshes and evaluation arrays must remain outside the repository')
    if (args.angular < 16 or args.angular % 2 or args.prefix_intervals < 4
            or args.tail_intervals < 4 or args.disk_intervals < 4):
        raise ValueError('Use an even angular grid and at least four intervals per region')
    times = [Q(value) for value in args.times]
    if not times or len(set(times)) != len(times) or any(not 0 <= t <= 1 for t in times):
        raise ValueError('Use distinct exact rational times in [0,1]')
    if sha(HERE/'qr_actual_closed_map.py') != REVIEWED_MAP_SHA:
        raise ValueError('The frozen complete-map implementation changed; review a new export entry')
    bundle = checked(ref(args.geometry_bundle))
    packet, modes, background_record = validate_actual_tail(bundle)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    model = ActualClosedMapV2(args.source_run, args.geometry_bundle, out/'verified-node-index.json',
        cylinder_half_length=args.cylinder_half_length, cut_width=args.cut_width,
        canonical_r67_marker=True, coupling_summary=args.coupling_summary)
    report = dict(status='evaluating_actual_complete_map_meshes', source=ref(__file__),
        source_run=ref(args.source_run), geometry_bundle=ref(args.geometry_bundle),
        coupling_summary=ref(args.coupling_summary) if args.coupling_summary else None,
        source_kind=('actual_lambda_one_qr_chord_final_physical_height' if args.coupling_summary
                     else 'original_design_raw_candidate_height'),
        actual_coupling_provenance=getattr(model.prefix, 'actual_coupling_provenance', None),
        source_homotopy=model.record['core_settings']['homotopy'],
        all_saved_modes_evaluated=True, Fourier_field_truncated=False,
        mesh_discretization_is_not_a_continuous_certificate=True,
        metric_certified=False, reach_certified=False, held_set_certified=False,
        euclidean_noncongruence_certified=False, completion_criteria_passed=False,
        frame=args.frame, phase_definition=f'alpha(t)=({phase_end})*t, exact real expression',
        cylinder_half_length=args.cylinder_half_length, cut_width=args.cut_width,
        canonical_marker_metadata=model.r67_marker.metadata(), files=[])
    try:
        report.update(explicit_phase_contract=phase_api.describe(model,phase_end,held_width),
            phase_contract_source=ref(Path(phase_api.__file__)),
            inherited_full_mesh_source=ref(REVIEWED_MESH),
            old_7a_source_kind_claimed=False)
        expected_height = (model.record['raw_return']['candidate_H'] if model.coupling_binding is None
                           else model.coupling_binding['candidate_H'])
        expected_bytes = complete_height_bytes(expected_height, modes)
        if any(complete_height_bytes(height, modes) != expected_bytes for height in (
                packet['request']['height'], packet['response']['checkpoint']['cutHeight'])):
            raise ValueError('The full mesh tail differs from the literal final source height')
        frame = phase_api.held_frame(model,phase_end,held_width,circle) if args.frame == 'held' else None
        report['held_frame_definition'] = ('R_(-(1-k)*alpha) G_alpha+O-R_(k*alpha) O; '
            'k is the actual exact core curvature and O its true arc center' if frame else None)
        report['held_frame_evaluation_only'] = (dict(center=frame[0].tolist(),
            literal_core_curvature_exact=str(Q(frame[1]))) if frame else None)
        rings = ring_parameters(model, args.prefix_intervals, args.tail_intervals, args.disk_intervals)
        faces, topology = faces_for_rings(len(rings), args.angular)
        report.update(topology=topology, angular_vertices_per_ring=args.angular,
            ring_count=len(rings), ring_parameters=rings,
            visualization_samples_do_not_bound_unresolved_spatial_frequencies=True)
        if 24*topology['vertices']+13*topology['faces']+1024 >= LIMIT:
            raise ValueError('This visualization grid cannot fit in a strict 5 MB file')
        theta = 2*np.pi*np.arange(args.angular)/args.angular
        reference_error = 0.
        for index, t in enumerate(times):
            phase = float(phase_end*t)
            values = [model.disk_jets(0., 0., -1)[0][None, :]]
            for kind, coordinate, side in rings:
                points = ring_positions(model, kind, coordinate, side, theta, phase)
                # Three actual reader comparisons per ring guard the vector
                # position adapter. This is not a continuous error estimate.
                for j in (0, args.angular//3, args.angular-1):
                    exact_reader = (model.prefix_jets(side*coordinate, theta[j], phase)[0]
                        if kind == 'prefix' else model.tail_jets(coordinate, theta[j], side, phase)[0])
                    reference_error = max(reference_error, float(np.max(abs(points[j]-exact_reader))))
                values.append(points)
            values.append(model.disk_jets(0., 0., 1)[0][None, :])
            vertices = transform(np.concatenate(values), phase, frame)
            if not np.all(np.isfinite(vertices)) or reference_error > 2e-12:
                raise ArithmeticError('The mesh position adapter differs from the actual frozen reader')
            normals = np.cross(vertices[faces[:, 1]]-vertices[faces[:, 0]],
                               vertices[faces[:, 2]]-vertices[faces[:, 0]])
            area2 = np.linalg.norm(normals, axis=1)
            if not np.all(np.isfinite(area2)) or np.any(area2 == 0):
                raise ArithmeticError('The sampled mesh has a nonfinite or zero-area triangle')
            record = write_ply(out/f'closed-t{index:02d}.ply', vertices, faces,
                               f't={t}; alpha=({phase_end})*t; frame={args.frame}')
            record.update(t_exact=str(t), phase_exact=str(phase_end*t),
                          minimum_double_triangle_area_sampled=float(np.min(area2)))
            report['files'].append(record)
            report.update(maximum_vector_vs_reader_position_difference=reference_error,
                          seconds=time.monotonic()-started)
            save(out/'summary.json', report)
            print(json.dumps(dict(mesh=index, t=str(t), bytes=record['bytes'],
                                  seconds=report['seconds'])), flush=True)
        sources = [Path(__file__), REVIEWED_MESH, Path(phase_api.__file__),
                   HERE/'qr_actual_closed_map.py',
                   HERE/'qr_actual_coupled_prefix.py',
            TAIL/'actual_cartesian_prefix.py',
            TAIL/'universal_threefold_marker.py',
            HERE.parent/'analytic/verify_complete_tail_radius_identity.py',
            SCRIPTS/'resume_20261126/seam_cut_height_compatibility.py',
            SCRIPTS/'resume_20261126/seam_export_tail_geometry_v2.py',
            SCRIPTS/'resume_20261126/seam_tail_spectrum_v2.py', background_record,
            SCRIPTS/'finite_closure/m3_m8_closed_map/closed_m3_map.py',
            SCRIPTS/'finite_closure/m3_m8_closed_map/phase_angle_chart.py']
        report.update(status='actual_finite_closed_map_meshes_exported',
            source_hashes={str(p):sha(p) for p in sources},
            full_node_check=ref(out/'verified-node-index.json'),
            every_file_strictly_below_5_million_bytes=True,
            seconds=time.monotonic()-started,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(out/'summary.json', report)
    finally:
        model.close()


if __name__ == '__main__':
    main()

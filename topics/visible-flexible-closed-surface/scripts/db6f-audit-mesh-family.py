#!/usr/bin/env python3
"""Read the three serialized PLYs and check their common material indexing.

The separate interval PLY reports certify PL embedding. This check binds
those reports and verifies identical faces and exact fixed-cap vertices.
The phase comparison is a floating-point diagnostic, not an error bound
for the underlying continuous maps.
"""
import argparse
from fractions import Fraction as Q
import importlib.util
import json
import math
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('mesh_family_reader', HERE/'db6f-audit-closed-mesh.py')
reader = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = reader
spec.loader.exec_module(reader)
check, sha = reader.check, reader.sha


def locate(path):
    path = Path(path)
    if not path.exists():
        path = HERE.parent/'notes'/path.name
    check(path.exists(), 'Missing bound input '+str(path))
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    data = json.loads(args.manifest.read_text())
    plan_path = locate(data['plan']['file'])
    check(sha(plan_path) == data['plan']['sha256'], 'Changed sampling plan')
    plan = json.loads(plan_path.read_text())
    mask_path = locate(data['fixed_vertex_indices_file']['file'])
    check(sha(mask_path) == data['fixed_vertex_indices_file']['sha256'], 'Changed fixed-vertex mask')
    mask = np.load(mask_path, allow_pickle=False)['fixed']
    angular, rings = int(plan['angular_nodes']), int(plan['rings'])
    upper_fixed = [row['kind'] == 'cap' or row.get('cuff', False) for row in plan['upper_rings']]
    expected = np.r_[True, np.repeat(upper_fixed[1:][::-1]+upper_fixed, angular), True]
    check(mask.dtype == np.dtype(bool) and np.array_equal(mask, expected), 'Fixed mask differs from the geometric plan')
    check([row['time_exact'] for row in data['mesh_files']] == ['0', '1/4', '1/2'], 'Unexpected output times')
    base, base_faces = None, None
    results = []
    for row in data['mesh_files']:
        path = locate(row['file'])
        check(sha(path) == row['sha256'], 'Changed serialized mesh')
        vertices, faces, raw_size, stored_size = reader.read_ply(path)
        check(len(vertices) == plan['vertices'] and len(faces) == plan['faces'], 'Changed mesh sizes')
        check(raw_size == row['uncompressed_bytes'] and stored_size == row['stored_bytes'], 'Changed byte counts')
        stem = path.name.replace('.ply.gz', '').replace('.ply', '')
        audit_path = path.parent/(stem+'-audit.json')
        audit = json.loads(audit_path.read_text())
        check(audit['status'] == 'PASS-closed-oriented-manifold-and-radial-PL-embedding'
              and audit['mesh_sha256'] == sha(path)
              and audit['script_sha256'] == sha(HERE/'db6f-audit-closed-mesh.py'), 'Missing matching PL certificate')
        if base is None:
            base, base_faces = vertices.copy(), faces.copy()
        check(np.array_equal(faces, base_faces), 'Different face connectivity across times')
        check(np.array_equal(vertices[mask].view(np.uint64), base[mask].view(np.uint64)),
              'Serialized fixed cap coordinates are not bitwise identical')
        t = Q(row['time_exact'])
        shift = angular*t/3
        check(shift.denominator == 1 and int(shift) == row['material_grid_shift'], 'Incorrect material shift')
        moved = np.roll(base[1:-1].reshape(rings, angular, 3), int(shift), axis=1).copy()
        alpha = 2*math.pi*float(t)/3
        co, si = math.cos(alpha), math.sin(alpha)
        x, y = moved[..., 0].copy(), moved[..., 1].copy()
        moved[..., 0], moved[..., 1] = co*x-si*y, si*x+co*y
        expected_vertices = np.concatenate([base[:1], moved.reshape(-1, 3), base[-1:]])
        expected_vertices[mask] = base[mask]
        discrepancy = float(np.max(np.abs(expected_vertices-vertices)))
        check(discrepancy < 1e-13, 'Serialized active-band phase fails the numeric material-grid check')
        results.append(dict(mesh=str(path), mesh_sha256=sha(path),
                            PL_report=str(audit_path), PL_report_sha256=sha(audit_path),
                            time_exact=str(t), phase_discrepancy_diagnostic=discrepancy))
    result = dict(status='PASS-three-serialized-closed-meshes-and-fixed-caps', scope=__doc__,
        script_sha256=sha(__file__), manifest=str(args.manifest), manifest_sha256=sha(args.manifest),
        plan_sha256=sha(plan_path), fixed_mask_sha256=sha(mask_path),
        mesh_reader_sha256=sha(HERE/'db6f-audit-closed-mesh.py'),
        fixed_vertices=int(mask.sum()), common_face_connectivity=True,
        serialized_fixed_cap_coordinates_bitwise_identical=True, files=results,
        fixed_g_convergence_gate_5_paid=False, continuous_vertex_error_certified=False)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], files=len(results), fixed_vertices=int(mask.sum()))))


if __name__ == '__main__':
    main()

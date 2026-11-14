#!/usr/bin/env python3
"""Verify the separately completed three PLY reruns and reread fixed caps."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT/'notes'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    script = ROOT/'scripts/db6f-audit-closed-mesh.py'
    spec = importlib.util.spec_from_file_location('root_mesh_file_reader', script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    manifest_path = NOTES/'2026-11-09-db6f-visible-m8-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    mask_record = manifest['fixed_vertex_indices_file']
    mask_path = ROOT/mask_record['file']
    assert sha(mask_path) == mask_record['sha256']
    mask_archive = np.load(mask_path, allow_pickle=False)
    assert mask_archive.files == ['fixed']
    fixed = mask_archive['fixed']
    assert fixed.dtype == np.bool_ and fixed.shape == (67250,)
    assert np.count_nonzero(fixed) == 4610
    keys = ['status', 'mesh_sha256', 'script_sha256', 'interval_backend_sha256',
            'uncompressed_bytes', 'stored_bytes', 'topology', 'geometric_certificate',
            'continuous_surface_C2_metric_reach_certified_here',
            'approximation_error_to_continuous_map_certified_here',
            'fixed_g_convergence_gate_5_paid']
    vertices, faces, items = [], [], []
    for name, row in zip(['t0', 't1of4', 't1of2'], manifest['mesh_files'], strict=True):
        mesh = ROOT/row['file']
        assert sha(mesh) == row['sha256']
        author_path = NOTES/f'2026-11-09-db6f-visible-m8-{name}-audit.json'
        replay_path = NOTES/f'2026-11-09-db6f-root-replay-visible-m8-{name}.json'
        author = json.loads(author_path.read_text())
        replay = json.loads(replay_path.read_text())
        assert all(author[key] == replay[key] for key in keys)
        assert replay['script_sha256'] == sha(script)
        assert replay['mesh_sha256'] == sha(mesh)
        vv, ff, uncompressed, stored = module.read_ply(mesh)
        assert uncompressed == row['uncompressed_bytes'] and stored == row['stored_bytes']
        vertices.append(vv)
        faces.append(ff)
        items.append(dict(time=row['time_exact'], mesh_sha256=sha(mesh),
                          author_report_sha256=sha(author_path),
                          independent_replay_file=str(replay_path.relative_to(ROOT)),
                          independent_replay_sha256=sha(replay_path),
                          mathematical_fields_identical=True))
    assert all(np.array_equal(faces[0], ff) for ff in faces[1:])
    assert all(np.array_equal(vertices[0][fixed].view(np.uint64),
                              vv[fixed].view(np.uint64)) for vv in vertices[1:])
    report = dict(
        status='PASS-independent-three-PLY-rerun-and-file-comparison',
        manifest_sha256=sha(manifest_path), validator_sha256=sha(script),
        review_script_sha256=sha(Path(__file__)), meshes=items,
        all_faces_identical_across_times=True,
        fixed_vertices_bitwise_identical_across_times=True, fixed_vertex_count=4610,
        scope='Independent full validator runs each completed with actual exit 0. '
              'This script verifies the saved mathematical reports and rereads PLY files. '
              'Export-source review and continuous approximation error remain separate.',
        continuous_approximation_error_certified=False, README_complete=False)
    output = NOTES/'2026-11-09-db6f-root-review-visible-m8-replays.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], meshes=len(items),
                          fixed_vertices=4610, report_sha256=sha(output))))


if __name__ == '__main__':
    main()

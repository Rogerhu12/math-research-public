#!/usr/bin/env python3
"""Validate an indexed binary PLY and certify its radial PL embedding.

The vertices in the file are exact binary64 inputs to the interval checks.
This proves a property of the exported piecewise-linear mesh, not a new
metric, curvature, C2 or convergence certificate for the continuous map.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('closed_mesh_intervals', HERE/'db6f-audit-continuous-hermite.py')
iv = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = iv
spec.loader.exec_module(iv)


def check(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_ply(path):
    payload = Path(path).read_bytes()
    check(len(payload) < 5_000_000, 'Compressed mesh file exceeds the limit')
    raw = gzip.decompress(payload) if payload[:2] == b'\x1f\x8b' else payload
    check(len(raw) < 5_000_000, 'Uncompressed PLY exceeds the limit')
    end = raw.find(b'end_header\n')
    check(0 <= end < 100_000, 'Missing or excessive PLY header')
    offset = end+len(b'end_header\n')
    lines = raw[:offset].decode('ascii').splitlines()
    check(lines[:2] == ['ply', 'format binary_little_endian 1.0'], 'Unexpected PLY format')
    meaningful = [line for line in lines[2:] if not line.startswith('comment ')]
    check(len(meaningful) == 7, 'Unexpected element or property in PLY')
    mv = re.fullmatch(r'element vertex (\d+)', meaningful[0])
    mf = re.fullmatch(r'element face (\d+)', meaningful[4])
    check(mv is not None and mf is not None, 'Missing element counts')
    nv, nf = int(mv.group(1)), int(mf.group(1))
    check(meaningful[1:4] == ['property double x', 'property double y', 'property double z']
          and meaningful[5:] == ['property list uchar int vertex_indices', 'end_header'],
          'Unsupported vertex or face representation')
    check(3 < nv < 2**31 and nf > 0 and 24*nv+13*nf+offset == len(raw), 'PLY payload size mismatch')
    vertices = np.frombuffer(raw, dtype='<f8', count=3*nv, offset=offset).reshape(nv, 3)
    face_dtype = np.dtype([('count', 'u1'), ('indices', '<i4', (3,))], align=False)
    records = np.frombuffer(raw, dtype=face_dtype, count=nf, offset=offset+24*nv)
    check(np.all(records['count'] == 3), 'A face is not triangular')
    return vertices, np.ascontiguousarray(records['indices']), len(raw), len(payload)


def topology(vertices, faces):
    nv, nf = len(vertices), len(faces)
    check(np.isfinite(vertices).all(), 'Nonfinite vertex')
    check(np.all((0 <= faces) & (faces < nv)), 'Invalid vertex index')
    check(np.all((faces[:, 0] != faces[:, 1]) & (faces[:, 1] != faces[:, 2])
                 & (faces[:, 2] != faces[:, 0])), 'Repeated corner in a face')
    check(len(np.unique(np.sort(faces, axis=1), axis=0)) == nf, 'Duplicate face')
    origin = faces.reshape(-1).astype(np.int64)
    destination = np.roll(faces, -1, axis=1).reshape(-1).astype(np.int64)
    key = np.minimum(origin, destination)*nv+np.maximum(origin, destination)
    order = np.argsort(key, kind='stable')
    check(len(order) % 2 == 0, 'Odd number of halfedges')
    first, second = order[0::2], order[1::2]
    check(np.array_equal(key[first], key[second]), 'Boundary edge or unmatched edge')
    check(np.all(np.diff(key[first]) > 0), 'An edge has more than two incident faces')
    check(np.array_equal(origin[first], destination[second])
          and np.array_equal(destination[first], origin[second]), 'Edge orientations do not oppose')
    opposite = np.empty(len(order), dtype=np.int64)
    opposite[first], opposite[second] = second, first
    index = np.arange(len(order), dtype=np.int64)
    successor = 3*(index//3)+(index+1) % 3
    rotation = successor[opposite]
    check(np.array_equal(origin[rotation], origin), 'Invalid vertex-link rotation')
    visited = np.zeros(len(order), dtype=bool)
    vertex_seen = np.zeros(nv, dtype=bool)
    valence = np.zeros(nv, dtype=np.int64)
    for start in range(len(order)):
        if visited[start]:
            continue
        vertex = origin[start]
        check(not vertex_seen[vertex], 'A vertex link has multiple cycles')
        vertex_seen[vertex] = True
        current, count = start, 0
        while True:
            check(not visited[current], 'A vertex-link walk merged into another cycle')
            visited[current] = True
            count += 1
            current = int(rotation[current])
            if current == start:
                break
        check(count >= 3, 'A vertex link has fewer than three edges')
        valence[vertex] = count
    check(np.all(vertex_seen), 'Isolated vertex')
    adjacent = opposite.reshape(nf, 3)//3
    face_seen = np.zeros(nf, dtype=bool)
    pending = [0]
    face_seen[0] = True
    while pending:
        current = pending.pop()
        for other in adjacent[current]:
            if not face_seen[other]:
                face_seen[other] = True
                pending.append(int(other))
    check(np.all(face_seen), 'Mesh has multiple connected components')
    edges = len(order)//2
    check(nv-edges+nf == 2, 'Euler characteristic differs from two')
    return dict(vertices=nv, edges=edges, faces=nf, euler_characteristic=2,
                connected=True, all_edges_exactly_twice_and_oppositely_oriented=True,
                every_vertex_link_one_cycle=True, duplicate_faces=0, boundary_edges=0,
                minimum_valence=int(valence.min()), maximum_valence=int(valence.max()))


def geometric_embedding(vertices, faces, batch):
    I = iv.I
    low, high, volume_low, volume_high = Q(0), Q(0), Q(0), Q(0)
    minimum_det, minimum_dot, maximum_q = float('inf'), float('inf'), 0.
    for start in range(0, len(faces), batch):
        index = faces[start:start+batch]
        a, b, c = [I(vertices[index[:, k]]) for k in range(3)]
        det = iv.dot(a, iv.cross(b, c))
        ab, bc, ca = iv.dot(a, b), iv.dot(b, c), iv.dot(c, a)
        check(np.all(det.lo > 0), 'A face is degenerate or fails strict outward radial orientation')
        check(np.all(ab.lo > 0) and np.all(bc.lo > 0) and np.all(ca.lo > 0),
              'A triangle edge does not lie in the required common hemisphere')
        na, nb, nc = iv.norm(a), iv.norm(b), iv.norm(c)
        denominator = na*nb*nc+ab*nc+bc*na+ca*nb
        check(np.all(denominator.lo > 0), 'Solid-angle denominator is not strictly positive')
        q = det/denominator
        lower, upper = 2*(q-q*q*q/3), 2*q
        check(np.isfinite(lower.lo).all() and np.isfinite(upper.hi).all(), 'Nonfinite angle enclosure')
        for x in lower.lo:
            low += Q(float(x))
        for x in upper.hi:
            high += Q(float(x))
        for x in det.lo:
            volume_low += Q(float(x))/6
        for x in det.hi:
            volume_high += Q(float(x))/6
        minimum_det = min(minimum_det, float(det.lo.min()))
        minimum_dot = min(minimum_dot, float(ab.lo.min()), float(bc.lo.min()), float(ca.lo.min()))
        maximum_q = max(maximum_q, float(q.hi.max()))
    check(low > Q(44, 7) and high < Q(18), 'The spherical-area interval does not isolate degree one')
    check(volume_low > 0, 'Signed volume is not strictly positive')
    return dict(
        all_exact_binary_faces_strictly_radially_outward=True,
        minimum_face_determinant_lower=minimum_det,
        minimum_adjacent_vertex_dot_lower=minimum_dot,
        maximum_solid_angle_half_tangent_upper=maximum_q,
        spherical_area_interval_exact=[str(low), str(high)],
        spherical_area_interval_outward=[float(iv.qbounds(low).lo), float(iv.qbounds(high).hi)],
        signed_volume_interval_exact=[str(volume_low), str(volume_high)],
        signed_volume_interval_outward=[float(iv.qbounds(volume_low).lo), float(iv.qbounds(volume_high).hi)],
        degree_one_isolated_by_rational_comparison=True,
        radial_projection_homeomorphism=True, piecewise_linear_mesh_embedded=True,
        proof='Positive face orientation and single-cycle vertex links give positive local degree. '
              'The solid-angle sum is 4*pi times integer degree; 44/7<L<=sum<=U<18 '
              'and 3<pi<22/7 isolate degree one, excluding branching and multiple preimages.')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mesh', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--batch', type=int, default=2048)
    args = ap.parse_args()
    check(args.batch > 0, 'Positive batch size required')
    started = time.monotonic()
    source_sha = sha(__file__)
    vertices, faces, uncompressed, compressed = read_ply(args.mesh)
    report = dict(status='PASS-closed-oriented-manifold-and-radial-PL-embedding', scope=__doc__,
        mesh=str(args.mesh), mesh_sha256=sha(args.mesh), script_sha256=source_sha,
        interval_backend_sha256=sha(HERE/'db6f-audit-continuous-hermite.py'),
        uncompressed_bytes=uncompressed, stored_bytes=compressed,
        topology=topology(vertices, faces), geometric_certificate=geometric_embedding(vertices, faces, args.batch),
        continuous_surface_C2_metric_reach_certified_here=False,
        approximation_error_to_continuous_map_certified_here=False,
        fixed_g_convergence_gate_5_paid=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'], vertices=len(vertices), faces=len(faces),
        stored_bytes=compressed, radial_degree=1, seconds=report['seconds'])))


if __name__ == '__main__':
    main()

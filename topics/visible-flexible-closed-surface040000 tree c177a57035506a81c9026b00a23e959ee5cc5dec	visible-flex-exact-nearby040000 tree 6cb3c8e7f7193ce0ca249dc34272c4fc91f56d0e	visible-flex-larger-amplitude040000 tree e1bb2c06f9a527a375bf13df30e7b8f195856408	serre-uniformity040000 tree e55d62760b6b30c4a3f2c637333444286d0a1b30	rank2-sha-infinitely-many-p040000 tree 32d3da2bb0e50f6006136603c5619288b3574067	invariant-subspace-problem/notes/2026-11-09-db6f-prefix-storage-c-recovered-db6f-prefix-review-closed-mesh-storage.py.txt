#!/usr/bin/env python3
"""Independent small-component and byte-replay review of the frozen G7 exporter.

This supplements the separate full discrete topology checker. The geometric
meaning is a numerical sampling of the already identified continuous map.
No new isometry/reach or rigorous per-vertex approximation error is claimed.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
EXPORTER_SHA = "d776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def resolve(name):
    p = Path(name)
    return p if p.exists() else TOPIC / "notes" / p.name


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def read_ply(path):
    packed = Path(path).read_bytes()
    raw = gzip.decompress(packed) if packed[:2] == b"\x1f\x8b" else packed
    marker = b"end_header\n"
    stop = raw.index(marker) + len(marker)
    header = raw[:stop].decode("ascii").splitlines()
    assert "format binary_little_endian 1.0" in header
    assert all("property double " + key in header for key in ["x", "y", "z"])
    nv = int(next(line for line in header if line.startswith("element vertex ")).split()[-1])
    nf = int(next(line for line in header if line.startswith("element face ")).split()[-1])
    assert "property list uchar int vertex_indices" in header
    assert len(raw) == stop + 24 * nv + 13 * nf
    vertices = np.frombuffer(raw, dtype="<f8", count=3 * nv, offset=stop).reshape(nv, 3)
    records = np.frombuffer(raw, dtype=np.dtype([("count", "u1"), ("indices", "<i4", (3,))]),
                            count=nf, offset=stop + 24 * nv)
    assert np.all(records["count"] == 3)
    return vertices, records["indices"], len(raw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--replay-manifest", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    assert not args.out.exists()
    exporter_path = HERE / "db6f-prefix-export-closed-mesh-storage.py"
    assert sha(exporter_path) == EXPORTER_SHA
    exporter = module("independent_mesh_exporter", exporter_path)
    manifest = json.loads(args.manifest.read_text())
    replay = json.loads(args.replay_manifest.read_text())
    plan_path = resolve(manifest["plan"]["file"])
    assert sha(plan_path) == manifest["plan"]["sha256"] == replay["plan"]["sha256"]
    plan = json.loads(plan_path.read_text())
    geometry_path = resolve(manifest["geometry"]["file"])
    assert sha(geometry_path) == manifest["geometry"]["sha256"]
    metadata = json.loads(geometry_path.read_text())
    assert manifest["diagnostics"] == replay["diagnostics"]
    assert manifest["source_sha256"] == replay["source_sha256"]

    # Independent exact-power evaluation of the already reviewed spline,
    # followed by independent monotone bisection of Theta.
    supplier = module("independent_mesh_spline", HERE / "db6f-prefix-metric-supplier-storage.py")
    prefix = SimpleNamespace(meta=metadata, x=np.array([0., plan["prefix_end"]]))
    us = [row["coordinate"] for row in plan["upper_rings"] if row["kind"] == "prefix"]
    actual_e = exporter.exact_chart_values(prefix, supplier, us)
    knots, coefficients = supplier.exact_clamped_spline(metadata["chart"])
    expected_e = []
    end = Q(float(plan["prefix_end"]))
    for u in us:
        x = Q(float(u)) / end
        j = max(i for i, knot in enumerate(knots[:-1]) if knot <= x)
        value = sum((coefficient * (x - knots[j])**k
                     for k, coefficient in enumerate(coefficients[j])), Q(0))
        if x > Q(3, 4):
            t = 4 * x - 3
            value *= 1 - 10*t**3 + 15*t**4 - 6*t**5
        expected_e.append(float(8 * Q(float(metadata["warp_reference_q"])) * value))
    assert np.array_equal(actual_e, expected_e)
    angular = int(plan["angular_nodes"])
    theta = 2 * math.pi * np.arange(angular) / angular
    computed, inverse_residual, iterations = exporter.invert_material_angle(theta, actual_e)
    e = actual_e[:, None]
    angles = np.broadcast_to(theta[None, :], computed.shape)
    left, right = angles - np.abs(e)/3, angles + np.abs(e)/3
    for _ in range(70):
        mid = (left + right) / 2
        value = mid - e * np.sin(3*mid)/3 - angles
        left = np.where(value < 0, mid, left)
        right = np.where(value >= 0, mid, right)
    reference = (left + right) / 2
    inverse_difference = float(np.max(np.abs(computed - reference)))
    assert inverse_difference < 3e-13

    mask_path = resolve(manifest["fixed_vertex_indices_file"]["file"])
    assert sha(mask_path) == manifest["fixed_vertex_indices_file"]["sha256"]
    mask = np.load(mask_path, allow_pickle=False)["fixed"]
    layout = plan["upper_rings"]
    ucount = len(layout)
    rcount = 2 * ucount - 1
    fixed_upper = np.array([row["kind"] == "cap" or bool(row.get("cuff"))
                            for row in layout], dtype=bool)
    fixed_rings = np.r_[fixed_upper[1:][::-1], fixed_upper]
    expected_mask = np.r_[True, np.repeat(fixed_rings, angular), True]
    assert np.array_equal(mask, expected_mask)
    meshes, files = [], []
    for original, rerun in zip(manifest["mesh_files"], replay["mesh_files"]):
        op, rp = resolve(original["file"]), resolve(rerun["file"])
        assert sha(op) == original["sha256"] == sha(rp) == rerun["sha256"]
        vertices, faces, raw_bytes = read_ply(op)
        assert vertices.shape == (plan["vertices"], 3)
        assert faces.shape == (plan["faces"], 3)
        assert np.isfinite(vertices).all()
        assert raw_bytes < 5_000_000 and op.stat().st_size < 5_000_000
        assert raw_bytes <= 1_000_000 or op.suffix == ".gz"
        assert faces.min() >= 0 and faces.max() < len(vertices)
        meshes.append((vertices, faces))
        files.append({"file": str(op), "sha256": sha(op), "byte_identical_replay": True})
    assert len(meshes) == 3
    zero, faces = meshes[0]
    zero_rings = zero[1:-1].reshape(rcount, angular, 3)
    phase_error = 0.
    for item, (vertices, other_faces) in zip(manifest["mesh_files"], meshes):
        assert np.array_equal(faces, other_faces)
        assert np.array_equal(zero[mask], vertices[mask])
        t = Q(item["time_exact"])
        shift = Q(angular) * t / 3
        assert shift.denominator == 1
        index = (np.arange(angular) - int(shift)) % angular
        selected = zero_rings[:, index, :]
        expected = selected.copy()
        rotated = (selected[..., 0] + 1j*selected[..., 1]) * np.exp(2j*math.pi*float(t)/3)
        expected[..., 0], expected[..., 1] = rotated.real, rotated.imag
        expected[fixed_rings] = zero_rings[fixed_rings]
        current = vertices[1:-1].reshape(rcount, angular, 3)
        phase_error = max(phase_error, float(np.max(np.abs(expected - current))))
    assert phase_error < 5e-15

    # The lower side is the complete Z reflection except its flat cap.
    mirror_xy_error, mirror_height_error, cap_error = 0., 0., 0.
    cap_height = manifest["diagnostics"]["fixed_cap_height_approx"]
    for j in range(1, ucount):
        lower, upper = zero_rings[ucount-1-j], zero_rings[ucount-1+j]
        mirror_xy_error = max(mirror_xy_error, float(np.max(np.abs(lower[:, :2]-upper[:, :2]))))
        if layout[j]["kind"] != "cap":
            mirror_height_error = max(mirror_height_error, float(np.max(np.abs(lower[:, 2]+upper[:, 2]))))
        else:
            assert np.all(lower[:, 2] == -cap_height)
        if fixed_upper[j]:
            a, radius, height = 2/25, 3/100, 1/2000
            expected_z = np.full(angular, cap_height)
            for center in [(a, 0.), (-a/2, a*math.sqrt(3)/2), (-a/2, -a*math.sqrt(3)/2)]:
                distance2 = np.sum((upper[:, :2] - center)**2, axis=1)
                expected_z += height * np.maximum(0., 1-distance2/radius**2)**3
            cap_error = max(cap_error, float(np.max(np.abs(expected_z-upper[:, 2]))))
    assert mirror_xy_error == 0. and mirror_height_error == 0. and cap_error < 2e-15
    assert zero[0, 2] == -cap_height and zero[-1, 2] == cap_height

    # Independent combinatorial checks of the pole and strip orientation.
    for j in range(angular):
        k = (j+1) % angular
        assert tuple(faces[j]) == (0, 1+k, 1+j)
        last = 1+(rcount-1)*angular
        assert tuple(faces[-angular+j]) == (last+j, last+k, len(zero)-1)
    for ring in [0, ucount-2, ucount-1, rcount-2]:
        offset = angular + 2*angular*ring
        low, high = 1+ring*angular, 1+(ring+1)*angular
        for j in [0, angular//3, angular-1]:
            k = (j+1) % angular
            assert tuple(faces[offset+2*j]) == (low+j, low+k, high+j)
            assert tuple(faces[offset+2*j+1]) == (low+k, high+k, high+j)

    report = {
        "status": "PASS-frozen-exporter-static-review-and-actual-independent-byte-replay",
        "reviewer": "/root/coupled_prefix explicit storage-interface adaptation",
        "scope": "Numerical mesh sampling, material chart, exact phase grid permutation, complete Z reflection, cap formula and face orientation. Separate topology validator supplies its full edge/component checks. No continuous map, isometry, reach or rigorous vertex error claim is added.",
        "script_sha256": sha(__file__),
        "exporter_sha256": EXPORTER_SHA,
        "manifest": {"file": str(args.manifest), "sha256": sha(args.manifest)},
        "replay_manifest": {"file": str(args.replay_manifest), "sha256": sha(args.replay_manifest)},
        "plan": {"file": str(plan_path), "sha256": sha(plan_path)},
        "mesh_files": files,
        "exact_chart_power_checks": len(us),
        "material_angle_queries": int(computed.size),
        "maximum_inverse_difference_against_independent_bisection": inverse_difference,
        "maximum_inverse_residual_approx": inverse_residual,
        "newton_iterations": iterations,
        "maximum_phase_coordinate_difference_approx": phase_error,
        "full_mirror_xy_difference": mirror_xy_error,
        "full_mirror_z_difference_excluding_upper_cap_bumps": mirror_height_error,
        "maximum_cap_formula_difference_approx": cap_error,
        "fixed_vertices_bitwise_identical": True,
        "pole_and_representative_strip_orientation_checks": True,
        "replay_diagnostics_identical": True,
    }
    args.out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["status", "material_angle_queries",
          "maximum_inverse_difference_against_independent_bisection",
          "maximum_phase_coordinate_difference_approx"]}))


if __name__ == "__main__":
    main()

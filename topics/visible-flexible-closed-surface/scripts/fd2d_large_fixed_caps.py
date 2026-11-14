#!/usr/bin/env python3
"""R111 fixed caps: exact parameter checks and optional reference cap mesh.

The proved C2 body is the compactly mollified-distance parallel body in R111.
The optional mesh uses (P0 + B_R) - epsilon e_z, within 2*epsilon of that
body before triangulation. It is an OPEN fixed cap, not a solved active
closed flexible surface. Mesh discretization error is not certified here.
No BVP, physical tail, or existing production input is changed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import json
import math
from pathlib import Path
import struct

import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull


R = Q(1, 10)
LAM = Q(1, 40)
A_NECK = Q(11, 50)
A_CUFF = Q(8, 25)
EPS = Q(1, 10000)
DELTA = Q(1, 1000000)
A_BASE = Q(21, 50) + 2 * DELTA
H_SIDE = Q(89, 125)
L_SIDE = Q(573, 500)
Z_TOP = Q(1349, 1000)
RHO_GLUE = Q(9, 100)
R_BALL = Q(29, 20)
VARIANT = "diameter2p9"
E_LOWER = Q(37, 725)


def configure_variant(name: str) -> None:
    """Select one of the two complete fixed-cap geometries proved in R111."""
    global R, LAM, H_SIDE, L_SIDE, Z_TOP, RHO_GLUE, R_BALL, VARIANT, E_LOWER
    VARIANT = name
    if name == "diameter3":
        R = Q(91, 1000)
        LAM = Q(1, 100)
        H_SIDE = Q(4, 5)
        L_SIDE = Q(5, 4) - R
        Z_TOP = Q(1499, 1000) - R
        RHO_GLUE = R
        R_BALL = Q(3, 2)
        E_LOWER = Q(503, 10000)


def ratio(q: Q) -> dict:
    return {"fraction": str(q), "float": float(q)}


def neck_height() -> tuple[float, float, float]:
    integral, quadrature_error = quad(
        lambda t: math.sqrt(max(0.0, math.sin(t))),
        0.0, math.pi, epsabs=2e-14, epsrel=2e-14, limit=200,
    )
    d = 2 * float(R) + float(LAM * R) * integral
    z_cuff = float(H_SIDE - EPS - R) - d
    return d, z_cuff, float(LAM * R) * quadrature_error


def summary() -> dict:
    d, z_cuff, qerr = neck_height()
    neck_min = A_NECK - R * (1 + 2 * LAM)
    ball_margin = (R_BALL - R - EPS) ** 2 - L_SIDE ** 2 - H_SIDE ** 2
    square_margin = (R_BALL - R - EPS) ** 2 - 2 * A_BASE ** 2 - H_SIDE ** 2
    top_margin = R_BALL - (Z_TOP + R + EPS)
    width_margin = Q(3, 4) - (A_BASE + R + EPS)
    body_bottom = H_SIDE - EPS - R
    z_cuff_lower = body_bottom - 2 * R - LAM * R * Q(22, 7)
    z_cuff_upper = body_bottom - 2 * R - 2 * LAM * R
    assert neck_min > R
    assert ball_margin > 0 and square_margin > 0 and top_margin > 0
    assert width_margin > 0 and body_bottom > Q(3, 5)
    assert A_BASE - DELTA > A_NECK + R
    assert A_NECK + RHO_GLUE < A_CUFF
    assert 2 * Q(2, 5) > 2 * RHO_GLUE
    return {
        "theorem": "R111",
        "variant": VARIANT,
        "status": "proved_fixed_C2_caps_and_conditional_grafting",
        "complete_problem_solution": False,
        "missing_input": "same-metric short n2 active closed core in |z|<=z_cuff",
        "parameters": {k: ratio(v) for k, v in {
            "R": R, "lambda": LAM, "neck_radius": A_NECK,
            "cuff_radius": A_CUFF, "epsilon": EPS, "mollifier_radius": DELTA,
            "base_square_halfwidth": A_BASE, "side_height": H_SIDE,
            "side_seed_radius": L_SIDE, "top_seed_height": Z_TOP,
        }.items()},
        "exact_bounds": {k: ratio(v) for k, v in {
            "minimum_neck_radius": neck_min,
            "body_bottom_height": body_bottom,
            "body_halfwidth_x_upper": A_BASE + R + EPS,
            "side_ball_squared_margin": ball_margin,
            "square_ball_squared_margin": square_margin,
            "top_ball_margin": top_margin,
            "wide_slab_margin": width_margin,
            "fixed_marker_error_upper": EPS,
            "plane_completion_reach_lower": R,
            "grafted_reach_lower_if_active_input": RHO_GLUE,
            "held_over_D_lower_if_active_input": Q(3, 5) / (2 * R_BALL),
            "delta_E_over_D_strict_lower_if_active_input": E_LOWER,
            "reach_over_D_lower_if_active_input": RHO_GLUE / (2 * R_BALL),
            "cuff_height_strict_lower": z_cuff_lower,
            "cuff_height_upper": z_cuff_upper,
            "reference_body_Hausdorff_error_before_meshing": 2 * EPS,
        }.items()},
        "quadrature_readings_not_certificates": {
            "neck_height": d, "cuff_height": z_cuff,
            "scipy_reported_absolute_error": qerr,
            "cuff_height_proved_interval": [float(z_cuff_lower), float(z_cuff_upper)],
        },
        "mesh_warning": "open cap only; reference C1,1 convex body; mesh error additional and unbounded here",
    }


def source_polytope() -> tuple[np.ndarray, ConvexHull]:
    aa, hh, ll, zz = map(float, (A_BASE, H_SIDE, L_SIDE, Z_TOP))
    vertices = np.array([
        [aa, aa, hh], [-aa, aa, hh], [-aa, -aa, hh], [aa, -aa, hh],
        [0., ll, hh], [0., -ll, hh], [0., 0., zz],
    ], dtype=float)
    return vertices, ConvexHull(vertices)


def distance_to_polytope(points: np.ndarray, vertices: np.ndarray,
                         hull: ConvexHull) -> np.ndarray:
    """Distance to a convex polytope through all triangular hull faces."""
    eq = hull.equations
    inside = np.max(points @ eq[:, :3].T + eq[:, 3], axis=1) <= 0.
    best = np.full(len(points), np.inf)
    for indices in hull.simplices:
        a, b, c = vertices[indices]
        ab, ac = b - a, c - a
        w = points - a
        aa, bb, cc = ab @ ab, ab @ ac, ac @ ac
        wa, wc = w @ ab, w @ ac
        denom = aa * cc - bb * bb
        u = (cc * wa - bb * wc) / denom
        v = (aa * wc - bb * wa) / denom
        projected = a + u[:, None] * ab + v[:, None] * ac
        d2 = np.einsum("ij,ij->i", points - projected, points - projected)
        projected_inside = (u >= 0.) & (v >= 0.) & (u + v <= 1.)
        candidate = np.where(projected_inside, d2, np.inf)
        for p, q in ((a, b), (b, c), (c, a)):
            edge = q - p
            t = np.clip(((points - p) @ edge) / (edge @ edge), 0., 1.)
            delta = points - p - t[:, None] * edge
            candidate = np.minimum(candidate, np.einsum("ij,ij->i", delta, delta))
        best = np.minimum(best, candidate)
    best[inside] = 0.
    return np.sqrt(np.maximum(best, 0.))


def reference_mesh(n_azimuth: int, n_body: int, n_neck: int) -> tuple[np.ndarray, np.ndarray]:
    """One upper reference cap, with a single outer boundary circle."""
    if min(n_azimuth, n_body, n_neck) < 8:
        raise ValueError("at least eight samples in each direction")
    vertices0, hull = source_polytope()
    d, z_cuff, _ = neck_height()
    rr, aa, ac = map(float, (R, A_NECK, A_CUFF))
    z_bottom = float(H_SIDE - EPS - R)
    center = np.array([0., 0., float((H_SIDE + Z_TOP) / 2 - EPS)])
    phi_end = math.pi - math.atan2(aa, center[2] - z_bottom)
    az = np.arange(n_azimuth) * (2 * math.pi / n_azimuth)
    ca, sa = np.cos(az), np.sin(az)
    phis = np.linspace(0., phi_end, n_body + 1)[1:]
    dirs = np.array([
        np.column_stack((math.sin(p) * ca, math.sin(p) * sa,
                         np.full(n_azimuth, math.cos(p)))) for p in phis
    ]).reshape(-1, 3)
    lo = np.zeros(len(dirs))
    hi = np.full(len(dirs), 3.)
    translated_center = center + np.array([0., 0., float(EPS)])
    for _ in range(48):
        mid = (lo + hi) * .5
        trial = translated_center + mid[:, None] * dirs
        outside = distance_to_polytope(trial, vertices0, hull) > rr
        hi = np.where(outside, mid, hi)
        lo = np.where(outside, lo, mid)
    body_rings = (center + ((lo + hi) * .5)[:, None] * dirs).reshape(n_body, n_azimuth, 3)
    # The final ring is known exactly and matches the upper neck ring.
    body_rings[-1, :, :] = np.column_stack((aa * ca, aa * sa, np.full(n_azimuth, z_bottom)))
    rings = list(body_rings)
    # Squared endpoint clustering follows the C2 arc-length endpoint behavior.
    u = np.linspace(0., 1., n_neck + 1)[1:]
    theta_values = math.pi * (1. - (3 * u * u - 2 * u ** 3))
    for theta in theta_values:
        sine = max(0., math.sin(theta))
        r = aa - rr * sine - 2 * float(LAM * R) * math.sqrt(sine)
        integ = quad(lambda t: math.sqrt(max(0., math.sin(t))),
                     0., theta, epsabs=1e-12, limit=100)[0]
        z = z_cuff + rr * (1. - math.cos(theta)) + float(LAM * R) * integ
        rings.append(np.column_stack((r * ca, r * sa, np.full(n_azimuth, z))))
    for r in np.linspace(aa, ac, 5)[1:]:
        rings.append(np.column_stack((r * ca, r * sa, np.full(n_azimuth, z_cuff))))
    top = np.array([[0., 0., float(Z_TOP + R - EPS)]])
    mesh_vertices = np.vstack((top, np.concatenate(rings, axis=0)))
    faces = []
    for k in range(n_azimuth):
        faces.append((0, 1 + k, 1 + (k + 1) % n_azimuth))
    for j in range(len(rings) - 1):
        start = 1 + j * n_azimuth
        nxt = start + n_azimuth
        for k in range(n_azimuth):
            kk = (k + 1) % n_azimuth
            faces.extend(((start + k, nxt + k, start + kk),
                          (start + kk, nxt + k, nxt + kk)))
    return mesh_vertices, np.asarray(faces, dtype=np.int32)


def write_binary_stl(path: Path, vertices: np.ndarray, faces: np.ndarray) -> None:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "wb") as out:
        out.write(b"R111 reference OPEN fixed cap; no active flexible core".ljust(80, b" "))
        out.write(struct.pack("<I", len(faces)))
        for face in faces:
            xyz = vertices[face]
            n = np.cross(xyz[1] - xyz[0], xyz[2] - xyz[0])
            length = np.linalg.norm(n)
            if length:
                n /= length
            out.write(struct.pack("<12fH", *n, *xyz.reshape(-1), 0))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=("diameter2p9", "diameter3"), default="diameter2p9")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--mesh", type=Path, help="optional upper reference .stl or .stl.gz")
    parser.add_argument("--azimuth", type=int, default=96)
    parser.add_argument("--body", type=int, default=48)
    parser.add_argument("--neck", type=int, default=48)
    args = parser.parse_args()
    configure_variant(args.variant)
    report = summary()
    if args.mesh:
        vv, ff = reference_mesh(args.azimuth, args.body, args.neck)
        args.mesh.parent.mkdir(parents=True, exist_ok=True)
        write_binary_stl(args.mesh, vv, ff)
        edges = np.sort(np.concatenate((ff[:, [0, 1]], ff[:, [1, 2]], ff[:, [2, 0]])), axis=1)
        unique_edges, counts = np.unique(edges, axis=0, return_counts=True)
        report["reference_mesh"] = {
            "vertices": len(vv), "faces": len(ff), "edges": len(unique_edges),
            "euler_characteristic": int(len(vv) - len(unique_edges) + len(ff)),
            "boundary_edges": int(np.count_nonzero(counts == 1)),
            "nonmanifold_edges": int(np.count_nonzero(counts > 2)),
            "sample_max_norm": float(np.max(np.linalg.norm(vv, axis=1))),
            "sample_max_abs_x": float(np.max(np.abs(vv[:, 0]))),
            "output": str(args.mesh), "bytes": args.mesh.stat().st_size,
            "certified_mesh_error": None,
        }
    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text + "\n", encoding="utf8")
    print(text)


if __name__ == "__main__":
    main()

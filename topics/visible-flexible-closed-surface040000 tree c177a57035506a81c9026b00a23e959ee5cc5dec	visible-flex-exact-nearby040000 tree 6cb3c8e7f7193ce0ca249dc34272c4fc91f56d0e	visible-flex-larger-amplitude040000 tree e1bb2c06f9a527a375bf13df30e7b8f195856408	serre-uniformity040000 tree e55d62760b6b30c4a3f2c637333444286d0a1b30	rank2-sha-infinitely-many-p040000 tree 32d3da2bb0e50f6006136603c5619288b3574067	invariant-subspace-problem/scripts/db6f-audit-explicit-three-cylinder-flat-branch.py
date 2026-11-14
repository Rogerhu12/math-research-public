#!/usr/bin/env python3
"""Exact algebra and rational gates for the explicit three-cylinder flat disk.

This is a pure formula checker, with optional small OBJ.gz samples.  It never
imports the primary numerical solver, reads its checkpoints, or runs any ODE,
RK, BVP, tail, optimization, or continuation code.  Floating quadrature values
are diagnostics only; the theorem's inequalities are analytic/Fraction gates.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


TOPIC = Path(__file__).resolve().parent.parent
STEM = "2026-11-09-db6f-audit-explicit-three-cylinder-flat-branch"
PROOF = TOPIC / "notes" / (STEM + ".md")
R = Q(1)
A = Q(579, 1000)
ELL = R - A
Z0 = Q(47, 500)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def qjson(x: Q) -> dict[str, object]:
    return {"numerator": x.numerator, "denominator": x.denominator,
            "display_only": float(x)}


def symbolic_checks() -> dict[str, object]:
    phi, kval = sp.symbols("phi kval", real=True)
    tangent = sp.Matrix([sp.cos(phi), 0, -sp.sin(phi)])
    ruling = sp.Matrix([0, 1, 0])
    normal = -tangent.cross(ruling)
    acceleration = kval * normal
    residuals = {
        "metric_ss_minus_1": sp.trigsimp(tangent.dot(tangent) - 1),
        "metric_sv": tangent.dot(ruling),
        "metric_vv_minus_1": ruling.dot(ruling) - 1,
        "normal_unit_minus_1": sp.trigsimp(normal.dot(normal) - 1),
        "normal_tangent": sp.trigsimp(normal.dot(tangent)),
        "normal_ruling": normal.dot(ruling),
        "II_ss_minus_k": sp.trigsimp(acceleration.dot(normal) - kval),
    }

    r = sp.symbols("r", positive=True)
    u = sp.symbols("u", real=True)
    kfun = sp.Function("k")
    ks = kfun(r * sp.cos(u))
    aa = ks * sp.cos(u) ** 2
    jj = -r * ks * sp.cos(u) * sp.sin(u)
    cc = r ** 2 * ks * sp.sin(u) ** 2
    residuals.update({
        "gauss_AC_minus_J2": sp.trigsimp(aa * cc - jj ** 2),
        "codazzi_Jr_minus_Au_plus_J_over_r":
            sp.simplify(sp.diff(jj, r) - sp.diff(aa, u) + jj / r),
        "codazzi_Cr_minus_Ju_minus_C_over_r_minus_rA":
            sp.simplify(sp.diff(cc, r) - sp.diff(jj, u) - cc / r - r * aa),
    })

    omega = 2 * sp.pi / 3
    rot = sp.Matrix([[sp.cos(omega), -sp.sin(omega), 0],
                     [sp.sin(omega), sp.cos(omega), 0], [0, 0, 1]])
    directions = [sp.Matrix([sp.cos(j * omega), sp.sin(j * omega), 0])
                  for j in range(3)]
    for j in range(3):
        residuals[f"C3_direction_{j}"] = sp.simplify(
            (rot * directions[j] - directions[(j + 1) % 3]).norm() ** 2)
    for j in range(3):
        for k in range(j + 1, 3):
            v = directions[j] + directions[k]
            residuals[f"separation_norm_squared_{j}_{k}_minus_1"] = (
                sp.simplify(v.dot(v) - 1))

    q = sp.symbols("q", positive=True)
    shape = q ** -2 * sp.exp(1 - 1 / q)
    residuals["log_derivative_for_exact_curvature_maximum"] = sp.simplify(
        sp.diff(shape, q) / shape - (q ** -2 - 2 / q))
    residuals["curvature_shape_at_half_minus_4_over_e"] = sp.simplify(
        shape.subs(q, sp.Rational(1, 2)) - 4 / sp.E)

    serialized = {name: str(sp.simplify(value))
                  for name, value in residuals.items()}
    assert all(value == "0" for value in serialized.values()), serialized
    return {"all_zero": True, "identity_count": len(serialized),
            "residuals": serialized}


def rational_checks() -> dict[str, object]:
    gates: list[dict[str, object]] = []

    def gt(name: str, left: Q, right: Q) -> None:
        passed = left > right
        gates.append({"name": name, "relation": ">", "left": qjson(left),
                      "right": qjson(right), "passed": passed})
        assert passed, name

    gt("disjoint_caps_2a_gt_R", 2 * A, R)
    gt("nonempty_caps_R_gt_a", R, A)
    gt("exp_series_upper_lt_11_over_4", Q(11, 4), Q(87, 32))
    gt("cube_10_over_7_gt_exp_upper", Q(10, 7) ** 3, Q(11, 4))
    lower_integral = Q(8, 363) + Q(1, 11) + Q(7, 40)
    held_lower = Q(5, 6) * ELL * lower_integral
    gt("actual_Hausdorff_witness_height_gt_1_over_10", held_lower, Q(1, 10))
    gt("held_over_initial_diameter_gt_1_over_20", held_lower / (2 * R), Q(1, 20))
    gt("fixed_disk_diameter_gt_one_fifth_D", 2 * A, Q(1, 5) * (2 * R))

    # cos(1)>1/2 and e>8/3 prove the strict analytic bound K<3/(2 ell).
    c_lower = Q(1, 2)
    curvature_upper = Q(3, 2) / ELL
    reach_lower = c_lower ** 2 / curvature_upper
    assert reach_lower == ELL / 6
    gt("disk_reach_lower_gt_3_over_100_D", reach_lower, Q(3, 100) * (2 * R))

    h0 = Q(1, 10)
    eps0 = Q(1, 40)
    plane_lower_squared = A ** 2 * h0 ** 2 / ((2 * A + R) ** 2 + h0 ** 2)
    gt("all_E3_distance_lower_gt_1_over_40_squared", plane_lower_squared,
       eps0 ** 2)
    weak_height_lower = Z0 - Q(1, 4) * ELL / 2
    assert weak_height_lower == Q(331, 8000)
    gt("weak_branch_entire_height_gt_core_top", weak_height_lower, Q(1, 100))

    return {
        "all_passed": True,
        "gate_count": len(gates),
        "parameters": {"R": qjson(R), "a": qjson(A), "ell": qjson(ELL),
                       "B_strong": qjson(Q(1)), "B_weak": qjson(Q(1, 4)),
                       "z0": qjson(Z0)},
        "initial_diameter_exact": qjson(2 * R),
        "held_strict_lower": qjson(held_lower),
        "reach_strict_lower": qjson(reach_lower),
        "euclidean_quotient_strict_lower": qjson(eps0),
        "weak_branch_height_lower": qjson(weak_height_lower),
        "gates": gates,
    }


def profile(s: float, bend_bound: float = 1.0) -> float:
    if s <= float(A):
        return 0.0
    q = (s - float(A)) / float(ELL)
    return bend_bound * math.exp(1.0 - 1.0 / q)


def adaptive_simpson_complex(f, lo: float, hi: float,
                             tolerance: float = 1.0e-13) -> tuple[complex, int]:
    """Floating diagnostic quadrature only; not a rigorous error enclosure."""
    if hi <= lo:
        return 0j, 0
    evaluations = 0

    def value(x: float) -> complex:
        nonlocal evaluations
        evaluations += 1
        return f(x)

    fl, fm, fr = value(lo), value((lo + hi) / 2), value(hi)
    first = (hi - lo) * (fl + 4 * fm + fr) / 6

    def recurse(a, b, fa, fm, fb, whole, tol, depth):
        mid = (a + b) / 2
        left_mid, right_mid = (a + mid) / 2, (mid + b) / 2
        flm, frm = value(left_mid), value(right_mid)
        left = (mid - a) * (fa + 4 * flm + fm) / 6
        right = (b - mid) * (fm + 4 * frm + fb) / 6
        defect = left + right - whole
        if abs(defect) <= 15 * tol:
            return left + right + defect / 15
        if depth == 0:
            raise RuntimeError("Diagnostic quadrature recursion limit reached")
        return (recurse(a, mid, fa, flm, fm, left, tol / 2, depth - 1)
                + recurse(mid, b, fm, frm, fb, right, tol / 2, depth - 1))

    return recurse(lo, hi, fl, fm, fr, first, tolerance, 30), evaluations


@lru_cache(maxsize=16384)
def primitives(s: float, amplitude: float, bend_bound: float = 1.0
               ) -> tuple[float, float, int]:
    if s <= float(A) or amplitude == 0:
        return 0.0, 0.0, 0

    def integrand(v):
        angle = amplitude * profile(v, bend_bound)
        return complex(math.cos(angle) - 1, math.sin(angle))

    integral, count = adaptive_simpson_complex(integrand, float(A), s)
    return integral.real, integral.imag, count


def position(x: float, y: float, amplitude: float,
             phase: float = 0.0, bend_bound: float = 1.0
             ) -> tuple[float, float, float]:
    # Rotating the three bending directions implements R_alpha G(R_-alpha x).
    px, py, pz = x, y, float(Z0)
    active_count = 0
    for j in range(3):
        angle = phase + 2 * math.pi * j / 3
        nx, ny = math.cos(angle), math.sin(angle)
        s = nx * x + ny * y
        if s > float(A):
            active_count += 1
            u, v, _ = primitives(s, amplitude, bend_bound)
            px += u * nx
            py += u * ny
            pz -= v
    assert active_count <= 1
    return px, py, pz


def floating_diagnostics() -> dict[str, object]:
    samples = []
    for amplitude in (0.0, 0.25, 0.5, 0.75, 1.0):
        u, v, count = primitives(float(R), amplitude)
        samples.append({"amplitude": amplitude,
                        "outer_apex_horizontal_radius": float(R) + u,
                        "outer_apex_height_drop": v,
                        "quadrature_evaluations": count})
    weak_u, weak_v, weak_count = primitives(float(R), 1.0, 0.25)
    return {
        "certified": False,
        "purpose": "display-only numerical evaluation of the exact integral formulas",
        "quadrature": "adaptive Simpson, complex paired integrands",
        "requested_tolerance_not_a_proof_bound": 1.0e-13,
        "strong_samples": samples,
        "weak_B_quarter": {"outer_apex_horizontal_radius": float(R) + weak_u,
                           "outer_apex_height_drop": weak_v,
                           "minimum_height": float(Z0) - weak_v,
                           "quadrature_evaluations": weak_count},
        "exact_formula_constants_display": {
            "co_lipschitz_cos_1": math.cos(1),
            "Hessian_bound_4_over_e_ell": 4 / (math.e * float(ELL)),
            "reach_bound_e_ell_cos_squared_1_over_4":
                math.e * float(ELL) * math.cos(1) ** 2 / 4,
        },
    }


def write_optional_mesh(path: Path, amplitude: float, phase: float,
                        rings: int = 24, angles: int = 96) -> dict[str, object]:
    """Small formula sample; no mesh is used in any theorem or gate."""
    vertices = [(0.0, 0.0, float(Z0))]
    for i in range(1, rings + 1):
        radius = float(R) * i / rings
        for j in range(angles):
            theta = 2 * math.pi * j / angles
            vertices.append(position(radius * math.cos(theta), radius * math.sin(theta),
                                     amplitude, phase))
    faces = []
    for j in range(angles):
        faces.append((1, 2 + j, 2 + (j + 1) % angles))
    for i in range(1, rings):
        previous, current = 2 + (i - 1) * angles, 2 + i * angles
        for j in range(angles):
            jn = (j + 1) % angles
            faces.append((previous + j, current + j, current + jn))
            faces.append((previous + j, current + jn, previous + jn))
    lines = ["# Explicit smooth disk sample; not a closed surface or certificate.\n"]
    lines.extend("v %.17g %.17g %.17g\n" % p for p in vertices)
    lines.extend("f %d %d %d\n" % f for f in faces)
    data = "".join(lines).encode("ascii")
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            zipped.write(data)
    assert path.stat().st_size < 5_000_000
    return {"path": str(path.relative_to(TOPIC)), "sha256": digest(path),
            "bytes": path.stat().st_size, "vertices": len(vertices),
            "triangles": len(faces), "amplitude": amplitude, "phase": phase,
            "certifying": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=TOPIC / "notes" / (STEM + ".json"))
    parser.add_argument("--mesh-prefix", type=Path,
                        help="Optional prefix for three small OBJ.gz samples; omitted by default")
    args = parser.parse_args()
    symbols = symbolic_checks()
    rationals = rational_checks()
    diagnostics = floating_diagnostics()
    meshes = []
    if args.mesh_prefix is not None:
        args.mesh_prefix.parent.mkdir(parents=True, exist_ok=True)
        for index, amplitude in enumerate((0.0, 0.5, 1.0)):
            path = Path(str(args.mesh_prefix) + f"-t{index}.obj.gz")
            meshes.append(write_optional_mesh(path, amplitude, 2 * math.pi * amplitude / 3))
    source_paths = [Path(__file__).resolve(), PROOF,
                    TOPIC / "results/R38-ck-local-exact-isometric-collar.md",
                    TOPIC / "results/R41-flat-annulus-conditional-local-geometry.md",
                    TOPIC / "results/R42-degenerate-flat-endpoint-and-finite-mode-uniqueness.md"]
    report = {
        "schema": "explicit-three-cylinder-flat-disk-v1",
        "scope": "Exact C-infinity embedded disk with boundary, not a closed surface",
        "main_candidate_data_read": False,
        "BVP_tail_RK_optimization_run": False,
        "proof_status": "author proof pending independent full-text review",
        "symbolic": symbols,
        "rational": rationals,
        "floating_diagnostics": diagnostics,
        "optional_meshes": meshes,
        "sources": [{"path": str(p.relative_to(TOPIC)), "sha256": digest(p),
                     "bytes": p.stat().st_size} for p in source_paths],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    assert args.output.stat().st_size < 1_000_000
    print(json.dumps({"output": str(args.output), "sha256": digest(args.output),
                      "symbolic_identities": symbols["identity_count"],
                      "rational_gates": rationals["gate_count"],
                      "all_exact_checks_passed": True,
                      "mesh_count": len(meshes)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

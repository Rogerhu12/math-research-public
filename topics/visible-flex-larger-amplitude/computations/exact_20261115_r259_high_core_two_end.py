#!/usr/bin/env python3
"""Complete R259 high-core diagnostic on one saved candidate, Actions only.

No resonance search, new tail call, nonlinear trial, FFT RHS or Jacobian is
performed.  Every one of the 112 retained modes is included.  The saved true
zero-height slope matrix is consumed in full and its actual diagonal form is
checked, not assumed from its name.  Two different objects are kept separate:

1. exact dyadic algebra of explicitly saved binary64 two-by-two cell blocks;
2. Arb enclosures for the declared real scalar expression, the same recorded
   grid constants, and the recorded zero-tail matrix treated as exact data.

The second object is not a roundoff bound for the first.  Neither object
certifies the accuracy of the saved tail derivative, a low-three resonance,
parameter transversality, a nonzero-amplitude BVP, or a closed surface.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import struct
import sys
import time
import traceback

SCHEMA = "R259-complete-high109-two-end-diagnostic-v1"
PARENT_SCHEMA = "R259-original-circle-collocation-low-three-resonance-diagnostic-v1"
HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
M, LOW, NODES, DIMENSION = 112, 3, 699, 453
EXPECTED = {
    "accepted": "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
    "prepared": "0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714",
    "tail_anchor": "e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51",
    "tail_config": "01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5",
}
FROZEN = {
    "geometry_20261114_small_core_resonance.py": "3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5",
    "geometry_20261114_constrained_trust_warm.py": "5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2",
    "geometry_20261114_constrained_collocation.py": "70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8",
    "geometry_20261114_full_dn_solve.py": "c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162",
    "geometry_20261114_full_dn_augmented.py": "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e",
    "geometry_20261114_full_dn_boundary.py": "4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2",
    "geometry_20261114_physical_test_boundary.py": "3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681",
    "geometry_20261114_lifted_modes_profile.py": "13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5",
    "geometry_20261114_full_prefix_operator.py": "a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703",
    "geometry_20261114_direct_operator_cell.py": "1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic is restricted to this public repository's Actions")


def same(actual, expected, label):
    if actual != expected:
        raise ValueError(label + " does not match the supplied original identity")


def digest(value):
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("An explicit lowercase SHA256 is required")
    return value


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def record(path, root=None):
    path = Path(path)
    name = str(path.relative_to(root)) if root is not None else path.name
    return {"file": name, "bytes": path.stat().st_size, "sha256": sha(path)}


def reject_constant(value):
    raise ValueError("Nonfinite JSON number: " + value)


def read_json(path, expected=None):
    path = Path(path)
    if expected is not None:
        same(sha(path), digest(expected), path.name + " SHA256")
    raw = path.read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw, parse_constant=reject_constant)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False).encode("utf-8")


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False,
        allow_nan=False).encode("utf-8") + b"\n"
    if path.suffix == ".gz":
        raw = gzip.compress(raw, compresslevel=6, mtime=0)
    temporary = path.with_name(path.name + ".partial")
    temporary.write_bytes(raw)
    temporary.replace(path)
    return record(path, path.parent)


def number(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("The defining binary64 constants must be finite")
    return {"value": value, "float64le_hex": struct.pack("<d", value).hex(),
        "negative_zero": value == 0 and math.copysign(1., value) < 0}


def f64_bytes(value):
    return np.asarray(value, dtype="<f8", order="C").tobytes(order="C")


def array_identity(value):
    a = np.asarray(value, dtype="<f8", order="C")
    raw = a.tobytes(order="C")
    return {"shape": list(a.shape), "dtype": "<f8", "order": "C",
        "raw_bytes": len(raw), "raw_sha256": hashlib.sha256(raw).hexdigest()}


class Arrays:
    def __init__(self, root):
        self.root = Path(root)
        self.directory = self.root / "large-arrays"
        self.directory.mkdir(exist_ok=True)
        self.entries = []

    def save(self, name, value, role):
        a = np.asarray(value, dtype="<f8", order="C")
        if np.any(~np.isfinite(a)):
            raise FloatingPointError("A defining array is nonfinite: " + name)
        raw = a.tobytes(order="C")
        path = self.directory / (name + ".f64.gz")
        path.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
        entry = dict(name=name, role=role, **record(path, self.root),
            shape=list(a.shape), dtype="<f8", order="C", raw_bytes=len(raw),
            raw_sha256=hashlib.sha256(raw).hexdigest())
        self.entries.append(entry)
        return entry

    def finish(self):
        path = self.root / "array-manifest.json"
        write_json(path, {"schema": "R259-complete-two-end-defining-arrays-v1",
            "arrays": self.entries, "every_nonzero_mode_retained": True})
        return record(path, self.root)


class Budget:
    def __init__(self, seconds, maximum_integer_bits):
        self.started = time.monotonic()
        self.deadline = self.started + seconds
        self.maximum_integer_bits = maximum_integer_bits
        self.largest_integer_bits = 0

    def remaining(self):
        return time.monotonic() < self.deadline

    def check(self, values=()):
        if not self.remaining():
            raise BudgetExhausted("Declared diagnostic wall-clock budget exhausted")
        for a, unused in values:
            bits = abs(a).bit_length()
            self.largest_integer_bits = max(self.largest_integer_bits, bits)
            if bits > self.maximum_integer_bits:
                raise BudgetExhausted("Declared exact-integer storage budget exhausted")


class BudgetExhausted(RuntimeError):
    pass


# A dyadic is an odd signed integer times 2**exponent; zero is (0, 0).
# No binary64 product, dot product, inverse, or threshold enters this kernel.
def dyadic(a, exponent=0):
    a = int(a)
    if a == 0:
        return (0, 0)
    shift = (abs(a) & -abs(a)).bit_length() - 1
    return (a >> shift, int(exponent) + shift)


def from_float(value):
    numerator, denominator = float(value).as_integer_ratio()
    return dyadic(numerator, -(denominator.bit_length() - 1))


def add(a, b):
    if a[0] == 0:
        return b
    if b[0] == 0:
        return a
    exponent = min(a[1], b[1])
    return dyadic((a[0] << (a[1] - exponent))
        + (b[0] << (b[1] - exponent)), exponent)


def neg(a):
    return (-a[0], a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if not a[0] or not b[0]:
        return (0, 0)
    return (a[0] * b[0], a[1] + b[1])


def exact_det(matrix):
    return sub(mul(matrix[0][0], matrix[1][1]),
        mul(matrix[0][1], matrix[1][0]))


def exact_step(left, right, vector):
    """v_next = -adj(R) L v; valid even when det(R) is zero."""
    u = add(mul(left[0][0], vector[0]), mul(left[0][1], vector[1]))
    v = add(mul(left[1][0], vector[0]), mul(left[1][1], vector[1]))
    return (add(neg(mul(right[1][1], u)), mul(right[0][1], v)),
        sub(mul(right[1][0], u), mul(right[0][0], v)))


def dyadic_record(value):
    a, exponent = value
    return {"odd_integer_hex": ("-" if a < 0 else "") + format(abs(a), "x"),
        "power_of_two": exponent, "integer_bits": abs(a).bit_length(),
        "sign": (a > 0) - (a < 0)}


def quotient_record(numerator, denominator):
    if denominator[0] == 0:
        return {"defined": False, "reason": "The exact denominator is zero"}
    a, b = numerator[0], denominator[0]
    exponent = numerator[1] - denominator[1]
    if b < 0:
        a, b = -a, -b
    common = math.gcd(abs(a), b)
    a, b = a // common, b // common
    if not a:
        exponent = 0
    with localcontext() as context:
        context.prec = 36
        context.Emax = 999999999
        context.Emin = -999999999
        approximate = Decimal(a) / Decimal(b) * (Decimal(2) ** exponent)
        text = format(approximate, ".24E")
    return {"defined": True,
        "numerator_odd_hex": ("-" if a < 0 else "") + format(abs(a), "x"),
        "denominator_odd_hex": format(b, "x"), "power_of_two": exponent,
        "sign": (a > 0) - (a < 0), "decimal_approximation": text,
        "decimal_is_not_an_outward_enclosure": True}


def exact_mode(mode, left, right, terminal_B, tail_diagonal, gamma, eh, budget):
    vector, determinant_product = ((1, 0), (0, 0)), (1, 0)
    determinants, zero_cells = [], []
    for cell in range(len(left)):
        L = [[from_float(value) for value in row] for row in left[cell]]
        R = [[from_float(value) for value in row] for row in right[cell]]
        det = exact_det(R)
        determinants.append(dyadic_record(det))
        if det[0] == 0:
            zero_cells.append(cell)
        determinant_product = mul(determinant_product, det)
        vector = exact_step(L, R, vector)
        if cell % 16 == 0:
            budget.check((*vector, determinant_product))
    B10, B11 = from_float(terminal_B[1, 0]), from_float(terminal_B[1, 1])
    coupling = mul(mul(from_float(gamma), from_float(eh)), from_float(tail_diagonal))
    boundary = (B10, sub(B11, coupling))
    numerator = add(mul(boundary[0], vector[0]), mul(boundary[1], vector[1]))
    height_derivative = add(mul(B10, vector[0]), mul(B11, vector[1]))
    budget.check((*vector, determinant_product, numerator))
    return {
        "schema": "R277-exact-dyadic-complete-two-end-mode-witness-v1",
        "mode": mode, "frequency": 2 * mode, "nodes": len(left) + 1,
        "square_two_end_matrix_dimension": 2 * (len(left) + 1),
        "row_order": "H_0; all L_i X_i + R_i X_(i+1); ell_N X_N",
        "column_order": "U_0,H_0,U_1,H_1,...,U_N,H_N",
        "terminal_boundary_exact_from_finite_operands": [dyadic_record(v) for v in boundary],
        "initial_projective_vector": [1, 0],
        "final_projective_vector": [dyadic_record(v) for v in vector],
        "right_cell_determinants": determinants,
        "exact_singular_right_cells": zero_cells,
        "product_of_right_cell_determinants": dyadic_record(determinant_product),
        "boundary_projective_numerator": dyadic_record(numerator),
        "full_two_end_determinant": dyadic_record(neg(numerator)),
        "finite_two_end_matrix_nonsingular": numerator[0] != 0,
        "unit_inlet_map_exists_for_this_finite_chain": not zero_cells,
        "unit_endpoint_U": quotient_record(vector[0], determinant_product),
        "unit_endpoint_H": quotient_record(vector[1], determinant_product),
        "unit_endpoint_Hprime": quotient_record(height_derivative, determinant_product),
        "unit_right_defect": quotient_record(numerator, determinant_product),
        "inverse_diagonal_right_map": (quotient_record(determinant_product, numerator)
            if not zero_cells else {"defined": False,
                "reason": "The unit-inlet elimination chart is undefined; use the complete two-end certificate"}),
        "no_floating_transfer_or_inverse_used": True,
        "rank_certificate_is_for_saved_reduced_cell_coefficients_only": True,
        "exact_original_FFT_or_tail_derivative_rank_claimed": False,
    }


def finite_blocks(ratio, radius, speed, vertical, frequency):
    """The frozen source matrix expression, extended to all 112 modes."""
    k2 = frequency ** 2
    answer = np.empty((len(radius), len(frequency), 2, 2), dtype=float)
    answer[:, :, 0, 0] = ratio[:, None] * (1 - k2)
    answer[:, :, 0, 1] = -vertical[:, None] * k2 / radius[:, None]
    answer[:, :, 1, 0] = (speed * ratio / vertical)[:, None] * (k2 - 1)
    answer[:, :, 1, 1] = ratio[:, None] * k2
    return answer


def finite_model(profile, prepared, circle, parameters, gamma, eh, J, arrays):
    x = np.asarray(circle["mesh"], dtype=float)
    y = np.asarray(circle["states"], dtype=float)
    same(x.shape, (NODES,), "All original mesh nodes")
    same(y.shape, (NODES, DIMENSION), "All saved circular augmented coordinates")
    if (np.any(~np.isfinite(y)) or np.any(~np.isfinite(x)) or np.any(np.diff(x) <= 0)
            or not np.array_equal(x, np.asarray(prepared["mesh"], dtype=float))):
        raise ValueError("The full original finite circular state and mesh must be retained")
    if not np.array_equal(y[:, 4 * M + 2:], np.broadcast_to(parameters, (NODES, 3))):
        raise ValueError("Every saved circular control row must retain the final candidate")
    if np.any(y[:, 3 * M + 2:4 * M + 2] != 0):
        raise ValueError("The supplied reference must be the actual zero-core circle")
    physical = y[:, :3 * M + 2].copy()
    physical[:, 0] = 0
    physical[:, 2 * M + 1] = 0
    if np.any(physical != 0):
        raise ValueError("Nonmean circular coordinates must all be zero")
    h = np.diff(x)
    middle_x = .5 * (x[:-1] + x[1:])
    base = np.asarray([profile.base_jet(s) for s in x])[:, :2]
    base_mid = np.asarray([profile.base_jet(s) for s in middle_x])[:, :2]
    controls = np.asarray([profile.control_jets(s) for s in x])[:, :2]
    controls_mid = np.asarray([profile.control_jets(s) for s in middle_x])[:, :2]
    scalar = base + np.einsum("mjk,k->mj", controls, parameters)
    scalar_mid = base_mid + np.einsum("mjk,k->mj", controls_mid, parameters)
    q, qm = scalar[:, 1] / scalar[:, 0], scalar_mid[:, 1] / scalar_mid[:, 0]
    radius = y[:, 0].copy()
    radius_mid = .5 * (radius[:-1] + radius[1:]) - h * (
        q[1:] * radius[1:] - q[:-1] * radius[:-1]) / 8
    speed, speed_mid = q * radius, qm * radius_mid
    margin, margin_mid = 1 - speed * speed, 1 - speed_mid * speed_mid
    if (np.any(~np.isfinite(scalar)) or np.any(~np.isfinite(scalar_mid))
            or np.any(scalar[:, 0] <= 0) or np.any(scalar_mid[:, 0] <= 0)
            or np.any(radius <= 0) or np.any(radius_mid <= 0)
            or np.any(margin <= 0) or np.any(margin_mid <= 0)):
        raise FloatingPointError("The saved candidate's reduced circular field is outside its domain")
    W, Wm = np.sqrt(margin), np.sqrt(margin_mid)
    frequency = 2. * np.arange(1, M + 1)
    B, Bm = (finite_blocks(q, radius, speed, W, frequency),
        finite_blocks(qm, radius_mid, speed_mid, Wm, frequency))
    hh = h[:, None, None, None]
    identity = np.eye(2)
    L = -identity - hh * (B[:-1] + 2 * Bm) / 6 - hh * hh * (Bm @ B[:-1]) / 12
    R = identity - hh * (B[1:] + 2 * Bm) / 6 + hh * hh * (Bm @ B[1:]) / 12
    # Keep the source's first-three binary operations as a separate replay.
    B3, Bm3 = (finite_blocks(q, radius, speed, W, frequency[:LOW]),
        finite_blocks(qm, radius_mid, speed_mid, Wm, frequency[:LOW]))
    L3 = -identity - hh * (B3[:-1] + 2 * Bm3) / 6 - hh * hh * (Bm3 @ B3[:-1]) / 12
    R3 = identity - hh * (B3[1:] + 2 * Bm3) / 6 + hh * hh * (Bm3 @ B3[1:]) / 12
    source_block_replay = {"B": f64_bytes(B[:, :LOW]) == f64_bytes(B3),
        "Bmid": f64_bytes(Bm[:, :LOW]) == f64_bytes(Bm3),
        "L": f64_bytes(L[:, :LOW]) == f64_bytes(L3),
        "R": f64_bytes(R[:, :LOW]) == f64_bytes(R3)}
    for name, value, role in (
        ("mesh", x, "All original binary64 stations"),
        ("cell-widths", h, "Original rounded np.diff mesh constants, treated exactly downstream"),
        ("midpoint-stations", middle_x, "Original rounded midpoint sample locations"),
        ("scalar-nodes", scalar, "All returned a/ap pairs at original nodes"),
        ("scalar-midpoints", scalar_mid, "All returned a/ap pairs at original midpoint samples"),
        ("circle-radius", radius, "Saved parent circle radius, not silently replaced by a"),
        ("circle-radius-midpoints", radius_mid, "Original Hermite expression from saved radius and returned q"),
        ("circle-height", y[:, 2 * M + 1], "Complete saved mean height"),
        ("ratio-nodes", q, "Returned ap/a, not a finite-Gauss derivative"),
        ("ratio-midpoints", qm, "Returned midpoint ap/a"),
        ("vertical-nodes", W, "sqrt(1-(q R)^2)"),
        ("vertical-midpoints", Wm, "sqrt(1-(q_mid R_mid)^2)"),
        ("complete-zero-tail-slope-J", J, "All actual 112 by 112 true-zero response entries"),
        ("B-nodes-all112", B, "All (U,H) source linearization blocks"),
        ("B-midpoints-all112", Bm, "All midpoint (U,H) blocks"),
        ("L-all112", L, "All original formed binary64 left cell blocks"),
        ("R-all112", R, "All original formed binary64 right cell blocks"),
    ):
        arrays.save(name, value, role)
    # The exact certificate uses the finite B terminal entries and exact
    # products of gamma, epsilon_h and the recorded J, not a rounded ell row.
    model = {"schema": "R259-all112-formed-reduced-chain-model-v1",
        "nodes": NODES, "modes": M, "high_modes": list(range(LOW + 1, M + 1)),
        "height_sign": number(eh), "cut_scale": number(gamma),
        "parameters": [number(v) for v in parameters],
        "binary64_model": "saved radius; original returned scalar samples; explicitly formed L/R; exact terminal arithmetic on finite B,gamma,epsilon_h,J",
        "first_three_extended_block_bytes_equal_separate_three_block_replay": source_block_replay,
        "circle_radius_is_saved_parent_data": True,
        "terminal_row_formation_rounding_applied": False,
        "full_FFT_J_recomputed": False, "native_tail_recomputed": False,
        "all_array_identities": {entry["name"]: {k: entry[k] for k in
            ("shape", "dtype", "order", "raw_bytes", "raw_sha256")} for entry in arrays.entries}}
    model["model_sha256"] = hashlib.sha256(canonical(model)).hexdigest()
    return x, h, middle_x, L, R, B, model


def mm(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0],
             a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0],
             a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


def arb_B(q, radius, vertical, k):
    k2 = k * k
    return [[q * (1 - k2), -vertical * k2 / radius],
        [(q * radius) * q / vertical * (k2 - 1), q * k2]]


def arb_cell(h, left_B, midpoint_B, right_B):
    a, b = mm(midpoint_B, left_B), mm(midpoint_B, right_B)
    left, right = [[], []], [[], []]
    for i in range(2):
        for j in range(2):
            identity = int(i == j)
            left[i].append(-identity - h * (left_B[i][j] + 2 * midpoint_B[i][j]) / 6
                - h * h * a[i][j] / 12)
            right[i].append(identity - h * (right_B[i][j] + 2 * midpoint_B[i][j]) / 6
                + h * h * b[i][j] / 12)
    return left, right


def arb_step(left, right, vector):
    a = left[0][0] * vector[0] + left[0][1] * vector[1]
    b = left[1][0] * vector[0] + left[1][1] * vector[1]
    return [-right[1][1] * a + right[0][1] * b,
        right[1][0] * a - right[0][0] * b]


def arb_circle(expression, primitive, old, x, h, middle_x, budget):
    b = primitive.ball
    q, qm, scalar, scalar_mid = [], [], [], []
    for output, samples, samples_out in ((q, x, scalar), (qm, middle_x, scalar_mid)):
        for index, station in enumerate(samples):
            point = Fraction.from_float(float(station))
            branch = expression.branch(point)
            a = expression.value(b(point), branch, point)
            ap = old.returned_ap(expression, b(point), branch, point)
            samples_out.append((a, ap))
            if not (a.is_finite() and ap.is_finite() and a > 0):
                return None, {"reason": "No strict finite positive scalar enclosure at a required sample",
                    "sample_index": index, "midpoint": output is qm}
            output.append(ap / a)
            if index % 64 == 0:
                budget.check()
    radius, midpoint_radius, right_denominators = [b(1)], [], []
    for i, width in enumerate(h):
        hh = b(float(width))
        left = -1 - hh * (q[i] + 2 * qm[i]) / 6 - hh * hh * qm[i] * q[i] / 12
        right = 1 - hh * (q[i + 1] + 2 * qm[i]) / 6 + hh * hh * qm[i] * q[i + 1] / 12
        right_denominators.append(right)
        if not right.is_finite() or right.contains(0):
            return None, {"reason": "The declared real circular radius cell denominator is unresolved",
                "cell": i, "right": primitive.ball_record(right)}
        radius.append(-left * radius[-1] / right)
        midpoint_radius.append((radius[-2] + radius[-1]) / 2 - hh * (
            q[i + 1] * radius[-1] - q[i] * radius[-2]) / 8)
    vertical, midpoint_vertical, margins, midpoint_margins = [], [], [], []
    for radii, ratios, out, out_margin in ((radius, q, vertical, margins),
            (midpoint_radius, qm, midpoint_vertical, midpoint_margins)):
        for index, (r, ratio) in enumerate(zip(radii, ratios)):
            margin = 1 - (ratio * r) ** 2
            out_margin.append(margin)
            if not (r.is_finite() and r > 0 and margin.is_finite() and margin > 0):
                return None, {"reason": "The declared real circular radius or square-root branch is unresolved",
                    "sample_index": index, "midpoint": radii is midpoint_radius,
                    "radius": primitive.ball_record(r), "beta_squared": primitive.ball_record(margin)}
            out.append(margin.sqrt())
    return {"q": q, "qm": qm, "radius": radius, "radius_mid": midpoint_radius,
        "W": vertical, "Wm": midpoint_vertical, "scalar": scalar,
        "scalar_mid": scalar_mid, "radius_right_denominators": right_denominators,
        "margin": margins, "margin_mid": midpoint_margins}, None


def arb_mode(mode, circle, h, gamma, eh, diagonal, primitive, budget):
    b = primitive.ball
    vector, determinant_product = [b(1), b(0)], b(1)
    unresolved_right = []
    previous = arb_B(circle["q"][0], circle["radius"][0], circle["W"][0], 2 * mode)
    for cell, width in enumerate(h):
        middle = arb_B(circle["qm"][cell], circle["radius_mid"][cell], circle["Wm"][cell], 2 * mode)
        following = arb_B(circle["q"][cell + 1], circle["radius"][cell + 1], circle["W"][cell + 1], 2 * mode)
        left, right = arb_cell(b(float(width)), previous, middle, following)
        det = right[0][0] * right[1][1] - right[0][1] * right[1][0]
        if not det.is_finite() or det.contains(0):
            unresolved_right.append(cell)
        determinant_product *= det
        vector = arb_step(left, right, vector)
        previous = following
        if cell % 32 == 0:
            budget.check()
    boundary = [previous[1][0], previous[1][1] - b(gamma) * b(eh) * b(diagonal)]
    numerator = boundary[0] * vector[0] + boundary[1] * vector[1]
    nonsingular = numerator.is_finite() and not numerator.contains(0)
    quotient_defined = (not unresolved_right and determinant_product.is_finite()
        and not determinant_product.contains(0))
    result = {"schema": "R277-declared-real-interval-two-end-mode-v1",
        "mode": mode, "frequency": 2 * mode, "nodes": NODES,
        "precision_bits": int(primitive.ctx.prec),
        "final_projective_vector": [primitive.ball_record(v) for v in vector],
        "product_of_right_cell_determinants": primitive.ball_record(determinant_product),
        "unresolved_right_cell_indices": unresolved_right,
        "terminal_boundary": [primitive.ball_record(v) for v in boundary],
        "boundary_projective_numerator": primitive.ball_record(numerator),
        "full_two_end_determinant": primitive.ball_record(-numerator),
        "declared_two_end_matrix_nonsingular": bool(nonsingular),
        "unit_inlet_map_certified_defined": bool(quotient_defined),
        "unit_right_defect": primitive.ball_record(numerator / determinant_product) if quotient_defined else None,
        "unit_endpoint_H": primitive.ball_record(vector[1] / determinant_product) if quotient_defined else None,
        "saved_true_tail_J_is_an_exact_parameter_in_this_model": True,
        "saved_true_tail_J_error_enclosed": False,
        "finite_collocation_not_continuous_ODE_nonresonance": True}
    return result


def interval_work(specification, scalar_certificate, x, h, middle_x,
        J, gamma, eh, args, budget, result):
    import geometry_20261114_direct_operator_cell as primitive
    from geometry_20261114_full_prefix_operator import ScalarExpression
    import geometry_20261114_small_core_resonance as old
    latest, histories, bits = {}, [], args.arb_bits
    partial = {"schema": "R259-complete-high109-interval-summary-v1",
        "initial_bits": args.arb_bits, "maximum_bits": args.arb_max_bits,
        "precision_histories": histories, "latest_modes": [],
        "all_high109_two_end_blocks_proved_nonsingular_in_declared_model": False,
        "all_high109_unit_inlet_maps_proved_defined": False,
        "high_free_core_Schur_is_diagonal_and_nonsingular_in_declared_model": False,
        "all_high_modes_present": False,
        "unresolved_high_modes": list(range(LOW + 1, M + 1)),
        "low_three_resonance_existence_proved": False,
        "three_parameter_interval_transversality_proved": False,
        "saved_tail_derivative_error_proved": False,
        "continuous_ODE_high_nonresonance_proved": False,
        "literal_binary64_FFT_derivative_nonresonance_proved": False}
    result["declared_real_interval_summary"] = partial
    pending = list(range(1, M + 1))
    while pending and bits <= args.arb_max_bits and budget.remaining():
        primitive.ctx.prec = bits
        expression = ScalarExpression(specification, scalar_certificate["descriptor"], primitive)
        circle, failure = arb_circle(expression, primitive, old, x, h, middle_x, budget)
        history = {"bits": bits, "requested_modes": pending.copy(),
            "circle_enclosure_complete": circle is not None, "failure": failure, "mode_receipts": []}
        histories.append(history)
        if circle is not None:
            saved_circle = {"schema": "R259-declared-real-discrete-circle-enclosure-v1",
                "bits": bits, "source_specification": specification,
                "scalar_descriptor_sha256": hashlib.sha256(canonical(scalar_certificate["descriptor"])).hexdigest(),
                "grid_scope": "exact recorded binary64 node, np.diff width and rounded midpoint constants",
                "circle_is_reconstructed_in_real_Arb_arithmetic_not_parent_f64_radius": True,
                "whole_s_interval_circle_domain_proved": False,
                "arrays": {key: ([[primitive.ball_record(w) for w in v] for v in value]
                    if key in ("scalar", "scalar_mid") else [primitive.ball_record(v) for v in value])
                    for key, value in circle.items()}}
            circle_path = args.out / "large-arrays" / ("arb-circle-%04d.json.gz" % bits)
            write_json(circle_path, saved_circle)
            history["circle_receipt"] = record(circle_path, args.out)
            for mode in pending:
                budget.check()
                row = arb_mode(mode, circle, h, gamma, eh, float(J[mode - 1, mode - 1]), primitive, budget)
                path = args.out / "large-arrays" / ("arb-mode-%03d-bits-%04d.json.gz" % (mode, bits))
                write_json(path, row)
                receipt = record(path, args.out)
                history["mode_receipts"].append(receipt)
                latest[mode] = {"mode": mode, "bits": bits, "receipt": receipt,
                    "two_end_nonsingular": row["declared_two_end_matrix_nonsingular"],
                    "unit_map_defined": row["unit_inlet_map_certified_defined"],
                    "unit_right_defect": row["unit_right_defect"],
                    "unit_endpoint_H": row["unit_endpoint_H"]}
                partial["latest_modes"] = [latest[j] for j in sorted(latest)]
                partial["completed_modes"] = len(latest)
                partial["completed_high_modes"] = len([j for j in latest if j > LOW])
                partial["unresolved_high_modes"] = [j for j in range(LOW + 1, M + 1)
                    if j not in latest or not (latest[j]["two_end_nonsingular"] and latest[j]["unit_map_defined"])]
                if mode % 8 == 0:
                    print(json.dumps({"event": "high_core_interval_mode", "mode": mode, "bits": bits,
                        "two_end_nonsingular": row["declared_two_end_matrix_nonsingular"]}), flush=True)
        # Low-three interval rows are diagnostic only.  Extra precision is
        # spent solely on unresolved high modes, without a new parameter search.
        pending = [j for j in range(1, M + 1)
            if j not in latest or (j > LOW and not (
                latest[j]["two_end_nonsingular"] and latest[j]["unit_map_defined"]))]
        result["interval_progress"] = {"completed_precision_passes": len(histories),
            "remaining_high_modes": [j for j in pending if j > LOW],
            "low_modes_not_yet_evaluated": [j for j in pending if j <= LOW]}
        bits *= 2
    if pending and not budget.remaining():
        partial["wall_clock_budget_ended_interval_work"] = True
        raise BudgetExhausted("Diagnostic wall-clock budget exhausted at an interval precision boundary")
    all_high = all(j in latest and latest[j]["two_end_nonsingular"] for j in range(LOW + 1, M + 1))
    all_maps = all(j in latest and latest[j]["unit_map_defined"] for j in range(LOW + 1, M + 1))
    return {"schema": "R259-complete-high109-interval-summary-v1",
        "initial_bits": args.arb_bits, "maximum_bits": args.arb_max_bits,
        "precision_histories": histories, "latest_modes": [latest[j] for j in sorted(latest)],
        "all_high109_two_end_blocks_proved_nonsingular_in_declared_model": all_high,
        "all_high109_unit_inlet_maps_proved_defined": all_maps,
        "high_free_core_Schur_is_diagonal_and_nonsingular_in_declared_model": all_high and all_maps,
        "unique_high_core_and_internal_response_to_zero_high_forcing_is_zero": all_high,
        "all_high_modes_present": len([j for j in latest if j > LOW]) == M - LOW,
        "completed_modes": len(latest),
        "completed_high_modes": len([j for j in latest if j > LOW]),
        "unresolved_high_modes": [j for j in pending if j > LOW],
        "low_modes_not_yet_evaluated": [j for j in pending if j <= LOW],
        "wall_clock_budget_ended_interval_work": bool(pending and not budget.remaining()),
        "low_three_resonance_existence_proved": False,
        "three_parameter_interval_transversality_proved": False,
        "saved_tail_derivative_error_proved": False,
        "continuous_ODE_high_nonresonance_proved": False,
        "literal_binary64_FFT_derivative_nonresonance_proved": False}


def bind_inputs(args):
    for name, expected in FROZEN.items():
        same(sha(HERE / name), expected, "Frozen scientific source " + name)
    current_sources = {name: record(HERE / name) for name in FROZEN}
    current_sources[Path(__file__).name] = record(Path(__file__))
    original_inputs = {}
    for name, expected in EXPECTED.items():
        path = getattr(args, name)
        same(sha(path), expected, "Original complete input " + name)
        original_inputs[name] = record(path)
    identity = read_json(args.parent_identity, args.parent_identity_sha256)
    same(identity.get("source_commit"), args.producer_source_commit, "Actual parent source commit")
    request = identity["request"]
    same(request.get("schema"), "public-small-core-resonance-request-v1", "Original request schema")
    same(request.get("scientific_entry"), "geometry_20261114_small_core_resonance.py", "Original entry")
    same(request.get("scientific_source_unchanged"), True, "Original low-core source scope")
    same(request.get("inputs", {}).keys(), EXPECTED.keys(), "All four original input names")
    # Retain the entire parent's supplied source ledger.  Verify its complete
    # scientific closure in the checkout; a later publisher-only revision is
    # recorded but cannot change this mathematical diagnostic or block it.
    verified_parent_sources = []
    names = set()
    for row in identity["verified_sources"]:
        name = row["file"]
        if Path(name).name != name or name in names:
            raise ValueError("The original source ledger must have unique local basenames")
        names.add(name)
        actual = record(HERE / name)
        if name == "root_20261114_publish_actions.py":
            verified_parent_sources.append({"parent_receipt": row,
                "current_receipt": actual,
                "current_bytes_equal_parent": actual["sha256"] == row["sha256"],
                "publication_only_not_imported_by_this_scientific_diagnostic": True})
        else:
            same(actual["sha256"], digest(row["sha256"]), "Actual source ledger " + name)
            same(actual["bytes"], row["bytes"], "Actual source byte count " + name)
            verified_parent_sources.append(actual)
    for row in identity["verified_original_inputs"]:
        same(row["sha256"], EXPECTED[row["name"]], "Parent original input ledger")
        same(row["bytes"], original_inputs[row["name"]]["bytes"], "Parent original input size")
    status = read_json(args.resonance_directory / "resonance-status.json", args.status_sha256)
    circle = read_json(args.resonance_directory / "circle-reference.json.gz", args.circle_sha256)
    scalar = read_json(args.resonance_directory / "complete-scalar-domain.json.gz", args.scalar_domain_sha256)
    same(status["schema"], PARENT_SCHEMA, "Parent status schema")
    same(circle["schema"], PARENT_SCHEMA, "Parent circle schema")
    same(status.get("diagnostic_completed"), True, "Parent diagnostic completion, not candidate acceptance")
    same(status["input_sha256"], EXPECTED, "Parent four-input identity")
    same(status["original_mesh_nodes"], NODES, "Parent original node count")
    same(status["field_and_tail_modes"], M, "Parent complete mode count")
    same(circle["M"], M, "Circle mode count")
    same(circle["N"], 2048, "Circle angular discretization")
    same(status["original_complete_circle_check"]["reference_sha256"], args.circle_sha256, "Status/circle binding")
    same(circle["source_prepared_sha256"], EXPECTED["prepared"], "Original circle preparation")
    same(circle.get("full_native_tail_at_nonzero_height_computed"), False, "Parent circle is not a nonlinear tail")
    same(scalar["schema"], "R259-complete-declared-scalar-domain-enclosure-v1", "Original scalar enclosure schema")
    for name, expected in status["consumed_source_sha256"].items():
        same(expected, sha(HERE / name), "Parent consumed scientific source " + name)
    parameters = np.asarray(status["final"]["parameters"], dtype=float)
    if parameters.shape != (3,) or np.any(~np.isfinite(parameters)):
        raise ValueError("Keep all three actually saved finite candidate parameters")
    same(f64_bytes(parameters), f64_bytes(circle["complete_scalar_profile"]["frozen_design_parameters"]),
        "Candidate parameter bytes in the complete scalar specification")
    binding = {"schema": "R259-complete-high109-input-binding-v1",
        "producer_run_id": args.producer_run_id,
        "producer_source_commit": args.producer_source_commit,
        "run_id_is_bound_by_the_upstream_artifact_transport_not_an_API_call_here": True,
        "parent_identity": record(args.parent_identity), "parent_request": request,
        "parent_status": record(args.resonance_directory / "resonance-status.json"),
        "parent_circle": record(args.resonance_directory / "circle-reference.json.gz"),
        "parent_scalar_enclosure": record(args.resonance_directory / "complete-scalar-domain.json.gz"),
        "original_inputs": original_inputs, "verified_parent_source_ledger": verified_parent_sources,
        "current_scientific_sources": current_sources,
        "saved_parameters": [number(v) for v in parameters],
        "parent_reported_low_resonance_flag": status.get("low_mode_candidate_has_small_full_recorded_right_residual"),
        "parent_reported_low_equations": status["final"]["low_equations_used"],
        "parent_full_BVP_acceptance_claimed": False,
        "this_input_check_does_not_require_a_low_mode_resonance": True}
    return status, circle, scalar, parameters, binding


def summary_of(result):
    exact = result.get("exact_finite_summary", {})
    interval = result.get("declared_real_interval_summary", {})
    return {"schema": SCHEMA, "phase": result["phase"],
        "diagnostic_completed": result.get("diagnostic_completed", False),
        "input_binding": result.get("input_binding"), "model": result.get("model"),
        "all_retained_modes": M, "free_high_modes": M - LOW,
        "parent_parameters": result.get("parent_parameters"),
        "parent_low_resonance_flag": result.get("parent_low_resonance_flag"),
        "complete_true_zero_J": result.get("complete_true_zero_J"),
        "exact_finite_summary": {k: v for k, v in exact.items() if k != "mode_receipts"},
        "declared_real_interval_summary": {k: v for k, v in interval.items()
            if k not in ("precision_histories", "latest_modes")},
        "budget": result.get("budget"), "elapsed_seconds": result.get("elapsed_seconds"),
        "array_manifest": result.get("array_manifest"),
        "resources": result.get("resources"),
        "full_result_file": "result.json.gz",
        "exception": result.get("exception"), "budget_exhaustion": result.get("budget_exhaustion"),
        "unsupported_scope": result.get("unsupported_scope"),
        "no_new_RHS_FFT_J_or_native_tail_calls": True,
        "no_parameter_search_or_nonlinear_candidate_solve": True,
        "scientific_arithmetic_only_in_public_Actions": True,
        "diagnostic_is_not_a_native_or_full_DN_acceptance_gate": True,
        "full_nonlinear_nonzero_lambda_solution_computed": False,
        "new_coupled_finite_acceptance": False, "complete_closed_surface": False,
        "low_mode_resonance_existence_or_full_IFT_proved": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "resonance-directory",
            "parent-identity", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    for name in ("status-sha256", "circle-sha256", "scalar-domain-sha256", "parent-identity-sha256"):
        parser.add_argument("--" + name, type=digest, required=True)
    parser.add_argument("--producer-run-id", required=True)
    parser.add_argument("--producer-source-commit", required=True)
    parser.add_argument("--arb-bits", type=int, default=160)
    parser.add_argument("--arb-max-bits", type=int, default=640)
    parser.add_argument("--budget-seconds", type=float, default=1800.)
    parser.add_argument("--maximum-integer-bits", type=int, default=4000000)
    args = parser.parse_args()
    require_actions()
    if (not args.producer_run_id.isdigit()
            or re.fullmatch(r"[0-9a-f]{40}", args.producer_source_commit) is None):
        raise ValueError("Use the actual public producer run and source commit")
    if not (64 <= args.arb_bits <= args.arb_max_bits <= 16384):
        raise ValueError("Declare a finite Arb precision schedule")
    if not (math.isfinite(args.budget_seconds) and args.budget_seconds > 0
            and args.maximum_integer_bits >= 1024):
        raise ValueError("Declare positive finite diagnostic resource budgets")
    if args.out.exists() and any(args.out.iterdir()):
        raise ValueError("Use a fresh independent diagnostic output directory")
    args.out.mkdir(parents=True, exist_ok=True)
    # No scientific package is imported before the public Actions restriction.
    for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[name] = "1"
    global np
    import numpy as np
    budget = Budget(args.budget_seconds, args.maximum_integer_bits)
    result = {"schema": SCHEMA, "phase": "binding-inputs", "diagnostic_completed": False,
        "success": False, "new_coupled_finite_acceptance": False,
        "complete_closed_surface": False, "source_sha256": sha(Path(__file__))}
    exit_code = 0
    arrays = None
    try:
        status, circle, scalar, parameters, binding = bind_inputs(args)
        binding_path = args.out / "input-binding.json"
        write_json(binding_path, binding)
        result["input_binding"] = record(binding_path, args.out)
        result["parent_parameters"] = status["final"]["parameters"]
        result["parent_low_resonance_flag"] = status.get("low_mode_candidate_has_small_full_recorded_right_residual")
        import geometry_20261114_small_core_resonance as old
        from geometry_20261114_constrained_trust_warm import setup
        accepted, prepared, anchor = [read_json(path) for path in
            (args.accepted, args.prepared, args.tail_anchor)]
        profile, unused_flow, boundary = setup(accepted, prepared, anchor, 4096, 1)
        J = np.asarray(anchor["heightJetJacobian"], dtype=float).reshape(3 * M + 2, M)[:M].copy()
        if np.any(~np.isfinite(J)):
            raise ValueError("The complete saved zero-tail derivative must be finite")
        offdiagonal = J.copy()
        np.fill_diagonal(offdiagonal, 0.)
        count = int(np.count_nonzero(offdiagonal))
        result["complete_true_zero_J"] = {"shape": [M, M], **array_identity(J),
            "nonzero_offdiagonal_entries": count, "actually_diagonal": count == 0,
            "all_entries_consumed": True, "ready_linear_graph_used": False,
            "new_native_response_computed": False}
        if count:
            result.update(phase="complete-J-is-not-diagonal",
                unsupported_scope="This consumer does not silently discard actual off-diagonal high-core coupling")
            return 0
        gamma, eh = float(boundary.cut_scale), float(boundary.eh)
        arrays = Arrays(args.out)
        x, h, middle_x, L, R, B, model = finite_model(profile, prepared, circle,
            parameters, gamma, eh, J, arrays)
        model_path = args.out / "finite-model.json"
        write_json(model_path, model)
        result["model"] = record(model_path, args.out)
        result["model"]["model_sha256"] = model["model_sha256"]
        result["phase"] = "exact-finite-all112"
        mode_rows, receipts = [], []
        result["exact_finite_summary"] = {"mode_receipts": receipts, "completed_modes": 0}
        for j in range(M):
            budget.check()
            row = exact_mode(j + 1, L[:, j], R[:, j], B[-1, j], float(J[j, j]), gamma, eh, budget)
            path = args.out / "large-arrays" / ("exact-mode-%03d.json.gz" % (j + 1))
            write_json(path, row)
            receipt = record(path, args.out)
            receipts.append(receipt)
            mode_rows.append({"mode": j + 1, "receipt": receipt,
                "two_end_nonsingular": row["finite_two_end_matrix_nonsingular"],
                "unit_map_exists": row["unit_inlet_map_exists_for_this_finite_chain"],
                "exact_singular_right_cells": row["exact_singular_right_cells"],
                "unit_right_defect": row["unit_right_defect"],
                "inverse_diagonal_right_map": row["inverse_diagonal_right_map"]})
            result["exact_finite_summary"]["completed_modes"] = j + 1
            print(json.dumps({"event": "high_core_exact_mode", "mode": j + 1,
                "two_end_nonsingular": row["finite_two_end_matrix_nonsingular"],
                "unit_map_exists": row["unit_inlet_map_exists_for_this_finite_chain"]}), flush=True)
        high = mode_rows[LOW:]
        all_high = all(row["two_end_nonsingular"] for row in high)
        all_maps = all(row["unit_map_exists"] for row in high)
        exact_schur = {"schema": "R259-recorded-diagonal-tail-complete-high109-Schur-v1",
            "all112_mode_rows": mode_rows,
            "complete_J_offdiagonal_is_exactly_zero": True,
            "left_low_high_and_high_low_couplings_are_zero_in_this_reduced_model": True,
            "high_block_is_diagonal_in_core_coordinates_if_all_unit_maps_exist": all_maps,
            "high_core_solution_for_zero_high_forcing": [0] * (M - LOW),
            "high_solution_is_unique_in_full_two_end_finite_system": all_high,
            "complete_high109_core_Schur_nonsingular_for_saved_cell_model": all_high and all_maps,
            "low_three_Schur_correction_is_exactly_zero_if_high_block_invertible": all_high and all_maps,
            "low_three_equations_remain_required": True,
            "low_three_target": status["final"]["source_target_first_three"],
            "nonzero_lambda_field_or_continuation_generated": False,
            "true_tail_derivative_uncertainty_or_full_FFT_roundoff_bound": False}
        schur_path = args.out / "large-arrays" / "finite-full-mode-schur.json.gz"
        write_json(schur_path, exact_schur)
        result["finite_schur"] = record(schur_path, args.out)
        result["exact_finite_summary"] = {
            "completed_modes": len(mode_rows), "completed_high_modes": len(high),
            "mode_receipts": receipts,
            "all_high109_two_end_matrices_nonsingular": all_high,
            "all_high109_unit_inlet_maps_exist": all_maps,
            "high109_finite_core_Schur_nonsingular": all_high and all_maps,
            "high_mode_singularities": [row["mode"] for row in high if not row["two_end_nonsingular"]],
            "high_mode_IVP_elimination_failures": [row["mode"] for row in high if not row["unit_map_exists"]],
            "finite_arrays_are_not_the_exact_mathematical_FFT_or_tail_derivative": True,
            "no_R_inverse_or_floating_rank_threshold_used": True}
        result["phase"] = "declared-real-interval-all112"
        result["declared_real_interval_summary"] = interval_work(
            circle["complete_scalar_profile"], scalar, x, h, middle_x,
            J, gamma, eh, args, budget, result)
        unresolved = result["declared_real_interval_summary"]["unresolved_high_modes"]
        result.update(phase=("bounded-diagnostic-completed-with-unresolved-high-intervals"
            if unresolved else "diagnostic-completed"), diagnostic_completed=True)
    except BudgetExhausted as error:
        result.update(phase="resource-budget-exhausted-with-partial-evidence",
            budget_exhaustion=str(error), diagnostic_completed=False)
    except Exception as error:
        exit_code = 1
        result.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
    finally:
        result["elapsed_seconds"] = time.monotonic() - budget.started
        result["budget"] = {"declared_seconds": args.budget_seconds,
            "maximum_integer_bits": args.maximum_integer_bits,
            "largest_integer_bits_observed": budget.largest_integer_bits,
            "resource_limits_are_not_nonlinear_acceptance_gates": True}
        result["resources"] = {"peak_RSS_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "retained_modes": M, "retained_high_modes": M - LOW,
            "nodes_per_mode": NODES, "cells_per_mode": NODES - 1,
            "two_end_unknowns_per_mode": 2 * NODES,
            "all_mode_cell_blocks": M * (NODES - 1),
            "formed_B_Bmid_L_R_raw_bytes": 8 * 4 * M * ((NODES + NODES - 1) + 2 * (NODES - 1)),
            "dense_full_two_end_matrix_formed": False,
            "dense_high109_Schur_matrix_factorized": False,
            "integer_work_is_not_constant_cost_per_arithmetic_operation": True,
            "thread_environment": {k: os.environ.get(k) for k in
                ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}}
        if arrays is not None:
            result["array_manifest"] = arrays.finish()
        result_path = args.out / "result.json.gz"
        write_json(result_path, result)
        summary = summary_of(result)
        summary["full_result"] = record(result_path, args.out)
        write_json(args.out / "summary.json", summary)
        print(json.dumps(summary, sort_keys=True, ensure_ascii=False, allow_nan=False), flush=True)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

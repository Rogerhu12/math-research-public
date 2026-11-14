#!/usr/bin/env python3
"""Exact cardinal nonplanarity witnesses for future accepted-A node artifacts.

Preparation only until a real complete 577-node readout and its owned exit 0
exist. This consumer performs no point roots, RK/ODE, shooting/BVP Newton,
variational flow, or interpolation of missing nodes. Coverage failure is a
mathematical diagnostic, not a parser or process failure.

The raw and pi-projected versions are two explicitly different finite fields.
The exact circular part uses cardinal cos/sin values, not stored libm values.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import time
from fractions import Fraction

READER_SHA = "aa6678f2411b1f4f106b64c75c25a3961cb680d8ba80f23b6218a3694527b0d2"
OWNED_SHA = "2652689a93a67f03c258121fe58e9d621a5dbda742682b4984d93c646e1166b5"
A_SHA = "917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf"
TAIL_SHA = "018d19c6ca8c27acc5cc1dde6d396ee783e34ae25e5b525158c5bb37086520d9"
MEAN_SHA = "59717e6b83c009671781054b7042624fa30ef39b9f8f9660e9511b1481092e14"
READER_NAME = "geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs"
COLUMNS = [
    "delta_X_round", "delta_Y_round", "height_oscillatory",
    "delta_X_r_round", "delta_Y_r_round", "height_r",
    "delta_X_theta_round", "delta_Y_theta_round", "height_theta",
    "height_rr", "height_rtheta", "height_thetatheta",
]
NODES = 577
ANGLES = 512
WIDTH = 12
CARDINAL = (0, 128, 256, 384)
RAW_BYTES = ANGLES * WIDTH * 8


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def bad_constant(value):
    raise ValueError("non-finite JSON constant: " + value)


def read_json(path):
    raw = path.read_bytes()
    return json.loads(raw, parse_constant=bad_constant), sha(raw)


def exact_binary(value, name):
    require(isinstance(value, (int, float)) and not isinstance(value, bool),
            name + " is not a JSON number")
    value = float(value)
    require(math.isfinite(value), name + " is not finite")
    return Fraction.from_float(value)


def qpack(value):
    return {"numerator": str(value.numerator),
            "denominator": str(value.denominator)}


def sign(value):
    return (value > 0) - (value < 0)


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def determinant(points):
    a, b, c = (subtract(points[j], points[0]) for j in (1, 2, 3))
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def projected_points(points):
    p0, p1, p2, p3 = points
    ax, ay = (p0[0] - p2[0]) / 2, (p0[1] - p2[1]) / 2
    bx, by = (p1[0] - p3[0]) / 2, (p1[1] - p3[1]) / 2
    za, zb = (p0[2] + p2[2]) / 2, (p1[2] + p3[2]) / 2
    projected = ((ax, ay, za), (bx, by, zb),
                 (-ax, -ay, za), (-bx, -by, zb))
    area = ax * by - ay * bx
    height = zb - za
    return projected, area, height


def option(command, name):
    positions = [i for i, value in enumerate(command) if value == name]
    require(len(positions) == 1, "owned command must contain one " + name)
    i = positions[0]
    require(i + 1 < len(command), "missing owned option value: " + name)
    return command[i + 1]


def check_owned(owned):
    require(owned.get("schema") == "new-A-tail-readout-owned-v1",
            "unexpected node-reader owned schema")
    require(owned.get("wrapper_sha256") == OWNED_SHA,
            "node-reader owned wrapper source mismatch")
    require(owned.get("wait4_observed") is True,
            "no observed wait4 termination for node reader")
    require(owned.get("exitcode") == 0
            and owned.get("termination_signal") is None,
            "node reader did not actually exit 0")
    command = owned.get("command")
    require(isinstance(command, list)
            and all(isinstance(x, str) for x in command),
            "owned command is missing")
    require(sum(Path(x).name == READER_NAME for x in command) == 1,
            "owned command is not the pinned node reader")
    require(option(command, "--first-node") == "0",
            "owned range does not start at node 0")
    require(option(command, "--last-node-exclusive") == "577",
            "owned range does not end at node 577")
    original_out_dir = option(command, "--out-dir")
    return command, original_out_dir


def check_complete(data):
    require(data.get("schema") ==
            "accepted-A-all-shooting-node-Cartesian-first-jet-readout-v1",
            "unexpected node readout schema")
    require(data.get("finished") is True, "node readout is unfinished")
    require(data.get("source_sha256") == READER_SHA,
            "node-reader source SHA differs")
    require(data.get("original_A_primary_sha256") == A_SHA,
            "readout is not the original accepted A")
    require(data.get("original_final_tail_sha256") == TAIL_SHA,
            "readout final tail differs")
    require(data.get("original_mean_primary_sha256") == MEAN_SHA,
            "readout saved mean differs")
    require(data.get("range") == [0, 577]
            and data.get("requestedNodes") == NODES
            and data.get("completedNodes") == NODES
            and data.get("whole_577_node_readout_complete") is True,
            "the complete 577-node readout is required")
    require(data.get("angular") == ANGLES and data.get("columns") == COLUMNS,
            "angular layout or columns differ")
    require(data.get("vertical_second_jets_only") is True
            and data.get("horizontal_rr_not_computed") is True,
            "unexpected horizontal second-jet claim")
    evaluations = data.get("evaluations", {})
    for key in ("RKSteps", "ODEFlows", "shootingOrBVPNewtonSolves",
                "newVariationalFlows"):
        require(evaluations.get(key) == 0,
                "readout operation scope differs: " + key)
    rows = data.get("rows")
    require(isinstance(rows, list) and len(rows) == NODES,
            "node rows are incomplete")
    return rows


def read_node(folder, row, node):
    require(row.get("node") == node, "node rows are missing or reordered")
    filename = "node-" + str(node).zfill(4) + ".f64le.gz"
    require(row.get("file") == filename, "unexpected node block filename")
    require(row.get("shape") == [ANGLES, WIDTH], "node shape differs")
    require(row.get("rawBytes") == RAW_BYTES, "node raw byte count differs")
    compressed = (folder / filename).read_bytes()
    require(len(compressed) == row.get("bytes"),
            "compressed byte count differs: " + filename)
    require(sha(compressed) == row.get("sha256"),
            "compressed SHA differs: " + filename)
    raw = gzip.decompress(compressed)
    require(len(raw) == RAW_BYTES and sha(raw) == row.get("rawSha256"),
            "decompressed shape or SHA differs: " + filename)
    require(all(math.isfinite(value[0]) for value in struct.iter_unpack("<d", raw)),
            "non-finite scalar in node block: " + filename)
    r = exact_binary(row["geometry"]["r"], "node radius")
    exact_binary(row["meanHeightInnerAnchor"], "node mean")
    delta = []
    for j in CARDINAL:
        offset = j * WIDTH * 8
        delta.append(tuple(Fraction.from_float(x)
                           for x in struct.unpack_from("<3d", raw, offset)))
    points = (
        (r + delta[0][0], delta[0][1], delta[0][2]),
        (delta[1][0], r + delta[1][1], delta[1][2]),
        (-r + delta[2][0], delta[2][1], delta[2][2]),
        (delta[3][0], -r + delta[3][1], delta[3][2]),
    )
    raw_det = determinant(points)
    projected, area, height = projected_points(points)
    projected_det = determinant(projected)
    factorized = 4 * height * area
    require(projected_det == factorized,
            "exact projected determinant factorization failed")
    projection_change = max(
        abs(projected[j][k] - points[j][k])
        for j in range(4) for k in range(3))
    record = {
        "node": node,
        "radius": qpack(r),
        "radius_positive": r > 0,
        "block_file": filename,
        "block_sha256": row["sha256"],
        "raw_block_sha256": row["rawSha256"],
        "raw_four_point_determinant": qpack(raw_det),
        "raw_determinant_sign": sign(raw_det),
        "pi_projected_four_point_determinant": qpack(projected_det),
        "pi_projected_determinant_sign": sign(projected_det),
        "pi_projected_horizontal_area_factor": qpack(area),
        "pi_projected_height_difference_factor": qpack(height),
        "pi_factorization_equal_exactly": True,
        "pi_projection_change_at_four_cardinals_coordinate_max":
            qpack(projection_change),
    }
    return r, raw_det, projected_det, record


def atomic_new(path, result):
    raw = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(fd, "wb") as out:
        out.write(raw)
        out.flush()
        os.fsync(out.fileno())
    return sha(raw), len(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--complete", required=True, type=Path)
    parser.add_argument("--owned", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    require(not args.out.exists(), "output already exists")
    started = time.monotonic()
    owned, owned_sha = read_json(args.owned)
    command, original_out_dir = check_owned(owned)
    complete, complete_sha = read_json(args.complete)
    rows = check_complete(complete)
    radii, raw_dets, projected_dets, node_results = [], [], [], []
    for node, row in enumerate(rows):
        r, raw_det, projected_det, record = read_node(
            args.complete.parent, row, node)
        radii.append(r)
        raw_dets.append(raw_det)
        projected_dets.append(projected_det)
        node_results.append(record)
    intervals, bad_order, raw_uncovered, projected_uncovered = [], [], [], []
    for i in range(NODES - 1):
        h = radii[i] - radii[i + 1]
        ordered = radii[i] > radii[i + 1] > 0
        raw_witness = next((j for j in (i, i + 1) if raw_dets[j] != 0), None)
        projected_witness = next(
            (j for j in (i, i + 1) if projected_dets[j] != 0), None)
        raw_ok = ordered and raw_witness is not None
        projected_ok = ordered and projected_witness is not None
        if not ordered:
            bad_order.append(i)
        if not raw_ok:
            raw_uncovered.append(i)
        if not projected_ok:
            projected_uncovered.append(i)
        intervals.append({
            "original_interval": i,
            "outer_node": i,
            "inner_node": i + 1,
            "exact_outer_minus_inner_radius": qpack(h),
            "strict_positive_radius_order": ordered,
            "raw_has_nonzero_endpoint_determinant": raw_witness is not None,
            "raw_witness_node": raw_witness,
            "raw_finite_piece_nonplanarity_covered": raw_ok,
            "pi_projected_has_nonzero_endpoint_determinant":
                projected_witness is not None,
            "pi_projected_witness_node": projected_witness,
            "pi_projected_finite_piece_nonplanarity_covered": projected_ok,
        })
    result = {
        "schema": "accepted-A-finite-cardinal-nonplanarity-exact-v1",
        "finished": True,
        "source_sha256": sha(Path(__file__).read_bytes()),
        "input": {
            "complete_file": str(args.complete),
            "complete_sha256": complete_sha,
            "owned_file": str(args.owned),
            "owned_sha256": owned_sha,
            "reader_sha256": READER_SHA,
            "reader_owned_wrapper_sha256": OWNED_SHA,
            "reader_original_command": command,
            "reader_original_out_dir": original_out_dir,
            "accepted_A_primary_sha256": A_SHA,
            "accepted_A_final_tail_sha256": TAIL_SHA,
            "accepted_A_saved_mean_sha256": MEAN_SHA,
            "fullflow_identity_sha256":
                complete["original_fullflow_identity_sha256"],
            "artifact_relocation_allowed_with_identical_bytes": True,
        },
        "definition": {
            "angular_nodes": ANGLES,
            "cardinal_indices": list(CARDINAL),
            "angles": ["0", "pi/2", "pi", "3pi/2"],
            "coordinates":
                "Exact saved binary perturbations plus exact cardinal circular part.",
            "determinant":
                "Rows are p1-p0, p2-p0, p3-p0 in the listed angular order.",
            "common_height":
                "Same node mean cancels exactly; no zero-mean rounding assumption.",
            "raw":
                "Real cardinal interpolation of unprojected saved sample values.",
            "pi_projected":
                "Horizontal odd and vertical even projection under theta -> theta+pi.",
            "projected_factorization":
                "4*(zb-za)*(ax*by-ay*bx), checked with exact Fractions.",
            "radial_piece":
                "Any R230 analytic finite Hermite piece with these endpoint positions.",
            "arithmetic":
                "Every input Float64 is its exact rational value; no tolerance.",
        },
        "node_count": NODES,
        "interval_count": NODES - 1,
        "strict_radius_order_pass": not bad_order,
        "radius_order_failure_intervals": bad_order,
        "nonpositive_radius_nodes":
            [i for i, r in enumerate(radii) if r <= 0],
        "raw": {
            "all_finite_pieces_nonplanarity_covered": not raw_uncovered,
            "covered_intervals": NODES - 1 - len(raw_uncovered),
            "uncovered_intervals": raw_uncovered,
            "exact_zero_determinant_nodes":
                [i for i, d in enumerate(raw_dets) if d == 0],
        },
        "pi_projected": {
            "all_finite_pieces_nonplanarity_covered": not projected_uncovered,
            "covered_intervals": NODES - 1 - len(projected_uncovered),
            "uncovered_intervals": projected_uncovered,
            "exact_zero_determinant_nodes":
                [i for i, d in enumerate(projected_dets) if d == 0],
            "full_projection_value_and_jet_error_budget_paid": False,
        },
        "nodes": node_results,
        "intervals": intervals,
        "evaluations": {
            "new_point_roots": 0, "new_ODE_or_RK": 0,
            "new_shooting_or_BVP_Newton": 0, "new_variational_flow": 0,
            "exact_four_point_determinants": 2 * NODES,
        },
        "limitations": [
            "A zero endpoint determinant is an unresolved witness, not evidence of planarity.",
            "Coverage refers to the explicitly defined finite field, not the original ODE tail.",
            "Raw and pi-projected fields have separate conclusions; projection error is not waived.",
            "Exact circular cardinals differ from a libm reconstruction unless that error is paid.",
            "Horizontal rr, metric, curvature, embedding, reach and closed-surface claims remain separate.",
            "The consumer may exit 0 with incomplete nonplanarity coverage; inspect the coverage booleans.",
        ],
        "seconds": time.monotonic() - started,
    }
    output_sha, output_bytes = atomic_new(args.out, result)
    print(json.dumps({
        "output": str(args.out), "sha256": output_sha, "bytes": output_bytes,
        "finished": True, "strict_radius_order_pass": not bad_order,
        "raw_covered": NODES - 1 - len(raw_uncovered),
        "pi_projected_covered": NODES - 1 - len(projected_uncovered),
    }), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

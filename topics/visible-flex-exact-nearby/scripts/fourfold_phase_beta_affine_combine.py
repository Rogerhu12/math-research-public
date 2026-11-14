#!/usr/bin/env python3
"""Combine a complete exact-affine beta cover without changing its object.

Every report is matched to the descriptor, exact parameter, origin, direction,
native dependency hashes, and complete collar.  Fractions reconstruct every
positive and negative scalar knot.  Rounded materialized exports are not used.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_combine import stored_ball, cover_rows
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, required=True)
    parser.add_argument("--collar", type=Path, required=True)
    parser.add_argument("--parts", type=Path, nargs="+", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    here = Path(__file__).parent
    definition, origin, direction, parameter = load_definition(args.object)
    object_sha, affine_sha = sha(args.object), sha(here/"fourfold_phase_beta_affine.py")
    dependencies = {name: sha(here/name) for name in (
        "fourfold_phase_beta_interval.py",
        "fourfold_phase_beta_bulk_interval.py",
        "fourfold_phase_beta_bulk_box.py")}

    def check_identity(report):
        if (report["object_sha256"] != object_sha
                or report["source_sha256"] != affine_sha
                or report["dependency_sha256"] != dependencies
                or report["origin_inputs_sha256"] != sha(origin)
                or report["direction_sha256"] != sha(direction)
                or Fraction(report["exact_delta_fraction"]) != parameter):
            raise ValueError("exact affine object or source mismatch")

    collar = json.loads(args.collar.read_text())
    check_identity(collar)
    if not collar["complete"]:
        raise ValueError("the exact affine collar is incomplete")
    collar_sha, cut = sha(args.collar), Fraction(collar["fixed_cut"])
    parts, waist = [], None
    for path in args.parts:
        part = json.loads(path.read_text())
        check_identity(part)
        if part["collar_sha256"] != collar_sha or Fraction(part["fixed_cut"]) != cut:
            raise ValueError("bulk has a different collar or cut")
        part_waist = Fraction(part["waist_width"])
        if waist is None:
            waist = part_waist
        if waist != part_waist:
            raise ValueError("bulk waist widths differ")
        parts.append((path, part))
    if not 0 < waist < cut:
        raise ValueError("invalid waist or collar cut")
    knots = {Fraction(0), waist, cut}
    with np.load(origin, allow_pickle=False) as source:
        for key in source.files:
            if key.endswith("_knots"):
                knots.update(q for q in
                    (abs(Fraction.from_float(float(x))) for x in source[key])
                    if 0 < q < cut)
    points = sorted(knots)
    if points[1] != waist:
        raise ValueError("waist crosses a frozen scalar knot")
    cells = [(a, b) for a, b in zip(points, points[1:]) if a >= waist]
    selected, waist_record, provenance = {}, None, []
    for path, part in parts:
        if part["radial_cells_total"] != len(cells):
            raise ValueError("bulk count differs from the exact knot partition")
        grouped = defaultdict(list)
        for row in part["accepted_cells"]:
            if not 0 <= row["index"] < len(cells):
                raise ValueError("invalid exact-span index")
            grouped[row["index"]].append(row)
        for index, rows in grouped.items():
            covered = cover_rows(rows, *cells[index])
            if covered is not None:
                selected[index] = path, covered
        if "waist_integral" in part:
            waist_record = path, part["waist_integral"]
        provenance.append({"path": str(path), "sha256": sha(path),
            "accepted_subcells": len(part["accepted_cells"]),
            "failed_subcells": len(part["failed_cells"])})
    missing = [index for index in range(len(cells)) if index not in selected]
    if missing or waist_record is None:
        raise ValueError(f"incomplete exact cover: missing={missing}, waist={waist_record is not None}")
    total = stored_ball(waist_record[1])
    rows, subcells = [], 0
    for index, (left, right) in enumerate(cells):
        path, accepted = selected[index]
        value = sum((stored_ball(row["integral"]) for row in accepted), arb(0))
        total += value
        subcells += len(accepted)
        rows.append({"index": index, "left": str(left), "right": str(right),
            "source_part": str(path), "subcells": len(accepted), "integral": ball_record(value)})
    collar_value = stored_ball(collar["collar_integral"])
    beta = (total+collar_value)/2
    scaled = 2*arb(5).sqrt()*beta/arb.pi()
    lower = int(scaled.lower().floor().unique_fmpz())
    upper = int(scaled.upper().ceil().unique_fmpz())
    odd = [q for q in range(lower-4, upper+5) if q % 2]
    norm_gap = min([arb(1)]+[abs(scaled-q).lower() for q in odd])
    if not norm_gap > 0:
        norm_gap = arb(0)
    phase_gap = (arb.pi()*norm_gap/(2*arb(5).sqrt())).lower()
    report = {
        "kind": "complete_exact_affine_beta_and_D5_norm_grid",
        "complete": True,
        "object_path": str(args.object), "object_sha256": object_sha,
        "exact_delta_fraction": str(parameter),
        "origin_inputs_sha256": sha(origin), "direction_sha256": sha(direction),
        "source_sha256": sha(__file__), "affine_source_sha256": affine_sha,
        "native_dependency_sha256": dependencies,
        "collector_helpers_sha256": sha(here/"fourfold_phase_beta_combine.py"),
        "collar_path": str(args.collar), "collar_sha256": collar_sha,
        "part_provenance": provenance,
        "exact_original_knot_cells": len(cells), "selected_subcells": subcells,
        "waist_path": str(waist_record[0]), "waist_width": str(waist), "fixed_cut": str(cut),
        "bulk_integral": ball_record(total), "collar_integral": ball_record(collar_value),
        "beta": ball_record(beta), "D5_scaled_beta": ball_record(scaled),
        "D5_odd_norm_gap_lower": ball_record(norm_gap),
        "D5_beta_lattice_distance_lower": ball_record(phase_gap),
        "D5_candidate_grid_points": [{"Q": q,
            "beta_grid": ball_record(arb.pi()*q/(2*arb(5).sqrt()))} for q in odd],
        "selected_cells": rows,
        "limitations": [
            "The beta interval belongs to the exact affine point above, not its rounded export",
            "No parameter-neighborhood beta estimate is inferred from one point",
            "The actual principal rotation, full scattering remainder, low block, and nonlinear closure remain separate matching requirements"
        ]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"beta": beta.str(30),
        "D5_norm_gap_lower": norm_gap.str(22),
        "D5_phase_gap_lower": phase_gap.str(22)}), flush=True)


if __name__ == "__main__":
    main()

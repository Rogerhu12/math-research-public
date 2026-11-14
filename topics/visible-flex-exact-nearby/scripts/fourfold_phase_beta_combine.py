#!/usr/bin/env python3
"""Check exact bulk coverage, combine its collar, and compare the D5 norm grid.

Partial integration files are allowed as inputs; the selected accepted cells
must form a complete exact cover. A completed rerun of one original knot cell
may replace the earlier partial version of that entire cell. All source and
input hashes must match the current frozen programs. The lattice comparison
is an arithmetic beta check, not a substitute for matching the actual return
map's principal rotation to the D5 target.
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
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stored_ball(record):
    # Arb's display ball may shorten the midpoint at low relative accuracy.
    # The separately printed outward endpoints retain the recorded precision.
    lower, upper = arb(record["lower"]), arb(record["upper"])
    return lower.union(upper)


def cover_rows(rows, left, right):
    ordered = sorted(rows, key=lambda row: Fraction(row["left"]))
    point = left
    for row in ordered:
        a, b = Fraction(row["left"]), Fraction(row["right"])
        if a != point or not a < b or not b <= right:
            return None
        point = b
    return ordered if point == right else None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--frozen-inputs", type=Path, required=True)
    ap.add_argument("--collar", type=Path, required=True)
    ap.add_argument("--parts", type=Path, nargs="+", required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = 192
    here = Path(__file__).parent
    native_sha, bulk_sha, box_sha = [sha(here/name) for name in
        ("fourfold_phase_beta_interval.py", "fourfold_phase_beta_bulk_interval.py", "fourfold_phase_beta_bulk_box.py")]
    input_sha = sha(args.frozen_inputs)
    collar = json.loads(args.collar.read_text())
    if not collar["complete"] or collar["input_sha256"] != input_sha or collar["source_sha256"] != native_sha:
        raise ValueError("collar is incomplete or its frozen input/source does not match")
    cut = Fraction(collar["fixed_cut"])
    parts, waist = [], None
    for path in args.parts:
        part = json.loads(path.read_text())
        if (part["input_sha256"] != input_sha or part["source_sha256"] != bulk_sha
                or part["native_source_sha256"] != native_sha or Fraction(part["fixed_cut"]) != cut):
            raise ValueError(f"bulk source/input/cut mismatch: {path}")
        if part["engine"] == "box" and part["box_source_sha256"] != box_sha:
            raise ValueError(f"directed kernel hash mismatch: {path}")
        candidate_waist = Fraction(part["waist_width"])
        if waist is None:
            waist = candidate_waist
        if waist != candidate_waist:
            raise ValueError("bulk parts use different waist cuts")
        parts.append((path, part))
    if not 0 < waist < cut:
        raise ValueError("invalid waist or fixed collar cut")
    knots = {Fraction(0), waist, cut}
    with np.load(args.frozen_inputs, allow_pickle=False) as inputs:
        for key in inputs.files:
            if key.endswith("_knots"):
                for value in inputs[key]:
                    q = abs(Fraction.from_float(float(value)))
                    if 0 < q < cut:
                        knots.add(q)
    points = sorted(knots)
    if points[1] != waist:
        raise ValueError("waist cap crosses a frozen scalar knot")
    cells = [(a, b) for a, b in zip(points, points[1:]) if a >= waist]
    selected, waist_record = {}, None
    provenance = []
    for path, part in parts:
        if part["radial_cells_total"] != len(cells):
            raise ValueError("bulk cell count differs from exact frozen knot partition")
        grouped = defaultdict(list)
        for row in part["accepted_cells"]:
            if not 0 <= row["index"] < len(cells):
                raise ValueError("accepted cell has an invalid exact-span index")
            grouped[row["index"]].append(row)
        for index, rows in grouped.items():
            complete = cover_rows(rows, *cells[index])
            if complete is not None:
                selected[index] = (path, complete)
        if "waist_integral" in part:
            waist_record = (path, part["waist_integral"])
        provenance.append({"path": str(path), "sha256": sha(path),
                           "accepted_subcells": len(part["accepted_cells"]),
                           "failed_subcells": len(part["failed_cells"])})
    missing = [j for j in range(len(cells)) if j not in selected]
    if missing or waist_record is None:
        raise ValueError(f"exact full bulk cover is missing cells {missing}; waist={waist_record is not None}")
    total = stored_ball(waist_record[1])
    cell_sums, selected_rows = [], 0
    for index in range(len(cells)):
        path, rows = selected[index]
        value = sum((stored_ball(row["integral"]) for row in rows), arb(0))
        total += value
        selected_rows += len(rows)
        cell_sums.append({"index": index, "left": str(cells[index][0]), "right": str(cells[index][1]),
                          "source_part": str(path), "subcells": len(rows), "integral": ball_record(value)})
    collar_value = stored_ball(collar["collar_integral"])
    beta = (total+collar_value)/2
    scaled = 2*arb(5).sqrt()*beta/arb.pi()
    lo = int(scaled.lower().floor().unique_fmpz())
    hi = int(scaled.upper().ceil().unique_fmpz())
    odd = [q for q in range(lo-4, hi+5) if q % 2]
    gaps = [abs(scaled-q).lower() for q in odd]
    norm_gap = min([arb(1)]+gaps)
    if not norm_gap > 0:
        norm_gap = arb(0)
    phase_gap = arb.pi()*norm_gap/(2*arb(5).sqrt())
    report = {"kind": "complete_actual_beta_integral_and_D5_norm_lattice_comparison", "complete": True,
        "input_sha256": input_sha, "source_sha256": sha(__file__),
        "native_source_sha256": native_sha, "bulk_source_sha256": bulk_sha, "box_source_sha256": box_sha,
        "collar_path": str(args.collar), "collar_sha256": sha(args.collar), "part_provenance": provenance,
        "exact_original_knot_cells": len(cells), "selected_subcells": selected_rows,
        "waist_path": str(waist_record[0]), "waist_width": str(waist), "fixed_cut": str(cut),
        "bulk_integral": ball_record(total), "collar_integral": ball_record(collar_value), "beta": ball_record(beta),
        "D5_scaled_beta": ball_record(scaled), "D5_odd_norm_gap_lower": ball_record(norm_gap),
        "D5_beta_lattice_distance_lower": ball_record(phase_gap.lower()),
        "D5_candidate_grid_points": [{"Q": q, "beta_grid": ball_record(arb.pi()*q/(2*arb(5).sqrt()))} for q in odd],
        "selected_cells": cell_sums,
        "limitations": ["The beta belongs only to the exact input hash above",
            "The D5 comparison does not transfer beta to a different mean/affine candidate",
            "The actual return rotation, full scattering remainder, low block, and nonlinear family need their own matching certificates"]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"beta": beta.str(30), "D5_norm_gap_lower": norm_gap.str(20),
                      "D5_phase_gap_lower": phase_gap.lower().str(20)}), flush=True)


if __name__ == "__main__":
    main()

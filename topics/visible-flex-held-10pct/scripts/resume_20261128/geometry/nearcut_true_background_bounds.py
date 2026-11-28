#!/usr/bin/env python3
"""Outward true-R58 background derivative bounds on a physical cut strip.

Reuse the already proved normalization, never a sampled radius/slope cache.
Complete original source pieces cover the requested physical interval. The
one-sided r_xx hull bounds the a.e. derivative of the continuous w_R, including
absolute-value cusps; it does not assert that the background is globally C3.
All detailed rational boxes are written only to the caller's scratch output.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2] / "resume_n4"))
from q060_true_background_oracle import Q060TrueBackgroundOracle


def ref(path):
    path = Path(path).resolve()
    with path.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    return {"path": str(path), "sha256": digest}


def upper_abs(oracle, value):
    row = oracle.bounds(value)
    return max(abs(Q(row["lower_exact"])), abs(Q(row["upper_exact"])))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--constants", type=Path, required=True)
    p.add_argument("--normalization", type=Path, required=True)
    p.add_argument("--width", type=float, default=0.02,
                   help="Literal binary64 width, interpreted as its exact rational.")
    p.add_argument("--subdivisions", type=int, default=128)
    p.add_argument("--max-depth", type=int, default=20)
    p.add_argument("--outdir", type=Path, required=True)
    a = p.parse_args()
    if not 1 <= a.subdivisions <= 4096 or not 1 <= a.max_depth <= 30:
        raise ValueError("Unsupported finite cover settings")
    a.outdir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    o = Q060TrueBackgroundOracle(a.constants, a.normalization)
    cut = Q.from_float(o.constants["parameters"]["rCut"])
    width = Q.from_float(a.width)
    rmin = cut - width
    if not 0 < width < cut:
        raise ValueError("Positive physical cut strip required")
    pieces, leaves = [], []
    maxima = {"w": Q(0), "w_R": Q(0), "w_RR_a.e.": Q(0)}
    minimum_rx = None
    covered = False
    for index in range(160 * 9):
        cell, segment = index // 9, 8 - index % 9
        r0 = o.primitives(cell, segment, 0)["r"]
        r1 = o.primitives(cell, segment, 1)["r"]
        piece = {"cell": cell, "segment": segment,
                 "inner_true_radius": o.bounds(r0),
                 "outer_true_radius": o.bounds(r1), "source_x": ["0", "1"]}
        stack = [(Q(k, a.subdivisions), Q(k+1, a.subdivisions), 0)
                 for k in reversed(range(a.subdivisions))]
        nleaves = 0
        while stack:
            left, right, depth = stack.pop()
            try:
                jets = o.local_jets(cell, segment, left, right)
                rx = jets["r_x"]
                wR = jets["w_x"] / rx
                wRR = (jets["w_xx"] * rx - jets["w_x"] *
                       jets["r_xx_one_sided_hull"]) / (rx ** 3)
                lower_rx = Q(o.bounds(rx)["lower_exact"])
                if lower_rx <= 0:
                    raise ArithmeticError("No strictly positive radius derivative")
                values = {"w": upper_abs(o, jets["w"]),
                          "w_R": upper_abs(o, wR),
                          "w_RR_a.e.": upper_abs(o, wRR)}
                # A finite enclosure is sufficient. Wide finite values are
                # reported honestly, not silently replaced by point values.
            except (ArithmeticError, ValueError, ZeroDivisionError):
                if depth >= a.max_depth:
                    raise
                middle = (left + right) / 2
                stack.extend([(middle, right, depth+1), (left, middle, depth+1)])
                continue
            for key, value in values.items():
                maxima[key] = max(maxima[key], value)
            minimum_rx = lower_rx if minimum_rx is None else min(minimum_rx, lower_rx)
            leaves.append({"cell": cell, "segment": segment,
                           "source_x": [str(left), str(right)],
                           "r_x_lower_exact": str(lower_rx),
                           "absolute_upper_exact": {k: str(v) for k,v in values.items()}})
            nleaves += 1
        piece["source_cover_leaves"] = nleaves
        pieces.append(piece)
        print(json.dumps({"cell": cell, "segment": segment,
                          "inner_radius_upper": o.bounds(r0)["upper"],
                          "leaves": nleaves,
                          "upper_display": {k: float(v) for k,v in maxima.items()},
                          "seconds": time.monotonic()-started}), flush=True)
        # For every admissible exact normalization, the included consecutive
        # source pieces extend below the requested lower physical endpoint.
        if Q(o.bounds(r0)["upper_exact"]) <= rmin:
            covered = True
            break
    if not covered:
        raise ArithmeticError("The declared original source pieces do not cover the strip")
    # Validate the exact source partition, not merely its sampled endpoints.
    for piece in pieces:
        rows = [row for row in leaves if
                (row["cell"], row["segment"]) == (piece["cell"], piece["segment"])]
        at = Q(0)
        for row in rows:
            left, right = map(Q, row["source_x"])
            if left != at or not left < right:
                raise ArithmeticError("Gap or overlap in original-source box cover")
            at = right
        if at != 1:
            raise ArithmeticError("Incomplete original-source piece")
    leaf_path = a.outdir / "source-boxes.json"
    leaf_path.write_text(json.dumps(leaves, separators=(",", ":")) + "\n")
    report = {"status": "true_R58_nearcut_background_first_and_lipschitz_second_bounds_certified",
              "source": ref(HERE), "oracle_provenance": o.provenance,
              "constants": ref(a.constants), "normalization": ref(a.normalization),
              "physical_interval_exact": [str(rmin), str(cut)],
              "literal_width_exact": str(width), "source_pieces": pieces,
              "source_boxes": ref(leaf_path), "source_box_count": len(leaves),
              "original_source_partition_exactly_verified": True,
              "physical_interval_covered_by_consecutive_monotone_source_pieces": True,
              "r_x_positive_lower_exact": str(minimum_rx),
              "absolute_upper_exact": {k: str(v) for k,v in maxima.items()},
              "absolute_upper_display": {k: float(v) for k,v in maxima.items()},
              "w_RR_interpretation": "a.e./one-sided derivative; w_R is continuous and piecewise absolutely continuous, hence this is its Lipschitz bound",
              "complete_normalization_recomputed": False,
              "finite_tail_field_or_nearcut_metric_certified": False,
              "seconds": time.monotonic()-started}
    report_path = a.outdir / "report.json"
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"report": ref(report_path), "status": report["status"],
                      "absolute_upper_display": report["absolute_upper_display"],
                      "source_box_count": len(leaves), "seconds": report["seconds"]}), flush=True)


if __name__ == "__main__":
    main()

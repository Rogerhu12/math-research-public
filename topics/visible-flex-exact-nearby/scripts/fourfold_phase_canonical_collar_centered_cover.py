#!/usr/bin/env python3
"""Continuous actual collar bounds with centered phase Taylor enclosures.

The raw cover and its source bounds remain separate from the Airy moment and
full-lag aggregation.  No final reflection norm or feedback cutoff is inferred
merely from a completed geometric/operator cover.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_canonical_collar_finite import (
    FiniteRootCoordinates, finite_canonical_operator,
    physical_polynomial_trial, root_potential_coefficients, trial_residual_coefficients,
)

from fourfold_phase_canonical_collar_centered import CenteredPhysicalRootGeometry as PhysicalRootGeometry

ROOT_ORDERS = {
    "cross_error": 6, "tangential_error": 7,
    "E12_normal": 5, "E12_angle": 6, "E22_angle": 7,
    "DB_without_Cphi": 2, "DB_Cphi": 3, "DC": 2,
    "LC_normal": 0, "LC_angle": 3, "LC_potential": 2,
    "LB_normal": 0, "LB_angle": 1, "LB_potential": 0,
    "trial_B": 0, "trial_C": 2,
    "B_y": 0, "B_phi": 0, "B_yphi": 0, "B_phiphi": 0,
    "C_y": 1, "C_phi": 2, "C_yphi": 1, "C_phiphi": 2}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def string(value):
    return arb(value).str(50)


def interval(value):
    return {"lower": string(value.lower()), "upper": string(value.upper())}


def uniform_derivative_row(value, radial_order, scale, angle_order=2):
    if value.m <= radial_order or value.n <= angle_order:
        raise ValueError("insufficient known mixed jet for the residual coefficient")
    # These are sup |partial_s^k partial_theta^j f| / k!.
    # After the complete radial cover, the root vanishing theorem permits
    # Taylor's integral formula to bound f/s^k and its theta derivatives.
    return [string((abs(value.coefficient(radial_order, j).real)
                    *math.factorial(j)/scale**radial_order).upper())
            for j in range(angle_order+1)]


def evaluate(model, left, right, radial_left, radial_right):
    angle = (exact_arb((left+right)/4)+arb(0, exact_arb((right-left)/4)))*arb.pi()
    model.prepare_offset(arb(0))
    root = model.principal(angle, at_root=True)
    coordinates = FiniteRootCoordinates(root, model.scale)
    root_values = root_potential_coefficients(root, model.scale)
    offset = exact_arb((radial_left+radial_right)/2)+arb(0, exact_arb((radial_right-radial_left)/2))
    model.prepare_offset(offset)
    actual = model.principal(angle)
    chart = coordinates.positive(offset, model.m-1, model.n)
    values = finite_canonical_operator(actual, chart, model.scale)
    amplitudes = physical_polynomial_trial(root_values, chart, offset, model.scale)
    residual = trial_residual_coefficients(values, amplitudes, model.scale)
    allvalues = {**values, **residual}
    positive = {}
    for name in ("defining_ratio", "ys", "pt", "J", "A11", "height", "physical_source_factor"):
        value = values[name].coefficient(0, 0).real
        if not value > 0:
            raise ValueError("finite true chart coefficient not positive: "+name)
        positive[name] = interval(value)
    return {
        "exact_quarter_interval": [str(left), str(right)],
        "exact_positive_radial_interval": [str(radial_left), str(radial_right)],
        "positive_chart_coefficients": positive,
        "derivative_sup_for_root_division": {
            name: uniform_derivative_row(allvalues[name], order, model.scale)
            for name, order in ROOT_ORDERS.items()},
        "ordinary_physical_theta_derivatives": {
            name: uniform_derivative_row(values[name], 0, model.scale)
            for name in ("defining_ratio", "height", "physical_source_factor",
                         "ys", "yt", "ps", "pt", "J", "A11")},
        "root_potential_physical_theta_derivatives": {
            name: [string((abs(value[j].real)*math.factorial(j)).upper())
                   for j in range(6)]
            for name, value in root_values.items()},
        "remaining_chart_angle_precision": coordinates.n}


def read(path):
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else Path(path).open()) as stream:
        return json.load(stream)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--half-width", type=Fraction, default=Fraction(1, 2500000))
    parser.add_argument("--root-certificate", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    parser.add_argument("--collar-height", type=Fraction, default=Fraction(1, 2048))
    parser.add_argument("--angle-cells", type=int, default=256)
    parser.add_argument("--first-cell", type=int, default=0)
    parser.add_argument("--last-cell", type=int, default=128)
    parser.add_argument("--radial-cells", type=int, default=1)
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--continue-after-failure", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if (not 0 <= args.first_cell < args.last_cell <= args.angle_cells//2
            or args.angle_cells % 2 or args.collar_height <= 0 or args.radial_cells < 1):
        raise ValueError("invalid actual half-quarter/collar range")
    ctx.prec, ctx.cap = args.bits, 32
    start = time.monotonic()
    model = PhysicalRootGeometry(args.object, args.half_width, args.root_certificate,
                                 nodes=args.nodes, radial_precision=10, angle_precision=16)
    config = {"source_sha256": sha(__file__),
              "phase_centered_engine_source_sha256": sha(Path(__file__).with_name("fourfold_phase_canonical_collar_centered.py")),
              "phase_taylor_source_sha256": sha(Path(__file__).with_name("fourfold_phase_root_potential_complex_strip.py")),
              "engine_source_sha256": sha(Path(__file__).with_name("fourfold_phase_canonical_collar_finite.py")),
              "object": provenance(model.target, args.object),
              "root_certificate_sha256": sha(args.root_certificate),
              "exact_collar_height": str(args.collar_height),
              "initial_angle_cells": args.angle_cells,
              "first_cell": args.first_cell, "last_cell": args.last_cell,
              "radial_cells": args.radial_cells, "maximum_angle_bisection_depth": args.max_depth,
              "nodes": args.nodes, "bits": args.bits,
              "dependencies": {name: sha(Path(__file__).parent/name) for name in (
                  "fourfold_phase_canonical_root_jets.py", "fourfold_time_angle_jets.py",
                  "fourfold_phase_beta_interval.py", "fourfold_phase_beta_bulk_interval.py")}}
    if args.resume:
        report = read(args.out)
        if report["configuration"] != config or report["failed_cells"]:
            raise ValueError("resumed cover has changed identities or unhandled failures")
        queue = deque((Fraction(a), Fraction(b), Fraction(c), Fraction(d), depth)
                      for a, b, c, d, depth in report["pending"])
        old_seconds = report["seconds"]
    else:
        queue = deque((Fraction(j, args.angle_cells), Fraction(j+1, args.angle_cells),
                       args.collar_height*k/args.radial_cells,
                       args.collar_height*(k+1)/args.radial_cells, 0)
                      for k in range(args.radial_cells)
                      for j in range(args.first_cell, args.last_cell))
        report = {
            "kind": "actual_finite_canonical_positive_collar_continuous_cover",
            "proved": False, "configuration": config, "cells": [], "failed_cells": [],
            "attempts": 0, "seconds": 0,
            "root_division_orders": ROOT_ORDERS,
            "scope": ["Same exact affine common parameter box and true moving root.",
                      "Physical positive root strip; negative cap follows exact radial symmetry.",
                      "Half-quarter is evaluated; exact D4 reflection supplies the second half.",
                      "Completed coefficient bounds alone do not assert an Airy operator norm or feedback inverse."]}
        old_seconds = 0

    def save():
        report["seconds"] = old_seconds+time.monotonic()-start
        report["pending"] = [[str(a), str(b), str(c), str(d), depth] for a, b, c, d, depth in queue]
        args.out.parent.mkdir(parents=True, exist_ok=True)
        temporary = args.out.with_suffix(args.out.suffix+".tmp")
        with (gzip.open(temporary, "wt") if str(args.out).endswith(".gz") else temporary.open("w")) as stream:
            json.dump(report, stream, indent=2)
            stream.write("\n")
        temporary.replace(args.out)

    while queue:
        left, right, radial_left, radial_right, depth = queue.popleft()
        report["attempts"] += 1
        try:
            row = evaluate(model, left, right, radial_left, radial_right)
            row["bisection_depth"] = depth
            report["cells"].append(row)
        except (ValueError, ZeroDivisionError) as exc:
            if depth < args.max_depth:
                middle = (left+right)/2
                queue.appendleft((middle, right, radial_left, radial_right, depth+1))
                queue.appendleft((left, middle, radial_left, radial_right, depth+1))
            else:
                report["failed_cells"].append({
                    "angle_interval": [str(left), str(right)],
                    "radial_interval": [str(radial_left), str(radial_right)], "reason": str(exc)})
                if not args.continue_after_failure:
                    save()
                    print(json.dumps({"stopped_on_unresolved_cell": report["failed_cells"][-1],
                                      "accepted": len(report["cells"])}), flush=True)
                    return
        if report["attempts"] % 16 == 0:
            save()
            print(json.dumps({"attempts": report["attempts"], "accepted": len(report["cells"]),
                              "pending": len(queue), "failed": len(report["failed_cells"]),
                              "seconds": report["seconds"]}), flush=True)
    # Every specified exact radial slab must have its exact angular tiling.
    for k in range(args.radial_cells):
        radial = [str(args.collar_height*k/args.radial_cells),
                  str(args.collar_height*(k+1)/args.radial_cells)]
        rows = sorted((r for r in report["cells"] if r["exact_positive_radial_interval"] == radial),
                      key=lambda r: Fraction(r["exact_quarter_interval"][0]))
        cursor = Fraction(args.first_cell, args.angle_cells)
        for row in rows:
            a, b = map(Fraction, row["exact_quarter_interval"])
            if a != cursor:
                raise ValueError("actual finite collar cover has a gap or overlap")
            cursor = b
        if cursor != Fraction(args.last_cell, args.angle_cells):
            raise ValueError("actual finite collar cover is incomplete")
    report["proved"] = (args.first_cell == 0 and args.last_cell == args.angle_cells//2
                        and not report["failed_cells"])
    report["covered_specified_range"] = not report["failed_cells"]
    save()
    print(json.dumps({"proved": report["proved"], "accepted": len(report["cells"]),
                      "seconds": report["seconds"]}), flush=True)


if __name__ == "__main__":
    main()

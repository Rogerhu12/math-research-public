#!/usr/bin/env python3
"""Independently check the exact closed cover and rational R80 conclusions.

This is a finite collector, not a replacement for the interval computation.
It does not trust a stored global maximum or a completed-index flag.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_affine import load_definition


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as f:
        return json.load(f)


def binary(value):
    return Fraction.from_float(float(value))


def exact_endpoint(value):
    m, e = value.man_exp()
    return Fraction(int(m)) * Fraction(2) ** int(e)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    base = "data/phase_ring_continuation/"
    parser.add_argument("--source-report", default=base+"type_fixed_step02_d5_step5_fixed_tau_parameter_source_full.json.gz")
    parser.add_argument("--object", default=base+"type_fixed_step02_d5_exact_affine_step5_object.json")
    parser.add_argument("--local-jets", default=base+"type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    parser.add_argument("--existence", default=base+"type_fixed_step02_d5_step5_real_parameter_return_existence.json")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    ctx.prec = 192
    report, root, existence = map(read, (args.source_report, args.local_jets, args.existence))
    _, origin, direction, center = load_definition(args.object)
    assert report["center_object_sha256"] == sha(args.object)
    assert report["origin_inputs_sha256"] == sha(origin)
    assert report["direction_sha256"] == sha(direction)
    assert report["local_root_jets_sha256"] == sha(args.local_jets)
    assert report["existence_inputs_sha256"] == sha(args.existence)
    assert existence["target_object_sha256"] == sha(args.object)
    assert existence["proved"] and root["proved"]
    assert Fraction(existence["coarse_physical_time_field_bound"]) == 5
    source = Path(__file__).with_name("fourfold_phase_fixed_tau_parameter_bounds.py")
    assert report["actual_source_sha256"] == report["source_sha256"] == sha(source)
    for name, digest in report["actual_dependency_sha256"].items():
        assert sha(Path(__file__).with_name(name)) == digest, name
    parameter = list(map(Fraction, report["exact_parameter_interval"]))
    requested = [center-Fraction(1, 2000000), center+Fraction(1, 2000000)]
    assert parameter == requested
    elo, ehi = map(Fraction, existence["exact_parameter_interval"])
    rlo, rhi = map(Fraction, root["exact_parameter_interval"])
    assert elo <= parameter[0] < parameter[1] <= ehi
    assert rlo <= parameter[0] < parameter[1] <= rhi
    tlo, thi = map(binary, root["root_interval"])
    split = Fraction(report["fixed_s_turn_split"])
    # The scan uses its own exact binary endpoints; they enclose the saved
    # local root, and their exact end is supplied in the cover.
    radial_end = Fraction(report["exact_positive_bulk_radial_cover"][1])
    scan_thi = radial_end / split
    turn_lo, turn_hi = map(Fraction, report["turn"]["exact_radial_envelope"])
    scan_tlo = turn_lo / split
    assert scan_tlo <= tlo <= thi <= scan_thi
    assert turn_hi == scan_thi
    assert list(map(Fraction, report["turn"]["fixed_s_interval"])) == [split, Fraction(1)]
    knots = {Fraction(0), radial_end}
    with np.load(origin, allow_pickle=False) as frozen:
        for key in frozen.files:
            if key.endswith("_knots"):
                for value in frozen[key]:
                    knot = binary(value)
                    for signed in (knot, -knot):
                        if 0 < signed < radial_end:
                            knots.add(signed)
    points = sorted(knots)
    cells = list(zip(points, points[1:]))
    assert len(cells) == report["total_common_cells"]
    leaves = report["rows"]
    assert report["turn"]["proved"]
    actual_counts = []
    for index, cell in enumerate(cells):
        pieces = sorted(tuple(map(Fraction, row["exact_radial_interval"]))
                        for row in leaves if row["common_cell_index"] == index)
        assert pieces and pieces[0][0] == cell[0] and pieces[-1][1] == cell[1]
        assert all(a < b for a, b in pieces)
        assert all(pieces[j][1] == pieces[j+1][0] for j in range(len(pieces)-1))
        actual_counts.append(len(pieces))
    assert sum(actual_counts) == len(leaves)
    assert all(row["proved"] for row in leaves)
    safe = {"physical_field_upper": 4,
            "physical_field_parameter_first_upper": 20,
            "physical_field_parameter_second_upper": 200}
    maxima = {}
    for key, bound in safe.items():
        upper = max(arb(row[key]["upper"]).upper() for row in leaves+[report["turn"]])
        assert upper < bound, key
        maxima[key] = {"upper": str(upper), "safe_strict_rational_bound": str(bound)}
    out = dict(kind="R80 exact-cover and rational-bound finite certificate", proved=True,
        source_sha256=sha(__file__), source_report_sha256=sha(args.source_report),
        actual_computation_source_sha256=sha(source), object_sha256=sha(args.object),
        origin_inputs_sha256=sha(origin), direction_sha256=sha(direction),
        local_root_jets_sha256=sha(args.local_jets), existence_inputs_sha256=sha(args.existence),
        exact_parameter_interval=list(map(str, parameter)), physical_theta_strip=report["physical_theta_strip"],
        exact_bulk_radial_cover=["0",str(radial_end)], common_cells=len(cells),
        proved_bulk_leaves=len(leaves), subdivision_counts=actual_counts,
        failed_coarse_attempts_retained=len(report["attempts"]),
        exact_turn_s_cover=[str(split),"1"], both_signs_and_negative_half_by_exact_reflection=True,
        explicit_R75_physical_field_bound_verified="5", bounds=maxima,
        limitations=["Checks finite coverage, recorded inequalities and identities; the source/proof justify each directed leaf.",
                     "This does not certify a flow, a signed time integral, a nonzero twist, or R31 PQT constants."])
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"proved":True,"common_cells":len(cells),"leaves":len(leaves),"bounds":maxima,"out":args.out}))


if __name__ == "__main__":
    main()

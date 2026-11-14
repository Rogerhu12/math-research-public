#!/usr/bin/env python3
"""Complete the true canonical root jet circle from its D4 half-quarter.

The input remains a partial-angle native report.  This separate certificate
uses the exact reflected scalar/operator identity proved in R83, and checks
an exact Fraction tiling of the entire circle orbit before declaring success.
No missing numerical cells are synthesized as if they had been evaluated.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if str(path).endswith(".gz") else path.open()) as stream:
        return json.load(stream)


def lower(value):
    return arb(value["lower"]).lower()


def upper(value):
    return arb(value["upper"]).upper()


def modulus(value):
    a, b = lower(value), upper(value)
    if not a.is_finite() or not b.is_finite() or not a <= b:
        raise ValueError("invalid finite real jet coefficient interval")
    return max(abs(a), abs(b)).upper()


def canonical_sha(row):
    return hashlib.sha256(json.dumps(row, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--common", type=Path, default=Path("notes/2026-11-12-common-core-exterior-parameter-interval.json"))
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    raw, common = read(args.raw), read(args.common)
    here = Path(__file__).parent
    native = here/"fourfold_phase_canonical_root_jets.py"
    if raw["kind"] != "actual_grounded_canonical_root_finite_jets" or raw["source_sha256"] != sha(native):
        raise ValueError("native partial root-jet source identity mismatch")
    for name, digest in raw["dependency_sha256"].items():
        if sha(here/name) != digest:
            raise ValueError("native root-jet dependency changed: "+name)
    if raw["parameter_adapter_source_sha256"] != sha(here/"fourfold_phase_beta_parameter_germ.py"):
        raise ValueError("native exact-affine adapter identity mismatch")
    if sha(raw["center_object_path"]) != raw["center_object_sha256"]:
        raise ValueError("exact center object identity changed")
    if sha(raw["root_certificate_path"]) != raw["root_certificate_sha256"]:
        raise ValueError("actual moving-root certificate identity changed")
    box = list(map(Fraction, raw["exact_parameter_interval"]))
    if box != list(map(Fraction, common["chosen_closed_interval"])):
        raise ValueError("root jets are not on the exact common core/exterior box")
    if raw["failed_cells"]:
        raise ValueError("raw report contains failed angular cells")
    fields = [name+"_canonical_angle_derivatives" for name in (
        "V_root", "V_xi_root", "root_momentum_shear", "physical_height",
        "source_root_factor", "grounded_flux_root_factor")]
    positives = ("alpha", "B", "Y_prime", "t0", "physical_Fz", "D", "W")
    half = []
    for row in raw["cells"]:
        a, b = map(Fraction, row["exact_quarter_interval"])
        if b <= Fraction(1, 2):
            if not 0 <= a < b:
                raise ValueError("invalid positive half-quarter interval")
            for name in positives:
                if not lower(row[name]) > 0:
                    raise ValueError("unresolved positive root factor: "+name)
            if not lower(row["physical_support_numerator"]) > 0:
                raise ValueError("unresolved true support numerator")
            for field in fields:
                if len(row[field]) != raw["canonical_angle_order"]+1:
                    raise ValueError("inconsistent canonical jet order")
                for coefficient in row[field]:
                    modulus(coefficient)
            half.append((a, b, row))
        elif a < Fraction(1, 2):
            raise ValueError("an evaluated cell straddles the reflection fixed angle")
    half.sort(key=lambda item: item[0])
    cursor = Fraction(0)
    for a, b, row in half:
        if a != cursor:
            raise ValueError("the evaluated half-quarter is incomplete or overlaps")
        cursor = b
    if cursor != Fraction(1, 2):
        raise ValueError("the evaluated half-quarter has not reached pi/4")
    virtual = [(a, b) for a, b, row in half]+[(1-b, 1-a) for a, b, row in half]
    cursor = Fraction(0)
    for a, b in sorted(virtual):
        if a != cursor:
            raise ValueError("the actual reflection orbits do not tile the quarter")
        cursor = b
    if cursor != 1:
        raise ValueError("the quarter reflection cover is incomplete")
    bounds = {}
    for field in fields:
        bounds[field] = [ball_record(max(modulus(row[field][j]) for a, b, row in half))
                         for j in range(raw["canonical_angle_order"]+1)]
    for name in positives:
        bounds[name] = {"lower": ball_record(min(lower(row[name]) for a, b, row in half)),
                        "upper": ball_record(max(upper(row[name]) for a, b, row in half))}
    lo_mean, hi_mean = arb(0), arb(0)
    for a, b, row in half:
        lo_mean += 2*exact_arb(b-a)*lower(row["Y_prime"])
        hi_mean += 2*exact_arb(b-a)*upper(row["Y_prime"])
    report = {"kind": "actual_canonical_root_jets_full_D4_reflection_cover", "proved": True,
              "complete": True, "source_sha256": sha(__file__),
              "raw_partial_report": {"path": str(args.raw), "sha256": sha(args.raw),
                  "original_proved_flag": raw["proved"], "used_evaluated_half_quarter_only": True},
              "dependency_sha256": {"fourfold_phase_canonical_root_jets.py": sha(native),
                  "fourfold_phase_beta_bulk_interval.py": sha(here/"fourfold_phase_beta_bulk_interval.py"),
                  "fourfold_phase_beta_interval.py": sha(here/"fourfold_phase_beta_interval.py")},
              "common_parameter_input_sha256": sha(args.common), "bits": args.bits,
              "exact_parameter_interval": list(map(str, box)),
              "origin_inputs_sha256": raw["origin_inputs_sha256"], "direction_sha256": raw["direction_sha256"],
              "root_certificate_sha256": raw["root_certificate_sha256"],
              "evaluated_half_quarter_leaf_count": len(half), "derived_quarter_leaf_count": len(virtual),
              "exact_evaluated_quarter_fraction": ["0", "1/2"],
              "exact_completed_quarter_fraction": ["0", "1"],
              "symmetry": {"physical_angle": "theta -> pi/2-theta",
                           "canonical_angle": "phi -> ell/4-phi",
                           "even_fields": list(positives)+[f.removesuffix("_canonical_angle_derivatives") for f in fields],
                           "odd_field": "q=M/D", "derivative_sign": "(-1)^canonical_derivative_order"},
              "uniform_bounds": bounds,
              "canonical_circumference": {"lower": ball_record((2*arb.pi()*lo_mean).lower()),
                                           "upper": ball_record((2*arb.pi()*hi_mean).upper())},
              "canonical_full_circle_frequency": {"lower": ball_record((1/hi_mean).lower()),
                                                   "upper": ball_record((1/lo_mean).upper())},
              "evaluated_leaf_manifest": [{"exact_quarter_interval": [str(a), str(b)],
                                            "canonical_row_sha256": canonical_sha(row)} for a, b, row in half],
              "scope": ["The raw native report is retained as partial; full coverage additionally uses the exact R83 reflection proof.",
                        "All fourfold physical angles and both actual radial roots are covered on the same exact parameter box.",
                        "No full canonical collar residual or final feedback inverse is asserted."]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with (gzip.open(args.out, "wt") if str(args.out).endswith(".gz") else args.out.open("w")) as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"complete": True, "evaluated_leaves": len(half), "report_sha256": sha(args.out)}))


if __name__ == "__main__":
    main()

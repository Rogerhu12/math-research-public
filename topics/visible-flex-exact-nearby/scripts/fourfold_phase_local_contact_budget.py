#!/usr/bin/env python3
"""R85: actual localized whole-cap Poisson/contact constants, including mean.

The source is supported in the existing true root-to-quarter collar.  The
solution and both contact outputs belong to the same complete R74 exterior.
No scalar source, root mean, or regular mean-flux row is dropped.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb, ctx

from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def lower(record):
    return arb(record["lower"]).lower()


def upper(record):
    return arb(record["upper"]).upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--collar", type=Path, default=Path("notes/2026-11-12-positive-family-root-collar.json"))
    parser.add_argument("--closed", type=Path, default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    parser.add_argument("--robin", type=Path, default=Path("notes/2026-11-12-actual-exterior-robin-certificate.json"))
    parser.add_argument("--common", type=Path, default=Path("notes/2026-11-12-common-core-exterior-parameter-interval.json"))
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    collar, closed, robin, common = [json.loads(p.read_text())
                                   for p in (args.collar, args.closed, args.robin, args.common)]
    if not all(d.get("complete") for d in (collar, closed, robin)):
        raise ValueError("all actual exterior inputs must be complete")
    if sha(args.collar) not in closed["input_sha256"].values():
        raise ValueError("the localized collar is not part of this closed object")
    if sha(args.closed) not in robin["input_sha256"].values():
        raise ValueError("the true Robin tail is not attached to this closed object")
    for key in ("origin_inputs_sha256", "direction_sha256"):
        if len({d[key] for d in (collar, closed, robin)}) != 1:
            raise ValueError("incompatible exact affine exterior objects")
    interval = list(map(Fraction, common["chosen_closed_interval"]))
    for d in (collar, closed, robin):
        left, right = map(Fraction, d["exact_parameter_interval"])
        if not left <= interval[0] <= interval[1] <= right:
            raise ValueError("the common box exceeds the actual exterior family")
    local = collar["operator_constants"]
    global_values = closed["complete_finite_positive_operator"]
    ell_lo, ell_hi = lower(local["length_lower"]), upper(local["length_upper"])
    m, M = lower(local["m_lower"]), upper(local["M_upper"])
    L_lo, MG = lower(global_values["length_lower"]), upper(global_values["matrix_upper"])
    if not 0 < ell_lo <= ell_hi < L_lo or not m > 0:
        raise ValueError("invalid true collar length or positive form constants")
    extension = max(1/ell_lo, arb(13)/12).upper()
    root_energy = (M*extension).upper()
    mean_energy = (MG/L_lo).upper()
    root_square = ((4+ell_hi**2)*root_energy/m+4+2*ell_hi).upper()
    mean_square = ((4+ell_hi**2)*mean_energy/m).upper()
    full = (root_square+mean_square).sqrt().upper()
    high_root = ((4+ell_hi**2)*M*arb(13)/(12*m)+4+2*ell_hi).sqrt().upper()
    if not full < 800 or not high_root < 90:
        raise ValueError("the proposed strict localized contact bounds did not pass")
    values = dict(collar_length_lower=ell_lo, collar_length_upper=ell_hi,
                  collar_matrix_lower=m, collar_matrix_upper=M,
                  whole_length_lower=L_lo, whole_matrix_upper=MG,
                  gradient_extension_squared=extension,
                  root_extension_energy_squared=root_energy,
                  regular_mean_extension_energy_squared=mean_energy,
                  root_localized_Poisson=root_square.sqrt().upper(),
                  regular_mean_localized_Poisson=mean_square.sqrt().upper(),
                  complete_localized_Poisson_and_contact=full,
                  high_root_localized_Poisson=high_root,
                  sufficient_high_frequency=((2/ell_lo)**(arb(3)/2)).upper())
    report = {"kind": "actual_complete_exterior_localized_root_collar_contact", "proved": True,
              "source_sha256": sha(__file__), "dependency_sha256": {
                  "fourfold_phase_beta_interval.py": sha(Path(__file__).with_name("fourfold_phase_beta_interval.py"))},
              "input_sha256": {str(p): sha(p) for p in (args.collar, args.closed, args.robin, args.common)},
              "exact_parameter_interval": list(map(str, interval)),
              "origin_inputs_sha256": closed["origin_inputs_sha256"],
              "direction_sha256": closed["direction_sha256"], "bits": args.bits,
              "constants": {k: ball_record(v) for k, v in values.items()},
              "spaces": {"trace": "H^(1/3)(root physical shear angle) direct_sum C regular physical mean",
                         "localized_source": "L2_x H^(-2/3), supported in the true root-to-quarter collar",
                         "contact": "H^(-1/3) root conormal direct_sum C regular mean flux"},
              "scope": ["The Poisson solution uses the entire same actual R74 exterior and true full-tail Robin.",
                        "Both mean slots and all source-contact cross terms remain in the Hilbert direct sum.",
                        "The coefficient in the report is in the actual grounded shear coordinates.",
                        "Sources outside the collar and regular loads retain the complete R81 bounds.",
                        "No whole-collar canonical Airy residual or feedback cutoff is asserted here."]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"proved": True, "complete_contact_upper": full.str(25),
                      "report_sha256": sha(args.out)}, indent=2))


if __name__ == "__main__":
    main()

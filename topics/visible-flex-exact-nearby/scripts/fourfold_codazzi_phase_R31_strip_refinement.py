#!/usr/bin/env python3
"""Recheck R31 losses and the physical conjugacy domain from a completed CI gate.

This consumes already proved whole-family constants. Each candidate loss is
independently checked; unsuccessful candidates are preserved. A physical
Wiener conjugacy strip is asserted only after the complete inverse-domain fee.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import os
from pathlib import Path
from flint import arb, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, ROOT
from fourfold_codazzi_phase_Wiener_transport_lift import upper
from fourfold_codazzi_phase_terminal_postcomposition import trig_norm
import fourfold_codazzi_phase_explicit_family_R31 as original_source
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

LOSSES = (Fraction(3, 200), Fraction(1, 100), Fraction(3, 400),
          Fraction(1, 200), Fraction(1, 250), Fraction(7, 2000),
          Fraction(3, 1000), Fraction(1, 400))
PHYSICAL = Fraction(1, 128)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--R31", type=Path, required=True)
    p.add_argument("--postcomposition", type=Path, required=True)
    p.add_argument("--root-contract", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("run mathematical refinement in the public repository's real Actions job")
    if args.out.exists():
        raise FileExistsError("preserve every actual completed loss refinement")
    ctx.prec = 320
    base, post, root = read(args.R31), read(args.postcomposition), read(args.root_contract)
    if (not base["complete"] or base["source_sha256"] != sha(original_source.__file__)
            or sha(args.root_contract) != ROOT or not post["complete"]
            or base["inputs"]["postcomposition"]["sha256"] != sha(args.postcomposition)
            or base["initial_lift"] != "identity"):
        raise ValueError("the actual completed same-coordinate R31 gate is required")
    epsilon = upper(base["complete_initial_error"])
    C, Z, LH, La = (upper(base[k]) for k in ("R31_C", "R31_Z", "LH", "La"))
    R0, sigma0 = exact_arb(Fraction(base["R0"])), exact_arb(Fraction(base["sigma0"]))
    s0 = Fraction(base["normalized_initial_KAM_strip"])
    S = Fraction(base["normalized_R31_family_strip"])
    ra = Fraction(base["exact_parameter_radius"])
    allowance = min(z.lower() for z in (1/(32*C), 1/(4*R0*LH), sigma0/(8*Z)))
    ha, hb = (list(map(Fraction, root[k])) for k in
              ("exact_H_sine_coefficients", "exact_H_cosine_coefficients"))
    ka, kb = (list(map(Fraction, post[k])) for k in
              ("exact_postcomposition_sine_coefficients", "exact_postcomposition_cosine_coefficients"))
    width = exact_arb(PHYSICAL)
    h0, h1 = trig_norm(ha, hb, width), trig_norm(ha, hb, width, 1)
    k0, k1 = trig_norm(ka, kb, width+h0), trig_norm(ka, kb, width+h0, 1)
    G0, G1 = (h0+k0).upper(), ((1+h1)*(1+k1)).upper()
    real_G1 = ((1+trig_norm(ha, hb, arb(0), 1))
               *(1+trig_norm(ka, kb, arb(0), 1))).upper()
    rows, eligible = [], []
    for loss in LOSSES:
        d = exact_arb(loss)
        final = s0-4*loss
        threshold = (d*d*allowance).lower()
        parameter = (2*La*epsilon).upper()
        coordinate = (2*LH*epsilon/d).upper()
        derivative = (2*LH*epsilon/(d*d)).upper()
        param_margin = (exact_arb(ra)-parameter).lower()
        angular_margin = (exact_arb(S-s0)-coordinate).lower()
        inverse_domain = (exact_arb(final-4*PHYSICAL)-4*G0-coordinate).lower()
        valid = bool(0 < loss < s0/4 and loss <= 1 and epsilon <= threshold
                     and param_margin > 0 and angular_margin > 0)
        physical = bool(valid and derivative < 1 and inverse_domain > 0)
        row = dict(exact_loss=str(loss), normalized_final_strip=str(final),
            R31_smallness_threshold=record(threshold), actual_R31_gates_passed=valid,
            parameter_change=record(parameter), normalized_conjugacy_change=record(coordinate),
            normalized_conjugacy_derivative_change=record(derivative),
            parameter_margin=record(param_margin), R31_composition_margin=record(angular_margin),
            physical_inverse_composition_margin=record(inverse_domain),
            physical_conjugacy_A1over128_proved=physical)
        if physical:
            row["physical_true_conjugacy_minus_G_norm"] = record((coordinate/4).upper())
            row["physical_true_conjugacy_derivative_minus_Gprime_norm"] = record((G1*derivative/(1-derivative)).upper())
            row["physical_true_conjugacy_derivative_Astrip_upper"] = record((G1/(1-derivative)).upper())
            row["physical_true_conjugacy_real_derivative_upper"] = record((real_G1/(1-derivative)).upper())
        rows.append(row)
        if valid:
            eligible.append((loss, row))
    if not eligible:
        raise ArithmeticError("even the original proved R31 loss did not pass its immutable constants")
    _, chosen = min(eligible, key=lambda z: z[0])
    output = dict(kind="actual_public_R31_smaller_loss_and_physical_conjugacy_strip",
        complete=True, source_sha256=sha(__file__), R31_native_sha256=sha(args.R31),
        postcomposition_native_sha256=sha(args.postcomposition), root_contract_sha256=ROOT,
        public_run_id=os.environ.get("GITHUB_RUN_ID"), public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        physical_requested_strip=str(PHYSICAL), exact_G_periodic_norm=record(G0),
        exact_G_derivative_norm=record(G1), all_actual_loss_trials=rows, selected=chosen,
        true_explicit_family_parameter_conjugacy_proved=True,
        physical_true_conjugacy_strip_proved=chosen["physical_conjugacy_A1over128_proved"],
        circle_homological_K=base["circle_K"],
        target15_native_sha256=base["inputs"]["target"]["sha256"],
        principal_fourth_root_gap="1/68",
        original_genuine_PDE_branch_or_full_body_inverse_claimed=False,
        first_scalar_phase_and_strong_operator_remainder_not_paid=True)
    save(args.out, output)
    print(dict(complete=True, selected_loss=chosen["exact_loss"],
        normalized_final_strip=chosen["normalized_final_strip"],
        physical_A1over128=chosen["physical_conjugacy_A1over128_proved"],
        physical_domain_margin=chosen["physical_inverse_composition_margin"]["ball"]), flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Give the exact same-background full-response error gate for the K48 row.

The original all-frequency response-return constants are proved in the fixed
R133 complete counterterm theorem. The norm of q_nu-Z is an explicit hypothesis;
this consumer does not manufacture a PDE inverse or a nonlinear solution.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from fourfold_codazzi_phase_complete_transport_cover import read
import fourfold_codazzi_phase_K48_parameter_row as row_source
from fourfold_codazzi_phase_Wiener_transport_lift import upper
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parameter-row", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve the complete response error contract")
    ctx.prec = 320
    row = read(args.parameter_row)
    if not row["complete"] or row["source_sha256"] != sha(row_source.__file__):
        raise ValueError("the actual full K48 parameter row is required")
    Gmax = ((1+upper(row["K48_real_derivative_minus_one_upper"]))
            *upper(row["old_H_derivative_A0_upper"])).upper()
    sigma = box_from_record(row["genuine_physical_parameter_row_lower"]).lower()
    constants = {"energy": Fraction(1273240, 10**6), "ordinary_L2": Fraction(1274436, 10**6)}
    epsilon = exact_arb(Fraction(1, 6500))
    data = {}
    for name, c in constants.items():
        functional = (Gmax*exact_arb(c)).upper()
        remaining = (sigma-functional*epsilon).lower()
        data[name] = dict(original_complete_return_error_constant=str(c),
            corrected_coordinate_full_row_error_constant=record(functional),
            conditional_remaining_physical_parameter_row=record(remaining),
            conditional_remaining_normalized_parameter_row=record((4*remaining).lower()),
            preserves_physical_row_above_one_over600=bool(remaining > exact_arb(Fraction(1, 600))))
    passed = all(x["preserves_physical_row_above_one_over600"] for x in data.values())
    result = dict(kind="conditional_same_background_K48_full_response_error_contract",
        complete=passed, source_sha256=sha(__file__), parameter_row_sha256=sha(args.parameter_row),
        fixed_prior_full_response_theorem="R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md, P.1 and P.17-P.25",
        complete_negative_body_and_true_root_and_even_mean_retained=True,
        actual_corrected_coordinate_derivative_sup=record(Gmax),
        actual_explicit_physical_row_lower=record(sigma),
        required_exact_response_error_upper="1/6500", response_norm_conventions={
            "energy": "L2_r of normalized-angular (|e1|^2+q^2|e2|^2)^(1/2), full even mean",
            "ordinary_L2": "L2_r L2_phi of the full physical pair, normalized angular measure"},
        paid_contracts=data, true_conjugacy_not_required_for_this_average_identity=True,
        fixed_metric_and_identical_continuous_background_required=True,
        q_nu_minus_Z_actual_bound_consumed=False,
        full_PDE_inverse_and_nonlinear_background_change_not_claimed=True,
        original_regular_mean_and_fourth_mode_rows_must_remain_in_q_nu=True)
    save(args.out, result)
    print(dict(complete=passed, G_derivative=Gmax.str(15),
        remaining={k: v["conditional_remaining_physical_parameter_row"]["ball"] for k, v in data.items()}), flush=True)
    if not passed:
        raise ArithmeticError("the actual complete response-error gate leaves insufficient parameter margin")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Pay the actual K48 change of the explicit-family parameter row.

For F_delta=G P_delta G^{-1}, G=K48 H, the initial KAM lift is the
identity. Its parameter row is independent of the chosen constant target.
The unknown genuine PDE response is not substituted for the explicit Z.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, ROOT
from fourfold_codazzi_phase_terminal_postcomposition import trig_norm
import fourfold_codazzi_phase_terminal_postcomposition as post_source
import fourfold_codazzi_phase_actual169_transversality as twist_source
from fourfold_codazzi_phase_Wiener_transport_lift import upper
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--postcomposition", type=Path, required=True)
    p.add_argument("--actual-twist", type=Path, required=True)
    p.add_argument("--root-contract", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve the complete corrected parameter row")
    ctx.prec = 320
    post, old, root = read(args.postcomposition), read(args.actual_twist), read(args.root_contract)
    if (not post["complete"] or not post["whole_negative_domain"] or not old["complete"]
            or post["source_sha256"] != sha(post_source.__file__)
            or old["source_sha256"] != sha(twist_source.__file__)
            or not old["actual_final_full_transport_defect_consumed"]
            or sha(args.root_contract) != ROOT or len(post["exact_postcomposition_sine_coefficients"]) != 48):
        raise ValueError("the actual K48 and completed169 explicit-family inputs are required")
    a = list(map(Fraction, root["exact_H_sine_coefficients"]))
    b = list(map(Fraction, root["exact_H_cosine_coefficients"]))
    Hmax = (1+trig_norm(a, b, arb(0), 1)).upper()
    P1 = upper(old["genuine_return_parameter_derivative_sup"])
    kappa = upper(post["postcomposition_real_derivative_minus_one_norm"])
    fee = ((2*kappa+kappa*kappa)*Hmax*Hmax*P1).upper()
    original = box_from_record(old["complete_physical_R31_parameter_twist_lower"]).lower()
    lower = (original-fee).lower()
    ok = bool(lower > exact_arb(Fraction(1, 540)))
    result = dict(kind="actual_K48_conjugated_explicit_family_parameter_row",
        complete=ok, source_sha256=sha(__file__),
        postcomposition_native_sha256=sha(args.postcomposition),
        actual_twist_native_sha256=sha(args.actual_twist), root_contract_sha256=ROOT,
        exact_family="F_delta=G P_delta G^{-1}, G=K48 o H; Q_delta=Qbar+delta Z, nu_delta=nu0+delta",
        physical_mean_parameter_row="<G'(P) d_delta P G'>",
        old_H_derivative_A0_upper=record(Hmax), true_return_parameter_sup=record(P1),
        K48_real_derivative_minus_one_upper=record(kappa),
        paid_full_parameter_row_change=record(fee),
        genuine_physical_parameter_row_lower=record(lower),
        genuine_normalized_circle_parameter_row_lower=record((4*lower).lower()),
        exact_initial_KAM_lift="identity", initial_KAM_M0="1", initial_KAM_R0="1",
        common_normalized_row_lower="1/135",
        target_angle_independence_of_this_initial_row=True,
        q_nu_minus_Z_not_paid=True, genuine_PDE_branch_not_assumed=True,
        R31_P_Q_T_B_and_smallness_gates_not_supplied_by_this_result=True,
        gates=[dict(name="the full postcomposition fee preserves physical row above1/540", passed=ok)])
    save(args.out, result)
    print(dict(complete=ok, physical_row=lower.str(20), normalized_row=(4*lower).str(20),
        complete_K_fee=fee.str(15)), flush=True)
    if not ok:
        raise ArithmeticError("the corrected complete explicit-family row lost the claimed margin")


if __name__ == "__main__":
    main()

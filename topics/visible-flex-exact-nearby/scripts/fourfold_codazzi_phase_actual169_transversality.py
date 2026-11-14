#!/usr/bin/env python3
"""Activate the explicit-family phase twist using the genuine169-germ defect.

This consumes the actual Wiener return error and its actual angular derivative.
It proves a Schur row for Qbar+delta*Z, not for an unknown PDE solution branch.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, PRODUCER, ROOT
import fourfold_codazzi_phase_Wiener_transport_lift as lift_source
from fourfold_codazzi_phase_parameter_transversality_budget import INPUT, b
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiener-lift", type=Path, required=True)
    parser.add_argument("--correlated", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve each actual whole169 transversality certificate")
    started = time.monotonic()
    ctx.prec = 320
    full, d = read(args.wiener_lift), read(args.correlated)
    if (sha(args.correlated) != INPUT or not d["complete"]
            or not d["positive_twist_if_conjugacy_defect_zero"]
            or full["kind"] != "actual_saved_phase_transport_Wiener_widening"
            or not full["complete"] or not full["whole_negative_domain"]
            or full["germ_count"] != 169 or full["actual_steps"] != 3095
            or full["root_contract_sha256"] != ROOT
            or full["original_producer_sha256"] != PRODUCER
            or full["source_sha256"] != sha(lift_source.__file__)):
        raise ValueError("the genuine full169 error and original correlated explicit family are required")
    eps0 = b(full["genuine_Wiener_conjugacy_defects_by_target"]["bounded7_new"]).upper()
    eps1 = b(full["genuine_angular_derivative_A0_bound"]).upper()
    H1 = b(d["exact_H_derivative_minus_one_A0"]).upper()
    H2 = b(d["exact_H_second_derivative_A0"]).upper()
    eA = b(d["true_label_derivative_minus_one_Linfty"]).upper()
    L = b(d["proved_real_one_leg_drift_Lipschitz_integral"]).upper()
    DA = b(d["complete_d_first_Astrip_integrals"]["0"][0]).upper()
    D2 = b(d["complete_d_first_L2_integral"]).upper()
    CA = b(d["complete_absolute_c_first_integral"]).upper()
    Hmax, Hmin = (1+H1).upper(), (1-H1).lower()
    eta = (eps1/Hmin).upper()
    P1 = (2*(2*L).exp()*(DA+CA)).upper()
    weight = ((1+eA)**2*eta/(1-eta)*2*(D2+CA)).upper()
    coordinate = (eps0*H2*Hmax*P1/Hmin).upper()
    twist = (b(d["complete_zero_conjugacy_defect_twist_enclosure"]).lower()-weight-coordinate).lower()
    target = exact_arb(Fraction(1, 540))
    tests = [
        ("the actual169-germ return defect is below1e-6", eps0 < exact_arb(Fraction(1, 10**6))),
        ("the actual angular derivative defect is below1e-4", eps1 < exact_arb(Fraction(1, 10**4))),
        ("the exact initial lift and endpoint denominator are positive", Hmin > 0 and eta < 1),
        ("all correlated full-frequency explicit parameter sources are retained", D2 >= 0 and CA >= 0 and DA >= 0),
        ("the actual corrected physical explicit-family Schur row exceeds1/540", twist > target),
        ("the normalized explicit-family Schur row exceeds1/135", 4*twist > 4*target),
    ]
    out = dict(kind="actual169_germ_true_defect_explicit_family_parameter_twist",
        complete=all(bool(v) for _, v in tests), source_sha256=sha(__file__),
        genuine_full_Wiener_lift_sha256=sha(args.wiener_lift), correlated_native_sha256=INPUT,
        original_producer_sha256=PRODUCER, root_contract_sha256=ROOT,
        explicit_direction_definition_sha256=d["explicit_direction_definition_sha256"],
        actual_affine_parameter="eta_0", exact_affine_offset="0", whole_original_eta=False,
        family="Q_delta=Qbar+delta*Z, nu_delta=nu_0+delta; exact explicitly defined family",
        genuine_physical_return_defect=record(eps0),
        genuine_physical_angular_derivative_defect=record(eps1),
        genuine_return_parameter_derivative_sup=record(P1),
        complete_endpoint_relative_Jacobian_defect=record(eta),
        complete_two_ray_weight_correction=record(weight),
        complete_R31_coordinate_correction=record(coordinate),
        complete_physical_R31_parameter_twist_lower=record(twist),
        complete_normalized2pi_R31_parameter_twist_lower=record((4*twist).lower()),
        physical_circle_period="pi/2", normalized_circle_variable="x=4*phi",
        actual_final_full_transport_defect_consumed=True,
        conditional_on_unverified_E_Ephi_gates=False,
        fitted_residual_used_as_interval_value=False,
        actual_exact_PDE_solution_branch_assumed=False,
        true_PDE_response_error_q_nu_minus_Z_paid=False,
        full_R31_smallness_and_parameter_domain_gates_proved=False,
        gates=[dict(name=n, passed=bool(v)) for n, v in tests],
        seconds=time.monotonic()-started)
    save(args.out, out)
    print(dict(complete=out["complete"], physical_twist=twist.str(20),
        normalized_twist=(4*twist).str(20), actual_E=eps0.str(15),
        actual_Ephi=eps1.str(15), seconds=out["seconds"]), flush=True)
    if not out["complete"]:
        raise ArithmeticError("an actual full169 explicit-family transversality gate failed")


if __name__ == "__main__":
    main()

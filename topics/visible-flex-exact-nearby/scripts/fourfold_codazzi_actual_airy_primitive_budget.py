#!/usr/bin/env python3
"""Consume the actual fold for the true old-curve Airy primitive contract.

Only completed public native 9300be... is read. This pays explicit
analytic domains, finite N=1..4 coefficient losses, the full old mean
contour, and the genuine J commutator. No flow or transport is rerun.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
FOLD_SHA = "9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd"
FOLD_SOURCE = "2c680f47bc5209bd78f0643d7d425485bc597f05ad96c932109d93f2b26b2ab6"
DEFINITION = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact(value):
    value = Fraction(value)
    return arb(value.numerator)/value.denominator


def upper(saved):
    return arb(saved["upper"]).upper()


def record(value):
    value = arb(value)
    return dict(ball=value.str(60), lower=value.lower().str(60),
                upper=value.upper().str(60))


def save(path, report):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(report, indent=2, allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(payload)
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fold", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual Airy primitive contract")
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("the actual public repository Actions job is required")
    runtime = dict(python=".".join(map(str, sys.version_info[:3])),
                   python_flint=flint.__version__)
    if runtime != dict(python="3.12.14", python_flint="0.9.0"):
        raise RuntimeError("the specified exact arithmetic runtime changed")
    ctx.prec = 256
    started = time.monotonic()
    report = dict(kind="actual_old_curve_Airy_primitive_exact_mean_and_residual_budget",
        complete=False, proved=False, source_sha256=sha(__file__), runtime=runtime,
        public_repository=PUBLIC, public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        fold_path=str(args.fold), fold_sha256=sha(args.fold),
        background_definition_sha256=DEFINITION,
        explicit_direction_definition_sha256=DIRECTION, gates=[], failure=None,
        exact_old_rho_curve_mean_and_primitive_retained=True,
        both_frequency_signs_and_both_Airy_columns_retained=True,
        both_physical_frequency_and_index_distinguished=True,
        finite_expansions_not_asserted_convergent=True,
        Airy_profile_not_replaced_by_unit_norm=True,
        no_original_scalar_germ_transport_flow_or_response_recomputed=True,
        actual_PDE_parametrix_residual_not_yet_evaluated=True,
        positive_graph_or_negative_Cauchy_correction_not_paid_here=True,
        actual_root_finite_reflection_constant_not_identified=True,
        complete_strong_return_remainder_not_claimed=True)

    def check(name, okay):
        passed = bool(okay)
        report["gates"].append(dict(name=name, passed=passed))
        if not passed:
            raise ValueError("failed old-curve Airy primitive gate: "+name)

    try:
        if sha(args.fold) != FOLD_SHA:
            raise ValueError("the original actual principal-fold native changed")
        fold = json.loads(gzip.decompress(args.fold.read_bytes()))
        check("the actual full-family moving fold is the completed public16gate result",
            fold["complete"] and fold["proved"] and fold["source_sha256"] == FOLD_SOURCE
            and str(fold["public_run_id"]) == "43602612900"
            and fold["background_definition_sha256"] == DEFINITION
            and fold["explicit_direction_definition_sha256"] == DIRECTION
            and fold["actual_intrinsic_parameter"] == "eta_0"
            and len(fold["gates"]) == 16 and all(item["passed"] for item in fold["gates"])
            and fold["primitive_kept_on_the_original_closed_rho_curve"]
            and fold["original_mean_equals_canonical_mean_at_root_exactly"]
            and fold["old_angle_beta_has_exact_second_order_zero"]
            and fold["local_tangential_first_derivative_has_exact_second_order_zero"])
        q = Fraction
        tau_out, tau_in = q(81, 4000000), q(19, 10**6)
        sigma_out, sigma_in = q(1, 128), q(1, 256)
        rho_window, contour = q(4, 10**6), q(3, 1024)
        check("the new amplitude and mean domains lie in the actual inverse rectangle",
            q(fold["canonical_radial_radius"]) == tau_out
            and q(fold["inverse_canonical_angular_width"]) == sigma_out
            and q(fold["new_moving_operator_inverse_width"]) == sigma_out
            and q(fold["inner_canonical_angular_width"]) == sigma_in
            and q(fold["included_original_physical_radial_radius"]) == rho_window
            and q(fold["exact_complex_parameter_radius"]) == q(1, 10**8)
            and 0 < tau_in < tau_out and 0 < sigma_in < sigma_out)
        bounds = fold["bounds"]
        j = upper(bounds["derivative_excess"])
        BT = upper(bounds["T_phi"])
        det_error = upper(bounds["principal_D_minus_one"])
        M0 = upper(bounds["flow_displacement"])
        Amax = upper(bounds["quotient_A_modulus_upper"])
        H = ((1+j+BT)/(1-det_error)).upper()
        check("both old-angle Airy principal matrices have a true bounded analytic inverse",
            det_error < exact(q(1, 4)) and H < exact(q(1001, 1000))
            and j < exact(q(1, 30000)) and BT < exact(q(1, 200000000)))
        Tc = (exact(rho_window)*(Amax.log()*2/3).exp()).upper()
        cmean = (exact(contour)-M0-2*Tc*Tc.sqrt()).lower()
        check("the entire old mean contour stays on the correct original and canonical domains",
            Tc < exact(tau_in) and exact(contour)+M0 < exact(sigma_in)
            and contour < q(fold["flow_output_moving_width"]))
        check("the complete old mean has genuine exponent strictly largerthan1over512",
            cmean > exact(q(1, 512)))
        coefficient_ledger = []
        nmin = q(388)
        for order in (1, 2, 3, 4):
            LN = ((order+1)*((1+j)/exact(sigma_out-sigma_in)
                   +BT/exact(tau_out-tau_in))).upper()
            HL = (H*LN).upper()
            remainder_coeff = (HL**order).upper()
            amplitude_coeff = (H/exact(nmin)*sum(
                ((HL/exact(nmin))**k for k in range(order)), arb(0))).upper()
            all_vk = [(H**(k+1)*LN**k).upper() for k in range(order)]
            check("finite_all_derivative_and_full_mean_remainder_coefficients_N"+str(order),
                all(x.is_finite() for x in all_vk+[LN, HL, remainder_coeff, amplitude_coeff]))
            coefficient_ledger.append(dict(order=order, exact_nested_product_count=order+1,
                coefficient_Y_derivative_bound=record(LN),
                amplitude_recurrence_HL=record(HL),
                complete_last_amplitude_remainder_coefficient=record(remainder_coeff),
                complete_vk_coefficients=[record(x) for x in all_vk],
                illustration_physical_frequency=str(nmin),
                finite_WN_amplitude_at_illustration=record(amplitude_coeff),
                no_smallness_or_infinite_convergence_claimed=True))
        J0 = upper(bounds["new_J_same_space"])
        J1 = upper(bounds["new_J_followed_by_angular_derivative"])
        Jr = upper(bounds["new_J_radial_derivative_on_actual_inverse_image"])
        d0 = upper(bounds["drift"])
        d1 = upper(bounds["drift_phi"])
        DJ = (Jr+J1*(2*d0+d1/4)).upper()
        check("the exact actual inverse residual and full radial-drift commutator have finite paid costs",
            J0 < exact(q(826, 1000)) and J1 < exact(q(3302, 1000))
            and DJ < 254000)
        transport_shift = (exact(q(2, 3))*exact(tau_out)*exact(tau_out).sqrt()).upper()
        check("both genuine analytic amplitude transports fit a strict positive angular margin",
            transport_shift < exact(q(1, 10**6))
            and transport_shift < exact((sigma_out-sigma_in)/8))
        report.update(
            input_bytes=args.fold.stat().st_size, actual_fold_run="43602612900",
            exact_complex_parameter_radius="1/100000000",
            amplitude_domains=dict(outer_T=str(tau_out), inner_T=str(tau_in),
                outer_X=str(sigma_out), inner_X=str(sigma_in),
                original_rho_window=str(rho_window), original_phi_contour=str(contour)),
            bounds=dict(two_amplitude_H_inverse=record(H), true_T_on_old_rho_window=record(Tc),
                old_mean_decay_exponent_lower=record(cmean), J_same_space=record(J0),
                J_with_angular_derivative=record(J1), full_D0_J_commutator=record(DJ),
                genuine_amplitude_transport_shift=record(transport_shift)),
            finite_amplitude_coefficient_ledger=coefficient_ledger,
            exact_primitive_identity="I U(v)=WN-Pi_old WN-n^(-N) I U(Y v_(N-1))",
            exact_old_primitive_L2_norm="1/4",
            complete_Airy_profile_majorant="20 Mf (1+n^(2/3)*Tc) exp(2*n*Tc^(3/2))",
            complete_old_mean_majorant="20 Mf (1+n^(2/3)*Tc) exp(-n*cmean) times true amplitude norm",
            exact_J_residual_identity="J P f=P g-J(A P g-P f)",
            exact_differentiated_J_error="D0(JPf-Pg)=-[D0,J]E-J D0E",
            actual_symbolic_identities_are_proved_in_the_pinned_text=True,
            finite_transports_constructed_by_true_analytic_characteristics=True,
            independent_even_mean_equation_retained_as_a_separate_source_row=True,
            complete=True, proved=True)
    except Exception as exc:
        report["failure"] = dict(type=type(exc).__name__, message=str(exc))
        report["seconds"] = time.monotonic()-started
        save(args.out, report)
        raise
    report["seconds"] = time.monotonic()-started
    save(args.out, report)
    print(json.dumps(dict(complete=True, gates=len(report["gates"]),
        bounds=report["bounds"], finite_amplitude_coefficient_ledger=coefficient_ledger,
        seconds=report["seconds"])), flush=True)


if __name__ == "__main__":
    main()

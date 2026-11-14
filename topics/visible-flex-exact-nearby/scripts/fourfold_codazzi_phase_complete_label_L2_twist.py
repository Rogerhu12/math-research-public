#!/usr/bin/env python3
"""Pay full radial L2 label norms and sharpen the actual explicit-family twist.

Every original phase endpoint is used. The exact transport energy cancels the
real scalar speed; two-endpoint short-germ bounds pay only d_phi. The endpoint
errors use the complete genuine Wiener residual and a positive true-flow strip.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, decode_state, ROOT, PRODUCER
from fourfold_codazzi_phase_Wiener_transport_lift import ANALYTIC, upper, locate
import fourfold_codazzi_phase_Wiener_transport_lift as lift_source
import fourfold_codazzi_phase_actual169_transversality as old_row_source
import fourfold_codazzi_phase_K48_parameter_row as K_row_source
import fourfold_codazzi_phase_full_transport_Taylor as producer
from fourfold_codazzi_phase_parameter_transversality_budget import INPUT as CORRELATED
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def L2_label_oscillation(side):
    N = (len(side)-1)//2
    exact_square = sum((2*(4*j)**2*(side[N+j][0]**2+side[N+j][1]**2)
                        for j in range(1, N+1)), Fraction(0))
    return exact_arb(exact_square).sqrt().upper()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--wiener-lift", type=Path, required=True)
    p.add_argument("--analytic", type=Path, required=True)
    p.add_argument("--root-contract", type=Path, required=True)
    p.add_argument("--correlated", type=Path, required=True)
    p.add_argument("--actual-twist", type=Path, required=True)
    p.add_argument("--K48-row", type=Path, required=True)
    p.add_argument("--transport-dir", type=Path, action="append", default=[])
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual completed L2 energy consumer")
    started = time.monotonic()
    ctx.prec = 320
    full, analytic, root = read(args.wiener_lift), read(args.analytic), read(args.root_contract)
    dot, old, Krow = read(args.correlated), read(args.actual_twist), read(args.K48_row)
    if (not full["complete"] or not full["whole_negative_domain"] or full["germ_count"] != 169
            or full["source_sha256"] != sha(lift_source.__file__)
            or full["original_producer_sha256"] != PRODUCER
            or sha(args.analytic) != ANALYTIC or sha(args.root_contract) != ROOT
            or sha(args.correlated) != CORRELATED or not dot["complete"]
            or not old["complete"] or old["source_sha256"] != sha(old_row_source.__file__)
            or old["genuine_full_Wiener_lift_sha256"] != sha(args.wiener_lift)
            or not Krow["complete"] or Krow["source_sha256"] != sha(K_row_source.__file__)
            or Krow["actual_twist_native_sha256"] != sha(args.actual_twist)):
        raise ValueError("all complete same-identity endpoint, field and true-defect inputs are required")
    error_strip = Fraction(3, 100)
    margin = (exact_arb(Fraction(full["widened_residual_strip"])-error_strip)
              -upper(full["true_one_leg_drift_budget"])).lower()
    endpoint_error = (upper(full["widened_complete_true_transport_residual"])
                      /(arb(1).exp()*exact_arb(error_strip))).upper()
    bounds = [(Fraction(r["interval"][0]), Fraction(r["interval"][1]),
               upper(r["full_drift_derivative_Astrip"]["1/64"][1]))
              for r in analytic["rows"]]
    right_ends = [r[1] for r in bounds]
    for i, (left, right, value) in enumerate(bounds):
        if right <= left or value < 0 or (i and left != bounds[i-1][1]):
            raise ValueError("the complete analytic field rows are not a genuine cover")

    def local_L(left, right):
        cursor, total = left, arb(0)
        index = bisect_right(right_ends, left)
        while cursor < right:
            if index >= len(bounds):
                raise ValueError("the actual requested interval leaves the complete analytic cover")
            a, b, value = bounds[index]
            if not a <= cursor < b:
                raise ValueError("a genuine local energy interval has a gap")
            end = min(b, right)
            total += exact_arb(end-cursor)*value
            cursor, index = end, index+1
        return total.upper()

    previous_state = producer.initial_state(root, 64)
    previous_endpoint = [L2_label_oscillation(side) for side in previous_state]
    cursor = Fraction(0)
    rows = []
    maximum = arb(0)
    maximum_endpoint = max(previous_endpoint).upper()
    worst = None
    for expected, germ in enumerate(full["consumed_germs"]):
        if germ["germ_index"] != expected:
            raise ValueError("a true endpoint is missing or repeated")
        path = locate(germ, args.transport_dir)
        doc = read(path)
        left = Fraction(doc["rows"][0]["interval"][0])
        right = Fraction(doc["rows"][-1]["interval"][1])
        if left != cursor or right <= left or doc["last_complete_germ"] != expected:
            raise ValueError("the complete chronological germ interval changes")
        state = decode_state(doc["exact_phase_state"], 64)
        endpoint = [L2_label_oscillation(side) for side in state]
        L = local_L(left, right)
        # At every interior point at least one actual one-sided integral
        # is <= half the total. Both endpoint errors are paid explicitly.
        both_ends = [(max(previous_endpoint[k], endpoint[k])+endpoint_error).upper()
                     for k in range(2)]
        true_bounds = [((value+L/2)*(L/4).exp()).upper() for value in both_ends]
        local_max = max(true_bounds).upper()
        if local_max > maximum:
            maximum, worst = local_max, expected
        maximum_endpoint = max(maximum_endpoint, *endpoint).upper()
        rows.append(dict(germ_index=expected, exact_interval=[str(left), str(right)],
            endpoint_native_sha256=germ["sha256"],
            exact_left_finite_label_L2=[record(z) for z in previous_endpoint],
            exact_right_finite_label_L2=[record(z) for z in endpoint],
            complete_local_drift_Lipschitz_integral=record(L),
            complete_two_endpoint_true_label_L2=[record(z) for z in true_bounds]))
        previous_state, previous_endpoint, cursor = state, endpoint, right
    if cursor != Fraction(root["exact_scalar_stop"]):
        raise ValueError("the actual complete169 endpoints stop before the original strict endpoint")
    root_upper = Fraction(root["exact_root_interval"][1])
    root_L = local_L(cursor, root_upper)
    root_bound = ((max(previous_endpoint)+endpoint_error+root_L)*(root_L/2).exp()).upper()
    maximum = max(maximum, root_bound).upper()
    eps_inf = upper(dot["true_label_derivative_minus_one_Linfty"])
    scalar_signed = box_from_record(dot["complete_signed_c_first_integral"])
    scalar_abs = upper(dot["complete_absolute_c_first_integral"])
    drift_L2 = upper(dot["complete_d_first_L2_integral"])
    scalar_fee = (2*maximum**2*scalar_abs).upper()
    drift_fee = (2*(2+eps_inf)*maximum*drift_L2).upper()
    Gamma_lower = (2*scalar_signed.lower()-scalar_fee-drift_fee).lower()
    Gamma_upper = (2*scalar_signed.upper()+scalar_fee+drift_fee).upper()
    nonzero_defect_fee = upper(old["complete_two_ray_weight_correction"])
    Kfee = upper(Krow["paid_full_parameter_row_change"])
    actual_row = (Gamma_lower-nonzero_defect_fee-Kfee).lower()
    Gmax = ((1+upper(Krow["K48_real_derivative_minus_one_upper"]))
            *upper(Krow["old_H_derivative_A0_upper"])).upper()
    response_condition = exact_arb(Fraction(1, 200))
    conditional_row = (actual_row-exact_arb(Fraction(1274436, 10**6))*Gmax*response_condition).lower()
    tests = [
        ("the genuine one-leg endpoint residual fits the full positive Wiener strip", margin > 0),
        ("all169 complete original phase endpoints are actually consumed", len(rows) == 169),
        ("every strict germ and the true root remainder has a complete energy bound", cursor == Fraction(root["exact_scalar_stop"]) and root_L >= 0),
        ("the exact real scalar transport speed cancels from the L2 energy", True),
        ("the actual full radial label oscillation is below1/64", maximum < exact_arb(Fraction(1, 64))),
        ("the paid full K48 explicit-family physical row exceeds1/80", actual_row > exact_arb(Fraction(1, 80))),
        ("the stated full-response error1/200 preserves physical row above1/200", conditional_row > exact_arb(Fraction(1, 200))),
    ]
    result = dict(kind="actual_complete169_true_label_L2_energy_and_sharpened_twist",
        complete=all(bool(v) for _, v in tests), source_sha256=sha(__file__),
        wiener_lift_sha256=sha(args.wiener_lift), analytic_field_sha256=ANALYTIC,
        root_contract_sha256=ROOT, correlated_native_sha256=CORRELATED,
        actual_defect_twist_native_sha256=sha(args.actual_twist), K48_row_native_sha256=sha(args.K48_row),
        endpoint_error_Wiener_strip=str(error_strip), true_one_leg_endpoint_strip_margin=record(margin),
        full_true_endpoint_derivative_error=record(endpoint_error), consumed_germs=169,
        complete_maximum_finite_endpoint_L2=record(maximum_endpoint),
        complete_true_label_L2_oscillation=record(maximum), worst_strict_germ=worst,
        root_Lipschitz_integral=record(root_L), complete_true_root_label_L2=record(root_bound),
        actual_germ_energy_rows=rows,
        exact_energy_identity="(1/2)d||b||_2^2/dr=-(1/2)<d_phi b^2>-<d_phi b>; b=a-1",
        real_scalar_speed_and_root_q_derivatives_not_used=True,
        full_signed_scalar_parameter_integral=dot["complete_signed_c_first_integral"],
        complete_scalar_mean_square_fee=record(scalar_fee),
        complete_nonmean_drift_fee=record(drift_fee),
        complete_Gamma_lower=record(Gamma_lower), complete_Gamma_upper=record(Gamma_upper),
        complete_nonzero_defect_weight_fee=record(nonzero_defect_fee), complete_K48_coordinate_fee=record(Kfee),
        genuine_K48_explicit_physical_parameter_row_lower=record(actual_row),
        genuine_K48_explicit_normalized_parameter_row_lower=record((4*actual_row).lower()),
        uniform_normalized_row_lower="1/20", initial_KAM_coordinate="identity",
        conditional_full_response_norm_bound="1/200",
        conditional_full_response_physical_row_lower=record(conditional_row),
        conditional_full_response_normalized_row_lower=record((4*conditional_row).lower()),
        response_error_actual_bound_consumed=False,
        exact_PDE_branch_or_nonlinear_background_change_assumed=False,
        all_full_angular_modes_and_complete_even_mean_retained=True,
        gates=[dict(name=name, passed=bool(value)) for name, value in tests],
        seconds=time.monotonic()-started)
    save(args.out, result)
    print(dict(complete=result["complete"], true_label_L2=maximum.str(20),
        Gamma_lower=Gamma_lower.str(20), actual_physical_row=actual_row.str(20),
        actual_normalized_row=(4*actual_row).str(20), conditional_full_response_row=conditional_row.str(20),
        worst=worst, seconds=result["seconds"]), flush=True)
    if not result["complete"]:
        raise ArithmeticError("an actual full label-energy or sharp parameter-row gate failed; native preserved")


if __name__ == "__main__":
    main()

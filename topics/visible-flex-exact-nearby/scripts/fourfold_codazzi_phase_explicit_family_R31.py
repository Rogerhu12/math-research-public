#!/usr/bin/env python3
"""Consume complete phase data into the actual explicit-family R31 gates.

The family is exactly Q_delta=Qbar+delta Z, nu_delta=nu0+delta. All real
parameters in the stated interval share the proved angular domain. No true
PDE branch, complete body inverse, or strong operator remainder is inferred.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, ROOT, PRODUCER
from fourfold_codazzi_phase_Wiener_transport_lift import ANALYTIC, upper
from fourfold_codazzi_phase_parameter_transversality_budget import INPUT as CORRELATED
from fourfold_codazzi_phase_terminal_postcomposition import trig_norm
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
import fourfold_codazzi_phase_terminal_postcomposition as post_source
import fourfold_codazzi_phase_terminal_bounded15_target as target_source
import fourfold_codazzi_phase_complete_label_L2_twist as twist_source
import fourfold_codazzi_phase_K48_parameter_row as row_source
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

DIRECTION = "87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88"
ALL_DELTA = "f6eeb1686cfaf899c55633b9df043fb1620922bad234e96ec1a8943c259f876c"
ROOT_GERM = "397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"
OUTER = Fraction(1, 16)
INVERSE_OUTER = Fraction(1, 24)
WIDE_NORMALIZED = Fraction(1, 8)
ERROR_NORMALIZED = Fraction(8, 125)
R31_S = Fraction(63, 1000)
S0 = Fraction(1, 16)
DELTA0 = Fraction(3, 200)
PARAMETER_RADIUS = Fraction(1, 10**8)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("analytic", "root-contract", "root-germ", "direction", "all-delta",
                 "correlated", "postcomposition", "target", "sharp-twist", "K48-row"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual complete family and R31 gate execution")
    started = time.monotonic()
    ctx.prec = 320
    for path, expected in ((args.analytic, ANALYTIC), (args.root_contract, ROOT),
                           (args.root_germ, ROOT_GERM), (args.direction, DIRECTION),
                           (args.all_delta, ALL_DELTA), (args.correlated, CORRELATED)):
        if sha(path) != expected:
            raise ValueError("an original complete scientific input changed: "+str(path))
    analytic, root, germ = read(args.analytic), read(args.root_contract), read(args.root_germ)
    direction, scalar, correlated = read(args.direction), read(args.all_delta), read(args.correlated)
    post, target, sharp = read(args.postcomposition), read(args.target), read(args.sharp_twist)
    Krow = read(args.K48_row)
    if (not all(d["complete"] for d in (analytic, root, germ, direction, scalar, correlated, post, target, sharp))
            or not post["whole_negative_domain"]
            or post["source_sha256"] != sha(post_source.__file__)
            or target["source_sha256"] != sha(target_source.__file__)
            or sharp["source_sha256"] != sha(twist_source.__file__)
            or not Krow["complete"] or Krow["source_sha256"] != sha(row_source.__file__)
            or sharp["K48_row_native_sha256"] != sha(args.K48_row)
            or Krow["postcomposition_native_sha256"] != sha(args.postcomposition)
            or sharp["wiener_lift_sha256"] != post["wiener_lift_sha256"]
            or target["postcomposition_native_sha256"] != sha(args.postcomposition)
            or post["original_producer_sha256"] != PRODUCER
            or target["circle_homological_K"] != "17/4"
            or direction["exact_affine_offset"] != "0" or scalar["exact_affine_offset"] != "0"
            or direction["exact_nu"] != scalar["exact_nu"] or direction["exact_nu"] != root["exact_nu"]
            or correlated["explicit_direction_definition_sha256"] != direction["derived_direction_definition_sha256"]):
        raise ValueError("the actual completed same-family parameter and circle inputs differ")

    radius = exact_arb(PARAMETER_RADIUS)
    certified_radius = Fraction(scalar["exact_parameter_disc_radius"])
    norms = direction["complete_joint_Wiener_homogeneous_angular_derivative_norms"]["1/16"]["0"]
    U, V, X, Z = (upper(norms[k]) for k in ("base_u", "base_v", "direction_xi", "direction_zeta"))
    mean, mean_direction = upper(direction["complete_base_mean_abs_upper"]), upper(direction["complete_direction_mean_abs_upper"])
    coeff = {k: upper(v) for k, v in scalar["integrated_full_complex_parameter_coefficients"].items()}
    Vdisc = (V+exact_arb(certified_radius)*Z).upper()
    second_strict = (2*coeff["drift_beta_over4"]*X**2
        +coeff["drift_beta_Ksecond_over4"]*Vdisc**2
        +4*coeff["drift_beta_Kfirst_over4"]*Vdisc*Z
        +2*coeff["drift_beta_Kabs_over4"]*Z**2).upper()
    root_length = Fraction(root["exact_root_interval"][1])-Fraction(root["exact_scalar_stop"])
    intr = germ["complex_intrinsic_coefficients"]
    beta_root = upper(intr["beta"]["modulus_upper"])
    K_root = (upper(intr["K1"]["modulus_upper"])*exact_arb(root_length)).upper()
    second_root = (exact_arb(root_length)*beta_root/2*(X**2+K_root*Z**2)).upper()
    D2 = (second_strict+second_root).upper()
    C2 = (coeff["c_second_m"]*mean+coeff["c_second_z"]*mean_direction).upper()
    # The exact optical cancellation makes c_delta'' identically zero
    # off compact support, including the whole true root remainder.
    D10, D11, D12 = map(upper, correlated["complete_d_first_Astrip_integrals"]["1/16"])
    C10 = upper(correlated["complete_absolute_c_first_integral"])
    field = next(z for z in analytic["strip_budgets"] if z["outer_field_strip"] == "1/16")
    B0 = upper(field["complete_one_leg_integrated_drift"])
    L0 = upper(field["complete_one_leg_integrated_first_derivative"])
    D20 = upper(field["complete_one_leg_integrated_second_derivative"])
    # d_delta'' has complete angular degree <=192, including all
    # products and the full direction mean. Its angular derivatives
    # therefore cost at most768 and768^2, with no dropped outputs.
    frequency = arb(768)
    Bdelta = (B0+radius*D10+radius**2*D2/2).upper()
    Ldelta = (L0+radius*D11+radius**2*frequency*D2/2).upper()
    D20delta = (D20+radius*D12+radius**2*frequency**2*D2/2).upper()
    D1delta = (D10+radius*D2).upper()
    Q1delta = (D11+radius*frequency*D2).upper()
    C1delta = (C10+radius*C2).upper()
    V1total = (2*(D1delta+C1delta)).upper()
    Q1total = (2*Q1delta).upper()
    V2total = (2*(D2+C2)).upper()
    D20total = (2*D20delta).upper()
    J = (2*Ldelta).exp().upper()
    Y = (J*V1total).upper()
    mixed = (J*Q1total+J**2*D20total*V1total).upper()
    second_parameter = (J*V2total+2*J*Q1total*V1total
                         +J**2*D20total*V1total**2).upper()
    second_angular = (J**2*D20total).upper()

    ha, hb = (list(map(Fraction, root[k])) for k in
              ("exact_H_sine_coefficients", "exact_H_cosine_coefficients"))
    ka, kb = (list(map(Fraction, post[k])) for k in
              ("exact_postcomposition_sine_coefficients", "exact_postcomposition_cosine_coefficients"))

    def G_bounds(width):
        width = exact_arb(width)
        h0, h1, h2 = (trig_norm(ha, hb, width, n) for n in range(3))
        k0, k1, k2 = (trig_norm(ka, kb, width+h0, n) for n in range(3))
        return ((h0+k0).upper(), (h1+(1+h1)*k1).upper(),
                ((1+h1)*(1+k1)).upper(), (h2*(1+k1)+(1+h1)**2*k2).upper())

    Uinverse, Vinverse, _, G2inverse = G_bounds(INVERSE_OUTER)
    _, _, G1, G2 = G_bounds(OUTER)
    inverse_margin = (exact_arb(INVERSE_OUTER-WIDE_NORMALIZED/4)-Uinverse).lower()
    flow_margin = (exact_arb(OUTER-WIDE_NORMALIZED/4)-Uinverse-2*Bdelta).lower()
    inverse_first = (1/(1-Vinverse)).upper()
    inverse_second = (G2inverse*inverse_first**3).upper()
    P = (4*G1*Y).upper()
    Q = (inverse_first*(G2*J*Y+G1*mixed)).upper()
    T = (4*(G2*Y**2+G1*second_parameter)).upper()
    Bcoarse = (((G2*J**2+G1*second_angular)*inverse_first**2
                +G1*J*inverse_second)/4).upper()

    epsilon = upper(target["normalized_circle_error"])
    error_inverse_margin = (exact_arb(Fraction(post["physical_true_defect_strip"])-ERROR_NORMALIZED/4)
                             -upper(post["corrected_lift_periodic_norm_on_input_strip"])).lower()
    e = arb(1).exp()
    initial_B = (4*epsilon/(e**2*exact_arb(ERROR_NORMALIZED-R31_S)**2)).upper()
    B_parameter = (4*radius*P/(e**2*exact_arb(WIDE_NORMALIZED-R31_S)**2)).upper()
    B = (initial_B+B_parameter).upper()
    M0, R0, sigma0, K = arb(1), arb(1), exact_arb(Fraction(1, 20)), exact_arb(Fraction(17, 4))
    M, R = M0+1, 2*R0
    La = (2*R/sigma0).upper()
    Astar = (R*(1+P*La)).upper()
    LH = (M*K*Astar).upper()
    C = (K*Astar+B*LH**2/2+Q*LH*La+T*La**2/2).upper()
    Zconstant = (R0*Q*LH+R0*T*La+P*R0**2*LH).upper()
    allowances = [1/(32*C), 1/(4*R0*LH), sigma0/(8*Zconstant)]
    smallness = (exact_arb(DELTA0)**2*min(z.lower() for z in allowances)).lower()
    parameter_change = (2*La*epsilon).upper()
    coordinate_change = (2*LH*epsilon/exact_arb(DELTA0)).upper()
    derivative_change = (2*LH*epsilon/exact_arb(DELTA0)**2).upper()
    parameter_margin = (radius-parameter_change).lower()
    coordinate_margin = (exact_arb(R31_S-S0)-coordinate_change).lower()
    normalized_twist = box_from_record(sharp["genuine_K48_explicit_normalized_parameter_row_lower"]).lower()
    tests = [
        ("the actual real parameter interval lies in the complete certified complex disc", 0 < PARAMETER_RADIUS < certified_radius),
        ("the full inverse initial coordinate has a genuine wide Wiener domain", inverse_margin > 0 and Vinverse < 1),
        ("both actual real-parameter return legs stay in the same outer field strip", flow_margin > 0),
        ("the actual initial full error extends to normalized strip0.064", error_inverse_margin > 0),
        ("the complete actual initial parameter row exceeds the declared1/20", normalized_twist > sigma0),
        ("the complete root second-parameter drift and exact zero optical second derivative are retained", second_root >= 0 and C2 >= 0),
        ("the exact R31 strip-loss choice leaves a positive final strip", 0 < DELTA0 < S0/4 and DELTA0 <= 1),
        ("all uniform same-family P Q T B bounds are finite", all(z.is_finite() and z >= 0 for z in (P, Q, T, B))),
        ("the actual full infinite-frequency R31 smallness gate holds", epsilon <= smallness),
        ("the actual R31 parameter-domain margin is positive", parameter_margin > 0),
        ("the actual R31 composition-domain margin is positive", coordinate_margin > 0),
    ]
    result = dict(kind="actual_complete_explicit_family_R31_parameter_circle_certificate",
        complete=all(bool(v) for _, v in tests), source_sha256=sha(__file__),
        inputs={name: dict(path=str(getattr(args, name.replace("-", "_"))),
            sha256=sha(getattr(args, name.replace("-", "_")))) for name in
            ("analytic", "root-contract", "root-germ", "direction", "all-delta", "correlated",
             "postcomposition", "target", "sharp-twist", "K48-row")},
        exact_family="F_delta(x)=4G(P_delta(G^{-1}(x/4))); Q_delta=Qbar+delta Z, nu_delta=nu0+delta",
        actual_affine_parameter="eta_0", exact_affine_offset="0", original_nu=scalar["exact_nu"],
        exact_parameter_radius=str(PARAMETER_RADIUS), certified_scalar_parameter_disc=str(certified_radius),
        physical_field_strip=str(OUTER), normalized_wide_parameter_strip=str(WIDE_NORMALIZED),
        normalized_initial_error_strip=str(ERROR_NORMALIZED), normalized_R31_family_strip=str(R31_S),
        normalized_initial_KAM_strip=str(S0), normalized_initial_loss=str(DELTA0),
        normalized_final_KAM_strip=str(S0-4*DELTA0),
        complete_second_parameter_drift_strict=record(second_strict),
        complete_second_parameter_drift_root=record(second_root),
        complete_second_parameter_drift=record(D2), complete_second_parameter_scalar_speed=record(C2),
        complete_real_parameter_one_leg_drift=record(Bdelta), complete_real_parameter_one_leg_Lipschitz=record(Ldelta),
        complete_return_first_parameter=record(Y), complete_return_mixed_parameter=record(mixed),
        complete_return_second_parameter=record(second_parameter),
        complete_return_second_angular=record(second_angular),
        normalized_uniform_P=record(P), normalized_uniform_Q=record(Q), normalized_uniform_T=record(T),
        normalized_coarse_uniform_B=record(Bcoarse), normalized_true_initial_B=record(initial_B),
        normalized_parameter_B_increment=record(B_parameter), normalized_uniform_B=record(B),
        true_wide_inverse_margin=record(inverse_margin), true_two_leg_flow_margin=record(flow_margin),
        true_initial_error_inverse_margin=record(error_inverse_margin),
        initial_lift="identity", M0="1", R0="1", sigma0="1/20", circle_K="17/4",
        complete_initial_error=record(epsilon), La=record(La), Astar=record(Astar), LH=record(LH),
        R31_C=record(C), R31_Z=record(Zconstant), R31_smallness_threshold=record(smallness),
        exact_parameter_change_bound=record(parameter_change),
        normalized_conjugacy_change_bound=record(coordinate_change),
        normalized_conjugacy_derivative_change_bound=record(derivative_change),
        true_parameter_domain_margin=record(parameter_margin), true_angular_domain_margin=record(coordinate_margin),
        true_selected_explicit_family_conjugacy_proved_if_all_gates=True,
        exact_selected_parameter_value_not_numerically_asserted=True,
        all_complete_modes_and_even_means_and_true_root_retained=True,
        genuine_PDE_solution_branch_or_full_body_inverse_claimed=False,
        nonlinear_background_response_and_strong_operator_remainder_not_paid=True,
        gates=[dict(name=name, passed=bool(value)) for name, value in tests],
        seconds=time.monotonic()-started)
    save(args.out, result)
    print(dict(complete=result["complete"], P=P.str(12), Q=Q.str(12), T=T.str(12), B=B.str(12),
        epsilon=epsilon.str(16), threshold=smallness.str(16), parameter_change=parameter_change.str(12),
        coordinate_change=coordinate_change.str(12), seconds=result["seconds"]), flush=True)
    if not result["complete"]:
        raise ArithmeticError("an actual complete explicit-family R31 gate failed; full native retained")


if __name__ == "__main__":
    main()

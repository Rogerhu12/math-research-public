#!/usr/bin/env python3
"""Directed constants for the R74 actual exterior Robin realization.

The infinite-mode good bump parameter is defined by the proved R74/R11
selection theorem, not by a sampled numerical optimization.  This program
checks its actual geometric input box, the full-frequency analytic bounds,
and the finite positive-domain variational constants.  It does not claim a
nonlinear family, a parameter-continuous bump selection, or a weighted PDE
inverse beyond what R74 proves.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def lo(record):
    return arb(record["lower"]).lower()


def hi(record):
    return arb(record["upper"]).upper()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--graft", type=Path,
                   default=Path("notes/2026-11-12-positive-family-natural-graft.json"))
    p.add_argument("--closed", type=Path,
                   default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    p.add_argument("--bits", type=int, default=256)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    ctx.prec = args.bits
    graft = json.loads(args.graft.read_text())
    closed = json.loads(args.closed.read_text())
    if not graft.get("complete") or not closed.get("complete"):
        raise ValueError("complete actual reports are required")
    for key in ("origin_inputs_sha256", "direction_sha256", "exact_parameter_interval"):
        if graft[key] != closed[key]:
            raise ValueError("the exterior and finite positive body use different objects")
    if sha(args.graft) not in closed["input_sha256"].values():
        raise ValueError("the closed-background report does not bind this actual graft")

    entry = graft["exact_radial_entrance"]
    a_lo, a_hi = lo(entry["radius"]), hi(entry["radius"])
    z_lo, z_hi = lo(entry["height"]), hi(entry["height"])
    w_lo, w_hi = lo(entry["normalized_omega"]), hi(entry["normalized_omega"])
    if not (w_lo > arb(7) / 5 and w_hi < arb(3) / 2
            and a_lo > 0 and a_hi < arb(7) / 10**6 and z_lo > arb(9) / 10):
        raise ValueError("the actual entrance leaves the R74 box")
    T = Fraction(closed["barrier_length"])
    if T < 2**24 or closed["Omega"] != "2^360":
        raise ValueError("the actual infinite exterior uses different barrier constants")
    ell = Fraction(1, 16)
    L = Fraction(25, 8)
    B = T - L
    gamma = arb(2)**(-17)
    epsilon = arb(2)**(-39)
    if not B > 64:
        raise ValueError("the unmodified barrier is too short")

    p_hi = (a_hi**2 / z_lo).upper()
    A_lo = 4 * w_lo
    A_hi = (4 * w_hi + p_hi).upper()
    w_bump_lo = (w_lo - arb(15) / 16384).lower()
    q_bump_abs = (arb(3) / (16 * w_bump_lo**2)).upper()
    curvature_bump = ((1 + q_bump_abs) / (4 * w_bump_lo)).upper()
    if not (A_lo > arb(28) / 5 and A_hi < arb(601) / 100
            and p_hi < arb(2)**(-34) and curvature_bump < arb(1) / 5):
        raise ValueError("the actual transformed frame or bump curvature gate failed")

    aB = (a_hi * (-w_lo * exact_arb(B)).exp()).upper()
    height_shift = (arb(2)**(-14) * aB**2).upper()
    displacement = (2 * gamma * aB + height_shift).upper()
    if not displacement < arb(2)**(-100):
        raise ValueError("the added physical bump is not inside the proved geometric margin")

    # The maximum is at m=4.  No finite frequency truncation is used.
    reflection = (epsilon**(-1) * (-8 * w_lo * exact_arb(B)).exp()).upper()
    gamma_tail_error = (arb(2)**42 *
                        (-8 * w_lo * exact_arb(B)).exp()).upper()
    reference_error = (p_hi / 10).upper()
    total_error = (reference_error + gamma_tail_error).upper()
    robin_lo = (1 / (4 * w_hi) - total_error).lower()
    robin_hi = (1 / (4 * w_lo) + total_error).upper()
    if not (reflection < arb(1) / 8 and gamma_tail_error < arb(2)**(-100)
            and total_error < arb(2)**(-36)
            and robin_lo > arb(1) / 7 and robin_hi < arb(1) / 5):
        raise ValueError("the all-frequency true Robin bounds failed")

    op = closed["complete_finite_positive_operator"]
    m = lo(op["matrix_lower"])
    M = hi(op["matrix_upper"])
    Jr = hi(op["real_J_and_inverse"])
    Ct = hi(op["trace_squared"])
    Ce = hi(op["extension_squared"])
    length = hi(op["length_upper"])
    coercive_inverse = ((1 + length**2 / 2) / m).upper()
    form_norm = (M + Jr * Ct / 5).upper()
    lift = Ce.sqrt().upper()
    poisson = (lift * (1 + coercive_inverse * form_norm)).upper()
    source_solution = coercive_inverse
    DN_augmented = (lift * form_norm * poisson).upper()
    contact = (lift * (form_norm * source_solution + 1)).upper()
    boundary_source = (Ct * Jr).sqrt().upper()
    mean_pivot_lower = (m / (length * Jr)).lower()
    mean_pivot_inverse = (length * Jr / m).upper()
    if not (coercive_inverse < 2**10 and form_norm < 180 and lift < 2
            and poisson < 2**19 and DN_augmented < 2**28
            and contact < 2**19 and boundary_source < 16
            and mean_pivot_lower > 0 and mean_pivot_inverse < 2**12):
        raise ValueError("the actual augmented positive-domain constants failed")

    report = dict(
        kind="actual_exterior_full_frequency_Robin_and_augmented_positive_domain",
        complete=True,
        source_sha256=sha(__file__),
        input_sha256={str(args.graft): sha(args.graft), str(args.closed): sha(args.closed)},
        dependency_sha256={name: sha(Path(__file__).with_name(name)) for name in
                           ("fourfold_phase_beta_bulk_interval.py",
                            "fourfold_phase_beta_interval.py")},
        exact_parameter_interval=graft["exact_parameter_interval"],
        origin_inputs_sha256=graft["origin_inputs_sha256"],
        direction_sha256=graft["direction_sha256"],
        bits=args.bits,
        barrier_length=str(T), bump_width=str(ell), bump_total_length=str(L),
        unmodified_length=str(B),
        bump_parameter_definition=(
            "For each fixed exact delta, choose the least point in the nonempty "
            "closed R74 all-frequency good set on the exact mode-four matching curve; "
            "no simultaneous or continuous choice over delta is asserted."),
        all_frequency_selection=dict(
            m="abs(n), n in 4Z and n != 0",
            angle_sine_lower="1/549755813888",
            one_cap_good_measure_lower="16301/16384",
            both_caps="the same exact choice by radial reflection"),
        actual_entrance={key: ball_record(value) for key, value in dict(
            radius_lower=a_lo, radius_upper=a_hi, height_lower=z_lo, height_upper=z_hi,
            omega_lower=w_lo, omega_upper=w_hi, A_lower=A_lo, A_upper=A_hi,
            radius_squared_over_height_upper=p_hi).items()},
        added_actual_geometry={key: ball_record(value) for key, value in dict(
            omega_lower=w_bump_lo, absolute_q_upper=q_bump_abs,
            principal_curvature_upper=curvature_bump,
            Cartesian_displacement_upper=displacement,
            outer_height_shift_upper=height_shift).items()},
        all_frequency_Robin={key: ball_record(value) for key, value in dict(
            reflection_coefficient_modulus_upper=reflection,
            normalized_true_tail_difference_from_exact_stable_line=gamma_tail_error,
            normalized_stable_line_difference_from_absD_over_4omega=reference_error,
            normalized_total_difference_from_absD_over_4omega=total_error,
            gamma_m_over_m_lower=robin_lo, gamma_m_over_m_upper=robin_hi).items()},
        actual_augmented_positive_operator={key: ball_record(value) for key, value in dict(
            one_Dirichlet_coercive_inverse=coercive_inverse,
            full_form_norm=form_norm, trace_lift=lift,
            full_Poisson=poisson, Vdual_source_to_solution=source_solution,
            turning_DN_and_regular_mean_output=DN_augmented,
            full_source_to_turning_contact_and_regular_mean=contact,
            physical_regular_Hminus_half_source_to_Vdual=boundary_source,
            absolute_regular_mean_response_to_turning_constant_lower=mean_pivot_lower,
            true_regular_mean_row_pivot_inverse=mean_pivot_inverse).items()},
        scope=[
            "The R69 core, body and natural graft remain exactly unchanged.",
            "Only the far radial double bump and its induced outer height shift are added.",
            "Every nonzero fourfold frequency uses its true infinite R72 tail line.",
            "The regular mean value is imposed and its remaining flux is retained as a finite output row.",
            "The positive-domain estimate is an unweighted Sobolev statement.",
            "No nonlinear exact family, parameter-continuous bump choice, reach, or visible-amplitude claim."
        ])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(complete=True, report_sha256=sha(args.out),
                         gamma_over_m_lower=report["all_frequency_Robin"]["gamma_m_over_m_lower"]["ball"],
                         gamma_over_m_upper=report["all_frequency_Robin"]["gamma_m_over_m_upper"]["ball"],
                         Poisson=report["actual_augmented_positive_operator"]["full_Poisson"]["ball"]),
                     ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Directed R76 constants for the actual weighted exterior/positive-domain inverse.

This consumes the complete, same-object R69 and R74 reports.  The proof of the
operator-valued analytic kernel bounds is in R76; this program pays every
constant in that proof with Arb.  The angular weight is in the actual sheared
coordinate.  No parameter-continuous choice of the far bump, nonlinear inverse,
or full central feedback inverse is asserted.
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


def upper_max(*values):
    return max(v.upper() for v in values)


def first_moment(modulus, width):
    # 2 M sum_{d>=1} d exp(-width*d/2).  expm1 avoids cancellation.
    return (2 * modulus * (-width / 2).exp()
            / (-(-width / 2).expm1())**2).upper()


def records(values):
    if not all(v.is_finite() for v in values.values()):
        raise ValueError("a directed constant is not finite")
    return {key: ball_record(value) for key, value in values.items()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--closed", type=Path,
                   default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    p.add_argument("--robin", type=Path,
                   default=Path("notes/2026-11-12-actual-exterior-robin-certificate.json"))
    p.add_argument("--bits", type=int, default=256)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.bits < 128:
        raise ValueError("use at least 128 bits")
    ctx.prec = args.bits
    closed = json.loads(args.closed.read_text())
    robin = json.loads(args.robin.read_text())
    if not closed.get("complete") or not robin.get("complete"):
        raise ValueError("both actual input reports must be complete")
    for key in ("origin_inputs_sha256", "direction_sha256", "exact_parameter_interval"):
        if closed[key] != robin[key]:
            raise ValueError("the actual input objects do not agree")
    if sha(args.closed) not in robin["input_sha256"].values():
        raise ValueError("the Robin report does not bind this closed-background report")

    op = closed["complete_finite_positive_operator"]
    rop = robin["actual_augmented_positive_operator"]
    ent = robin["actual_entrance"]
    sigma0 = exact_arb(Fraction(closed["physical_angular_strip"]))
    Ir = hi(op["integrated_real_drift"])
    Ic = hi(op["integrated_complex_drift"])
    small_physical_strip = sigma0 / 20
    flow_factor = (Ir + Ic / 19).exp().upper()
    rho = (small_physical_strip / (2 * flow_factor)).lower()
    M = (Ir + Ic / 39).exp().upper()
    argument = (Ic / 39).upper()
    mu = (arb(49) / (50 * M)).lower()
    sector = arb(10) / 49
    if not (sigma0 == arb(1) / 512 and rho > 0 and argument < arb(1) / 5
            and mu > 0 and sector < arb(1) / 4):
        raise ValueError("the actual refined angular-flow sector gate failed")

    r = rho / 2
    M2 = (2 * M / rho).upper()
    M3 = (8 * M / rho**2).upper()
    kernel_near = ((M2**2 + arb(2) * M * M3 / 3) / mu**2 + M**2 + 1).upper()
    kernel_far = (16 * M**4 / mu**2 + 10 * M**2).upper()
    kernel = upper_max(kernel_near, kernel_far)

    wlo = lo(ent["omega_lower"])
    Alo = lo(ent["A_lower"])
    Ahi = hi(ent["A_upper"])
    p_hi = hi(ent["radius_squared_over_height_upper"])
    b_lower = (4 * wlo / Ahi).lower()
    c0_upper = (1 / (4 * wlo)).upper()
    c1_upper = (2 * p_hi / Alo**2).upper()
    if not (b_lower > 0 and b_lower < 1 and Alo > 0):
        raise ValueError("the exact stable-line splitting leaves its admissible box")
    resolvent = (M**2 * (8 / b_lower + 2 * (1 + 2 / mu**2).log() + 2)).upper()
    B = exact_arb(Fraction(robin["unmodified_length"]))
    attenuation = (2 * wlo * B - 2 * M * r).lower()
    if not attenuation > 1:
        raise ValueError("the true infinite-tail error is not analytic on this tube")
    q_tail = (-4 * attenuation).exp().upper()
    tail = (M**2 * arb(2)**45 * q_tail / (1 - q_tail)**2).upper()
    boundary_remainder = (c0_upper * kernel + c1_upper * (M + resolvent) + tail).upper()
    # R69's old modulus is exactly the physical coefficient maximum times its
    # old flow factor.  Directed division recovers an upper bound for that maximum.
    physical_matrix = (hi(op["complex_matrix_modulus"])
                       / lo(op["complex_J_and_inverse"])).upper()
    matrix = (physical_matrix * M).upper()
    NB = first_moment(boundary_remainder, r)
    NC = first_moment(matrix, rho)
    NJ = first_moment(M, rho)

    Ct = hi(op["trace_squared"])
    Ce = hi(op["extension_squared"])
    lift = Ce.sqrt().upper()
    g = hi(rop["one_Dirichlet_coercive_inverse"])
    form = hi(rop["full_form_norm"])
    T0 = ((Ct * Ce).sqrt() * NJ).upper()
    N0 = (NC + Ct * NB).upper()
    Nstar = (2 * N0 + 3 * form * T0).upper()
    weight = arb(2)**(-100)
    weight_budget = min((rho / 4).lower(), (1 / (4 * T0)).lower(),
                        (1 / (2 * g * Nstar)).lower())
    transport_error = (weight * T0).upper()
    form_error = (weight * N0).upper()
    transported_error = (weight * Nstar).upper()
    neumann_ratio = (g * transported_error).upper()
    if not (weight > 0 and weight < weight_budget
            and transport_error < arb(1) / 4 and neumann_ratio < arb(1) / 2
            and tail < arb(2)**(-100)):
        raise ValueError("the actual signed same-width inverse gate failed")

    Tnorm = (1 + transport_error).upper()
    weighted_form = (form + form_error).upper()
    solution_source = (2 * g * Tnorm**2).upper()
    poisson = (lift * (1 + solution_source * weighted_form)).upper()
    contact_data = (lift * weighted_form * poisson).upper()
    contact_source = (lift * (weighted_form * solution_source + 1)).upper()
    mean_pivot = hi(rop["true_regular_mean_row_pivot_inverse"])
    trace_source = Ct.sqrt().upper()
    if not (poisson < 2**21 and solution_source < 2**12
            and contact_data < 2**30 and contact_source < 2**21
            and mean_pivot < 2**12 and trace_source < 7):
        raise ValueError("the declared weighted Poisson/source/contact constants failed")

    report = dict(
        kind="actual_same_width_exterior_Robin_and_augmented_positive_domain",
        complete=True,
        source_sha256=sha(__file__),
        input_sha256={str(args.closed): sha(args.closed), str(args.robin): sha(args.robin)},
        dependency_sha256={name: sha(Path(__file__).with_name(name)) for name in
                           ("fourfold_phase_beta_bulk_interval.py",
                            "fourfold_phase_beta_interval.py")},
        exact_parameter_interval=closed["exact_parameter_interval"],
        origin_inputs_sha256=closed["origin_inputs_sha256"],
        direction_sha256=closed["direction_sha256"],
        bits=args.bits,
        angular_convention="physical angle phi, period 2*pi; restrict the proved operator to 4Z",
        signed_weight="1/1267650600228229401496703205376",
        weight_types=["exp(s*abs(n))", "exp(s*(log(e+abs(n))^(3/2)-1))"],
        refined_actual_flow=records(dict(
            physical_strip=sigma0, bootstrap_strip=small_physical_strip,
            bootstrap_flow_factor=flow_factor, sheared_angular_strip=rho,
            complex_derivative_and_inverse=M, logarithmic_derivative_argument=argument,
            derivative_real_part_lower=mu, derivative_sector_slope_upper=sector,
            common_translation_strip=r, second_derivative=M2, third_derivative=M3)),
        actual_boundary_kernel=records(dict(
            near_absD_kernel_difference=kernel_near,
            far_absD_kernel_difference=kernel_far, absD_kernel_difference=kernel,
            stable_line_b_lower=b_lower, stable_line_c0_upper=c0_upper,
            stable_line_c1_upper=c1_upper, pulled_resolvent=resolvent,
            true_tail_analytic_attenuation=attenuation,
            true_tail_analytic_ratio=q_tail, true_tail_operator=tail,
            normalized_order_zero_boundary_remainder=boundary_remainder)),
        actual_commutators=records(dict(
            physical_coefficient_modulus=physical_matrix, improved_matrix_modulus=matrix,
            boundary_first_lag_moment=NB, matrix_first_lag_moment=NC,
            mean_density_first_lag_moment=NJ, mean_space_transport_rate=T0,
            untransported_form_rate=N0, transported_form_rate=Nstar,
            sufficient_weight_budget=weight_budget, selected_weight=weight,
            mean_space_transport_error=transport_error, untransported_form_error=form_error,
            transported_form_error=transported_error, Neumann_ratio=neumann_ratio)),
        actual_weighted_solution=records(dict(
            full_Poisson=poisson, Vdual_source_to_solution=solution_source,
            turning_DN_and_regular_mean_output=contact_data,
            full_source_to_turning_contact_and_regular_mean=contact_source,
            already_pulled_regular_Hminus_half_source_to_Vdual=trace_source,
            true_regular_mean_row_pivot_inverse=mean_pivot)),
        scope=[
            "The regular boundary operator is C_H^* Gamma_ext C_H in real dphi measure.",
            "Its principal term is c0*abs(D_phi) because both boundary density factors are retained.",
            "The trial and test mean constraints are transported separately by T_s and T_minus_s.",
            "The full turning contact and regular physical mean-flux row are retained.",
            "Sources are weighted after the actual shear/ground-state density conversion.",
            "The signed negative-weight statement is in the corresponding Fourier completion and dual pairing.",
            "The constants are uniform pointwise over the exact affine input interval.",
            "The R74 far-bump selection is not asserted continuous in the parameter.",
            "No full central feedback inverse, nonlinear family, reach, or visible-amplitude claim."
        ])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(complete=True, report_sha256=sha(args.out),
                         signed_weight=report["signed_weight"],
                         rho=float(rho), derivative_modulus=float(M),
                         neumann_ratio=float(neumann_ratio), Poisson=float(poisson)),
                     ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()

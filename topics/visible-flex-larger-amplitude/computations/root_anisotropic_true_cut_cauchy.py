#!/usr/bin/env python3
"""Complete true-cut value and Cauchy budgets on the actual R74 polydisc.

Uses exact Fraction arithmetic on immutable, outward endpoint certificates.
The R63 source, its omitted-and-corrected far lift, and R58-minus-auxiliary
correction are separate summands. No quadrature, Arb, ODE or Node is used.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import gc
import json
from pathlib import Path
import resource
import time

from root_moving_auxiliary_centre_family import (
    digest, exact, lower, upper, pow2, read, record, write_new)


def ceil_fraction(value):
    return -((-value.numerator) // value.denominator)


def uprecord(value, bits=192):
    """An outward dyadic bound, retaining every positive summand before rounding."""
    value = F(value)
    if value < 0:
        raise ValueError("This ledger contains nonnegative majorants only")
    if not value:
        return record(value)
    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    if value < pow2(exponent):
        exponent -= 1
    unit = pow2(exponent + 1 - bits)
    rounded = ceil_fraction(value / unit) * unit
    if rounded < value:
        raise ArithmeticError("An outward serialization rounded down")
    return record(rounded)


def require_hashes(doc):
    for name, sha in doc.get("input_hashes", {}).items():
        if digest(name) != sha:
            raise ValueError("An immutable prerequisite changed: " + name)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("family", "source", "far-completion", "trace", "out"):
        ap.add_argument("--" + name, type=Path, required=True)
    ap.add_argument("--rss-kib", type=int, default=51200)
    args = ap.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError("Use a fresh immutable executed output")
    paths = {key: getattr(args, key) for key in
             ("family", "source", "far_completion", "trace")}
    hashes = {str(path): digest(path) for path in paths.values()}

    family = read(args.family)
    require_hashes(family)
    if not family["all_gates"] or not all(family["gates"].values()):
        raise ValueError("The actual anisotropic family was not paid")
    if ([r["cell"] for r in family["auxiliary_rows"]] != list(range(12,225))
            or [r["index"] for r in family["joint_rows"]] != list(range(641))
            or [r["cell"] for r in family["domain_rows"]] != list(range(12,225))):
        raise ValueError("An original auxiliary, full-frequency or physical row is absent")
    alpha = exact(family["main_linear_factor"])
    kappa_aux = exact(family["auxiliary_nonlinear_factor"])
    kappa_rest = exact(family["rest_coefficient_factor"])
    scale = exact(family["envelope_factor"])
    if (alpha, kappa_aux, kappa_rest, scale) != (
            F(1025,1024), F(259,256), F(65,64), F(257,256)):
        raise ValueError("Keep the actual R74 domain and its proved multipliers")
    axes = family["parameter_axes"]
    if [a["mode"] for a in axes] != list(range(2,41,2)):
        raise ValueError("Every independent input parameter is required")
    for row in axes:
        expected = F(1,16) if row["mode"] == 4 else F(1,1024)
        if (exact(row["relative_radius"]) != expected or
                exact(row["half_axis"]) != expected*abs(exact(row["exact_centre"]))):
            raise ValueError("A normalized input parameter axis changed")
    axes_by_mode = {a["mode"]: exact(a["half_axis"]) for a in axes}
    rho = pow2(-30)
    if not all(exact(r["total_correction"]) < rho and r["mean_domain"]
               and r["physical_domain"] for r in family["domain_rows"]):
        raise ValueError("The original physical working domain must remain valid")
    cut_t = exact(family["domain_rows"][0]["total_correction"])
    if not all(exact(r["new_radius"]) == 4*exact(r["old_radius"])
               and r["map_inclusion"] and r["contraction"]
               for r in family["joint_rows"]):
        raise ValueError("The complete correction must be exactly the proved4r box")
    if not upper(family["auxiliary_far_upper"]) < pow2(-2224):
        raise ValueError("The actual auxiliary far graph left its original ball")
    family_reference_hash = family["input_hashes"][
        "notes/2026-11-12-closure-newg-strong-m20-real-reference.json"]
    del family
    gc.collect()

    source = read(args.source)
    require_hashes(source)
    if (not source["all_gates"] or source["selected_modes"] != [2,4]
            or source["auxiliary_input_modes"] != list(range(2,93,2))
            or source["cells"] != list(range(12,225))
            or source["outer_strip"] != "1/64"):
        raise ValueError("The original complete selected source ledger is required")
    source_values = {}
    for row in source["rows"]:
        if [s["cell"] for s in row["source_rows"]] != list(range(12,225)):
            raise ValueError("A selected source omitted an original physical cell")
        source_values[row["mode"]] = upper(row["auxiliary_Kbar_Wsigma1_upper"])
    del source
    gc.collect()

    far, trace = read(args.far_completion), read(args.trace)
    require_hashes(far)
    require_hashes(trace)
    if not far["all_gates"] or not trace["all_gates"]:
        raise ValueError("The actual far completion and full-frequency trace are needed")
    if trace["input_hashes"][
            "notes/2026-11-12-closure-newg-strong-m20-real-reference.json"] != family_reference_hash:
        raise ValueError("The cut trace and family use different actual centres")
    columns = read("notes/2026-11-12-closure-strong-parameter-columns-r2-summary.json")
    if exact(columns["physical_domain"]) != rho:
        raise ValueError("The mean-height and joint physical domains differ")
    del columns
    far_bound = exact(far["whole_low46_far_K_Wsigma1_upper"])
    if not 0 < far_bound < pow2(-7800):
        raise ValueError("The complete far summand must be explicitly positive")
    if lower(trace["B"]) < 1:
        raise ValueError("The balanced norm must dominate the unbalanced mean input")

    source_factor = kappa_rest**2
    component_factors = {
        "pure_main_squared": alpha**2,
        "main_times_rest": alpha*kappa_rest,
        "rest_squared": kappa_rest**2,
        "generic_quadratic": scale**2,
        "complete_mean_and_inverse_cubic_remainder": scale**3,
    }
    if not all(factor <= source_factor for factor in component_factors.values()):
        raise ArithmeticError("The common source multiplier omitted a positive family")
    full_correction_factor = 4*scale
    radius = F(3,4)
    first_factor = 1/(1-radius)
    second_factor = 4/(1-radius)**2

    def cauchy(value):
        return dict(uniform_value_upper=uprecord(value),
                    first_derivative_linf_to_output_upper=uprecord(first_factor*value),
                    second_derivative_linf_pair_to_output_upper=uprecord(second_factor*value))

    selected = []
    selected_value = {}
    old_full_low = upper(trace["beta"]["outer"]["full_head_low_correction_K"])
    for mode in (2,4):
        source_part = source_factor*source_values[mode]
        full_head_part = full_correction_factor*old_full_low
        value = source_part + far_bound + full_head_part
        selected_value[mode] = value
        selected.append(dict(mode=mode,
            norm="(1+m) exp(m/64) times the complete cosine coefficient absolute value",
            old_source_only=uprecord(source_values[mode]),
            rescaled_complete_source=uprecord(source_part),
            complete_auxiliary_far=record(far_bound),
            full_frequency_minus_auxiliary=uprecord(full_head_part),
            **cauchy(value)))

    trace_rows = {}
    for strip in ("outer", "head"):
        old = trace["beta"][strip]
        low_value = kappa_aux*upper(old["auxiliary_low_correction_K"])
        low_value += full_correction_factor*upper(old["full_head_low_correction_K"])
        high_parts = [full_correction_factor*upper(v) for v in old["high_bands_joint"]]
        high_value = sum(high_parts,F(0))
        if len(high_parts) != 3:
            raise ValueError("Every near/rest/infinite trace band must be retained")
        trace_rows[strip] = dict(
            all46_low_nonlinear_K=cauchy(low_value),
            complete_high_balanced_P_K=cauchy(high_value),
            high_bands_value_upper=[uprecord(v) for v in high_parts],
            complete_high_P=cauchy(high_value/lower(trace["B"])),
            low_Q_and_P_nonlinear_remainder_identically_zero=True)

    point_R = scale*upper(trace["true_point_epsilon_upper"])*(1+cut_t)
    if not point_R < F(1,10000):
        raise ArithmeticError("The complete complex R23 mean small root domain failed")
    mean_slope = 40*point_R**2
    # Both auxiliary and full-head means use the same physical rho. The new
    # auxiliary quadratic mean costs S^2; the joint difference costs4S^2.
    # The unchanged infinite tail bound also fits inside that larger factor.
    mean_height_factor = 4*scale**2
    mean_height = mean_height_factor*upper(
        trace["beta"]["cuff_normalized_mean_height_vs_background_at_zero"])

    propagated = []
    for row in far["propagation_rows"]:
        node, mode = row["endpoint_physical_node"], row["mode"]
        if exact(row["whole_low_K_far_upper"]) != far_bound:
            raise ValueError("The old propagation did not use this defined far bound")
        # E is an outward bound for C*F_b, with F_b the exact positive defined
        # majorant, not an unknown measured response. Therefore E/F_b >= C.
        transfer = exact(row["cut_Q_centre_addition_upper"])/far_bound
        value = transfer*selected_value[mode]/axes_by_mode[mode]
        propagated.append(dict(endpoint_physical_node=node, mode=mode,
            transfer_from_Wsigma1_K_to_canonical_Q_upper=uprecord(transfer),
            output_axis=record(axes_by_mode[mode]),
            normalized_inner_nonlinear_feedback=cauchy(value),
            complete_outer_Schur_or_all_frequency_response_claimed=False))
    if sorted((r["endpoint_physical_node"],r["mode"]) for r in propagated) != [
            (10,2),(10,4),(11,2),(11,4)]:
        raise ValueError("Both actual readouts and both selected modes are required")

    gates = dict(
        actual_R74_full213_641_and_parameter_axes_retained=True,
        source_scaling_covers_every_quadratic_and_complete_remainder_component=True,
        same_complex_Wiener_and_full_mean_domain=True,
        complete_auxiliary_far_explicitly_added=True,
        separate_complete_full_frequency_minus_auxiliary_added=True,
        all46_coarse_low_and_all_three_high_bands_retained=True,
        complete_mean_slope_and_single_cuff_normalized_height_retained=True,
        dimension_free_linf_Cauchy_on_radius_three_quarters=True,
        both_actual_normalized_boundary_readouts_included=True,
        both_selected_inner_feedback_row_bounds_below_one=all(
            upper(r["normalized_inner_nonlinear_feedback"][
                "first_derivative_linf_to_output_upper"]) < 1 for r in propagated))
    result = dict(
        status="Executed complete true-cut value/Cauchy ledger on the actual R74 complex polydisc",
        author="/root (GPT-6 Astra Pro, AI-assisted)",
        all_gates=all(gates.values()), gates=gates,
        parameter_norm="xi_m=(a_m-q_m*)/v_m; max_m |xi_m|; all20 inputs simultaneous",
        parameter_axes=axes, interior_parameter_radius=record(radius),
        source_factor=record(source_factor), component_factors={
            name:record(value) for name,value in component_factors.items()},
        full_head_correction_factor=record(full_correction_factor),
        first_Cauchy_factor=record(first_factor), second_Cauchy_factor=record(second_factor),
        selected_true_DN_minus_exact_linear_DN=selected,
        complete_coarse_trace_rows=trace_rows,
        complete_nonmean_cut_mean_input_upper=uprecord(point_R),
        complete_mean_slope=cauchy(mean_slope),
        cuff_normalized_complete_mean_height=cauchy(mean_height),
        mean_height_factor=record(mean_height_factor),
        mean_height_convention="Same single cuff value as the axisymmetric background; no per-cell or per-parameter free vertical shifts",
        actual_selected_boundary_feedback_rows=propagated,
        input_hashes=hashes, source_sha256=digest(__file__),
        helper_sha256=digest(Path(__file__).with_name("root_moving_auxiliary_centre_family.py")),
        no_new_ODE=True, no_new_source_integral=True, no_Arb=True, no_Node=True,
        complete_outer_matching_or_inverse_paid=False,
        scope="True inner DN and mean interface only; outer nonlinear response, all output-frequency Schur rows and global closed-family geometry remain open",
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result["peak_rss_kib"] > args.rss_kib:
        raise MemoryError("The declared owned Fraction-memory observer was exceeded")
    output = write_new(args.out,result)
    print(json.dumps(dict(event="done",all_gates=result["all_gates"],output=output,
        feedback_rows=[dict(node=r["endpoint_physical_node"],mode=r["mode"],
            derivative=r["normalized_inner_nonlinear_feedback"][
                "first_derivative_linf_to_output_upper"]["display"]) for r in propagated],
        elapsed_seconds=result["elapsed_seconds"],peak_rss_kib=result["peak_rss_kib"])),flush=True)
    if not result["all_gates"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()

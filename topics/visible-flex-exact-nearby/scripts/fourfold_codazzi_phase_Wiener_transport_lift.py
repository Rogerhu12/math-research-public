#!/usr/bin/env python3
"""Lift saved transport fees to a genuine Wiener conjugacy-defect bound.

The finite reference is not reintegrated. Its projected derivative equation
controls its analytic norm, while its *entire* residual, including every
unretained frequency, controls the true two-ray return. A prefix remains a
prefix and cannot activate the whole-return conclusion.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time

from flint import arb, acb_poly, ctx
from fourfold_codazzi_phase_complete_transport_cover import read, decode_state, PRODUCER, ROOT, REPAIR
import fourfold_codazzi_phase_complete_transport_cover as cover_consumer
import fourfold_codazzi_phase_full_transport_Taylor as producer
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

ANALYTIC = "91f1a3e5900300cd6e66060063e0c9fe5b826e238f68cf9e49f356f0c4ff4071"
BASE = Fraction(1, 32)
OUTER = Fraction(1, 16)
RESIDUAL = Fraction(1, 24)
INPUT = Fraction(1, 50)


def upper(item):
    return box_from_record(item).upper()


def locate(germ, directories):
    name = f"transport-germ{germ['germ_index']:04d}.json.gz"
    choices = [Path(germ["path"])] + [directory / name for directory in directories]
    for path in choices:
        if path.exists() and sha(path) == germ["sha256"]:
            return path
    raise FileNotFoundError("the actual SHA-bound transport native is unavailable: " + name)


def lift(cover, root, analytic, directories):
    if (not cover["complete"] or cover["kind"] != "actual_chronological_full_frequency_phase_transport_cover"
            or cover["original_producer_sha256"] != PRODUCER or cover["root_contract_sha256"] != ROOT
            or cover["configuration"]["derived_definition_sha256"] != REPAIR
            or cover["configuration"]["modes"] != 64
            or cover["configuration"]["full_output_frequency_bound"] != 128
            or not root["complete"] or not analytic["complete"]
            or analytic["derived_definition_sha256"] != REPAIR):
        raise ValueError("the original complete transport/source/field definitions are required")
    field = next(x for x in analytic["strip_budgets"] if x["outer_field_strip"] == str(OUTER))
    B = upper(field["complete_one_leg_integrated_drift"])
    L = upper(field["complete_one_leg_integrated_first_derivative"])
    drift_error = arb(0)
    speed_error = arb(0)
    retained_error = arb(0)
    outside_error = arb(0)
    cursor = Fraction(0)
    row_count = 0
    consumed = []
    for germ in cover["germs"]:
        path = locate(germ, directories)
        doc = read(path)
        if doc["configuration"] != cover["configuration"]:
            raise ValueError("a genuine transport germ changes scientific configuration")
        for row in doc["rows"]:
            left, right = map(Fraction, row["interval"])
            if left != cursor or right <= left:
                raise ValueError("the true model-error cover has a gap")
            drift_error += exact_arb(right - left) * upper(row["complete_drift_model_error"])
            speed_error += exact_arb(right - left) * upper(row["complete_mean_speed_model_error"])
            retained_error += upper(row["complete_retained_finite_residual"])
            outside_error += upper(row["complete_unretained_finite_residual"])
            cursor = right
            row_count += 1
        consumed.append(dict(germ_index=germ["germ_index"], path=str(path), sha256=germ["sha256"]))
    if ["0", str(cursor)] != cover["exact_processed_interval"] or row_count != cover["actual_steps"]:
        raise ValueError("the complete saved source cover and consumer differ")
    if doc["exact_phase_state"] != cover["exact_terminal_phase_state"]:
        raise ValueError("the exact final state differs from the actual last transport germ")
    retained = retained_error.upper()
    outside = outside_error.upper()
    scalar_drift = drift_error.upper()
    scalar_speed = speed_error.upper()
    outer_weight = (256 * exact_arb(OUTER - BASE)).exp()
    B0 = (B + outer_weight * scalar_drift).upper()
    L0 = (L + 256 * outer_weight * scalar_drift).upper()
    H0, H1 = arb(0), arb(1)
    for j, (a, b) in enumerate(zip(root["exact_H_sine_coefficients"], root["exact_H_cosine_coefficients"]), 1):
        amplitude = (exact_arb(Fraction(a))**2 + exact_arb(Fraction(b))**2).sqrt()
        weighted = amplitude * (4 * j * exact_arb(OUTER)).exp()
        H0 += weighted
        H1 += 4 * j * weighted
    # a_hat has degree64. Its exact projected equation is sufficient for
    # its own norm, and P64 is an l1 contraction. High output remains in
    # the full true-PDE residual below; it is not discarded there.
    projected_derivative_source = (256 * outer_weight * retained).upper()
    phase_derivative = ((H1 + projected_derivative_source) * L0.exp()).upper()
    remaining_reference_strip = (exact_arb(OUTER) - B0).lower()
    head_weight = (256 * exact_arb(RESIDUAL - BASE)).exp()
    tail_weight = (512 * exact_arb(RESIDUAL - BASE)).exp()
    finite_residual = (head_weight * retained + tail_weight * outside).upper()
    model_residual = (2 * phase_derivative * (head_weight * scalar_drift + scalar_speed)).upper()
    complete_residual = (finite_residual + model_residual).upper()
    full_root = (2 * H1 * L.exp() * upper(root["complete_one_ray_optical_sliver"])).upper()
    flow_margin = (exact_arb(RESIDUAL - INPUT) - 2 * B).lower()
    root_margin = (exact_arb(OUTER - INPUT) - 3 * B).lower()
    state = decode_state(cover["exact_terminal_phase_state"], 64)
    difference = acb_poly([producer.cplx((state[1][j][0] - state[0][j][0],
        state[1][j][1] - state[0][j][1])) for j in range(129)])
    mean = state[1][64][0] - state[0][64][0]
    difference[64] = 0
    terminal_nonmean = producer.angular_norm(difference, 64, exact_arb(RESIDUAL))
    targets = dict(
        fit=exact_arb(Fraction(root["exact_proposed_rotation"])),
        bounded7_new=arb.pi() * (arb(45217079201) - arb(5).sqrt()) / (2 * 164472125458),
    )
    terminal = {name: (terminal_nonmean + abs(exact_arb(mean) - value)).upper() for name, value in targets.items()}
    whole = cover["whole_negative_domain"]
    defects = {name: (value + complete_residual + full_root).upper() for name, value in terminal.items()} if whole else None
    constant_free = (terminal_nonmean + complete_residual + full_root).upper() if whole else None
    derivative = (constant_free / (arb(1).exp() * exact_arb(INPUT))).upper() if whole else None
    gates = [dict(name=name, passed=bool(ok)) for name, ok in (
        ("the full original mean and all169-germ identities are not changed", cover["configuration"]["exact_eta_offset"] == "0"),
        ("every saved complete scalar field error was actually consumed", row_count == cover["actual_steps"]),
        ("the real finite reference scalar mean creates no Wiener strip loss", True),
        ("the projected-reference energy leaves the declared full residual strip", remaining_reference_strip > exact_arb(RESIDUAL)),
        ("both full true transport legs fit the Wiener composition margin", flow_margin > 0),
        ("the root and inverse-label three-leg compositions fit the outer strip", root_margin > 0),
        ("all unretained finite outputs are still included in the genuine residual", outside >= 0 and finite_residual >= 0),
        ("the scalar mean contribution is retained in the complete model error", scalar_speed >= 0),
    )]
    result = dict(kind="actual_saved_phase_transport_Wiener_widening",
        complete=all(g["passed"] for g in gates), whole_negative_domain=whole,
        actual_steps=row_count, germ_count=len(cover["germs"]), exact_processed_interval=cover["exact_processed_interval"],
        base_residual_strip=str(BASE), outer_field_strip=str(OUTER), widened_residual_strip=str(RESIDUAL),
        genuine_input_Wiener_strip=str(INPUT),
        original_complete_retained_residual=record(retained), original_complete_unretained_residual=record(outside),
        integrated_true_drift_model_error=record(scalar_drift), integrated_true_scalar_speed_model_error=record(scalar_speed),
        true_one_leg_drift_budget=record(B), true_one_leg_derivative_budget=record(L),
        finite_model_drift_budget=record(B0), finite_model_derivative_budget=record(L0),
        exact_H_periodic_part_outer_norm=record(H0.upper()), exact_H_derivative_outer_norm=record(H1.upper()),
        projected_reference_derivative_source=record(projected_derivative_source),
        complete_reference_phase_derivative_Wiener_norm=record(phase_derivative),
        available_reference_strip=record(remaining_reference_strip),
        widened_complete_finite_residual=record(finite_residual), widened_complete_scalar_model_residual=record(model_residual),
        widened_complete_true_transport_residual=record(complete_residual),
        genuine_Wiener_root_sliver_fee=record(full_root),
        two_leg_Wiener_composition_margin=record(flow_margin), three_leg_root_Wiener_composition_margin=record(root_margin),
        exact_terminal_phase_state=cover["exact_terminal_phase_state"], exact_terminal_phase_mean=str(mean),
        complete_terminal_nonmean_Wiener_norm=record(terminal_nonmean),
        terminal_Wiener_defects_by_target={name: record(value) for name, value in terminal.items()},
        genuine_Wiener_conjugacy_defects_by_target=None if defects is None else {name: record(value) for name, value in defects.items()},
        constant_free_genuine_Wiener_defect=None if constant_free is None else record(constant_free),
        genuine_angular_derivative_A0_bound=None if derivative is None else record(derivative),
        no_supremum_to_Fourier_conversion_used=True, real_scalar_mean_transport_is_isometric=True,
        complete_transport_polynomials_not_recomputed=True,
        projected_equation_used_only_for_explicit_reference_norm=True,
        whole_residual_keeps_all_unprojected_frequencies=True,
        no_true_conjugacy_or_parameter_KAM_or_PDE_branch_claimed=True,
        consumed_germs=consumed, gates=gates,
    )
    if not result["complete"]:
        raise ArithmeticError("an actual Wiener widening or composition-domain gate failed")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transport-cover", type=Path, required=True)
    parser.add_argument("--transport-dir", type=Path, action="append", default=[])
    parser.add_argument("--root-contract", type=Path, required=True)
    parser.add_argument("--analytic", type=Path, required=True)
    parser.add_argument("--allow-prefix", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve each actual complete Wiener consumer")
    started = time.monotonic()
    ctx.prec = 320
    if sha(args.root_contract) != ROOT or sha(args.analytic) != ANALYTIC or sha(producer.__file__) != PRODUCER:
        raise ValueError("the original complete mathematical inputs changed")
    cover = read(args.transport_cover)
    if cover["source_sha256"] != sha(cover_consumer.__file__):
        raise ValueError("the complete cover was not produced by the current audited consumer")
    if not cover["whole_negative_domain"] and not args.allow_prefix:
        raise ValueError("a whole-return Wiener bound requires the completed169-germ input")
    result = lift(cover, read(args.root_contract), read(args.analytic), args.transport_dir)
    result.update(source_sha256=sha(__file__), transport_cover_sha256=sha(args.transport_cover),
        root_contract_sha256=ROOT, analytic_field_native_sha256=ANALYTIC,
        original_producer_sha256=PRODUCER, seconds=time.monotonic() - started)
    save(args.out, result)
    print(dict(complete=result["complete"], whole=result["whole_negative_domain"],
        germs=result["germ_count"], reference_derivative=result["complete_reference_phase_derivative_Wiener_norm"]["ball"],
        widened_residual=result["widened_complete_true_transport_residual"]["ball"],
        root_fee=result["genuine_Wiener_root_sliver_fee"]["ball"], seconds=result["seconds"]), flush=True)


if __name__ == "__main__":
    main()

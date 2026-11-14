#!/usr/bin/env python3
"""Certify a terminal postcomposition by full Laurent exponential arithmetic.

A floating least-squares calculation only proposes exact dyadic coefficients.
Every claimed norm uses Arb, every Laurent product/output is included, and the
whole infinite exponential tail and K' transport/root costs are paid. The saved
transport recurrence is not repeated. A prefix never becomes a true return.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_poly, ctx
from fourfold_codazzi_phase_complete_transport_cover import read, decode_state, PRODUCER, ROOT
from fourfold_codazzi_phase_Wiener_transport_lift import upper, INPUT, RESIDUAL, OUTER
import fourfold_codazzi_phase_Wiener_transport_lift as wiener_consumer
import fourfold_codazzi_phase_full_transport_Taylor as producer
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def trig_norm(sines, cosines, width, derivative=0):
    return sum(((exact_arb(a)**2 + exact_arb(b)**2).sqrt()
                * (4*j)**derivative * (4*j*width).exp()
                for j, (a, b) in enumerate(zip(sines, cosines), 1)), arb(0)).upper()


def propose(state, modes, grid, omega):
    N = (len(state[0])-1)//2
    x = np.arange(grid, dtype=float) * (np.pi/(2*grid))
    values = []
    for side in state:
        w = np.full(grid, float(side[N][0]))
        for j in range(1, N+1):
            a, b = side[N+j]
            w += 2*(float(a)*np.cos(4*j*x)-float(b)*np.sin(4*j*x))
        values.append(w)
    ap, am = x+values[0], x+values[1]
    columns = [np.sin(4*j*am)-np.sin(4*j*ap) for j in range(1, modes+1)]
    columns += [np.cos(4*j*am)-np.cos(4*j*ap) for j in range(1, modes+1)]
    columns += [-np.ones(grid)]
    matrix = np.stack(columns, axis=1)
    answer, _, rank, singular = np.linalg.lstsq(
        matrix, -(values[1]-values[0]-float(omega)), rcond=None)
    if rank != 2*modes+1 or not np.isfinite(answer).all():
        raise ArithmeticError("the proposed terminal fit is rank deficient or nonfinite")
    a = [Fraction(float(z)) for z in answer[:modes]]
    b = [Fraction(float(z)) for z in answer[modes:2*modes]]
    proposed = omega + Fraction(float(answer[-1]))
    return a, b, proposed, dict(
        method="binary64 sampled least squares, used only to choose exact dyadic coefficients",
        grid=grid, rank=int(rank), smallest_singular_value=float(singular[-1]),
        sampled_residual_not_used_as_a_bound=True)


def powers(p, degree):
    result = [acb_poly([1])]
    for _ in range(degree):
        result.append(result[-1]*p)
    return result


def terminal(state, a, b, degree, width):
    N = (len(state[0])-1)//2
    J = len(a)
    full = N*degree+J
    positive = acb_poly([])
    remainder = arb(0)
    tail_rows = []
    for side_index, side in enumerate(state):
        m = side[N][0]
        coeff = [producer.cplx(z) for z in side]
        coeff[N] = 0
        w = acb_poly(coeff)
        norm = producer.angular_norm(w, N, width)
        wp = powers(w, degree)
        sign = -1 if side_index == 0 else 1
        for j, (sj, cj) in enumerate(zip(a, b), 1):
            amplitude = (exact_arb(sj)**2+exact_arb(cj)**2).sqrt()
            kc = acb(exact_arb(cj/2), exact_arb(-sj/2))
            taylor = acb_poly([])
            scale = acb(1)
            for n, p in enumerate(wp):
                taylor += p.left_shift(N*(degree-n))*scale
                scale *= acb(0, 4*j)/(n+1)
            phase = acb(0, 4*j*exact_arb(m)).exp()
            positive += taylor.left_shift(J+j)*(sign*kc*phase)
            z = (4*j*norm).upper()
            # amplitude is |k_j|+|k_-j|, so both reflected terms are paid.
            fee = (amplitude*(4*j*width).exp()*z.exp()
                   * z**(degree+1)/math.factorial(degree+1)).upper()
            remainder += fee
            tail_rows.append(dict(side="plus" if side_index == 0 else "minus",
                mode=j, zero_mean_phase_norm=record(norm), exponential_argument=record(z),
                full_positive_and_negative_exponential_tail=record(fee)))
    # The true real terminal polynomial equals positive + its reflected
    # conjugate. This constructs every coefficient up to +/-full.
    real_part = acb_poly([positive[k]+positive[2*full-k].conjugate()
                         for k in range(2*full+1)])
    base = acb_poly([producer.cplx((state[1][k][0]-state[0][k][0],
                                  state[1][k][1]-state[0][k][1]))
                     for k in range(2*N+1)])
    result = real_part+base.left_shift(full-N)
    central = result[full]
    if not central.imag.contains(0):
        raise ArithmeticError("the certified real terminal polynomial has a nonreal central coefficient")
    nonmean = acb_poly([result[k] if k != full else 0 for k in range(2*full+1)])
    norm = producer.angular_norm(nonmean, full, width)
    shells = []
    for left in range(0, full+1, 64):
        right = min(left+63, full)
        subtotal = arb(0)
        for j in range(left, right+1):
            if j:
                subtotal += (abs(result[full+j])+abs(result[full-j]))*(4*j*width).exp()
        shells.append(dict(absolute_frequencies=[left, right], nonmean_norm=record(subtotal.upper())))
    digest = hashlib.sha256()
    for c in result:
        digest.update((c.str(100)+"\n").encode())
    return result, full, norm, remainder.upper(), central, tail_rows, shells, digest.hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--wiener-lift", type=Path, required=True)
    p.add_argument("--root-contract", type=Path, required=True)
    p.add_argument("--post-modes", type=int, default=24)
    p.add_argument("--exp-degree", type=int, default=24)
    p.add_argument("--proposal-grid", type=int, default=2048)
    p.add_argument("--proposal-from", type=Path)
    p.add_argument("--allow-prefix", action="store_true")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve each actual full Laurent postcomposition certificate")
    if not 1 <= args.post_modes <= 96 or not 1 <= args.exp_degree <= 64:
        raise ValueError("the requested finite dimensions are outside this declared implementation")
    start = time.monotonic()
    ctx.prec = 320
    native, root = read(args.wiener_lift), read(args.root_contract)
    if (sha(args.root_contract) != ROOT or sha(producer.__file__) != PRODUCER
            or native["kind"] != "actual_saved_phase_transport_Wiener_widening"
            or not native["complete"] or native["root_contract_sha256"] != ROOT
            or native["original_producer_sha256"] != PRODUCER
            or native["source_sha256"] != sha(wiener_consumer.__file__)
            or native["genuine_input_Wiener_strip"] != str(INPUT)
            or native["widened_residual_strip"] != str(RESIDUAL)):
        raise ValueError("the exact source, root contract and genuine Wiener lift are required")
    whole = native["whole_negative_domain"]
    if not whole and not args.allow_prefix:
        raise ValueError("an actual postcomposition return requires the whole169-germ endpoint")
    state = decode_state(native["exact_terminal_phase_state"], 64)
    omega = Fraction(root["exact_proposed_rotation"])
    if args.proposal_from:
        proposal = read(args.proposal_from)
        a = list(map(Fraction, proposal["exact_postcomposition_sine_coefficients"]))
        b = list(map(Fraction, proposal["exact_postcomposition_cosine_coefficients"]))
        proposed = Fraction(proposal["exact_proposed_terminal_rotation"])
        if len(a) != args.post_modes or len(b) != args.post_modes:
            raise ValueError("the reused exact postcomposition has a different number of modes")
        proposal_info = dict(method="reuse exact finite proposal", source_sha256=sha(args.proposal_from))
    else:
        a, b, proposed, proposal_info = propose(state, args.post_modes, args.proposal_grid, omega)
    poly, degree, nonmean, tail, central, tail_rows, shells, digest = terminal(
        state, a, b, args.exp_degree, exact_arb(RESIDUAL))
    reference_width = exact_arb(RESIDUAL)+(upper(native["complete_reference_phase_derivative_Wiener_norm"])-1)/4
    root_width = exact_arb(OUTER)+upper(native["exact_H_periodic_part_outer_norm"])
    MK = (1+trig_norm(a, b, reference_width, 1)).upper()
    MKroot = (1+trig_norm(a, b, root_width, 1)).upper()
    source_fee = (MK*upper(native["widened_complete_true_transport_residual"])).upper()
    root_fee = (MKroot*upper(native["genuine_Wiener_root_sliver_fee"])).upper()
    targets = dict(old_fit=exact_arb(omega), exact_new_proposal=exact_arb(proposed),
        bounded7_new=arb.pi()*(arb(45217079201)-arb(5).sqrt())/(2*164472125458))
    terminal_errors = {name: (nonmean+abs(central-acb(target))+tail).upper()
                       for name, target in targets.items()}
    errors = {name: (bound+source_fee+root_fee).upper()
              for name, bound in terminal_errors.items()} if whole else None
    constant_free = (nonmean+tail+source_fee+root_fee).upper() if whole else None
    derivative = (constant_free/(arb(1).exp()*exact_arb(INPUT))).upper() if whole else None
    ha = list(map(Fraction, root["exact_H_sine_coefficients"]))
    hb = list(map(Fraction, root["exact_H_cosine_coefficients"]))
    Hh = trig_norm(ha, hb, exact_arb(INPUT))
    Hd = trig_norm(ha, hb, exact_arb(INPUT), 1)
    newh = (Hh+trig_norm(a, b, exact_arb(INPUT)+Hh)).upper()
    newd = (Hd+(1+Hd)*trig_norm(a, b, exact_arb(INPUT)+Hh, 1)).upper()
    inverse_margin = (exact_arb(INPUT-Fraction(1, 64))-newh).lower()
    inverse_ok = bool(newd < 1 and inverse_margin > 0)
    K_real_derivative = trig_norm(a, b, arb(0), 1)
    gates = [dict(name=name, passed=bool(value)) for name, value in (
        ("the input is a complete genuine Wiener consumer of its declared scope", native["complete"]),
        ("all full Laurent coefficients and every exponential tail are included", len(tail_rows) == 2*len(a)),
        ("the exact real postcomposition lift is orientation preserving", K_real_derivative < 1),
        ("the corrected exact lift has a Wiener inverse on physical strip1/64", inverse_ok),
        ("complete residual and root multipliers are charged", MK >= 1 and MKroot >= 1),
        ("the true-return scope agrees with the actual169-germ endpoint", whole or args.allow_prefix),
    )]
    result = dict(kind="actual_full_Laurent_terminal_postcomposition_certificate",
        complete=all(z["passed"] for z in gates), whole_negative_domain=whole,
        original_producer_sha256=PRODUCER, root_contract_sha256=ROOT,
        source_sha256=sha(__file__), wiener_lift_sha256=sha(args.wiener_lift),
        exact_postcomposition_sine_coefficients=list(map(str, a)),
        exact_postcomposition_cosine_coefficients=list(map(str, b)),
        exact_proposed_terminal_rotation=str(proposed), proposal=proposal_info,
        exponential_degree=args.exp_degree, complete_Laurent_degree=degree,
        complete_Laurent_coefficient_count=2*degree+1,
        complete_Laurent_coefficients_100digit_sha256=digest,
        complete_Laurent_nonmean_norm=record(nonmean),
        complete_Laurent_central_real_coefficient=record(central.real),
        complete_infinite_exponential_tail=record(tail),
        complete_nonmean_frequency_shells=shells, complete_exponential_tails=tail_rows,
        residual_multiplier_argument_strip=record(reference_width),
        root_multiplier_argument_strip=record(root_width),
        full_residual_multiplier=record(MK), full_root_multiplier=record(MKroot),
        multiplied_complete_true_transport_residual=record(source_fee),
        multiplied_genuine_Wiener_root_sliver=record(root_fee),
        complete_terminal_Wiener_defects_by_target={k: record(v) for k, v in terminal_errors.items()},
        genuine_Wiener_conjugacy_defects_by_target=None if errors is None else {k: record(v) for k, v in errors.items()},
        constant_free_genuine_Wiener_defect=None if constant_free is None else record(constant_free),
        genuine_angular_derivative_A0_bound=None if derivative is None else record(derivative),
        corrected_lift_periodic_norm_on_input_strip=record(newh),
        corrected_lift_derivative_minus_one_norm_on_input_strip=record(newd),
        corrected_lift_inverse_Wiener_margin=record(inverse_margin),
        corrected_lift_inverse_derivative_bound=record((1/(1-newd)).upper()) if inverse_ok else None,
        postcomposition_real_derivative_minus_one_norm=record(K_real_derivative),
        physical_true_defect_strip=str(INPUT), physical_conjugated_map_strip="1/64",
        normalized_circle_map_strip="1/16",
        normalized_circle_map_defects_by_target=None if errors is None or not inverse_ok else {
            k: record((4*v).upper()) for k, v in errors.items()},
        full_frequency_conjugacy_not_claimed=True, true_fitted_rotation_not_claimed=True,
        parameter_KAM_and_true_PDE_response_error_not_claimed=True,
        scalar_cache_and_transport_reference_not_recomputed=True,
        all_complete_unprojected_frequencies_and_even_mean_retained=True,
        gates=gates, seconds=time.monotonic()-start)
    save(args.out, result)
    print(dict(complete=result["complete"], whole=whole, Laurent_degree=degree,
        nonmean=nonmean.str(18), exponential_tail=tail.str(10),
        mean=central.real.str(18),
        error=None if errors is None else {k: v.str(18) for k, v in errors.items()},
        inverse_margin=inverse_margin.str(12), seconds=result["seconds"]), flush=True)
    if not result["complete"]:
        raise ArithmeticError("an actual terminal postcomposition certification gate failed; native saved")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Certify a bounded15 quadratic target near the actual certified K48 terminal.

The true rotation is enclosed by the complete return error, but the target is
not claimed to be realized. Principal fourth-root gaps and circle K costs are
paid anew; the bounded7 target and all its results remain intact.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_codazzi_phase_complete_transport_cover import read, ROOT, PRODUCER
from fourfold_codazzi_phase_nearby_bounded7_rotation import periodic_one
import fourfold_codazzi_phase_terminal_postcomposition as post_source
from fourfold_codazzi_phase_Wiener_transport_lift import upper
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

PREFIX = [0, 3, 1, 1, 1, 3, 7, 1, 3, 1, 1, 1, 2, 2, 1, 15, 5, 4, 8]
QUADRATIC = (5831714953207175, 1, 21212218271020390)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--postcomposition", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every exact arithmetic target and paid error")
    started = time.monotonic()
    ctx.prec = 320
    d = read(args.postcomposition)
    if (not d["complete"] or not d["whole_negative_domain"]
            or d["source_sha256"] != sha(post_source.__file__)
            or d["root_contract_sha256"] != ROOT or d["original_producer_sha256"] != PRODUCER
            or len(d["exact_postcomposition_sine_coefficients"]) != 48):
        raise ValueError("the actual full-frequency K48 terminal certificate is required")
    proposal = exact_arb(Fraction(d["exact_proposed_terminal_rotation"]))
    number = 2*proposal/arb.pi()
    x = number
    quotients = []
    for expected in PREFIX:
        unique = x.floor().unique_fmpz()
        if unique is None or int(unique) != expected:
            raise ArithmeticError("the actual proposed rotation CF prefix was not certified")
        quotients.append(dict(complete_quotient=record(x), partial_quotient=expected))
        x = 1/(x-expected)
    quadratic, convergents = periodic_one(PREFIX)
    if quadratic != QUADRATIC:
        raise ValueError("the exact bounded15 quadratic identity differs")
    n, s, denominator = quadratic
    rho = (arb(n)+s*arb(5).sqrt())/denominator
    omega = arb.pi()*rho/2
    target_difference = omega-proposal
    # The entire open CF cylinder a_15=15 excludes every irrational
    # whose positive partial quotients are at most14.
    edge_high = arb.pi()/2*exact_arb(Fraction(173969, 632793))
    edge_low = arb.pi()/2*exact_arb(Fraction(185047, 673088))
    cylinder_distance = min(proposal-edge_low, edge_high-proposal).lower()
    source = upper(d["multiplied_complete_true_transport_residual"])
    sliver = upper(d["multiplied_genuine_Wiener_root_sliver"])
    nonmean = upper(d["complete_Laurent_nonmean_norm"])
    tail = upper(d["complete_infinite_exponential_tail"])
    central = box_from_record(d["complete_Laurent_central_real_coefficient"])
    genuine = (nonmean+abs(central-omega)+tail+source+sliver).upper()
    proposal_error = upper(d["genuine_Wiener_conjugacy_defects_by_target"]["exact_new_proposal"])
    old_error = upper(d["genuine_Wiener_conjugacy_defects_by_target"]["bounded7_new"])
    ratio = exact_arb(Fraction(17, 9))
    improvement = (old_error/genuine/ratio**2).lower()
    true_rotation = arb(proposal.mid(), proposal.rad()+proposal_error)
    tests = [
        ("the actual whole169 K48 identity and every paid full residual are retained", d["complete"]),
        ("the complete proposed CF prefix is certified through entry18", len(quotients) == len(PREFIX)),
        ("the exact target has all positive partial quotients at most15", max(PREFIX[1:]) == 15 and min(PREFIX[1:]) > 0),
        ("the primitive quadratic identity is strictly irrational", s != 0 and denominator > 0),
        ("the new target differs from the exact proposal by less than2.2e-18", abs(target_difference) < exact_arb(Fraction(22, 10**19))),
        ("every bounded14 target is farther than7.39e-13 from the proposal", cylinder_distance > exact_arb(Fraction(739, 10**15))),
        ("the genuine full Wiener error for the bounded15 target is below1.464e-13", genuine < exact_arb(Fraction(1464, 10**16))),
        ("the same-data worst-case R31 smallness improvement exceeds106", improvement > 106),
    ]
    out = dict(kind="actual_K48_bounded15_quadratic_target_and_true_Wiener_error",
        complete=all(bool(v) for _, v in tests), source_sha256=sha(__file__),
        postcomposition_native_sha256=sha(args.postcomposition),
        original_producer_sha256=PRODUCER, root_contract_sha256=ROOT,
        exact_terminal_proposed_angular_rotation=d["exact_proposed_terminal_rotation"],
        proposed_rotation_CF_prefix=PREFIX, certified_complete_quotients=quotients,
        exact_new_rotation_number=dict(rational_numerator=n, sqrt5_coefficient=s, denominator=denominator),
        new_CF_prefix=PREFIX, new_CF_period=[1], convergents=convergents,
        new_rotation_number=record(rho), new_angular_rotation=record(omega),
        new_target_minus_exact_proposal=record(target_difference),
        CF_cylinder_angular_endpoints=[record(edge_low), record(edge_high)],
        minimum_distance_to_any_bounded14_irrational_target=record(cylinder_distance),
        genuine_full_Wiener_defect=record(genuine), physical_Wiener_strip=d["physical_true_defect_strip"],
        normalized_circle_error=record((4*genuine).upper()), normalized_circle_strip=d["normalized_circle_map_strip"],
        genuine_angular_derivative_A0_bound=d["genuine_angular_derivative_A0_bound"],
        true_return_translation_angle_enclosure=record(true_rotation),
        translation_enclosure_from_exact_real_iterate_inequality=True,
        maximum_partial_quotient=15, all_denominator_Diophantine_constant="1/17",
        all_fourth_root_phase_gap_constant="1/68", circle_homological_K="17/4",
        previous_bounded7_circle_K="9/4", previous_bounded7_quarter_gap="1/36",
        relative_homological_K_cost="17/9", worst_case_R31_smallness_cost="289/81",
        same_other_data_R31_smallness_improvement_lower=record(improvement),
        R31_other_input_bounds_not_yet_claimed=True,
        beta_over_j_and_strong_remainder_must_be_repaid_for_gap_1_over68=True,
        prior_bounded7_target_not_overwritten=True, new_target_not_claimed_true_rotation=True,
        actual_PDE_solution_branch_not_assumed=True,
        gates=[dict(name=name, passed=bool(value)) for name, value in tests],
        seconds=time.monotonic()-started)
    save(args.out, out)
    print(dict(complete=out["complete"], target=quadratic,
        target_difference=target_difference.str(24), genuine_error=genuine.str(20),
        bounded14_distance=cylinder_distance.str(16),
        R31_relative_improvement=improvement.str(12), seconds=out["seconds"]), flush=True)
    if not out["complete"]:
        raise ArithmeticError("an actual bounded15 arithmetic or complete error gate failed")


if __name__ == "__main__":
    main()

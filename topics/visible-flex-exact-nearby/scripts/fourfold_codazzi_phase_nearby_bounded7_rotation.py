#!/usr/bin/env python3
"""Choose an exact bounded-seven rotation near the unchanged phase fit.

Only the arithmetic target changes. This script does not claim that the
actual return has that rotation, that the nu Schur scalar is nonzero, or
that the regular/nonlinear boundary problem is solved.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import gcd
from pathlib import Path
import time

from flint import arb, ctx

ROOT_SHA = "1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43"
REPAIR = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
FIT = Fraction(3889733506671123, 9007199254740992)
PREFIX = [0, 3, 1, 1, 1, 3, 7, 1, 3, 1, 1, 1, 2, 2, 1, 7]
FITTED_PREFIX = [0, 3, 1, 1, 1, 3, 7, 1, 3, 1, 1, 1, 2, 2, 1, 19]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact(x):
    x = Fraction(x)
    return arb(x.numerator) / x.denominator


def ball(x):
    return dict(ball=x.str(75), lower=x.lower().str(75), upper=x.upper().str(75))


def periodic_one(prefix):
    """Exact (n+s sqrt(5))/d for [prefix; overline(1)]."""
    previous_p, p, previous_q, q = 0, 1, 1, 0
    convergents = []
    for index, a in enumerate(prefix):
        previous_p, p = p, a * p + previous_p
        previous_q, q = q, a * q + previous_q
        convergents.append(dict(index=index, a=a, p=p, q=q))
    A, B, C, D = p + 2 * previous_p, p, q + 2 * previous_q, q
    n, s, d = A * C - 5 * B * D, B * C - A * D, C * C - 5 * D * D
    if d < 0:
        n, s, d = -n, -s, -d
    common = gcd(gcd(n, s), d)
    return (n // common, s // common, d // common), convergents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-contract", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve the earlier arithmetic native")
    started = time.monotonic()
    ctx.prec = 256
    raw = args.root_contract.read_bytes()
    root = json.loads(gzip.decompress(raw) if args.root_contract.suffix == ".gz" else raw)
    if sha(args.root_contract) != ROOT_SHA:
        raise ValueError("the exact previously proved phase contract changed")
    if not root["complete"] or root["derived_definition_sha256"] != REPAIR:
        raise ValueError("the complete original repaired-centre contract is required")
    if Fraction(root["exact_proposed_rotation"]) != FIT:
        raise ValueError("the actual finite fitted rotation differs")

    fitted_rho = 2 * exact(FIT) / arb.pi()
    x = fitted_rho
    found = []
    continued_fraction_intervals = []
    for index in range(len(FITTED_PREFIX)):
        unique = x.floor().unique_fmpz()
        if unique is None:
            raise ArithmeticError("the fitted continued-fraction coefficient is not certified")
        a = int(unique)
        found.append(a)
        continued_fraction_intervals.append(dict(index=index, complete_quotient=ball(x), a=a))
        x = 1 / (x - a)
    if found != FITTED_PREFIX:
        raise ValueError("the certified fitted prefix changed")

    coefficients, convergents = periodic_one(PREFIX)
    n, s, d = coefficients
    rho = (arb(n) + s * arb(5).sqrt()) / d
    omega = arb.pi() * rho / 2
    difference = omega - exact(FIT)
    old_rho = (arb(612575) - arb(5).sqrt()) / 2228182
    old_difference = exact(FIT) - arb.pi() * old_rho / 2
    lower = Fraction(68387956541454, 10**24)
    upper = Fraction(68387956541455, 10**24)
    old_lower = Fraction(31609581821389, 10**19)
    old_upper = Fraction(31609581821390, 10**19)
    gates = [dict(name=name, passed=bool(passed)) for name, passed in (
        ("the complete root contract and exact fitted lift are unchanged", sha(args.root_contract) == ROOT_SHA),
        ("the actual fitted continued-fraction prefix is interval-certified", found == FITTED_PREFIX),
        ("the new prefix agrees through its first fourteen positive entries", PREFIX[:-1] == FITTED_PREFIX[:-1]),
        ("the exact quadratic identity is the stated primitive expression", coefficients == (45217079201, -1, 164472125458)),
        ("all new positive partial quotients and the periodic tail are at most seven", max(PREFIX[1:]) == 7 and min(PREFIX[1:]) > 0),
        ("the quadratic target is strictly irrational", s != 0 and d > 0),
        ("the new signed angular target shift satisfies the strict rational lower bound", difference > exact(lower)),
        ("the new signed angular target shift satisfies the strict rational upper bound", difference < exact(upper)),
        ("the full target shift is below seven times ten to the minus eleven", difference < exact(Fraction(7, 10**11))),
        ("the old target discrepancy has a strict rational lower bound", old_difference > exact(old_lower)),
        ("the old target discrepancy has a strict rational upper bound", old_difference < exact(old_upper)),
    )]
    report = dict(
        kind="actual_bounded7_quadratic_rotation_near_unchanged_phase_fit",
        complete=all(g["passed"] for g in gates), source_sha256=sha(__file__), bits=ctx.prec,
        root_contract_path=str(args.root_contract), root_contract_sha256=ROOT_SHA,
        derived_definition_sha256=REPAIR, exact_fitted_angular_rotation=str(FIT),
        fitted_rotation_number=ball(fitted_rho), fitted_certified_CF_prefix=found,
        fitted_CF_complete_quotients=continued_fraction_intervals,
        new_CF_prefix=PREFIX, new_CF_period=[1], convergents=convergents,
        exact_new_rotation_number=dict(rational_numerator=n, sqrt5_coefficient=s, denominator=d),
        new_rotation_number=ball(rho), new_angular_rotation=ball(omega),
        new_minus_fitted_angular_rotation=ball(difference),
        new_shift_strict_rational_interval=[str(lower), str(upper)],
        old_rotation_number=dict(rational_numerator=612575, sqrt5_coefficient=-1, denominator=2228182),
        fitted_minus_old_angular_rotation=ball(old_difference),
        old_shift_strict_rational_interval=[str(old_lower), str(old_upper)],
        maximum_partial_quotient=7,
        all_denominator_Diophantine_constant="1/9",
        all_fourth_root_phase_gap_constant="1/36",
        infinite_phase_gap_proved_by_continued_fraction_lemma_not_frequency_scan=True,
        true_return_rotation_not_claimed=True, nu_Schur_or_parameter_correction_not_claimed=True,
        beta_over_j_and_strong_return_remainders_still_required=True,
        scalar_or_transport_native_recomputation_required_for_target_change=False,
        gates=gates, seconds=time.monotonic() - started,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.out.with_suffix(args.out.suffix + ".tmp")
    temporary.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    temporary.replace(args.out)
    print(json.dumps(dict(complete=report["complete"], quadratic_target=coefficients,
        target_shift=difference.str(35), gap_constant="1/36", seconds=report["seconds"])), flush=True)
    if not report["complete"]:
        raise ArithmeticError("a certified arithmetic gate failed")


if __name__ == "__main__":
    main()

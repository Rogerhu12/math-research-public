#!/usr/bin/env python3
"""Consume R936 on a new prime window and check the R939 identities.

Run mathematical calculations ONLY in this repository's public GitHub Actions.
The default window is 109 <= p <= 1000, restricted to the original allowed
classes p == 5 mod 6 and p == 2 or 5 mod 9.  The six primes already evaluated
by R936 are always excluded.  Raw polynomial arrays stay in process memory;
only a compact reproducible summary is written, and that output is not to be
committed.  The original phase, full t*H algebra, weight 1 at t=0, weight 3 at
the H roots, and zero elliptic contributions are retained.

Import API:
    calculate_checked_prime(p) -> compact row
    calculate_window(minimum=109, maximum=1000, stop_on_zero=True,
                     on_row=None) -> deterministic summary
    write_summary(summary, output_path) -> SHA-256 receipt

No finite window proves uniform nonvanishing or Serre uniformity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import time

# Support both direct CLI use and importlib loading from a combined consumer.
SCRIPT_DIRECTORY = pathlib.Path(__file__).resolve().parent
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

import R936_whole_supersingular_trace as source


OLD_PRIMES = frozenset((41, 47, 59, 71, 83, 107))
EXPECTED_R936_SHA256 = "6dc82247decc1f16dc17a2a2bee81756f6447dc62a0f83cf98b819ed8285d5a9"


def compact_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def source_receipt():
    source_path = pathlib.Path(source.__file__).resolve()
    digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
    if digest != EXPECTED_R936_SHA256:
        raise RuntimeError("R936 source changed: review its contract before this new calculation")
    return {
        "R936_script": source_path.name,
        "R936_script_sha256": digest,
        "R939_script": pathlib.Path(__file__).name,
        "R939_script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    }


def require_equal(actual, expected, label, p):
    if actual != expected:
        raise ArithmeticError(f"p={p}: {label} failed")


def calculate_checked_prime(p):
    """One NEW allowed prime, using the unchanged original R936 source."""
    if p in OLD_PRIMES:
        raise ValueError(f"p={p} was already evaluated in R936; no recomputation")
    if p < 109 or p % 6 != 5 or p % 9 not in (2, 5) or not source.is_prime(p):
        raise ValueError("require a new prime p >= 109 in the original allowed classes")

    original = source.calculate_prime(p)
    ar = source.Arithmetic(p)
    h = original["H_N"]
    c = original["C_remainder"]
    modulus = original["monic_tH_N"]
    n = original["N"]
    r = original["r"]
    d = [ar.one, ar.scalar(-4)]
    x = [ar.one, ar.scalar(-8)]
    td = [ar.zero] + d
    hp = ar.derivative(h)
    hpp = ar.derivative(hp)

    # This is a polynomial identity, not just equality at H roots.
    hasse_ode = ar.psub(
        ar.padd(
            ar.pscale(ar.pmul(td, hpp), ar.scalar(9)),
            ar.pscale(ar.pmul(x, hp), ar.scalar(12)),
        ),
        ar.pscale(h, ar.scalar(25)),
    )
    require_equal(hasse_ode, [], "fixed Hasse ODE", p)

    beta_full = ar.pneg(
        ar.padd(ar.pmul(x, h), ar.pscale(ar.pmul(td, hp), ar.scalar(3)))
    )
    require_equal(
        ar.derivative(beta_full),
        ar.pscale(h, ar.scalar(-pow(3, -1, p))),
        "beta' = -H/3 as a polynomial", p,
    )
    beta = ar.pmod(beta_full, modulus)
    require_equal(beta, original["b_remainder"], "beta = b on the complete t*H algebra", p)
    require_equal(ar.ppowmod(beta, p, modulus), beta, "beta^p = beta on the complete algebra", p)
    require_equal(ar.ppowmod(beta, p - 1, modulus), [ar.one], "beta^(p-1) = 1", p)

    companion_check = "not_applicable_r8"
    if r == 2:
        cp = ar.derivative(c)
        cpp = ar.derivative(cp)
        lhs = ar.psub(
            ar.padd(
                ar.pscale(ar.pmul(td, cpp), ar.scalar(3)),
                ar.pmul([ar.scalar(2), ar.scalar(-24)], cp),
            ),
            ar.pscale(c, ar.scalar(3)),
        )
        # The corrected original scalar F has (-1)^J, and J is odd.
        rhs = ar.pscale(h, ar.mul(ar.scalar(-pow(9, -1, p)), ar.s))
        require_equal(lhs, rhs, "original r=2 companion ODE with negative RHS", p)
        companion_check = "proved_identity_verified_negative_rhs"

    denominator_free = ar.pmulmod(
        ar.ppowmod(d, 2 * n + 2, modulus),
        ar.ppowmod(c, p + 1, modulus),
        modulus,
    )
    denominator_free = ar.pmulmod(
        denominator_free, ar.ppowmod(beta, r - 2, modulus), modulus
    )
    require_equal(
        denominator_free, original["R_remainder"],
        "denominator-free R939 value equals original R936 value", p,
    )
    weight = ar.psub([ar.scalar(3)], ar.pscale(original["e0_remainder"], ar.scalar(2)))
    weighted = ar.pmulmod(weight, denominator_free, modulus)
    require_equal(weighted, original["weighted_R_remainder"], "full weight 1/3 retained", p)
    # R936 has independently checked Euler coefficient against all diagonal
    # entries.  Here apply that exact Euler trace to the new denominator-free
    # expression, without materializing a second multiplication matrix.
    trace_euler = ar.pmod(ar.pmul(weighted, ar.derivative(modulus)), modulus)
    new_trace = ar.coeff(trace_euler, len(modulus) - 2)
    require_equal(new_trace, original["trace_weighted_R"], "new trace equals original full trace", p)
    require_equal(original["elliptic_D_zero_contribution"], [0, 0], "elliptic zero contribution", p)
    require_equal(original["fine_tame_cover_degree"], 12, "fine tame cover degree", p)

    # A digest permits exact reconstruction without storing the raw arrays.
    raw_digest = hashlib.sha256(compact_json(original)).hexdigest()
    return {
        "prime": p,
        "prime_mod_9": p % 9,
        "prime_mod_12": p % 12,
        "r": r,
        "N": n,
        "J": original["J"],
        "trace_algebra_dimension": n + 1,
        "trace_weighted_R": list(new_trace),
        "fine_sum_S_to_p": list(original["fine_sum_S_to_p"]),
        "fine_sum_S": list(original["fine_sum_S"]),
        "fine_sum_is_nonzero": original["fine_sum_is_nonzero"],
        "u_zero_contribution_before_fine_degree": list(original["u_zero_contribution_before_fine_degree"]),
        "H_roots_trace_before_factor_three": list(original["H_N_roots_trace_before_factor_three"]),
        "elliptic_D_zero_contribution": [0, 0],
        "full_hasse_ode_verified": True,
        "full_beta_derivative_verified": True,
        "beta_equals_b_on_complete_algebra": True,
        "beta_frobenius_verified": True,
        "beta_unit_power_verified": True,
        "original_r2_companion_ode": companion_check,
        "denominator_free_equals_original_R": True,
        "denominator_free_equals_original_whole_trace": True,
        "original_R936_raw_row_sha256": raw_digest,
    }


def calculate_window(minimum=109, maximum=1000, stop_on_zero=True, on_row=None):
    """Return a compact deterministic result; on_row(row) may stream progress."""
    if minimum < 109 or maximum < minimum:
        raise ValueError("require 109 <= minimum <= maximum")
    receipt = source_receipt()
    requested = [
        p for p in range(minimum, maximum + 1)
        if p not in OLD_PRIMES and p % 6 == 5 and p % 9 in (2, 5) and source.is_prime(p)
    ]
    rows = []
    stopped_at_zero = None
    for p in requested:
        row = calculate_checked_prime(p)
        rows.append(row)
        if on_row is not None:
            on_row(row)
        if not row["fine_sum_is_nonzero"] and stop_on_zero:
            stopped_at_zero = p
            break
    return {
        "contract": "R936 corrected original source; R939 fixed ODEs and denominator elimination",
        "status": "exact_finite_computation_only",
        "source_receipt": receipt,
        "inclusive_minimum": minimum,
        "inclusive_maximum": maximum,
        "allowed_prime_conditions": "prime p >= 109; p % 6 == 5; p % 9 in (2,5)",
        "excluded_already_computed_primes": sorted(OLD_PRIMES),
        "requested_new_primes": requested,
        "completed_new_primes": [row["prime"] for row in rows],
        "stop_on_zero": stop_on_zero,
        "stopped_at_zero_prime": stopped_at_zero,
        "complete_requested_window": len(rows) == len(requested),
        "zero_primes_found": [row["prime"] for row in rows if not row["fine_sum_is_nonzero"]],
        "rows": rows,
        "raw_polynomial_arrays_saved": False,
        "local_mathematical_execution_authorized": False,
        "execution_location_required": "Rogerhu12/math-research-public GitHub Actions",
        "all_prime_nonvanishing_proved": False,
        "Q_prime_source_comparison_proved": False,
        "serre_uniformity_proved": False,
    }


def write_summary(summary, output_path):
    output = pathlib.Path(output_path)
    payload = (json.dumps(summary, sort_keys=True, indent=2) + "\n").encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(payload)
    return {"output_bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minimum", type=int, default=109)
    parser.add_argument("--maximum", type=int, default=1000)
    parser.add_argument("--continue-after-zero", action="store_true")
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()

    def report(row):
        # Timing is progress-only, excluded from the deterministic summary hash.
        print(json.dumps({"checked_row": row, "elapsed_seconds": time.perf_counter() - started}, separators=(",", ":")), flush=True)

    summary = calculate_window(
        minimum=args.minimum, maximum=args.maximum,
        stop_on_zero=not args.continue_after_zero, on_row=report,
    )
    receipt = write_summary(summary, args.output)
    print(json.dumps({
        "completed_prime_count": len(summary["rows"]),
        "zero_primes_found": summary["zero_primes_found"],
        "complete_requested_window": summary["complete_requested_window"],
        **receipt,
    }, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()

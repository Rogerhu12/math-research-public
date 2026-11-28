#!/usr/bin/env python3
"""Public-Actions-only ball enclosure for the R630 full-reference beta_0.

The omitted tails are bounded analytically in the accompanying note.
Only a successful exact rational comparison at the end certifies the
whole-reference statement; this does not certify a flat-ended connector.

Primary API references:
https://python-flint.readthedocs.io/en/latest/acb.html
https://python-flint.readthedocs.io/en/latest/arb.html
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from datetime import datetime, timezone


def main() -> None:
    if not (
        os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY", "").lower()
        == "rogerhu12/math-research-public"
        and os.environ.get("GITHUB_RUN_ID")
    ):
        raise SystemExit(
            "Scientific calculation requires the public "
            "Rogerhu12/math-research-public GitHub Actions runner."
        )
    parser = argparse.ArgumentParser()
    parser.add_argument("--prec", type=int, default=128)
    parser.add_argument("--max-seconds", type=float, default=300)
    parser.add_argument("--eval-limit", type=int, default=50000)
    args = parser.parse_args()
    started = time.perf_counter()
    import flint
    from flint import acb, arb, ctx, fmpq

    ctx.prec = args.prec
    counts = {
        "quadrature_callback_calls": 0,
        "analytic_rejections": 0,
        "hyperu_calls": 0,
        "port_formula_evaluations": 0,
    }
    source_head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()
    print(
        json.dumps(
            {
                "kind": "provenance",
                "utc": datetime.now(timezone.utc).isoformat(),
                "git_head": source_head,
                "run_id": os.environ["GITHUB_RUN_ID"],
                "python_flint_version": flint.__version__,
                "prec_bits": args.prec,
                "normalization": "r(0)=w(r(0))=f2(0)=f3(0)=1",
                "scope": "R630 full-line left-regular reference",
            },
            sort_keys=True,
        ),
        flush=True,
    )

    s = arb(5).sqrt()
    eta = ((36 * s - 27) / 20).sqrt()
    big_b = (33 - 14 * s) / 20
    beta = (eta**2 + big_b).sqrt()
    a = beta - s / 2 + arb(1) / 2
    b = 1 + 2 * beta
    alpha2 = s - arb(1) / 2
    kappa3 = (3 * s - 3) / 2
    exponent = alpha2 + kappa3 - eta - 1

    z1 = 2 * s
    counts["hyperu_calls"] += 1
    u_at_one = z1.hypgeom_u(a, b)
    counts["hyperu_calls"] += 1
    up_at_one = z1.hypgeom_u(a + 1, b + 1)
    psi_at_one = (-s).exp() * z1**beta * u_at_one
    nu_at_one = eta + s - beta + a * z1 * up_at_one / u_at_one
    f2_at_one = (-2 * s).exp()
    f3_at_one = (-3 * s).exp() * (-3 * s - 2)
    c_ref = nu_at_one * psi_at_one**3 / (2 * f2_at_one * f3_at_one)
    if not c_ref.is_finite():
        raise RuntimeError("Non-finite normalization constant")
    c_bound = c_ref.abs_upper().fmpq()
    if not c_bound < 10000:
        raise RuntimeError("The analytic-tail normalization bound was not certified")

    print(
        json.dumps(
            {
                "kind": "normalization_ball",
                "C_ref": c_ref.str(30),
                "absolute_upper_dyadic": str(c_bound),
                "bound_below_10000_certified": True,
                "psi1_at_t1": psi_at_one.str(30),
                "nu_at_t1": nu_at_one.str(30),
                "actual_call_counts": dict(counts),
            },
            sort_keys=True,
        ),
        flush=True,
    )

    def integrand(t, analytic):
        counts["quadrature_callback_calls"] += 1
        if time.perf_counter() - started > args.max_seconds:
            raise RuntimeError("The explicit calculation time budget was reached")
        if not t.is_finite() or not t.real.lower().fmpq() > 0:
            counts["analytic_rejections"] += 1
            return acb(arb.nan(), arb.nan())
        # Re(t)>0 guarantees that both power and U branches are analytic.
        # Possible zeros of denominators are handled by ball division;
        # a ball containing such a zero returns a non-finite enclosure.
        counts["port_formula_evaluations"] += 1
        z = 2 * s * t
        counts["hyperu_calls"] += 1
        u0 = z.hypgeom_u(a, b)
        counts["hyperu_calls"] += 1
        u1 = z.hypgeom_u(a + 1, b + 1)
        psi = (-z / 2).exp() * z.pow(beta, analytic=analytic) * u0
        nu = eta + z / 2 - beta + a * z * u1 / u0
        k2 = eta - alpha2 + 2 * s * t
        poly = 3 * s - 2 - 6 * s * t
        q = (eta - kappa3 + 3 * s * t) * poly + 6 * s * t
        h = k2 * q / nu**2 - 9 * k2 * poly / nu - 4 * q / nu + 12 * poly
        return (
            -c_ref
            * t.pow(exponent, analytic=analytic)
            * (-5 * s * t).exp()
            * h
            / psi**3
        )

    knots = [
        fmpq(1, 1024),
        fmpq(1, 64),
        fmpq(1, 8),
        fmpq(1, 4),
        fmpq(1, 2),
        fmpq(1),
        fmpq(2),
        fmpq(4),
        fmpq(8),
        fmpq(12),
    ]
    total = acb(0)
    for lo, hi in zip(knots, knots[1:]):
        before = dict(counts)
        segment_started = time.perf_counter()
        value = acb.integral(
            integrand,
            acb(lo),
            acb(hi),
            abs_tol=1e-10,
            rel_tol=1e-10,
            eval_limit=args.eval_limit,
            depth_limit=100,
        )
        total += value
        print(
            json.dumps(
                {
                    "kind": "segment_ball",
                    "left": str(lo),
                    "right": str(hi),
                    "integral": str(value),
                    "finite_enclosure": bool(value.is_finite()),
                    "segment_seconds": time.perf_counter() - segment_started,
                    "actual_segment_calls": {
                        key: counts[key] - before[key] for key in counts
                    },
                    "elapsed_seconds": time.perf_counter() - started,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        if not value.is_finite():
            raise RuntimeError("No finite ball obtained for this segment")
    if not total.imag.contains(0):
        raise RuntimeError("Real-path integral enclosure failed to contain zero imaginary part")

    # These rational tail bounds have a separate written analytic proof.
    tail_bound = fmpq(1, 10000) + fmpq(1, 100000000)
    lower = total.real.lower().fmpq() - tail_bound
    upper = total.real.upper().fmpq() + tail_bound
    certified = bool(lower > fmpq(1, 3) and upper < fmpq(3, 8))
    print(
        json.dumps(
            {
                "kind": "whole_reference_certificate",
                "compact_integral_ball": str(total),
                "absolute_omitted_tail_bound": str(tail_bound),
                "whole_beta0_lower_exact_rational": str(lower),
                "whole_beta0_upper_exact_rational": str(upper),
                "certified_1_over_3_lt_beta0_lt_3_over_8": certified,
                "actual_call_counts": counts,
                "elapsed_seconds": time.perf_counter() - started,
                "scope": (
                    "Whole R630 reference only; no true-flat-tail port "
                    "or finite nonlinear embedding is certified here."
                ),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    if not certified:
        raise SystemExit("The requested strict rational sign certificate was not obtained")


if __name__ == "__main__":
    main()

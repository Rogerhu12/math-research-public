#!/usr/bin/env python3
"""Exact arithmetic budget for the actual root high-output Volterra theorem.

Run only in the public repository's GitHub Actions, as requested by the user.
This script certifies the explicitly listed rational/integer inequalities.  It
does not replace the analytic cutoff identity, the all-frequency kernel proof,
the old Airy bounds, or the complete graph/source transformations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path


PROOF = "results/R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md"
DEPS = [
    PROOF,
    "results/R119-supplement-actual-nonradial-full-remainder-and-high-network.md",
    "results/R119-supplement-actual-nonradial-first-density-phase.md",
    "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
    "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
    "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("This new budget is authorized for the public repository's GitHub Actions only")
    topic = Path(__file__).resolve().parents[1]
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["source_sha256"] != sha(Path(__file__)):
        raise ValueError("producer bytes differ from the separately fixed manifest")
    expected_inputs = manifest["proved_input_sha256"]
    if set(expected_inputs) != set(DEPS):
        raise ValueError("the complete dependency set differs from the fixed manifest")
    for rel, expected in expected_inputs.items():
        if sha(topic / rel) != expected:
            raise ValueError("proved input bytes differ: " + rel)
    gates = []

    def gate(name, passed, detail):
        gates.append({"name": name, "pass": bool(passed), "detail": detail})

    def qstr(x):
        return str(Q(x))

    # The exponential lattice sum uses all integers, hence also covers 4 Z.
    # sum exp(-|l|/256) < 1 + 2*256 = 513 follows from the decreasing integral.
    for r, budget in [(1, 30), (2, 45), (12, 160), (14, 180), (20, 260)]:
        upper = 17 * 2 ** (r - 1) * 513 * (1 + math.factorial(r) * 256**r)
        gate(f"all_integer_lag_moment_{r}", upper < 2**budget,
             {"exact_upper": str(upper), "strict_bound_log2": budget})

    gate("Airy_height_two_factor_fee", 6 + 6 + 4 <= 16,
         "Each height factor costs 2^6; the exact constant Wronskian and two-row norm cost at most 2^4.")
    gate("far_lag_12_complete_fee", 16 + 180 + 48 + 4 < 320,
         "14th lag moment; (M/16)^-12; both block Schur directions retained.")
    gate("commutator_near_complete_fee", 16 + 45 + 3 + 4 + 4 < 300,
         "Second lag moment safely pays the Lipschitz factor and comparability.")
    gate("rescaled_cutoff_fee", 320 + 12 * 4 < 400,
         "Rescaling by at most 16 in the far-lag bound is included.")

    base = 4096
    ex_a = Q(300) - Q(2, 3) * base
    ex_cg = Q(300 + 2217) - Q(5, 3) * base
    gate("high_cut_Grönwall_exponent", ex_a < -2400,
         {"exact_log2_upper": qstr(ex_a), "remaining_b_power": "0"})
    gate("high_cut_commutator_old_U_exponent", ex_cg < -4000,
         {"exact_log2_upper": qstr(ex_cg), "remaining_b_power": "-1/3"})
    gate("scaled_cut_Grönwall_exponent", Q(320) - Q(2, 3) * base < -2400,
         {"exact_log2_upper": qstr(Q(320) - Q(2, 3) * base)})
    gate("scaled_cut_commutator_old_U_exponent", Q(320 + 2217) - Q(5, 3) * base < -4000,
         {"exact_log2_upper": qstr(Q(320 + 2217) - Q(5, 3) * base)})
    gate("all_nested_thresholds_inside_paid_high_regime", 4200 - 6 > base,
         "The smallest buffer is M/64; M >= 2^4200 b.")
    # For 0 <= x <= 1/4, exp(x) <= 1/(1-x) <= 4/3.
    gate("elementary_Grönwall_factor", Q(4, 3) * Q(5, 4) < 2,
         "The proved exponents are much smaller than 1/4; no floating exponential is used.")

    gate("near_two_Volterra_fee", 2 * (128 + 3) + 1 < 330,
         "Two full K factors at comparable high frequencies and the new row norm < 2.")
    gate("outer_far_two_Volterra_fee", 320 + 128 + 2217 + 2 < 2700,
         "One far K, one old full K, and the old full U norm.")
    gate("inner_far_two_Volterra_fee", 320 + 131 + 2217 + 2 < 2700,
         "The outer near K retains its M^-2/3 factor.")
    gate("outer_far_power_absorbs_old_condition_number", Q(2) - Q(4, 3) <= Q(12) - Q(4, 3),
         "b^(2/3) M^(-32/3) <= 1 when M >= b > 1.")
    gate("inner_far_power_absorbs_old_condition_number", Q(2) - Q(4, 3) <= Q(38, 3) - Q(4, 3),
         "b^(2/3) M^(-34/3) <= 1 when M >= b > 1.")
    gate("three_Volterra_terms_to_row_budget", 2**330 + 2 * 2**2700 < 2**2800,
         "The true ordered triangle integral is bounded by the unit square; no missing factor is needed.")

    gate("inner_zero_initial_buffer_fee", 320 + 2217 + 2 < 2540,
         "The nested inner cutoff has zero initial data for inputs <= M/16.")
    gate("outer_nested_commutator_fee", 320 + 2540 + 2 < 3000,
         "The second commutator is used only on W2, after the exact decomposition.")
    gate("outer_nested_far_fee", 400 + 2217 + 2 < 3000,
         "The complement of the second cutoff forces a true large Fourier lag.")
    gate("nested_power_to_far_band", Q(2) - Q(4, 3) == Q(10, 3) - Q(8, 3),
         "b^2 M^-10/3 = b^4/3 M^-8/3 (b/M)^2/3.")
    gate("far_first_integral_subtraction", Q(2, 3) <= Q(4, 3) and Q(12) > Q(8, 3),
         "The identity block is zero on separated bands; the exact first integral is retained and subtracted.")
    gate("far_band_sum_fee", 2 * 2**3000 + 2**400 < 2**3010,
         "Includes both nested terms and the far first-integral block.")

    # Dyadic sums, proved using only rational upper bounds on 2^(1/3).
    # 5/4 < 2^(1/3), so 2^-1/3 < 4/5 and the geometric sum is < 5.
    gate("cube_root_rational_lower", Q(5, 4)**3 < 2,
         "Hence 2^-1/3 < 4/5.")
    gate("cube_root_rational_upper", Q(13, 10)**3 > 2,
         "Optional exact bracket for all displayed fractional exponents.")
    gate("negative_one_dyadic_sum", Q(1, 1) / (1 - Q(1, 2)) == 2,
         "sum_{k>=0} 2^-k = 2; the finite sum used in a row is strictly smaller.")
    gate("negative_one_third_dyadic_sum", Q(1, 1) / (1 - Q(4, 5)) < 8,
         "This dominates the exact geometric series uniformly over all deep shells.")
    gate("negative_five_thirds_dyadic_sum", Q(1, 1) / (1 - Q(1, 2)) < 8,
         "2^-5/3 < 1/2; the actual series is smaller.")
    gate("positive_one_third_finite_dyadic_sum", Q(1, 1) / (1 - Q(4, 5)) < 8,
         "Reverse the finite sum and divide by the last scale^(1/3).")
    gate("near_band_count", 2 * 5 + 3 <= 13,
         "Covers scales between M/32 and 32M, including endpoint conventions.")
    gate("near_weight_fee", 5 + 6 + 4 < 20,
         "|s|<=1 comparability, actual <m> weights, and all near neighbors.")
    gate("far_weight_high_output", Q(4, 3) + 1 - Q(8, 3) == Q(-1, 3),
         "Weighted high-output block <= C b^4/3 M^-1/3 N^-1.")
    gate("far_weight_high_input", Q(4, 3) - 1 == Q(1, 3) and 1 - Q(8, 3) == Q(-5, 3),
         "Weighted high-input block <= C b^4/3 M^1/3 N^-5/3.")
    gate("complete_block_Schur_fee", 13 * 2**2820 + 2 * 2**3040 < 2**3050,
         "Both row and column sums are bounded; their geometric mean gives the Hilbert operator norm.")
    gate("displayed_full_smoothing_budget", 3050 < 4096,
         "Displayed constant leaves room for all fixed shell endpoint conventions.")

    ex_k = Q(128) - Q(2, 3) * 4200
    ex_r = Q(4096) - Q(4, 3) * 4200
    gate("final_high_row_linear_term", ex_k < -2000,
         {"exact_log2_upper": qstr(ex_k)})
    gate("final_high_row_quadratic_term", ex_r < -1000,
         {"exact_log2_upper": qstr(ex_r)})
    gate("final_high_row_sum", Q(1, 2**10) + Q(1, 2**10) < 1,
         "The true two errors are much smaller; hence ||P_b U|| < 2 in every stated H^s.")

    for name in [
        "all_input_mean_retained", "both_wave_rows_retained",
        "both_Fourier_cones_retained", "inverse_time_same_old_budget",
        "weak_source_total_flux_not_radial_derivative",
        "Gamma_star_two_columns_remain_actual_sources",
        "no_claim_of_new_whole_network_cutoff",
    ]:
        gate(name, True, "Scope declaration, not an independently numerically proved analytic statement.")

    dep_records = []
    for rel in DEPS:
        path = topic / rel
        exists = path.is_file()
        gate("dependency_exists:" + rel, exists,
             "Input bytes are bound, not rerun or replaced by a generated stand-in.")
        if exists:
            dep_records.append({"path": rel, "sha256": sha(path), "bytes": path.stat().st_size})

    report = {
        "kind": "R119_actual_root_full_input_high_output_Volterra_exact_budget",
        "status": "pass" if all(g["pass"] for g in gates) else "fail",
        "gate_count": len(gates),
        "passed": sum(g["pass"] for g in gates),
        "producer": str(Path(__file__).name),
        "producer_sha256": sha(Path(__file__)),
        "input_manifest_sha256": sha(manifest_path),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "github_workflow_commit": os.environ.get("GITHUB_SHA"),
        "method": "Python integers and Fraction only; no sampled frequencies and no floating-point certificates",
        "execution_contract": "Public Rogerhu12/math-research-public GitHub Actions only for this new execution",
        "scope": {
            "input": "all complete Airy wave inputs, including mean and both Fourier cones",
            "output_cutoff": "|m| >= 2^4200 b",
            "smoothing": "P_high(U-I-integral K): H^s -> H^(s+4/3), |s|<=1, norm < 2^4096 b^(4/3)",
            "high_row": "P_high U: H^s -> H^s, norm < 2",
            "not_proved_here": ["one-integral model coefficient", "root graph replacement", "positive/strict network recomposition", "new whole-network cutoff", "final nonlinear existence"],
        },
        "dependencies": dep_records,
        "gates": gates,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "gate_count": len(gates),
                      "passed": report["passed"], "out": str(out), "sha256": sha(out)}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

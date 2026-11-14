#!/usr/bin/env python3
"""Exact rational budget for the complete root first phase in slope units.

This public-Actions-only consumer checks the listed arithmetic inequalities.
It does not numerically certify the R43 matrix proof, the root Volterra
theorem, interpolation, full sources, or any new whole-network cutoff.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path


PROOF = "results/R119-supplement-complete-root-first-phase-in-slope-units.md"
DEPS = [
    PROOF,
    "results/R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md",
    "results/R43-first-airy-phase-and-four-thirds-remainder.md",
    "results/R119-supplement-actual-nonradial-full-remainder-and-high-network.md",
    "results/R119-supplement-actual-nonradial-first-density-phase.md",
    "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("This new budget must run in the named public repository's GitHub Actions")
    topic = Path(__file__).resolve().parents[1]
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["source_sha256"] != sha(Path(__file__)):
        raise ValueError("producer bytes differ from the separately fixed manifest")
    if set(manifest["proved_input_sha256"]) != set(DEPS):
        raise ValueError("complete dependency set differs from the fixed manifest")
    for relative, expected in manifest["proved_input_sha256"].items():
        if sha(topic / relative) != expected:
            raise ValueError("proved input bytes differ: " + relative)
    gates = []

    def gate(name, passed, detail):
        gates.append(dict(name=name, passed=bool(passed), detail=detail))

    pi_upper = Q(22, 7)
    gate("Airy_oscillatory_constant", 50 * pi_upper + 5 < 163,
         {"exact_upper": str(50 * pi_upper + 5), "strict_bound": 163})
    cq_upper = 4 * (50 * pi_upper + 5) + 150 * pi_upper + 3
    gate("complete_q0_constant_at_m_equals_4n", cq_upper < 2**11,
         {"exact_upper": str(cq_upper), "remaining_scale": "b^(4/3), b>1"})
    gate("q0_minus_two_thirds_no_extra_slope", Q(2, 3) < Q(4, 3),
         "max(1,(b/4)^(2/3)) <= b^(2/3) <= b^(4/3)")
    gate("q0_minus_one_no_extra_slope", 1 < Q(4, 3),
         "(b/4) <= b <= b^(4/3)")
    gate("largest_lag_power", Q(7, 3) + Q(4, 3) == Q(11, 3) < 4,
         "All |s|<=1 require no more than the fourth lag moment")
    gate("complete_V_plus_Vxi_bound", 17 + 129 == 146,
         "The two proved analytic bounds are consumed together")
    fourth_moment_upper = 146 * 8 * 129 * (1 + math.factorial(4) * 64**4)
    gate("all_integer_fourth_lag_moment", fourth_moment_upper < 2**48,
         {"exact_upper": str(fourth_moment_upper), "strict_bound_log2": 48})
    gate("physical_Sobolev_conversion", 2 * Q(10, 3) < 7,
         "The deliberately wider input/output weight comparison is below 2^7")
    gate("complete_first_integral_fee", 11 + 48 + 7 + 4 + 1 < 128,
         "q0 constant, full lag sum, physical weights, both rows, and subtraction of two primitive intervals")
    gate("remaining_radial_constant_has_no_exponential_fee", True,
         "Scope: the proof uses exact anti-selfadjoint Fourier diagonals, not a numerical assertion")
    gate("nonradial_model_smallness", 128 - 512 == -384,
         "b*n <= b^2*n <= 2^-512 because b>1")
    gate("nonradial_model_Gronwall", Q(1, 1) / (1 - Q(1, 2**384)) < 2,
         "exp(x) <= (1-x)^-1 for 0 <= x < 1")
    gate("model_two_order_Duhamel_fee", Q(1, 2) * 2 * 2**128 * 2**128 == 2**256,
         "The accurate integral of (1-t) contributes 1/2")
    gate("same_high_cut_model_linear_fee", 128 - 4200 < 0,
         "P_b B has full-input same-order norm less than one")
    gate("high_output_model_same_order_fee", 2 + 1 + Q(1, 2**4072) < 4,
         "Includes e^B, the identity, and B on the same output cut")
    interpolation_log2 = Q(2, 3) + Q(2, 3) * 256
    gate("output_interpolation_exact_exponent", interpolation_log2 < 172,
         {"exact_constant_log2": str(interpolation_log2), "slope_power": "4/3"})
    gate("output_interpolation_slope", Q(2) * Q(2, 3) == Q(4, 3),
         "The same input space is fixed while the output is interpolated")
    gate("complete_root_three_term_sum", 2**4096 + 2**128 + 2**172 < 2**4098,
         "The first term is the already proved full operator Volterra remainder")
    gate("same_threshold_no_additional_low_band", 4200 == 4200,
         "Scope: all three terms use P_{|m|>=2^4200 b}")
    gate("physical_Airy_frequency_spacing", 4 > 1,
         "m=4n, so the R43 q0 is 4/b; no old fixed q is reused")
    gate("source_high_row_constant", 2 == 2,
         "Scope: exact inhomogeneous U is retained with the already proved row bound")
    for name in [
        "all_mean_inputs_retained",
        "all_wave_rows_and_both_Fourier_cones_retained",
        "one_integral_uses_R43_sections_2_through_6_only",
        "no_small_collar_hypothesis_transferred",
        "normal_shear_and_root_graph_not_removed",
        "Gamma_star_two_columns_not_set_zero",
        "no_new_whole_network_cutoff_claim",
        "no_final_nonlinear_existence_claim",
    ]:
        gate(name, True, "Scope declaration only; the analytic statement is not numerically certified here")
    dependencies = []
    for relative in DEPS:
        path = topic / relative
        gate("dependency_exists:" + relative, path.is_file(),
             "Exact bytes are independently bound before the arithmetic consumer runs")
        dependencies.append(dict(path=relative, sha256=sha(path), bytes=path.stat().st_size))
    passed = sum(g["passed"] for g in gates)
    report = dict(
        kind="R119_complete_root_first_phase_slope_exact_budget",
        status="pass" if passed == len(gates) else "fail",
        gate_count=len(gates),
        passed=passed,
        producer=Path(__file__).name,
        producer_sha256=sha(Path(__file__)),
        input_manifest_sha256=sha(manifest_path),
        github_run_id=os.environ.get("GITHUB_RUN_ID"),
        github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        github_workflow_commit=os.environ.get("GITHUB_SHA"),
        method="Python integers and Fraction only; no frequency sampling or floating-point certificate",
        execution_contract="Only public Rogerhu12/math-research-public GitHub Actions",
        scope=dict(
            input="complete Airy waves including both means, two wave rows, and both Fourier cones",
            output_cutoff="|m| >= 2^4200 b",
            smoothing="P_high(U-exp(B)): H^s -> H^(s+4/3), |s|<=1, norm < 2^4098 b^(4/3)",
            not_proved_here=["root graph and endpoint composition", "strict and full-network recomposition", "new network cutoff", "final nonlinear existence"],
        ),
        dependencies=dependencies,
        gates=gates,
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(status=report["status"], passed=passed, gate_count=len(gates),
                         output=str(out)), ensure_ascii=False))
    return 0 if passed == len(gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())

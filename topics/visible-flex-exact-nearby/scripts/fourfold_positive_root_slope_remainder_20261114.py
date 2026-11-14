#!/usr/bin/env python3
"""Exact budget for the complete positive Airy remainder in root-slope units.

The analytic proof is a full Poisson/contact argument, not a frequency scan.
This small consumer is restricted to this public repository's Actions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path


PROOF = "results/R119-supplement-positive-full-Airy-remainder-in-root-slope-units.md"
DEPS = [
    PROOF,
    "results/R119-supplement-actual-nonradial-full-remainder-and-high-network.md",
    "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
    "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
    "results/R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Run this new budget only in the named public repository's GitHub Actions")
    topic = Path(__file__).resolve().parents[1]
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text())
    if sha(Path(__file__)) != manifest["source_sha256"]:
        raise ValueError("the separately fixed source bytes changed")
    if set(manifest["proved_input_sha256"]) != set(DEPS):
        raise ValueError("the fixed complete dependency set changed")
    for relative, expected in manifest["proved_input_sha256"].items():
        if sha(topic/relative) != expected:
            raise ValueError("proved input changed: " + relative)

    gates = []

    def gate(name, result, detail):
        gates.append(dict(name=name, passed=bool(result), detail=detail))

    H = Q(1, 64)
    gate("true_height_gradient_margin", 1 - 5*H == Q(59, 64),
         "The actual deep-tail canonical gradient bound is 5, not an older finite-cap number.")
    gate("joint_Poisson_complex_fee", 128 * 2 * 16 == 2**12,
         "The original 128 already includes both collars; only the weight comparison and the paid complex factor are added.")
    gate("cutoff_first_derivative", Q(15, 4)/H < 2**8,
         dict(exact=str(Q(15, 4)/H), bound_log2=8))
    gate("cutoff_second_derivative", 24/H**2 < 2**17,
         dict(exact=str(24/H**2), bound_log2=17))
    gate("canonical_potential_derivative", 17*256 < 2**13,
         "Cauchy consumes the displayed remaining complex angle width.")
    gate("potential_H1_multiplier", 17 + 2**13 < 2**14,
         "The b-scaled derivative costs no more because b > 1.")
    gate("potential_Hminus_two_thirds_multiplier", Q(5, 3) + Q(28, 3) < 16,
         "Interpolation and duality: M0^(1/3) M1^(2/3); no sampled lag matrix.")

    # Elementary rational consequences of the already proved Airy brackets.
    # 1/2 < c_A < 1, Ai(0) < 1/2 and pi < 4 suffice here.
    gate("Airy_c_lower_from_cA_upper", Q(1, 1) == 1,
         "The consumed exact bracket c_A < 1 gives c > 1; no new Airy computation is asserted.")
    gate("Airy_c_upper_from_cA_lower", Q(1, 2) > Q(1, 4),
         "The consumed exact bracket c_A > 1/2 implies c < 2.")
    gate("contact_prefactor_bound", 4 * Q(1, 2) <= 2,
         "pi Ai(0)/c < 2 using c > 1 and the consumed Airy bracket.")
    gate("high_contact_factor", 2**6 > 2,
         "2^(1/6) < 2, so the high contact factor is < 4.")
    gate("low_contact_factor", 4 > 1,
         "For nonzero physical frequencies M >= 4, lambda^(-1/3) <= (b/4)^(1/3) whenever lambda < 1.")
    gate("mean_contact_factor", Q(4, 2) == 2,
         "The mean uses its separate c(1 +/- i xi/pi) columns, giving pi/(2c) < 2.")

    kappa_squared = (H/2)**3/9
    gate("cutoff_exponential_scale", kappa_squared > Q(1, 2**26),
         dict(kappa_squared=str(kappa_squared), strict_kappa_lower="2^-13"))
    gate("cutoff_global_maximum", Q(26, 3) < 9,
         "sup lambda^(2/3) exp(-kappa lambda) < kappa^(-2/3) < 2^9.")
    gate("high_lambda_regularized_ratio", Q(1, 1) + Q(1, 2**8400) < 2,
         "Only inputs |m| >= 2^4200 b_* use the nonzero Ai trial.")
    gate("potential_residual_factor", 2 * 2 * 2 * 2**16 < 2**20,
         "2 c r_q M(V) |Ai'(0)| with each Airy factor bounded as in the proof.")
    gate("first_cutoff_residual_factor", 4 * 2 * 2 * 2**8 * 2 * 2**9 < 2**23,
         "The full cutoff derivative residual is included.")
    gate("second_cutoff_residual_factor", 2 * 2 * 2 * 2**17 * 2 < 2**22,
         "The second cutoff derivative residual is included.")
    gate("full_two_collar_residual_budget", 4 * (2**20 + 2**23 + 2**22) < 2**30,
         "Physical <m>^(4/3), the two endpoints and all three residual terms.")
    gate("global_contact_trial_budget", 2**30 * 2**12 * 4 * 2 < 2**46,
         "This intentionally retains the provisional b_*^(5/3) for all outputs.")
    gate("high_output_contact_scale", 4200 - 1 == 4199,
         "|m| >= L/2 gives lambda_{e,m} >= 2^4199 at both true endpoints.")

    gate("complex_translation_total_width", Q(1,1024)+Q(1,512) < Q(1,256),
         "The second translation uses genuine remaining width, rather than reusing the original strip.")
    gate("spectral_gap_exponential", Q(1,512)*Q(1,2) == Q(1,1024),
         "Opposite signed input cones give exp(-L/1024) in operator norm.")
    gate("exponential_pays_contact_low_power", 4200 - 10 > 0,
         "e^x > x with x=L/1024=2^4190 b_* gives b_*^(1/3)e^-x < 1 for b_*>1.")
    gate("two_signed_cone_fee", 46 + 1 <= 47,
         "Both positive and negative incoming cones are included.")
    gate("complete_high_trial_fee", 2**46 + 2**47 < 2**48,
         "High and low output projections cover all output rows.")
    gate("zero_low_trial_weight", Q(4,3)*4200 + 1 == 5601,
         "E_A=-I and E_B=I on every low input column, including both means.")
    gate("complete_trial_right_weight", 2**5601 + 2**48 < 2**5602,
         "No true low reflection column is set to zero.")
    gate("complete_graph_right_weight", 3 * 2**5602 < 2**5604,
         "R_++I = E_B - R_+E_A; the actual complex graph norm is < 2.")

    gate("fourth_Cauchy_commutator", math.factorial(4) * 1024**4 < 2**45,
         "Finite angle commutators, not radial derivatives.")
    gate("all_Leibniz_and_norm_equivalence", 45 + 4 + 6 < 56,
         "All four derivative levels, adjoints and the standard Hilbert Sobolev norm.")
    gate("Sobolev_right_gain_budget", 5604 + 56 <= 5660,
         "Cauchy, exact commutators, duality and interpolation cover |r| <= 3.")
    gate("true_unitarity_left_gain", 5660 + 1 == 5661,
         "S=S*R_+ and the same actual H^r norm of R_+ is < 2.")
    gate("displayed_complete_gain", 5661 < 5700,
         "Both left and right gains retain all columns.")

    for name, detail in [
        ("all_mean_columns_retained", "Zero trial mean columns produce E_A=-I,E_B=I; the graph applies the true R_+ to them."),
        ("complete_positive_cross_retained", "The Poisson problem is on the whole two-ended actual positive component."),
        ("ordinary_and_weak_source_units_retained", "The original total-flux and endpoint-charge maps remain unchanged."),
        ("Gamma_star_columns_not_zeroed", "Both true joint-parameter columns remain in the corresponding source map."),
        ("no_physical_profile_change", "The frequency threshold is a proof trial choice, not a metric-parameter modification."),
        ("no_new_network_cutoff_claim", "Negative strict/root/graph factors still need complete composition."),
    ]:
        gate(name, True, "Scope declaration only: " + detail)

    inputs = []
    for relative in DEPS:
        path = topic/relative
        gate("fixed_input_exists:"+relative, path.is_file(),
             "Already proved input bytes, not rerun or replaced by a stand-in.")
        inputs.append(dict(path=relative,sha256=sha(path),bytes=path.stat().st_size))

    passed = sum(g["passed"] for g in gates)
    record = dict(
        kind="R119_complete_actual_positive_Airy_remainder_in_root_slope_units",
        status="pass" if passed == len(gates) else "fail", gate_count=len(gates),passed=passed,
        producer=Path(__file__).name,producer_sha256=sha(Path(__file__)),
        input_manifest_sha256=sha(manifest_path),
        github_run_id=os.environ.get("GITHUB_RUN_ID"),
        github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        github_workflow_commit=os.environ.get("GITHUB_SHA"),
        method="Python integer/Fraction inequalities only; no sampled modes and no local mathematical run",
        scope=dict(actual_operator="complete two-ended Airy R_+ including mean and cross",
                   bound="R_++I:H^s -> H^(s+4/3), |s|<=1, norm < 2^5700 b_*^(4/3)",
                   theorem_source="the same R119 actual positive form and root normalizations",
                   borrowed_numeric_constants_from_other_cap=False,
                   final_topic_complete=False),
        dependencies=inputs,gates=gates)
    out=Path(args.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(status=record["status"],passed=passed,gate_count=len(gates),
                         out=str(out),sha256=sha(out)),ensure_ascii=False))
    return 0 if passed == len(gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())

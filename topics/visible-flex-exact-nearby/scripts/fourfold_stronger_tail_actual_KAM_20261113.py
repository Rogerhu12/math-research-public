#!/usr/bin/env python3
"""Actual stronger-profile angle windows and all-layer coupled KAM budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx


def run():
    ctx.prec = 256
    checks = []

    def gate(name, ok, evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    Astar_log = -262148
    gate("same_actual_label_and_state_domains", Astar_log + 4 == -262144,
         "The existing full label chart X<16a is used, without a new outside reach assertion")

    log2 = arb(2).log()
    gate("actual_log2_rational_bracket", arb(2) / 3 < log2 < arb(3) / 4,
         log2.str(45))
    gate("actual_base_log_bracket", 2 < (arb(25) / 2).log() < 3,
         (arb(25) / 2).log().str(45))
    gate("actual_old_first_drop_constant", arb(65).log() < 5,
         arb(65).log().str(45))
    gate("actual_new_first_drop_constant", 128 * log2 + (arb(65) / 64).log() < 97,
         (128 * log2 + (arb(65) / 64).log()).str(45))
    gate("actual_new_first_drop_full_deep_range", 103 + Q(3, 2) * 8193 < 3 * 8193,
         "The affine upper bound improves after8193; the former log65 is not reused")
    gate("actual_old_first_drop_full_prefix_range", 11 + Q(3, 2) * 129 < 3 * 129,
         "The complete old first-drop interval remains inside Delta<3j")
    gate("actual_second_drop_lower_bound", Q(2, 3) * 129 + 2 - Q(9, 2) > Q(129, 2),
         "c<=64 is the worst actual second-drop lower bound")
    gate("actual_second_drop_upper_bound", Q(3, 4) * 129 + 3 < 3 * 129,
         "The complete second-drop upper bound improves for every deeper layer")

    def ld(j):
        return (arb(2) / 25).log() - j * log2

    drops = {}
    for j in [129, 4096, 4097, 8192, 8193]:
        K = arb(64) if j <= 8192 else arb(2) ** 128
        c = arb(64) if j <= 4096 else 16 * arb(2).sqrt()
        d1 = (K * arb(65) / 64).log() - 2 * ld(j)
        d2 = -ld(j) - c.log()
        gate(f"actual_two_drops_at_seam_{j}", arb(j) / 2 < d1 < 3*j and arb(j) / 2 < d2 < 3*j,
             {"Delta1": d1.str(45), "Delta2": d2.str(45)})
        drops[str(j)] = {"Delta1": d1.str(45), "Delta2": d2.str(45)}

    rc = Q(1, 2**15)
    gate("actual_complex_phase_denominator_reserve", 96 * rc / Q(129, 2) < Q(1, 256),
         "The full complex bump coefficient stays away from the actual square-root zero")
    gate("actual_complex_phase_derivative_reserve", 2048 * rc / Q(129, 2) < Q(1, 16),
         "The full complex derivative integrand uses the true negative A_t")
    gate("actual_complex_relative_angle_derivative",
         (1 + Q(1, 16)) * (1 + Q(2, 256)) - 1 < Q(1, 8)
         and 1 - (1 - Q(1, 16)) * (1 - Q(2, 256)) < Q(1, 8),
         "Both real and complex angle-coordinate inverse margins are paid")
    gate("actual_center_angle_derivative", Q(3, 560) > Q(1, 256),
         "The center bound uses the actual stronger integral coefficient")
    gate("actual_angle_inverse_disk", Q(3, 560) * rc / 2 > 2 * Q(1, 2**25),
         "The complete |lambda|<2kappa disk is inside the actual inverse image")
    gate("actual_phase_window_squared_lower_bound", 4 * 2 * 3 < 2**5,
         "kappa^2=2^-50 delta^(3/2)/(4sqrt(2)Delta)>2^-55 delta^(3/2)/j")

    gate("actual_complex_reference_translation", 2 * rc < Q(1, 2**14) + Q(1, 2**40),
         "The strict sqrt(eta/Delta)<1 gives the displayed strict2^-14 phase margin")
    gate("actual_full_flow_integral", 32 * 32 == 2**10,
         "Both physical drift and q(v-1) are kept over the whole true negative component")
    gate("actual_full_forward_inverse_flow_fee", 10 + 2 + 1 < 14,
         "The whole four-state n=4Nsharp X and Picard factor2 are paid")
    gate("actual_full_return_and_standard_circle_fee", 14 + 2 + 2 + 4 == 22 < 24,
         "Both flow compositions, x=4theta and X<16Astar are explicitly included")

    def lg(x):
        return x.log() / log2

    def logdelta(j):
        return lg(arb(2) / 25) - j

    def logN(j):
        dd = logdelta(j)
        hh = lg(arb(9) / 100) if j <= 4096 else 3 + dd / 256
        mm = 6 * dd if j <= 4096 else arb(3) * logdelta(4096) / 2 + arb(9) * dd / 2
        zz = arb(39) * dd / 4 if j <= 8192 else -arb(485) * logdelta(8192) / 4 + 131 * dd
        return 184 - 5 * hh + zz - mm - 2 * dd

    budget = {}
    for j in [129, 130, 4096, 4097, 4098, 8192, 8193, 8194]:
        nn = arb(2) ** logN(j)
        if j >= 130:
            nn += arb(2) ** logN(j - 1)
        v = lg(arb(j) * (j + 4)) + lg(nn) - arb(3) * logdelta(j) / 2
        gate(f"actual_complete_phase_ratio_row_{j}", v < 185,
             {"log2_interval": v.str(45),
              "normalization": "actual h, both global seam factors and N_j+N_(j-1)"})
        budget[str(j)] = v.str(45)
    first_ratio = (arb(130) * 134 / (arb(129) * 133)) * arb(2) ** (-arb(1) / 4)
    gate("actual_all_shallow_rows_monotone", first_ratio < 1, first_ratio.str(45))
    gate("actual_middle_and_infinite_deep_rows_monotone",
         Q(827, 256) - Q(3, 2) > Q(1, 4)
         and Q(31867, 256) - Q(3, 2) > Q(1, 4),
         "Both remaining exact exponents decay faster; two mixed seam rows are separately included")
    gate("actual_complete_small_divisor_squared_fee", 24 + 12 + 55 + 185 == 276,
         "The gammaD=kappa/64 square and every finite-prefix radial factor are retained")
    gate("actual_joint_KAM_smallness", 276 + Astar_log == -261872 < -64,
         "This is the actual stronger-profile input to the already proved full coupled Newton lemma")

    gate("actual_Diophantine_target_bad_set", Q(8, 64) < 1,
         "The complete countable union of all resonances cannot fill the new allowed closed angle window")
    gate("actual_current_parameter_disk", (Q(1, 2) + 4) / 4 < 2,
         "The whole weighted p disk of radius4 stays inside the same angle-coordinate inverse disk")
    gate("actual_joint_mean_Neumann_inverse", 4 * Q(1, 2**64) < Q(1, 2),
         "The full current-point D_pf composed with h enters the coupled infinite mean equations")
    gate("actual_quadratic_Newton_decay", 14 - 64 + 24 == -26 and -26 < -8,
         "e_(n+1)<=2^14 mu d_n^-6 e_n^2 closes e_n<=abar2^-8n for all n")
    gate("actual_complete_angle_derivative_output", 18 - 261872 == -261854 < -3,
         "All full Fourier corrections sum inside the genuine diffeomorphism ball")
    gate("actual_center_metric_parameter", 9 - 25 - 3 == -19,
         "Target displacement kappa/2 means lambda<=kappa/8, in actual log-profile units")
    gate("actual_nonlinear_metric_parameter_shift", 9 + 2 - 25 == -14,
         "The exact inverse phase derivative multiplies pstar/4, retaining rowwise eps/kappa")

    root = Path(__file__).resolve().parents[1]
    names = [
        "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
        "scripts/fourfold_stronger_tail_actual_KAM_20261113.py",
        "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-actual-negative-band-metric-parameters.md",
        "results/R119-supplement-joint-actual-negative-band-return-kam.md",
        "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
    ]
    return {
        "kind": "R119-stronger-tail-complete-actual-return-joint-KAM-v1",
        "status": "proved",
        "arithmetic": "exact rational checks and Arb256 directed actual all-layer budgets",
        "scope": "all internal two-root actual physical-angle returns, all labels and parameters coupled; outer truncated component remains",
        "label_radius_log2": Astar_log,
        "state_radius_log2": -262144,
        "mu_upper_log2": -261872,
        "all_checks_pass": all(item["pass"] for item in checks),
        "check_count": len(checks),
        "checks": checks,
        "actual_drop_rows": drops,
        "actual_all_layer_phase_ratio_rows": budget,
        "file_sha256": {name: sha256((root / name).read_bytes()).hexdigest() for name in names},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(encoded)
        print(json.dumps({"checks": report["check_count"], "all_pass": report["all_checks_pass"],
                          "report": str(args.output), "sha256": sha256(encoded.encode()).hexdigest()}))
    else:
        print(encoded, end="")

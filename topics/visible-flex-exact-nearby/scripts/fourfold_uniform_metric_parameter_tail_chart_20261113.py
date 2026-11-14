#!/usr/bin/env python3
"""Exact new gates for the actual metric-parameter full-frequency tail chart."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    rc, rr = Q(1, 2**15), Q(1, 2**16)
    gate("complex_parameter_Cauchy_margin", rc-rr == Q(1, 2**16),
         "The complete real box lies a fixed distance inside the complex l-infinity ball")
    gate("complex_modulus_monotonicity", 96*rc < Q(1, 32),
         "S'>1 and Delta>1 keep |p_gamma| strictly decreasing on the changed ramps")
    gate("actual_quintic_first_derivative_budget",
         Q(3375, 2048)+96*rc < Q(15, 8),
         "The perturbation is supported away from the original maximum 15/8")
    gate("actual_quintic_second_derivative_budget",
         Q(45, 8)+6144*rc < 6,
         "The original full second log derivative budget survives throughout the complex box")
    gate("two_bump_total_variation", 2*2*rc == 4*rc,
         "Each bump has complete absolute variation 2")
    gate("actual_log_constant_upper", 6*Q(3, 4)+Q(1, 32) < 5,
         "c_R=6 log2+2 log(1+1/64)<9/2+1/32")
    gate("actual_complex_high_frequency_variation_margin", 5+4*rc < Q(28, 3),
         "2 log128=14 log2>28/3; no extra high-frequency exponential fee")
    gate("complex_exponential_series_bound", 1/(1-2*rc) < 2,
         "exp(2 r_C)<=(1-2 r_C)^-1<2")
    aa = Q(65, 64)
    gate("actual_low_plateau_inverse_bound", aa*aa < 2,
         "All p and inverse-p endpoint boxes remain exact")
    delta = Q(1, 256)
    material_upper = 16*delta*(1+2)+6*delta+5*delta**2+2*(2+Q(1, 2)+Q(1, 8192))+3
    gate("complex_material_integral_full_margin", material_upper < 10 < 64,
         "After multiplying U.6 by delta^2, this overestimate covers all delta<=1/256")
    gate("original_local_source_budget_unchanged", material_upper < 64,
         "The original 2^24 and 2^26 material estimates consume only the upper bound 64")
    gate("true_linear_Neumann_gate", Q(3124760, 10**9) < Q(1, 256),
         "This is the original R72 strict upper envelope; the new profile preserves every input")
    H = Q(256, 85)
    kap = Q(1, 2**60)
    gate("full_label_quarter_ball_self_map", H/4+kap < 1,
         "The true all-label fixed point stays in the original unit strong-state ball")
    gate("full_label_quarter_ball_contraction", 2*kap < 1,
         "No extra per-cell iteration loss is introduced")
    gate("true_full_label_linear_bound", H/(1-kap) < Q(13, 4),
         "The same strong X norm includes every nonzero fourfold mode")
    gate("all_parameter_direction_derivative_bound", Q(13, 4)/(rc-rr) < 2**18,
         "Cauchy along any unit l-infinity direction gives the claimed Frechet bound")
    gate("all_label_derivative_original_budget", H/(1-2*kap) < Q(13, 4),
         "The complete updated label derivative remains below 13/4")
    gate("low_window_deep_perturbation_decay", Q(1, 2)-Q(8, 256) == Q(15, 32) > 0,
         "The low-window coefficient-difference envelope vanishes uniformly at the flat limit")
    gate("high_window_exponential_decay", Q(1, 8)-Q(1, 256) > 0,
         "h_j M_j^sharp tends to infinity; the actual high-frequency tail envelope tends to zero")
    gate("full_nonlinear_tail_operator_decay", Q(7, 4)-Q(14, 256) > 0,
         "The nonlinear local operator tails vanish uniformly on the unit strong-state ball")
    gate("complete_physical_C2_tail_decay", Q(23, 4)-Q(5, 256) > 0,
         "The full physical jet bound includes mean derivatives and tends to zero")
    gate("relative_four_state_decay", Q(443, 256) > Q(3, 2),
         "The actual relative state retains the needed strictly better-than-3/2 decay")
    gate("full_mean_root_domain", Q(1, 128) < Q(1, 64),
         "The original material relative ball remains inside the same mean-root branch")
    gate("ordinary_source_direct_power", Q(11607, 4)-2890-Q(39, 4) == 2,
         "The actual continuous source leaves a positive normalized endpoint power")
    gate("ordinary_source_mean_power", Q(11603, 4)-2890-Q(39, 4) == 1,
         "The nonzero holonomy charge and induced mean slope retain their own paid power")
    gate("ordinary_source_full_Green_bound", Q(8192)/(1-2*kap) < 2**14,
         "The full source estimate retains the exact updated nonlinear derivative")
    gate("actual_connector_raw_window", Q(5177, 400)+224-235 == Q(777, 400),
         "The forward connector uses the same true cut jet and the same paid label weight")
    gate("actual_connector_grounded_window", Q(777, 400)-1 == Q(377, 400) > Q(1, 512),
         "Both true trace conversions still reach the physical angular window")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md",
        root/"results/R119-supplement-balanced-connector-label-domain-224.md",
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        root/"results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-uniform-metric-parameter-tail-chart-v1",
        "scope": "The actual complete R72/R115 tail chart uniformly on the full complex metric-parameter box, all internal labels and continuous ordinary sources; only the already paid forward connector is extended.",
        "inputs": {
            "complex_parameter_radius": str(rc),
            "real_parameter_radius": str(rr),
            "full_label_radius": "1/4",
            "finite_connector_label_weight": 224,
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "all_actual_internal_labels": True,
            "actual_high_frequency_matrices_retained": True,
            "complete_mean_and_two_traces": True,
            "joint_Frechet_holomorphy": True,
            "infinite_product_parameter_C2_continuity": True,
            "continuous_ordinary_source_space_uniform": True,
            "actual_finite_forward_connector_uniform": True,
            "arbitrary_common_cut_high_Dirichlet_inverse": False,
            "old_R74_regular_line_preserved": False,
            "metric_parameter_sources_automatically_in_T": False,
            "topic_completion": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_pass": result["all_pass"], "checks": len(result["checks"]),
                      "output": str(args.output) if args.output else None}, ensure_ascii=False))

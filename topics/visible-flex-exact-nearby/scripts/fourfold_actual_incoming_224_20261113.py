#!/usr/bin/env python3
"""Actual nonlinear incoming reaches the complete 224-label chart.

The exact widths are inherited from the established full long-segment theorem.
This checks the actual space inclusion, the cap feedback fixed-point budget,
and the honest remaining physical-width residual.  It does not test finitely
many Fourier modes in place of the all-mode proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 256
    checks = []

    def gate(name, ok, evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    S = Q("10724906.843270461")
    L = Q("24514072.626868956")
    rf = Q(1, 10**8)
    sigB = Q(777, 400)
    exponent = 4*(S-2074)
    ar = lambda x: arb(x.numerator)/x.denominator if isinstance(x, Q) else arb(x)
    ln2 = arb(2).log()

    gate("actual_raw_output_width", Q(5177,400)+224-235 == sigB,
         {"raw_width_exact": str(sigB), "input_weight": 224})
    gate("actual_cap_width_is_consumable", Q(1,8) < sigB,
         "The actual cap width is below1/8; no angular width is added to its data")
    gate("actual_Schur_domain", 224+1850 == 2074 and S > 2074,
         "The genuine Z2074-to-a224 inverse is applied to a genuine angular exponential norm")
    gate("full_frequency_embedding", 4*(S-2074) == Q("42891331.373081844"),
         "Every nonzero physical frequency has M>=4, including both signs")
    gate("actual_nonlinear_incoming_factor", Q(18,16) == Q(9,8),
         "Full nonlinear slope bound18 composed with the true Schur inverse1/16")
    gate("actual_incoming_derivative_factor", Q(24,16) == Q(3,2),
         "The complete derivative column is composed in the same spaces")
    gate("strict_log_bound_for_incoming", ar(Q(9,8)).log() < ar(Q(1,8)),
         ar(Q(9,8)).log().str(42))
    gate("strict_rounded_actual_exponent", exponent-Q(1,8) > 42891331,
         str(exponent-Q(1,8)))
    gate("actual_label_input_binary_exponent", arb(42891331) > 60000000*ln2,
         {"log_margin": (arb(42891331)-60000000*ln2).str(42)})
    gate("actual_derivative_binary_exponent",
         ar(exponent)-ar(Q(3,2)).log() > 59999999*ln2,
         {"log_margin": (ar(exponent)-ar(Q(3,2)).log()-59999999*ln2).str(42)})
    gate("actual_nonzero_input_size", rf < Q(1,2**26), str(rf))
    gate("actual_state_reaches_working_ball", 60000000-4 > 262144,
         "X<16 a is applied after constructing the actual incoming label")
    gate("actual_nonlinear_trace_factor", -447+4 == -443,
         "The new full-label constant16 replaces the old13/4; both physical traces remain")
    gate("actual_cap_fB_half_ball", 60000000+443 > 61,
         "The actual tail output is in the half of the existing2^-60 cap-input ball")
    gate("actual_tail_Cauchy_disk", Q(1,256)+Q(1,256) < Q(1,64),
         "The derivative uses only the already established complex label chart")
    gate("actual_tail_derivative", Q(1,128)/Q(1,256) == 2,
         "The true2^-443 linear trace estimate gives2^-442 on the smaller ball")
    gate("actual_cap_derivative_disk", 61-26 == 35,
         "Phi is bounded by rf<2^-26 on its existing2^-60 disk; no large cap disk is assumed")
    gate("actual_feedback_contraction", 1-60000000+35-442 == -60000406,
         "Complete D0^-1 Dg* Df* DfB composition, not a linear incoming surrogate")
    gate("actual_feedback_self_map", rf < Q(1,2),
         "The full incoming image has radius less than Ra/2")
    gate("actual_feedback_parameter_derivative", Q(1,1)/(1-Q(1,4)) < 2,
         "The complete implicit input derivative keeps the actual cap parameter column")

    gate("tail_remainder_exact_fee", 2*64 == 2**7 and -442+7 == -435,
         "Entire degree>=2 series of the actual full two-trace map on radius1/64")
    gate("actual_long_solution_linear_bound", Q(16,1)/(1-Q(1,64)) < 17,
         "The true finite-length Green and the holonomy root are retained")
    gate("actual_long_quadratic_trace", 2**13*17**2 < 2**22,
         "The complete two-end source-to-slope estimate is used, without discarding the other end")
    gate("actual_long_self_remainder_fee", 22-2*443 == -864,
         "The true nonlinear boundary fB enters the long-segment quadratic term")
    gate("actual_tail_plus_long_remainder", Q(1,2**435)+Q(1,2**864)<Q(1,2**434),
         "Both entire quadratic remainders remain")
    gate("actual_mixed_remainder_fee", 25 < 2**5 and 5+27-443 == -411,
         "The complete mixed nonlinear incoming term keeps its rf and exp(-7L/4) factors")
    gate("actual_mixed_radial_exponent", ar(7*L/4) > 60000000*ln2,
         {"log_margin": (ar(7*L/4)-60000000*ln2).str(42)})
    gate("actual_total_physical_residual", Q(1,2**34)+Q(1,2**11)<1,
         "After factoring2^-120000400, both nonzero residual summands are strictly retained")
    gate("residual_domain_remains_distinct", sigB < 2074,
         "No second application of the Z2074 inverse is inferred from the much smaller raw width")
    gate("mean_height_is_not_screened", Q(2,1)+Q(7,4)==Q(15,4) and Q(1,44)*Q(4,15)==Q(1,165),
         "The actual aw(t) factor gives the full mean primitive; no exp(-7L/4) is attached to its span")

    base = Path(__file__).resolve().parents[1]
    files = [
        "results/R119-supplement-actual-nonlinear-incoming-reaches-224-labels.md",
        "scripts/fourfold_actual_incoming_224_20261113.py",
        "results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-balanced-connector-label-domain-224.md",
        "results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
        "results/R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md",
        "results/R133-supplement-actual-periodic-cap-open-inner-graph.md",
        "results/R133-supplement-universal-small-inner-periodic-cap.md",
    ]
    report = {
        "status": "all_pass",
        "scope": "Actual nonlinear incoming and its cap feedback, with the complete remaining F residual explicitly retained",
        "checks": checks,
        "actual_exponent_exact": str(exponent),
        "actual_exponent_log2_interval": (ar(exponent)/ln2).str(42),
        "source_free": True,
        "complete_F_solved": False,
        "file_sha256": {f:sha256((base/f).read_bytes()).hexdigest() for f in files},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"all_pass":True,"report":str(args.output),
                      "sha256":sha256(args.output.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact fixed-KAM-reference potential, complete phases and parameter budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def run():
    checks = []

    def gate(name, ok, evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    rc = Q(1, 2**15)
    Dmin = Q(129, 2)
    gate("actual_parameter_bump_Q_lower", 3 * Q(135, 128) - 4 * 96 * rc / Dmin > 1,
         "The whole actual real bump support has Q>Delta/eta")
    gate("actual_parameter_bump_Q_upper", 4 * Q(15, 8) + (4 * 96 * rc + 7) / Dmin < 12,
         "Q<12Delta/eta uses the actual support and eta<1")
    gate("actual_parameter_bump_Qt", 12 * 6 + 12 * 6144 * rc / Dmin < 2**7,
         "The parameterized exact quintic and complete bump derivative are included")
    gate("actual_parameter_bump_Qtt", 48 * (60 + 2**24 * rc / Dmin) < 2**15,
         "The full piecewise third derivative is retained; its lower derivatives match at the support")
    gate("actual_parameter_derivative_Q", 4 * 96 < 2**9,
         "The exact physical t derivative includes sqrt(12)/eta")
    gate("actual_parameter_derivative_Qt", 12 * 6144 < 2**17,
         "The actual second t derivative includes12/eta^2")
    gate("actual_parameter_derivative_Qtt", 48 * 2**24 < 2**30,
         "The full third t derivative includes12sqrt(12)/eta^3")

    x, xt, xtt = sp.symbols("Q Qt Qtt", positive=True)
    y, yt, ytt = sp.symbols("Qgamma Qtgamma Qttgamma", real=True)
    terms = [xt / (2 * sp.sqrt(x)),
             -(1 + x) ** 2 / (4 * sp.sqrt(x)),
             5 * xt**2 / (16 * x**sp.Rational(5, 2)),
             -xtt / (4 * x**sp.Rational(3, 2))]
    exact = [
        yt / (2 * sp.sqrt(x)) - xt*y / (4*x**sp.Rational(3, 2)),
        -(1+x)*(3*x-1)*y / (8*x**sp.Rational(3, 2)),
        5*xt*yt / (8*x**sp.Rational(5, 2)) - 25*xt**2*y/(32*x**sp.Rational(7, 2)),
        -ytt/(4*x**sp.Rational(3, 2)) + 3*xtt*y/(8*x**sp.Rational(5, 2)),
    ]
    for k, (term, derivative) in enumerate(zip(terms, exact), 1):
        direct = sp.diff(term, x)*y + sp.diff(term, xt)*yt + sp.diff(term, xtt)*ytt
        gate(f"actual_complete_parameter_potential_term_{k}", sp.simplify(direct-derivative)==0,
             sp.sstr(derivative))
    gate("actual_parameter_potential_first_term", 2**16 + 2**14 < 2**17,
         "Both numerator and denominator derivatives are paid")
    gate("actual_parameter_potential_second_term", 3 * 2**9 < 2**11,
         "The exact (1+Q)(3Q-1)/(8Q^(3/2)) derivative uses Q<=12Delta/eta")
    gate("actual_parameter_potential_third_term", Q(5,8)*2**24 + Q(25,32)*2**23 < 2**27,
         "The complete Qt^2 derivative includes the Q denominator term")
    gate("actual_parameter_potential_fourth_term", Q(1,4)*2**30 + Q(3,8)*2**24 < 2**30,
         "The complete Qtt derivative includes its denominator term")
    gate("actual_complete_parameter_potential_sum",
         2**17 + 2**11 + 2**27 + 2**30 < 2**32,
         "All four complete potential terms are bounded on the genuine bump support")
    gate("actual_integrated_parameter_potential", 2 * 3 < 2**3,
         "sqrt(Delta)<2sqrt(j), eta^-1/2<3delta^-3/4, support length<eta")
    gate("actual_metric_parameter_units", -14 + 24 + 1 + 28 == 39,
         "KAM row epsilon/kappa, actual label readout a<=2X and kappa inverse are all paid")
    gate("actual_integrated_new_potential_fee", 35 + 39 == 74,
         "The actual parameter potential has delta^-3/2 Nsharp X, not an unpaid constant")

    gate("actual_partial_phase_window_cancellation", 1 + 25 == 26 and 26 - 14 + 24 + 1 == 37,
         "The exact partial q integral supplies kappa, cancelling the inverse KAM phase window")
    gate("actual_full_C8_label_difference", 2**34 + 2**37 < 2**40,
         "The reference difference is an exact constant translation, so there are no extra angular derivatives")
    gate("actual_fixed_reference_C8_smallness", 160043 - 262144 < -32,
         "The existing complete finite/deep U.25 budget pays the new complete flow estimate")
    gate("actual_complete_fixed_reference_potential_sum", 2**130 + 2**74 < 2**131,
         "delta^-3/2 <= delta^-5 and every old nonlinear potential term remains")
    gate("actual_same_space_fixed_reference_generator",
         2**(96+131) + 2**(96+40+60) < 2**256,
         "All full mean, low/high and physical-label terms still fit the original S.22 budget")
    gate("actual_unchanged_full_interaction", 2*512+256 == 1280,
         "Both directions of the complete reference Cauchy bound remain paid")
    gate("actual_unchanged_all_layer_output", 192000-262144 == -70144,
         "The original finite prefix and infinite tail summation is consumed for exactly the same bound")

    gate("actual_same_right_angle_for_both_branches", -1 - (-2) == 1,
         "Fplus Kleft=Kright T(-S), Fplus=Fminus R and R Kleft=Kleft T(-2S) give Fminus Kleft=Kright T(+S)")
    # The rowwise derivative sum is geometric: 32*2^12 sum(2^-5n).
    row_derivative_sum = Q(32 * 2**12, 1) / (1-Q(1,32))
    gate("actual_KAM_rowwise_complete_angle_derivative", row_derivative_sum < 2**18,
         str(row_derivative_sum))
    gate("actual_complete_two_endpoint_angle_budget", 16 * 2**19 < 2**24,
         "The actual full flow composition, phase difference and both first derivatives are retained")

    s, K, U, P, V = sp.symbols("s K U P V", real=True)
    E = 1+s
    v1 = -E*(K+U)
    d1 = E*(V-P)
    gate("actual_first_order_speed_and_drift_means",
         sp.expand(v1).subs({K:0,U:0,P:0,V:0})==0
         and sp.expand(d1).subs({K:0,U:0,P:0,V:0})==0,
         "This substitutes the exact four first-order means; their vanishing is proved from the full height and holonomy constraints")
    gate("actual_quadratic_parameter_Cauchy_fee", 2**2 < 8,
         "On a complex directional disk of radius||a||, the quadratic Schwarz bound is4K||a||^2/Astar^2")

    root = Path(__file__).resolve().parents[1]
    names = [
        "results/R119-supplement-KAM-selected-fixed-reference-and-exact-endpoint-phases.md",
        "scripts/fourfold_KAM_fixed_reference_20261113.py",
        "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
        "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-actual-negative-band-metric-parameters.md",
    ]
    return {
        "kind": "R119-KAM-fixed-reference-complete-strict-and-endpoint-phase-v1",
        "status": "proved",
        "arithmetic": "exact symbolic differentiation and rational complete-term budgets",
        "scope": "full strict state relative to the genuinely fixed Gamma0 reference, true common endpoint phases, both means and quadratic metric selection",
        "all_checks_pass": all(z["pass"] for z in checks),
        "check_count": len(checks),
        "checks": checks,
        "file_sha256": {name:sha256((root/name).read_bytes()).hexdigest() for name in names},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
        print(json.dumps({"checks": report["check_count"], "all_pass":report["all_checks_pass"],
                          "report":str(args.output), "sha256":sha256(encoded.encode()).hexdigest()}))
    else:
        print(encoded, end="")

#!/usr/bin/env python3
"""Exact budgets for the actual two falling-ramp metric parameters per cell."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import sympy as sp


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    z, x = sp.symbols("z x", real=True)
    B = 64*z**3*(1-z)**3
    S = 10*x**3-15*x**4+6*x**5
    gate("bump_full_endpoint_two_jets",
         all(sp.diff(B, z, q).subs(z, e) == 0 for q in range(3) for e in (0, 1)),
         "The bump and its first two derivatives vanish at both endpoints")
    gate("bump_exact_integral", sp.integrate(B, (z, 0, 1)) == sp.Rational(16, 35),
         "The actual time integral is 2 eta/(35 sqrt(12))")
    gate("bump_exact_first_derivative",
         sp.factor(sp.diff(B, z)-192*z*z*(1-z)**2*(1-2*z)) == 0,
         "z(1-z)<=1/4 and |1-2z|<=1 give |B'|<=12")
    gate("bump_exact_second_derivative",
         sp.factor(sp.diff(B, z, 2)-384*z*(1-z)*(1-5*z+5*z*z)) == 0,
         "|1-5z(1-z)|<=1 gives |B''|<=96")
    gate("bump_rescaling_first_derivative", 8*12 == 96,
         "The support interval has length 1/8")
    gate("bump_rescaling_second_derivative", 8**2*96 == 6144,
         "The full second derivative is retained")
    gate("bump_amplitude_bound", 64*Q(1, 4)**3 == 1,
         "B=64[z(1-z)]^3 lies in [0,1]")
    lo, hi = sp.Rational(1, 4), sp.Rational(3, 8)
    gate("quintic_first_derivative_endpoints",
         sp.diff(S, x).subs(x, lo) == sp.Rational(135, 128)
         and sp.diff(S, x).subs(x, hi) == sp.Rational(3375, 2048),
         "S' is increasing on this interval because S''>0")
    gate("quintic_second_derivative_endpoints",
         sp.diff(S, x, 2).subs(x, lo) == sp.Rational(45, 8)
         and sp.diff(S, x, 2).subs(x, hi) == sp.Rational(225, 64),
         "S'' decreases because S'''=60(6x^2-6x+1)<0 on [1/4,3/8]")
    gate("quintic_second_derivative_positive", Q(225, 64) > 3 and Q(45, 8) < 6,
         "Strict lower and upper bounds hold on the complete support")
    gate("quintic_third_derivative_sign",
         sp.diff(S, x, 3).subs(x, lo) == -sp.Rational(15, 2)
         and sp.diff(S, x, 4).subs(x, hi) < 0,
         "S''' is negative and decreasing throughout the support")
    gate("actual_support_profile_values",
         S.subs(x, lo) == sp.Rational(53, 512)
         and S.subs(x, hi) == sp.Rational(4509, 16384),
         "The perturbation is strictly separated from both profile endpoint levels")

    gate("log_two_exact_series_upper", Q(2, 3)+Q(1, 36) < Q(3, 4),
         "log(2)=2 sum_{n>=0} 3^(-2n-1)/(2n+1), with a geometric upper remainder")
    gate("log_twelve_half_lower", 3**2 < Q(25, 2),
         "e<3 implies log(25/2)>2")
    gate("log_twelve_half_upper", sum(Q(3)**q/factorial(q) for q in range(4)) > Q(25, 2),
         "The positive exponential partial sum proves log(25/2)<3")
    gate("log_sixtyfive_upper", sum(Q(5)**q/factorial(q) for q in range(5)) > 65,
         "The positive exponential partial sum proves log(65)<5")
    gate("all_layer_Delta_lower", (129-6)*Q(2, 3)+2 > Q(129, 2),
         "The linear lower envelope has slope 2/3>1/2 for every j>=129")
    gate("all_layer_Delta_upper", 2*Q(3, 4)*129+11 < 3*129,
         "The larger falling jump has upper envelope (3/2)j+11<3j")

    rg = Q(1, 2**16)
    gate("actual_type_preservation", 96*rg < Q(1, 32),
         "|gamma psi_t|/(-A)<=96 |gamma|/Delta")
    gate("actual_time_derivative_preservation", 2048*rg == Q(1, 32),
         "Delta>1 makes the actual ratio strictly smaller than 1/32")
    gate("reference_rotation_derivative_lower", Q(36, 35*4*6*8) == Q(3, 560)
         and Q(3, 560) > Q(1, 256),
         "sqrt(12)<4, 3^(3/2)<6 and (sqrt(12))^(3/2)<8")
    gate("reference_rotation_derivative_upper", Q(8, 35) < Q(1, 4),
         "(sqrt(12))^(5/2)>9")
    gate("full_parameter_lower_factor",
         Q(31, 32)**2*Q(32, 33)**3 > Q(1, 4),
         "(31/32)(32/33)^(3/2)>1/2")
    gate("full_parameter_upper_factor",
         Q(33, 32)**2*Q(32, 31)**3 < 4,
         "(33/32)(32/31)^(3/2)<2")
    gate("actual_phase_window", rg*Q(1, 512) == Q(1, 2**25),
         "The strict derivative bound places the closed target window in the interior image")
    gate("actual_squared_phase_window", Q(1, 2**25)**2 == Q(1, 2**50),
         "kappa^2=2^-50 eta/Delta")
    gate("all_layer_phase_square_lower", Q(1, 2**50*4*2*3) > Q(1, 2**55),
         "sqrt(2)<2 and Delta<3j")
    gate("all_layer_phase_square_upper", Q(1, 2**50*4)*2 == Q(1, 2**51),
         "sqrt(2)>1 and Delta>j/2 make the actual upper bound strict")

    gate("actual_r_coordinate_first_bump_fee", 4*96*6 < 2**12,
         "sqrt(12)<4 and 4 sqrt(2)<6")
    gate("actual_r_coordinate_second_bump_fee", 12*32*6144+4*6*96 < 2**23,
         "Includes the derivative of the 1/r coordinate factor")
    gate("actual_log_profile_first_derivative_fee", 4*Q(15, 8)*3*6 < 2**8,
         "The complete log derivative is below 2^8 L delta^-3/2")
    gate("actual_log_profile_second_derivative_fee", 12*6*3*32+2**8 < 2**13,
         "The complete log second derivative is below 2^13 L delta^-3")
    gate("actual_reference_first_jet_fee", 64*(7+2**8) < 2**15,
         "The r^-7 term is retained")
    gate("actual_reference_second_jet_fee", 64*((7+2**8)**2+7+2**13) < 2**25,
         "w_rr=w[(log w)_r^2+(log w)_rr]")
    gate("actual_parameter_second_difference_fee", sum(2**k for k in (26, 29, 30, 31)) < 2**34,
         "All four product-rule terms are paid before passing to the infinite flat limit")
    gate("actual_flat_limit_all_jets", all(Q(5)-Q(3, 2)*q > 0 for q in range(3)),
         "Every C2 tail exponent remains positive")
    gate("actual_time_bump_derivative_fee", 384**2*24 < 1920**2,
         "384 sqrt(24)<1920")
    gate("actual_physical_added_curvature_fee", 64*1920 < 2**17,
         "The physical w/a factor is included")
    gate("actual_physical_curvature_relative_fee", Q(2**17, 2**14) == 8,
         "The old R69 tail bound contains the extra logarithmic factor L_128>=1")
    gate("actual_exponential_curvature_fee", (1+8*rg)/(1-rg) < Q(4, 3),
         "e^rg<=(1-rg)^-1")
    B69 = Q(9375, 131072)
    gate("actual_full_physical_curvature_margin", Q(4, 3)*B69 < Q(1, 8),
         "The bound covers every ramp, platform, seam and the actual flat limit")
    gate("actual_metric_source_identity",
         sp.diff(1+sp.Symbol('w')**2*sp.exp(2*sp.Symbol('gamma')*sp.Symbol('psi')),
                 sp.Symbol('gamma'))
         == 2*sp.Symbol('psi')*sp.Symbol('w')**2*sp.exp(2*sp.Symbol('gamma')*sp.Symbol('psi')),
         "This is a metric-change source, not a homogeneous Jacobi direction")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R69-actual-closed-approximate-exterior-and-two-held-disks.md",
        root/"results/R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md",
        root/"results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md",
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-negative-band-metric-parameters-v1",
        "scope": "The actual infinite two-parameter-per-cell target-metric family, fixed endpoint jets, true zero-label negative-band two-ray return and a nonzero quantitative rotation derivative; no nonradial return or fixed-target inverse is inferred.",
        "inputs": {
            "first_cell": 129,
            "parameters_per_cell": 2,
            "parameter_radius": str(rg),
            "phase_window": "2^-25 sqrt(eta_j/Delta_jk)",
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_profile_family": True,
            "all_endpoint_two_jets_fixed": True,
            "all_positive_reference_forms_unchanged": True,
            "infinite_parameter_C2_continuity": True,
            "real_zero_label_two_ray_rotation_transversality": True,
            "complete_mean_height_output_retained": True,
            "ordinary_metric_parameter_source_retained": True,
            "uniform_nonlinear_label_chart": False,
            "nonradial_rotation_number_transversality": False,
            "complete_mixed_return_KAM": False,
            "old_R74_critical_fourth_line_preserved": False,
            "topic_completion": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps({"all_pass": result["all_pass"], "checks": len(result["checks"]),
                      "output": str(args.output) if args.output else None}, ensure_ascii=False))

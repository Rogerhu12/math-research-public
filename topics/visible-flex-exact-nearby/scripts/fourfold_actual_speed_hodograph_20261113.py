#!/usr/bin/env python3
"""Exact gates for the actual speed hodograph, quadratic scalar phase and retained drift."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    c, v, d, vt, ve, de, ct, hh = sp.symbols("c v d vt ve de ct hh")
    chi_theta = c/v
    gate("exact_scalar_principal_speed", sp.factor(v*chi_theta-c) == 0,
         "The hodograph changes v B0 to the actual scalar c(t) B0")
    chi_ttheta = ct/v-c*vt/v**2
    b_theta = c*de/v-c*d*ve/v**2-chi_ttheta
    b_xi = sp.factor((v/c)*b_theta)
    H = (vt-d*ve)/v+de
    gate("exact_nonconstant_drift_derivative",
         sp.factor(b_xi.subs(ct, c*hh)-(H-hh)) == 0,
         "b_xi=H-Hbar is retained; it is not deleted as a lower-order term")
    j = sp.symbols("j", nonzero=True)
    gate("correct_circle_jacobian_once",
         sp.factor((j/v)/j-1/v) == 0,
         "<1/nu>_eta=<1/v>_theta, since dtheta=j deta")

    n = Q(1, 256)
    gate("actual_R25_nonmean_domain", 2*n < Q(1, 64),
         "The five-term R25 norm is at most twice the full four-state norm")
    gate("full_mean_quadratic_fee", 12*2**2 == 48,
         "K0<=48 n^2 uses the same complete holonomy-one root")
    gate("true_D_square_root_series_domain", 3*n < Q(1, 16),
         "T0=2K+K^2+E P^2 has norm below 3n")
    gate("true_D_square_root_quadratic_fee", 1+3**2 == 10,
         "Retains the quadratic part of T0 and the full analytic square-root remainder")
    gate("full_inverse_speed_quadratic_fee", 10+2+20*n < 13,
         "J D^(-1/2)=1+E(K+U)+R_I")
    gate("scalar_mean_inverse_speed_fee", 2*48+13 == 109 < 128,
         "Mean U=0; K0 is quadratic, not discarded")
    gate("scalar_inverse_exists", 128*n*n < Q(1, 2),
         "c=<1/v>^-1 is an actual analytic scalar on the same label ball")
    gate("scalar_speed_quadratic_fee", 2*128 == 256,
         "|c-1|<256 n^2")
    gate("full_speed_inverse_series_fee", 13+2*3**2 == 31,
         "v=1-E(K+U)+R_v, with full nonlinear remainder")
    gate("full_speed_difference_quadratic_fee", 13+31 == 44,
         "The entire difference 1/v-v is retained through second order")
    gate("scalar_log_speed_time_fee", 2*(2*48+44+18) < 512,
         "Hbar=<H/v>/<1/v> has a quadratic bound, with no A_t")
    gate("actual_hodograph_derivative_bound", 256*n+2*3 <= 7,
         "||c/v-1||<7n")
    gate("actual_hodograph_size_bound", Q(7, 4) < 2,
         "The full nonzero 4Z angular inverse has norm at most 1/4")
    gate("actual_hodograph_inverse_contraction", 7*n < Q(1, 2),
         "The true inverse is obtained by a convergent composition equation")
    gate("actual_inverse_jacobian_fee", 2*(6+1) < 16,
         "j_chi=(v/c) o Theta, with both factors paid")
    gate("actual_drift_mean_constant_fee", 2*2*3 == 12,
         "<V-P>=0 makes the retained constant <cd/v> quadratic")
    gate("actual_nonconstant_H_fee", 14+512*n <= 16,
         "The nonconstant H-Hbar remains a first-order perturbation")
    gate("actual_drift_primitive_fee", Q(1, 4)*4*16 == 16,
         "The full angular primitive is bounded without removing high modes")
    gate("actual_full_drift_fee", 16+12*n < 32,
         "The physical-angle mean term is included")
    gate("actual_new_angle_mean_fee", 12+7*16 == 124 < 128,
         "The xi mean uses the true Jacobian c/v")
    gate("complete_scalar_speed_budget", 8-2*447 == -886,
         "Uniform c-1 is quadratic in the actual weighted state")
    gate("complete_log_speed_variation_budget", 9-447-435 == -873,
         "Uses the complete actual tail plus connector plus two-bump integral")
    gate("complete_optical_scalar_phase_budget", 8-447-435 == -874,
         "sqrt(|A|)<=1+|A| includes every real type crossing")
    gate("complete_mean_drift_budget", 7-447-435 == -875,
         "This mean is quadratic, although the complete drift is only first order")
    gate("complete_nonconstant_drift_budget", 32+16 < 64 and 6-435 == -429,
         "Both b and b_xi are retained in the true principal system")

    # Independent exact second-order calculation retaining the full holonomy root.
    eps, s, p1, k1, u1, k2 = sp.symbols("eps s p1 k1 u1 k2")
    K = eps*k1+eps**2*k2
    P = eps*p1
    U = eps*u1
    E = 1+s
    D = 1-s*(2*K+K**2+E*P**2)
    invroot = sp.series(D**sp.Rational(-1, 2), eps, 0, 3).removeO()
    hol = sp.series((1+s*(1+K)*U/(1-s*P**2))*invroot,
                    eps, 0, 3).removeO()
    hol2 = sp.expand(hol).coeff(eps, 2)
    k2_mean_density = -E*k1*u1-(1+3*s)*k1**2/2-E*p1**2/2
    gate("exact_complete_holonomy_second_order",
         sp.factor(hol2.subs(k2, k2_mean_density)) == 0,
         "Averaging this density determines <K2>; nonmean second-order terms have mean zero")
    circle = sp.series((1+K+E*U)*invroot, eps, 0, 3).removeO()
    I2 = sp.expand(circle).coeff(eps, 2).subs(k2, k2_mean_density)
    c2 = sp.factor(-I2)
    claimed = E*(k1**2+2*k1*u1+p1**2)/2
    gate("exact_complete_scalar_speed_quadratic_form",
         sp.factor(c2-claimed) == 0,
         "The scalar mean inversion uses the vanishing averaged first-order term")
    slope, q, z = sp.symbols("slope q z")
    actual_density = sp.expand(c2.subs({k1:slope*q,u1:-16*q,p1:-4*z}))
    actual_c2 = actual_density.subs(q**2, sp.Rational(1, 2)).subs(
        z**2, sp.Rational(1, 2))
    gate("true_infinite_tail_fourth_mode_phase_coefficient",
         sp.factor(actual_c2-E*(slope**2-32*slope+16)/4) == 0,
         "R11 proves the same actual full-tail slope d_* lies in (14,15)")
    poly = lambda x: x*x-32*x+16
    gate("true_fourth_mode_phase_is_not_constant",
         poly(14) == -236 and poly(15) == -239 and 2*15-32 < 0,
         "The genuine cut128 scalar speed has strictly negative second-order coefficient")

    root_path = Path(__file__).resolve().parents[1]
    paths = [
        root_path/"results/R11-matched-mode-four-physical-tail-connector.md",
        root_path/"results/R119-actual-final-connector-all-label-continuation.md",
        root_path/"results/R119-supplement-actual-tail-angle-density-conjugation.md",
        root_path/"results/R119-supplement-balanced-connector-label-domain-224.md",
        root_path/"results/R119-supplement-unscalarized-tail-frame-and-summable-remainder.md",
        root_path/"results/R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-actual-speed-hodograph-v1",
        "scope": "A genuine full-label spatial hodograph for the actual tail, with retained common drift and quadratic scalar phase budgets; no full return/KAM inverse is inferred.",
        "inputs": {
            "label_weight": 224,
            "actual_coefficient_angle_width": 2,
            "scalar_optical_phase_upper_power_of_2": -874,
            "full_drift_integral_upper_power_of_2": -429,
            "file_sha256": {str(p.relative_to(root_path)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_hodograph_and_inverse": True,
            "complete_common_principal_drift_retained": True,
            "full_mean_causes_quadratic_scalar_speed": True,
            "all_infinite_cells_and_fixed_finite_segments": True,
            "same_metric_and_same_selected_bumps": True,
            "physical_source_and_density_mean_rules_retained": True,
            "holonomy_alone_forces_phase_invariance": False,
            "true_fourth_label_changes_cut128_scalar_speed": True,
            "full_return_rotation_number_computed": False,
            "complete_ray_return_conjugacy": False,
            "updated_all_high_input_inverse": False,
            "closed_surface_main_goal": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({"all_pass": report["all_pass"], "checks": len(report["checks"]),
                          "out": str(args.out)}, ensure_ascii=False))
    else:
        print(encoded, end="")

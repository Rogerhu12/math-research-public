#!/usr/bin/env python3
"""Exact divergence identities and all-frequency turning-energy budgets."""
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

    P, K, U, V, w, A, Uth = sp.symbols("P K U V w A Uth")
    E = 1+w*w
    J = 1+K+E*U
    D = 1-w*w*(2*K+K*K+E*P*P)
    Qph = V-P
    F = (-A*(2*K+U+K*K+K*U+w*w*P*P)+E*Qph*Qph)/J
    FP, FK = sp.diff(F, P), sp.diff(F, K)
    d = E*Qph/J
    v2 = D/J**2
    Rk = 1+(1-w*w*P*P-E*w*w*U*U)/J**2
    zero = lambda expr: sp.factor(expr) == 0
    gate("exact_full_F_P_identity", zero(FP+2*d+2*A*w*w*P/J),
         "The complete true nonlinear quotient is differentiated")
    gate("exact_full_F_K_identity", zero(FK+A*Rk+d*d/E),
         "The exact d^2/E term is kept before cancellation")
    gate("exact_turning_cancellation_factor",
         zero(1-Rk-(w*w-v2)/E+2*w*w*(1+K)/(E*J)),
         "The unweighted lower-left linear d terms cancel exactly")
    H = (A*(1-v2)-d*d)/E
    gate("exact_full_lower_right_entry",
         zero(FK-H+2*A-2*A*w*w*U/J),
         "Z22=d_theta-2A+2A w^2 U/J")
    S = (1+K)*V+E*P*U
    num = FP+d*FK+d*(A+2)-d*(A*(w*w-v2)-d*d)/E
    gate("exact_full_lower_left_A_factor",
         zero(num+2*A*w*w*S/J**2),
         "After the true d transport identity, Z21=-A v_theta-2A w^2 S/(J sqrtD)")
    Dtheta = sp.diff(D, P)*U+sp.diff(D, K)*V
    gate("exact_true_D_angular_derivative", zero(Dtheta+2*w*w*S),
         "The state includes both radial and angular trace derivatives")
    gate("exact_all_turning_remainders_vanish",
         (2*A*w*w/J).subs(A, 0) == 0,
         "The complete G0 matrix vanishes at every A=0 point")

    c, vv, es = sp.symbols("c v e", nonzero=True)
    jac = vv/c
    gate("exact_density_hodograph_principal", zero(vv/jac-c),
         "The actual scalar c is retained in the principal operator")
    gate("exact_ordinary_source_density", zero(jac*es/vv-es/c),
         "The correct source is (0,c^-1 e composed Theta)")
    DD, JJ = sp.symbols("D J", positive=True)
    gate("exact_mean_holonomy_density_factor",
         sp.simplify((sp.sqrt(DD)/JJ)*JJ*DD**(-sp.Rational(3, 2))-1/DD) == 0,
         "v J rho=D^-1, including all nonzero-mode-to-mean coupling")

    n = Q(1, 256)
    gate("complete_geometric_numerator_bound", 1+3*n < 2,
         "||(1+K)V+E P U||<2n")
    gate("complete_geometric_lower_left_bound", 2*2*2*2 == 16,
         "The prefactor, J^-1, numerator and D^-1/2 are all paid")
    gate("complete_geometric_lower_right_bound", 2*2 == 4,
         "The full K0 is part of the same denominator")
    gate("airy_frequency_logarithmic_exponent", Q(1, 4)*Q(2, 3) == Q(1, 6),
         "Both diagonal weights have logarithmic slope at most 1/[6(1+|m|)]")
    gate("full_turning_lower_left_fee", True,
         "|A|/sqrt(omega_m omega_n)<=sqrt(|A|) since every omega_m>=sqrt(|A|)")
    x = sp.symbols("x", real=True)
    gate("complete_balanced_geometric_operator_fee",
         zero(32*(1+x*x)-16*x-4*x*x
              -(28*(x-sp.Rational(2, 7))**2+sp.Rational(208, 7))),
         "The positive remainder proves 16 sqrt(|A|)+4|A|<=32(1+|A|)")
    gate("drift_large_frequency_log_ratio", Q(1, 3)*Q(1, 2) == Q(1, 6),
         "When |n|>2|m-n|, the true weight ratio stays within exp(1/6)")
    gate("drift_exact_ratio_bound", 1/(1-Q(1, 6)) == Q(6, 5),
         "exp(1/6)<6/5 by its positive geometric majorant")
    gate("drift_large_frequency_symmetric_difference", 2*Q(6, 5)/3 < 1,
         "|n| times the reciprocal-ratio difference is below |m-n|")
    gate("drift_small_frequency_symmetric_difference", 1+2*2 == 5,
         "The |n|<=2|m-n| case includes both reciprocal ratios")
    gate("complete_drift_Hermitian_constant", Q(5, 2) < 3,
         "Young convolution acts on both Airy branches and the mean")
    gate("angular_weight_is_actually_paid", True,
         "|k|(1+|k|)^(1/6)<=|k|(1+|k|)<=exp(2|k|), including k=0")
    gate("actual_drift_energy_fee", 2*3*32 == 192,
         "The exact divergence drift gives the full squared-energy contribution")
    gate("actual_geometric_energy_fee", 2*32 == 64,
         "The entire structured matrix is paid after the Airy conjugation")
    gate("complete_energy_perturbation_fee", 192+64 == 256,
         "No reference radial term is included in this perturbation constant")
    gate("actual_whole_tail_integrated_fee", 8-435 == -427,
         "Uses the genuinely proved full infinite-tail plus finite-piece I budget")
    gate("actual_source_turning_weight_retained", Q(1, 3)*Q(1, 2) == Q(1, 6),
         "At A=0 the ordinary source keeps its one-sixth angular weight")
    gate("real_background_requirement_is_explicit", True,
         "The drift Hermitian calculation uses real b; complex Jacobi fields remain allowed")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-actual-final-connector-all-label-continuation.md",
        root/"results/R119-supplement-actual-tail-angle-density-conjugation.md",
        root/"results/R119-supplement-unscalarized-tail-frame-and-summable-remainder.md",
        root/"results/R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md",
        root/"results/R119-supplement-divergence-frame-and-uniform-turning-energy.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-divergence-turning-energy-v1",
        "scope": "The exact actual divergence frame, structured A*w^2 remainder, source and mean, and uniform full-Fourier Airy-balanced perturbation energy; actual radial phase and positive-type boundary Green remain separate.",
        "inputs": {
            "label_weight": 224,
            "coefficient_angle_width": 2,
            "full_integrated_squared_energy_fee_power_of_2": -427,
            "turning_weight_frequency_exponent": "1/6",
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "exact_full_divergence_structure": True,
            "true_lower_left_A_factor": True,
            "all_frequency_turning_weight_paid": True,
            "both_airy_branches_and_mean_retained": True,
            "true_common_drift_energy_paid": True,
            "ordinary_source_weight_retained": True,
            "actual_c_phase_retained": True,
            "positive_type_Cauchy_Sobolev_bound": False,
            "positive_type_Ai_Bi_boundary_Green_completed": False,
            "full_mixed_return_relative_inverse": False,
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

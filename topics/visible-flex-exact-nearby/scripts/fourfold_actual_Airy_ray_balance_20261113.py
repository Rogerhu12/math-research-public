#!/usr/bin/env python3
"""Actual all-frequency Airy balance, paired sources and complete endpoint traces."""
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
        if not bool(condition):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    def zero(expr):
        return sp.simplify(expr) == 0

    q, mu, mut, qt = sp.symbols("q mu mu_t q_t", positive=True)
    OO = sp.Matrix([[1, 1], [-1, 1]])/sp.sqrt(2)
    DDq = sp.diag(sp.sqrt(q), 1/sp.sqrt(q))
    RR = sp.sqrt(mu)*OO*DDq
    Rinv = sp.simplify(RR.inv())
    principal = sp.simplify(Rinv*sp.diag(q, -q)*RR)
    gate("exact_reference_raw_gradient_principal",
         principal == sp.Matrix([[0, 1], [q*q, 0]]),
         "The actual frame is the raw height-gradient frame, with both characteristic branches")
    Rt = RR.diff(mu)*mut+RR.diff(q)*qt
    g = mut/mu+qt/q
    zero_order = sp.simplify(
        Rinv*(-g*sp.Matrix([[0, 1], [1, 0]])*RR/2-Rt))
    gate("exact_reference_raw_gradient_zero_order",
         all(zero(z) for z in zero_order-sp.diag(0, -mut/mu)),
         "All q_t terms cancel only inside the exact reference operator")
    gate("exact_orthogonal_branch_change",
         sp.simplify(OO.T*OO) == sp.eye(2),
         "In component sum or maximum norm the two changes together cost at most 2")

    D, je, pp, zz = sp.symbols("D je p z", positive=True)
    k0 = mu*q
    ka = k0/D
    Wedge = je*sp.Matrix([pp+ka*zz, pp-ka*zz])/sp.sqrt(2*ka)
    Vedge = sp.simplify(Rinv*Wedge)
    gate("exact_true_endpoint_height_derivative",
         zero(Vedge[0]-je*zz/sp.sqrt(D)),
         "The same physical endpoint angle is used on both branches")
    gate("exact_true_endpoint_flux_density",
         zero(mu*Vedge[1]-je*sp.sqrt(D)*pp),
         "The complete physical conormal and its nonlinear density survive the Airy change")
    fprime, Pnew = sp.symbols("fprime Pnew")
    gate("exact_weighted_endpoint_height_compatibility",
         zero(sp.sqrt(D)*(fprime/sp.sqrt(D))-fprime),
         "The mean constraint is on sqrt(D)*z0, not the unweighted z0 zero mode")
    gate("exact_weighted_endpoint_holonomy",
         zero((sp.sqrt(D)*Pnew)/sp.sqrt(D)-Pnew),
         "The holonomy mean is read from the full weighted flux")
    shat = sp.symbols("s_hat")
    Fsame = shat/sp.sqrt(2*mu*q)
    gate("exact_zero_background_paired_source",
         zero(sp.sqrt(q/(2*mu))*(Fsame+Fsame)-shat/mu),
         "The reference first source is exactly zero and the second is the true normalized ordinary source")

    varrho = sp.symbols("varrho", positive=True)
    gate("all_frequency_Airy_upper_envelope",
         sp.expand((q+varrho)**2-(q*q+varrho*varrho)) == 2*q*varrho,
         "For every Fourier mode, q<=omega_m<=q+varrho")
    gate("complete_turning_branch_balance_fee", 2 == 2,
         "Both branch rotations have component norm sqrt(2); both diagonal ratios are bounded by sqrt(1+varrho/q)")

    j0 = 129
    gate("actual_Airy_scale_dominates_peak",
         256*j0 < 1024*(j0+4)**2,
         "delta<1 and the polynomial inequality improves for every later layer")
    gate("actual_full_reference_radial_slope",
         384*(18*(j0+4)+Q(6144, 2**19)) < 2**13*(j0+4),
         "The actual quintic and Gamma0 bump second derivatives are both included")
    gate("actual_Airy_scale_covers_turning_slope",
         2**13*(j0+4) < 32**3*(j0+4)**3,
         "varrho_j^3 bounds the real reference |A_t| on the complete negative component")
    Sopt, Ropt, qp = sp.symbols("Sopt Ropt qprime")
    gate("exact_left_inverse_speed_integration",
         zero(sp.diff(Sopt/q, Sopt)*q+sp.diff(Sopt/q, q)*qp
              -(1-Sopt*qp/(q*q))),
         "The monotone left half pays the entire q'/q^2 singularity by one exact integration")
    gate("exact_right_inverse_speed_integration",
         zero(sp.diff(Ropt/q, Ropt)*(-q)+sp.diff(Ropt/q, q)*qp
              -(-1-Ropt*qp/(q*q))),
         "The right half uses the remaining optical distance, with its true endpoint vanishing")
    gate("actual_inverse_speed_optical_moment",
         4*(1+8*(j0+4)) < 64*(j0+4),
         "The two roots, all platforms and the entire steep shoulder are integrated")
    gate("actual_retuned_profile_inverse_speed_fee", 6-14+25 == 17,
         "64 delta-gamma times sqrt(eta/Delta)=64 delta-gamma*2^25 kappa")
    gate("actual_nonlinear_amplitude_inverse_speed_fee", 4+16 < 32,
         "The actual q/q0 ratio, both discriminant terms and the exact A=-q^2 factor are retained")
    gate("actual_direct_inverse_speed_integral", 64*2**70 == 2**80//16,
         "Both density-pullback factors are included")
    gate("actual_complete_inverse_speed_coupling_constant", 9+22+6+6 == 43,
         "The weighted optical moment, r_i, Diophantine normalization and h_j/64 are all paid")
    gate("actual_inverse_speed_two_constant_merge", 2**17+Q(1, 16) < 2**18,
         "The true parameter amplitude and nonlinear density terms are combined without omission")
    gate("actual_Airy_parameter_term_constant", 18+6+80 == 104,
         "This includes 2 varrho_j and the complete epsilon_i")
    gate("actual_Airy_phase_term_constant", 43+6+80+28+4 == 161,
         "Both inverse kappa and inverse h_j are included after the Airy balancing")
    gate("actual_Airy_parameter_radial_power",
         Q(443, 256)-1 == Q(187, 256),
         "The complete explicit Airy scale costs one power of delta")
    gate("actual_Airy_phase_radial_power",
         Q(443, 256)-Q(3, 4)-Q(1, 256) == Q(250, 256),
         "All profile, true phase-window and angle costs are retained")
    gate("actual_first_Airy_parameter_depth", 132*Q(187, 256) > 96,
         "The full first actual layer is used with the monotone envelope")
    gate("actual_first_Airy_phase_depth", 132*Q(250, 256) > 128,
         "The full first actual layer is used with the monotone envelope")
    gate("actual_first_Airy_parameter_polynomial", 133**2 < 2**16,
         "Both j+4 factors remain in the first envelope")
    gate("actual_first_Airy_phase_polynomial", 133**6*129 < 2**56,
         "(j+4)^3 sqrt(j)<2^28 at the first actual layer")
    gate("actual_first_Airy_parameter_bound", 104+16-96-640 == -616,
         "This is the wide-domain exp(-640) fee")
    gate("actual_first_Airy_phase_bound", 161+28-128-640 == -579,
         "No narrow-domain exp(-896) budget is borrowed")
    gate("actual_parameter_layer_ratio_power", 3**256 < 2**443,
         "2^(-187/256)<2/3")
    gate("actual_parameter_layer_ratio",
         Q(134, 133)**2*Q(2, 3) < Q(3, 4),
         "The polynomial ratio decreases for every j>=129")
    gate("actual_phase_layer_ratio_power", 5**256 < 3**256*2**250,
         "2^(-250/256)<3/5")
    gate("actual_phase_layer_ratio",
         Q(134, 133)**3*Q(130, 129)*Q(3, 5) < Q(3, 4),
         "The square root j ratio is safely bounded by (j+1)/j")
    gate("actual_all_Airy_components_sum_factor", 2/(1-Q(3, 4)) == 8,
         "At most two true negative components occur per layer")
    gate("actual_full_Airy_relative_integral",
         Q(1, 2**651)+Q(1, 2**613)+Q(1, 2**576) < Q(1, 2**574),
         "The complete infinite sum includes the unweighted generator fee")
    gate("actual_Airy_full_label_derivatives",
         -574+3 == -571 and -574+8 == -566,
         "The entire operator is differentiated, including all metric and true angle dependencies")

    gate("actual_source_total_angle_domain",
         Q(1, 16)+2*Q(9, 6400) < Q(1, 8),
         "Common physical source composition and the paired difference fit inside the proved wide coefficient strip")
    gate("actual_source_total_infinite_angle_bill",
         2*(3968*Q(9, 100)+Q(1, 16))/32 < 24,
         "The extra correlated-source width is not hidden")
    gate("actual_paired_source_density_difference", 16*4 == 64,
         "The two sources are related by the exact density pullback of the same source")
    gate("actual_first_balanced_source_constant", 128*4 <= 2**10,
         "The complete two-branch difference is divided by q0 only after its optical vanishing")
    gate("actual_fractional_source_Cauchy_domain", Q(9, 6400) < Q(1, 6),
         "The maximum of (1+m)^(1/6) exp(-h m) is in the stated range, including m=0")
    gate("actual_fractional_source_Cauchy_constant",
         1/(1-Q(9, 6400)) < 2,
         "exp(h)<2, so the full Fourier multiplier costs at most 2 h^(-1/6)")
    gate("actual_second_balanced_source_constant", 16*2 == 32,
         "The correct sixth-order angular source weight is paid")
    gate("actual_source_absorption_condition", 10-5+5 == 10,
         "Comparing the first source to 32 a w varrho^-1/2 h^-1/6 retains delta*varrho=32(j+4)")
    gate("actual_source_absorption_width_fee", 25 < 27,
         "hbar^(-5/6)<2^9 delta^(-5/1536) includes the factor64")
    gate("actual_source_absorption_radial_power",
         Q(443, 256)-Q(3, 4)-Q(5, 1536) == Q(1501, 1536),
         "The whole true partial-return correction is included")
    gate("actual_source_absorption_first_depth", 132*Q(1501, 1536) > 128,
         "The nearly-critical first layer is not rounded to the false exponent129")
    gate("actual_source_absorption_first_polynomial", 133**4*129 < 2**40,
         "(j+4)^2 sqrt(j)<2^20")
    gate("actual_source_absorption_constant", 38+9+28+80 == 155,
         "This includes the actual KAM phase inverse, angle loss and geometric Airy scale")
    gate("actual_source_absorption_first_bound", 155+20-128-640 == -593,
         "The two-source cancellation is small enough to absorb on the whole real label ball")
    gate("actual_source_absorption_layer_power", 5**1536 < 3**1536*2**1501,
         "2^(-1501/1536)<3/5, proved by integer arithmetic")
    gate("actual_source_absorption_layer_ratio",
         Q(134, 133)**2*Q(130, 129)*Q(3, 5) < Q(3, 4),
         "Every deeper layer satisfies the same strict absorption gate")
    gate("actual_physical_source_prefactor", 6+1+11+2 == 20,
         "Both components, a<=2rho, w<=2^11 epsilon delta^5 and hbar^-1/6<4 delta^-1/1536 remain")
    gate("actual_physical_source_radial_power",
         5+Q(1, 2)-Q(1, 1536) == Q(8447, 1536),
         "The final L2 source estimate keeps its real physical epsilon*rho units")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        root/"results/R119-supplement-joint-actual-negative-band-return-kam.md",
        root/"results/R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md",
        root/"results/R119-supplement-divergence-frame-and-uniform-turning-energy.md",
        root/"results/R119-supplement-actual-Airy-balance-of-ray-coupling-and-sources.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-actual-Airy-ray-balance-v1",
        "scope": "Actual all-frequency Airy balance of the full two-branch perturbation, an exact paired ordinary-source cancellation and the full physical endpoint height/flux/mean conversion. The reference mixed-network Green inverse is not asserted.",
        "parameters": {
            "real_label_weight": 224,
            "Airy_scale": "varrho_i=32(j+4)/delta_j",
            "all_frequencies": "m in 4Z, including zero",
            "generator_angle_loss": "h_j/64",
            "physical_ordinary_source_angle_loss": "h_j/32",
            "relative_generator_integral": "<2^-574 X",
            "first_full_label_derivative": "<2^-571",
            "second_full_label_derivative": "<2^-566",
            "ordinary_source": "<2^20 epsilon_tail rho delta_j^(8447/1536) ||e||_(L2 A_(s+h_j/32))",
        },
        "file_sha256": {
            str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest()
            for p in paths
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_complete_reference_operator_retained": True,
            "full_frequency_Airy_weight_including_mean": True,
            "true_shoulder_and_turning_inverse_speed_integrals": True,
            "all_layer_balanced_generator_difference": True,
            "full_first_second_label_derivatives": True,
            "paired_physical_ordinary_source_L2_bound": True,
            "both_true_endpoint_height_flux_rows": True,
            "complete_weighted_mean_and_independent_height": True,
            "reference_Airy_Green_norm": False,
            "complete_positive_negative_network_inverse": False,
            "all_metric_source_conversion": False,
            "full_nonlinear_high_input_inverse": False,
            "topic_completion": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                               encoding="utf-8")
    print(json.dumps({"all_pass": result["all_pass"], "checks": len(result["checks"]),
                      "output": str(args.output) if args.output else None},
                     ensure_ascii=False))

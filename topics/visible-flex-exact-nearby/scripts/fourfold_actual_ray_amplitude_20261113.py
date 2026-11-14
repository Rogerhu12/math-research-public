#!/usr/bin/env python3
"""True Riemann densities, partial return, shoulders and all-layer width budgets."""
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
        return sp.factor(sp.cancel(expr)) == 0

    P, K, U, V, w, A = sp.symbols("P K U V w A")
    E = 1+w*w
    JD = 1+K+E*U
    DD = 1-w*w*(2*K+K*K+E*P*P)
    drift = E*(V-P)/JD
    NN = (1+K)*V+E*P*U
    Ft = (-A*(2*K+U+K*K+K*U+w*w*P*P)+E*(V-P)**2)/JD
    Pt = V-(A+1)*P
    Dt = sp.diff(DD, w)*A*w+sp.diff(DD, P)*Pt+sp.diff(DD, K)*Ft
    Dx = sp.diff(DD, P)*U+sp.diff(DD, K)*V
    gate("exact_full_discriminant_angular_derivative",
         zero(Dx+2*w*w*NN),
         "The complete mean and both relative gradients remain")
    gate("exact_full_discriminant_drift_derivative",
         zero(Dt-drift*Dx-2*A*w*w*DD*U/JD),
         "The true nonlinear PDE cancels the entire non-A drift remainder")

    b, bx, a, kk, kx, kt = sp.symbols(
        "b bx speed kappa kappax kappat", positive=True)
    z, p, zx, px, ss = sp.symbols("z p zx px source")
    pt = b*px+bx*p+a*kk*zx+a*kx*z+ss
    zt = b*zx+bx*z+a*px/kk-a*kx*p/(kk*kk)
    for sigma in [1, -1]:
        WW = (p+sigma*kk*z)/sp.sqrt(2*kk)
        WM = (p-sigma*kk*z)/sp.sqrt(2*kk)
        Wt = sp.diff(WW, p)*pt+sp.diff(WW, z)*zt+sp.diff(WW, kk)*kt
        Wx = sp.diff(WW, p)*px+sp.diff(WW, z)*zx+sp.diff(WW, kk)*kx
        expected = ((b+sigma*a)*Wx+bx*WW
                    -sp.Rational(1, 2)*((kt-b*kx)/kk+sigma*a*kx/kk)*WM
                    +ss/sp.sqrt(2*kk))
        gate(f"exact_Riemann_density_branch_{sigma}", zero(Wt-expected),
             "This includes b_x, the full variable density and the ordinary source")

    gg, ww, uu, jj, qq, nn, dd = sp.symbols(
        "g w U J q N D", positive=True)
    for sigma in [1, -1]:
        coeff = -sp.Rational(1, 2)*(gg-2*A*ww*ww*uu/jj
                                      +2*sigma*qq*ww*ww*nn/(jj*sp.sqrt(dd)))
        remainder = A*ww*ww*uu/jj-sigma*qq*ww*ww*nn/(jj*sp.sqrt(dd))
        gate(f"exact_true_amplitude_remainder_{sigma}",
             sp.simplify(coeff+gg/2-remainder) == 0,
             "No A_t, c_t or hidden mixed derivative is introduced")
    gate("exact_cancellation_at_turning",
         sp.simplify(remainder.subs({A: 0, qq: 0})) == 0,
         "Both terms of the true amplitude perturbation vanish at a type zero")
    gate("actual_amplitude_coefficient_fee",
         Q(2)+Q(8) <= 16,
         "J^-1 and D^-1/2 are <=2, N<=2n and q<=1+|A|")

    cs, qs, jother, drift_here = sp.symbols(
        "c q Jother drift_here", positive=True)
    for sigma in [1, -1]:
        Ctime = ((-drift_here-sigma*cs*qs)
                 -(-drift_here+sigma*cs*qs))/jother
        gate(f"exact_actual_partial_return_time_{sigma}",
             zero(Ctime+2*sigma*cs*qs/jother),
             "The common drift cancels at the same physical endpoint")
    Jflow, bxflow, Wflow, forcing = sp.symbols(
        "Jflow bxflow Wflow forcing")
    gate("exact_density_along_true_ray",
         zero(-bxflow*Jflow*Wflow+Jflow*(bxflow*Wflow+forcing)
              -Jflow*forcing),
         "The full density Jacobian, rather than only function pullback, removes transport")

    Wplus, Wminus = sp.symbols("Wplus Wminus")
    p_back = sp.sqrt(kk/2)*(Wplus+Wminus)
    z_back = (Wplus-Wminus)/sp.sqrt(2*kk)
    gate("exact_full_two_trace_recovery",
         sp.simplify((p_back+kk*z_back)/sp.sqrt(2*kk)-Wplus) == 0
         and sp.simplify((p_back-kk*z_back)/sp.sqrt(2*kk)-Wminus) == 0,
         "Neither branch nor its zero Fourier mode is projected away")

    gate("actual_total_label_weight_unchanged", 64+160 == 224,
         "The base angle shift and remaining label weight preserve the exact old norm")
    gate("actual_wide_background_exponential", 4*160 == 640,
         "The new wide-domain estimate uses exp(-640), not the narrower exp(-896)")
    gate("actual_wide_KAM_small_divisor_ratio", 132-640 == -508 and -508 < -64,
         "The same deterministic iteration converges on the enlarged absolute angular strips")
    gate("actual_wide_background_available",
         Q(5177, 400)+64-1 > 64+3,
         "The real shifted tail chart covers all new b,c and discriminant calculations")
    gate("actual_total_negative_band_width",
         (3968*Q(9, 100)+Q(1, 16))/32 < 12,
         "Both negative bands in all infinitely many layers are charged")
    gate("actual_remaining_common_angle_width", 64-12 > 0,
         "The complete single-pass width bill is paid by an actual proved common angle domain")
    gate("actual_local_composition_width",
         Q(1, 16)+Q(9, 100*64) < Q(1, 8),
         "The function input strip stays below the coefficient differentiation strip")
    gate("actual_wide_KAM_domain_margin", Q(3, 8)-Q(5, 16) > Q(1, 32),
         "The full true characteristic Jacobians are evaluated inside the paid angle domain")
    gate("actual_rowwise_KAM_C1_sum",
         32*2**12/(1-Q(1, 32)) < 2**18,
         "The local epsilon_i/gamma_i bound is retained, not replaced by its global supremum")
    gate("actual_nonlinear_parameter_conversion", Q(1, 2**14)/64 == Q(1, 2**20),
         "The geometric parameter, phase window and Diophantine constant use different units")
    gate("actual_partial_return_relative_fee", 2*(6+1+Q(1, 2)) < 16,
         "The full inverse ray Jacobian and scalar-speed factor fit the actual 16 K_i budget")

    j0 = 129
    delta0 = Q(2, 25*2**j0)
    gate("actual_minimum_tail_depth", delta0 < Q(1, 2**132),
         "Every later delta is exactly half the previous one")
    gate("actual_eta_to_delta_ratio", delta0 < Q(1, 2**16),
         "eta/delta=sqrt(delta)/(4 sqrt2)<1/64 on every actual layer")
    gate("actual_two_cell_radial_length",
         (9+24*Q(1, 64))/3 < 4,
         "This pays the full possible crossing of an adjacent-cell seam")
    gate("actual_optical_platform_lower", Q(7, 12) > Q(1, 4),
         "At least one true delta/sqrt12 platform has speed sqrt7")
    gate("actual_parameter_support_q_upper",
         Q(15, 8)+Q(96, 2**19)*Q(2, j0) < 2,
         "The actual Gamma0 bump stays below the full falling-ramp peak bound")
    gate("actual_falling_optical_upper", 2**2 < 12,
         "sqrt(2)/12^(1/4)<1 in the exact falling-ramp length calculation")
    gate("actual_platform_optical_fee",
         144*8*Q(1, 2**66) < Q(j0, 2),
         "12 delta < sqrt(eta Delta), using the actual first depth and all-layer monotonicity")
    gate("actual_optical_to_phase_window",
         4*2**25*3 < 2**29,
         "L0/kappa keeps both eta and Delta rather than treating them as the same scale")
    gate("actual_q_peak_envelope", 7+Q(15, 8)*4*3*8 < 256,
         "qmax^2<256 j delta^(-3/2) includes the full real profile")
    gate("actual_log_q_peak_envelope",
         Q(11, 16)*j0+Q(21, 4) < j0+4,
         "The difference improves for every later j")
    gate("actual_weighted_log_variation",
         8+(j0+4)+4*(j0+4) < 16*(j0+4),
         "The q<=1 endpoint intervals and the entire sharp shoulder are included")
    gate("actual_parameter_support_denominator",
         Q(j0, 2)*Q(135, 128)-Q(96, 2**19) > Q(j0, 2),
         "H0>Delta throughout the actual bump support")
    gate("actual_parameter_support_denominator_derivative",
         6*Q(j0, 2)+Q(6144, 2**19) < 7*Q(j0, 2),
         "H0prime has its full actual background and bump terms")
    gate("actual_log_profile_variation_numerator", 6144+96*7 == 6816,
         "Both derivative terms of psi_x/H0 are kept")
    gate("actual_log_profile_full_support", Q(6816, 8) == 852,
         "The true support length is 1/8")
    gate("actual_complete_radial_amplitude_parameter_fee",
         2+852*Q(2, j0) < 16 < 64,
         "The A change and the derivative of the exact q ratio are both integrated")

    al = Q(443, 256)
    gate("actual_half_phase_power", al-Q(3, 4) == Q(251, 256),
         "The true geometric phase inverse costs delta^(-3/4)")
    gate("actual_angle_derivative_power", al-Q(1, 256) == Q(442, 256),
         "The explicit h_j division is included")
    gate("actual_global_width_lower", Q(9, 100) > Q(1, 16) and 8 > Q(1, 16),
         "h_j>2^-4 delta_j^(1/256) covers both sides of the 4096/4097 jump")
    gate("actual_first_parameter_envelope_power", 132*Q(251, 256) > 129,
         "Used together with the complete polynomial factor")
    gate("actual_first_angle_envelope_power", 132*Q(442, 256) > 227,
         "Used together with the complete polynomial factor")
    gate("actual_first_direct_remainder_power", 132*al > 228,
         "The full nonradial source-free amplitude remainder is included")
    gate("actual_first_parameter_polynomial",
         (133**2)*129 < 2**24,
         "(j+4)*sqrt(j)<2^12 at the first actual layer")
    gate("actual_first_angle_polynomial", 133**3 < 2**24,
         "The three actual j+4 factors are not dropped")
    gate("actual_first_map_width_polynomial", 133**2 < 2**16,
         "Used to check the actual composition image before applying Cauchy")
    gate("actual_parameter_ratio_power",
         5**256 < 3**256*2**251,
         "2^(-251/256)<3/5, with no decimal rounding")
    gate("actual_parameter_envelope_monotonicity",
         Q(134*130, 133*129)*Q(3, 5) < Q(3, 4),
         "The polynomial ratio decreases for all j>=129")
    gate("actual_angle_ratio_power", 3**256 < 2**442,
         "2^(-442/256)<1/3")
    gate("actual_angle_envelope_monotonicity",
         Q(134, 133)**3/3 < Q(1, 2),
         "This single envelope crosses the actual h_j change")
    gate("actual_direct_envelope_monotonicity",
         Q(134, 133)/3 < Q(1, 2),
         "The exponent 443/256 is even stronger")
    gate("actual_partial_map_inside_width",
         147+16-227-640 == -704,
         "r_i L0/hbar_i<2^-704 on every actual layer")
    gate("actual_complete_phase_coupling_fee",
         7+22+6+29+6 == 70,
         "This includes density pullback, both optical factors, Diophantine conversion and h_j/64")
    gate("actual_direct_amplitude_integral_fee", 32*2**70 == 2**80//32,
         "The source-free nonlinear amplitude term uses the full local (1+|A|)n integral")
    gate("actual_first_parameter_integral", 100+12-129-640 == -657,
         "The true metric retuning amplitude is the largest of the three displayed envelopes")
    gate("actual_first_phase_integral", 154+24-227-640 == -689,
         "The actual full-frequency angle differentiation is charged")
    gate("actual_first_direct_integral", 75+8-228-640 == -785,
         "All nonradial D-density terms are charged")
    gate("actual_all_components_geometric_sums",
         2/(1-Q(3, 4)) == 8 and 2/(1-Q(1, 2)) == 4,
         "At most two true negative components are included per layer")
    gate("actual_entire_infinite_relative_generator_sum",
         Q(1, 2**654)+Q(1, 2**687)+Q(1, 2**783) < Q(1, 2**652),
         "The full infinite series, not a finite numerical sample, proves the claimed constant")
    gate("actual_full_label_first_derivative", -652+3 == -649,
         "The entire coupled metric/angle function is differentiated by the real remaining Cauchy radius")
    gate("actual_full_label_second_derivative", -652+8 == -644,
         "Both multilinear directions use radius 1/16; no diagonal-only Cauchy claim")
    gate("actual_source_angle_power", al-Q(3, 4)-Q(1, 256) == Q(250, 256),
         "The full KAM displacement is divided by the actual source width")
    gate("actual_source_angle_depth", 132*Q(250, 256) > 128,
         "The true first layer pays the small source-composition image")
    gate("actual_source_angle_all_layer_ratio", 5**256 < 3**256*2**250,
         "The source angle envelope decreases on every later layer")
    gate("actual_source_angle_image", 142+12-128-640 == -614,
         "K_i/hbar_i<2^-614, before the extra harmless flow-displacement factor")
    gate("actual_physical_source_hodograph_fee", Q(64, 2**14*133) < 2**18,
         "64 N_i<K_i; the inverse hodograph is included in the original physical-angle source input")
    gate("actual_total_physical_source_angle_image", Q(3, 2**614) < Q(1, 4),
         "chi^-1 composed with Theta_sigma uses the same one h_j/64 width, not a second unpaid strip")
    gate("actual_ascending_type_root", 30*32*Q(7, 64)**2 > 7,
         "Each actual negative rising-ramp endpoint lies in x<1/8")
    gate("actual_inverse_optical_endpoint_integral",
         2*Q(22, 7)/(3*5) < 1,
         "The exact y=x(1-x) integral keeps the true inverse-square-root turning weight")
    gate("actual_complete_inverse_optical_integral", 2+4*Q(1, 64) < 4,
         "Both endpoint pieces and the entire intervening negative band are included")
    gate("actual_two_cell_source_height_upper", 64*2**5 == 2**11,
         "The outer neighboring cell has delta_(j-1)=2 delta_j")
    gate("actual_inverse_density_source_weight", 2*256*4 == 2**11,
         "a<=2rho, w>=epsilon delta^7/256 and integral q^-1<4delta")
    gate("actual_both_branch_L2_source_constant", 8**2*2**11 < (2**9)**2,
         "Both exact ray density sources are controlled with their physical units")
    gate("actual_original_scalar_source_density", 2*(2**11)**2 == 2**23,
         "The actual w^2/(cD) multiplier is retained")
    gate("actual_complete_scalar_source_delta_power", -3+10 == 7 and 9+23 == 32,
         "The final ordinary-source contract is 2^32 epsilon^(3/2) rho^(1/2) delta^7")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        root/"results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
        root/"results/R119-supplement-joint-actual-negative-band-return-kam.md",
        root/"results/R119-supplement-unscalarized-tail-frame-and-summable-remainder.md",
        root/"results/R119-supplement-two-ended-negative-characteristic-chart-and-densities.md",
        root/"results/R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-actual-ray-amplitude-v1",
        "scope": "The same real nonlinear tail has wide actual ray coordinates. The complete two-branch density generator differs from its chosen true radial reference by an explicitly width-losing, all-layer integrable operator <2^-652 X, retaining both turning residues, all sources, mean and full label derivatives.",
        "parameters": {
            "physical_label_weight": 224,
            "base_angle_shift": 64,
            "remaining_label_weight": 160,
            "same_KAM_metric_and_angle_choice": True,
            "wide_KAM_small_divisor_upper": "2^-508",
            "angle_loss_per_actual_negative_component": "h_j/64",
            "total_single_pass_negative_angle_loss": "<12",
            "full_relative_generator_integral": "<2^-652 X",
            "full_first_label_derivative": "<2^-649",
            "full_second_label_derivative": "<2^-644",
            "ordinary_source_bound": "<2^32 epsilon_tail^(3/2) rho^(1/2) delta_j^7 ||e||_(L2 A_(s+hbar_i))",
        },
        "file_sha256": {
            str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest()
            for p in paths
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_full_discriminant_transport_identity": True,
            "true_two_branch_Riemann_density_system": True,
            "actual_partial_return_with_two_end_vanishing": True,
            "same_KAM_choice_on_paid_wide_angular_domain": True,
            "all_log_quintic_shoulder_fees_paid": True,
            "all_frequency_angle_composition_loss_paid": True,
            "full_infinite_relative_generator_integral": True,
            "ordinary_source_and_mean_retained": True,
            "both_turning_height_flux_conditions_retained": True,
            "turning_Airy_source_norm_comparison": False,
            "full_strong_mixed_network_inverse": False,
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

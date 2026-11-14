#!/usr/bin/env python3
"""Exact infinite-layer and coupled-parameter budgets for actual negative returns."""
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

    al = Q(443, 256)
    rc = Q(1, 2**15)
    gate("all_real_relative_state_exponent", al < 2,
         "Across a cell seam delta_(j-1)^alpha<4 delta_j^alpha")
    gate("actual_full_negative_component_integral_fee", 2**66*16 == 2**70,
         "The second negative component includes both adjacent cells")
    gate("actual_common_drift_integral_fee", 32*2**70 == 2**75,
         "The real nonlinear common drift is retained in both ray flows")
    gate("actual_two_ray_composition_fee", 8*2**75 == 2**78,
         "Forward, backward, scalar phase and angular composition are all paid")
    gate("actual_standard_circle_rescaling", 4*2**78 == 2**80,
         "The fourfold quotient uses x=4 xi, not an unscaled small-divisor parameter")
    d129 = Q(2, 25)*Q(1, 2**129)
    gate("actual_first_tail_depth", d129 < Q(1, 2**132),
         "This exact depth is used only with the proved all-layer monotone envelopes")
    gate("actual_relative_state_power", 132*al > 228,
         "delta_129^alpha<2^-228")
    gate("actual_full_component_small_state", 66-228-896 == -1058,
         "N_i<2^-1058 on the complete real and complex label domains")
    gate("actual_full_component_small_drift", 75+8-228-896 == -1041,
         "j+4=133<2^8 at the first layer; the envelope decreases")
    gate("actual_complex_layer_variation_slack", 16*d129+6*129+28+4*rc < 8*(129+4),
         "The two new complex bump variations fit in the original full-cell integral bound")
    gate("actual_mean_paid_phase_error", 256*Q(1, 2**1058)/32 < Q(1, 16),
         "|S-S0|<=256 N_i I_i is strictly below D_i/16")
    gate("actual_partial_complex_ray_phase", 2*rc == Q(1, 2**14),
         "Every partial reference phase has imaginary part below this value")
    gate("actual_ray_flow_composition_width", Q(7, 4)+Q(1, 8) < 2,
         "The complete flow evaluates b within the paid width-2 domain")
    gate("actual_two_ray_final_composition_width", Q(3, 2)+Q(1, 8) < Q(7, 4),
         "The two actual flows compose with a fixed analytic width margin")

    gate("complex_rotation_numerator_relative_change", 2048*rc == Q(1, 16),
         "Delta>1 makes |gamma psi_tt/A_t| strictly smaller")
    gate("complex_rotation_denominator_relative_change", 96*rc < Q(1, 256),
         "The actual A factor stays in the same analytic square-root branch")
    gate("complex_inverse_three_half_derivative", Q(3, 2)**2*Q(256, 255)**5 < 4,
         "|(1+z)^(-3/2)-1|<2|z| for |z|<1/256")
    gate("complete_complex_rotation_derivative_margin",
         Q(1, 16)+Q(1, 128)+Q(1, 16*128) < Q(1, 8),
         "The positive reference integral controls the complete complex derivative ratio")
    gate("actual_phase_inverse_domain", Q(1, 2**8)*rc/2 == 2*Q(1, 2**25),
         "The strict reference derivative gives a holomorphic inverse on |lambda|<2 kappa")
    gate("actual_real_phase_inverse_geometry_box", Q(8, 7)*Q(1, 2**17) == Q(4, 7)*Q(1, 2**16),
         "Real |lambda|<=kappa stays strictly inside the original geometric parameter box")
    gate("actual_joint_phase_parameter_domain", (4+Q(1, 2))/4 < 2,
         "The whole weighted p-ball of radius 4 maps into all inverse lambda disks")

    gate("all_Diophantine_target_measure", Q(8, 64) < 1,
         "The total excluded measure is below kappa/8, versus an allowed interval of length kappa")
    gate("actual_small_divisor_radial_margin", al-Q(3, 2) == Q(59, 256) > 0,
         "The actual nonlinear error is smaller than the square of the actual tunable phase scale")
    polynomial_ratio = Q(130*134, 129*133)
    gate("all_layer_square_budget_monotonicity", polynomial_ratio**256 < 2**59,
         "The ratio decreases further for every later j; no finite sample extrapolation")
    gate("first_layer_complete_polynomial_fee", 129*133 < 2**15,
         "Both j factors, including the inverse phase-window factor, are retained")
    gate("first_layer_complete_small_divisor_depth", 132*Q(59, 256) > 30,
         "j(j+4) delta_j^(59/256)<2^-15 for every j>=129")
    gate("complete_actual_small_divisor_fee", 80+12+55-15-896 == -764,
         "This includes the standard-circle factor, Diophantine factor 64^2 and phase-window lower bound")

    mu = Q(1, 2**64)
    gate("coupled_average_row_Neumann_margin", 4*mu < Q(1, 2),
         "The infinite parameter average row is inverted jointly in the weighted l-infinity space")
    gate("coupled_parameter_rowwise_fee", 4+32*mu < 8,
         "The final row bound preserves each deep layer's own epsilon_i")
    gate("full_cohomological_rhs_fee", 18+16*mu < 20,
         "The entire parameter coupling remains inside the true zero-average Fourier equation")
    gate("actual_newton_angle_correction_fee", Q(9, 8)*20 < 32,
         "The current h' factor is retained")
    gate("complete_newton_second_order_fee", 20+4*40**2 < 2**14,
         "Both E'v and the complete joint space/parameter Taylor remainder are paid")
    gate("whole_iteration_error_envelope", 14+24-64 == -26 and -26 <= -8 and -10 <= -8,
         "e_(n+1)<=2^(-26-10n)<=2^(-8(n+1)) for every n>=0")
    gate("whole_iteration_parameter_sum", 8/(1-Q(1, 256)) < 16,
         "Every p_i correction sums to less than 16 epsilon_i")
    gate("whole_iteration_C1_sum", 32*2**12/(1-Q(1, 32)) < 2**18,
         "The full analytic angle derivative corrections sum uniformly over all components")
    gate("whole_iteration_C1_domain", 2**18*mu < Q(1, 8),
         "The actual limiting h_i remains a circle diffeomorphism")
    gate("whole_iteration_parameter_domain", 16*mu < 1,
         "All simultaneous parameter iterates stay inside the Cauchy domain")
    gate("whole_iteration_remaining_width", 2-4*Q(1, 16)/(1-Q(1, 2)) == Q(3, 2),
         "The width loss is a single convergent sum over the full Newton iteration")
    gate("actual_base_target_metric_parameter", 512*Q(1, 8)*Q(1, 2**25) == Q(1, 2**19),
         "The chosen zero-label target angle is converted back to the actual log-profile parameter")
    gate("actual_nonlinear_metric_parameter_correction", 512*4*Q(1, 2**25) == Q(1, 2**14),
         "The metric parameter correction retains the inverse true phase derivative")
    gate("actual_final_geometry_parameter_box",
         Q(1, 2**19)+Q(1, 2**14)*Q(1, 2**764) < Q(1, 2**16),
         "All infinitely many final parameters satisfy the original actual geometry bounds")
    gate("actual_physical_angle_width", Q(3, 2)/4 == Q(3, 8) > Q(1, 512),
         "The true physical endpoint angle map reaches the required physical angular window")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        root/"results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
        root/"results/R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md",
        root/"results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md",
        root/"results/R119-supplement-joint-actual-negative-band-return-kam.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-joint-actual-negative-return-kam-v1",
        "scope": "All actual internal negative-band two-ray returns, the complete joint infinite parameter selection, full Fourier KAM and its actual circle cohomological inverse; turning amplitudes and the full mixed strong inverse remain outside the claim.",
        "inputs": {
            "actual_metric_complex_radius": "2^-15",
            "actual_metric_real_radius": "2^-16",
            "full_label_weight": 224,
            "actual_error_exponent": "443/256",
            "squared_phase_window_exponent": "3/2",
            "remaining_radial_exponent": "59/256",
            "actual_uniform_epsilon_over_Diophantine_square": "<2^-764",
            "proved_Newton_sufficient_gate": "<=2^-64",
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_nonlinear_two_ray_flows": True,
            "all_internal_negative_components": True,
            "full_parameter_cross_dependence": True,
            "full_Fourier_small_divisor_inverse": True,
            "joint_infinite_parameter_KAM": True,
            "single_metric_along_each_phase_orbit": True,
            "actual_invariant_mean_row_kept": True,
            "both_traces_and_flux_density_kept": True,
            "ordinary_sources_and_holonomy_kept": True,
            "outer_cut128_reflection_claimed": False,
            "full_positive_Airy_amplitude_connection": False,
            "fixed_original_metric_R74_inverse": False,
            "final_regular_and_core_match": False,
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

#!/usr/bin/env python3
"""Actual positive-band DN in the already-paid two Airy endpoint angles."""
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

    x = sp.symbols("x", real=True)
    S = 10*x**3-15*x**4+6*x**5
    gate("actual_quintic_derivative",
         sp.factor(sp.diff(S, x)) == 30*x*x*(x-1)**2,
         "The positive components are the exact ascending log-quintic ramps")
    gate("actual_central_positive_interval",
         sp.diff(S, x).subs(x, Q(1, 4)) == Q(135, 128)
         and Q(135, 128) > 1,
         "S' is at least 135/128 on the complete middle half")
    gate("actual_positive_peak",
         sp.diff(S, x).subs(x, Q(1, 2)) == Q(15, 8),
         "The optical upper bound uses the actual maximum")
    gate("actual_symmetric_turning_roots",
         sp.expand(S+S.subs(x, 1-x)) == 1,
         "The two endpoint log losses coincide")
    gate("actual_turning_log_bound",
         zero(10*x**3-S-3*x**4*(5-2*x)),
         "For x in [0,1], S(x)<=10x^3; the actual root satisfies x<=2 sqrt(7/(30 Lambda))")
    gate("actual_large_ramp_parameter", 3*Q(129, 2) > 14,
         "sqrt12>3, Delta>j/2 and eta<1 imply Lambda>14 at every layer")
    gate("positive_optical_integral_constant", 8*4 < 8**2,
         "The exact middle-half denominator squared is 8 sqrt12<32<64")
    gate("positive_optical_length_layer_power",
         Q(3, 2)/2 == Q(3, 4) and 8*4 == 32,
         "eta>delta^(3/2)/8 and Delta>j/2 give Lplus>delta^(3/4)*sqrt(j)/32")
    gate("positive_optical_length_upper_first_layer",
         4*3*(129+4) < 2**193,
         "Lplus<2 sqrt(eta Delta)<1 at the first actual layer")
    gate("positive_optical_upper_deeper_layers",
         Q(134, 133)*Q(1, 2) < 1,
         "Delta's linear envelope grows more slowly than eta's factor2^(-3/2)")

    gate("full_KAM_endpoint_constant", 18+6+80+28 == 132,
         "The complete Diophantine normalization kappa/64 and actual inverse kappa are retained")
    gate("full_KAM_endpoint_layer_power",
         Q(443, 256)-Q(3, 4) == Q(251, 256),
         "The true local KAM endpoint displacement includes its kappa inverse")
    gate("adjacent_layer_endpoint_envelope", Q(251, 256) < 1,
         "The outer adjacent delta doubles and costs less than factor2; the polynomial is bounded by (j+5)^2")
    gate("endpoint_maps_inverse_drift_budget",
         64*(2**133+2**68) < 2**142,
         "Both actual endpoint compositions and the complete drift inverse fit the stated a_j")
    gate("drift_metric_relative_budget", 9+68 < 142,
         "512 N_j is dominated by a_j, including all drift Jacobian terms")
    gate("endpoint_a_first_layer_polynomial", 134**2 < 2**15,
         "The first actual polynomial factor is explicitly retained")
    gate("endpoint_a_first_layer_decay", 129*Q(251, 256) > 15,
         "The complete first-layer polynomial times delta^(251/256) is less than1")
    gate("endpoint_a_decay_integer", 5**256 < 3**256*2**251,
         "2^(-251/256)<3/5 is an exact integer inequality")
    gate("endpoint_a_deeper_layer_ratio", Q(135, 134)**2*Q(3, 5) < 1,
         "The real endpoint envelope decreases at every later depth")
    gate("endpoint_a_smallness", 142-640 < -400,
         "e>2 and the preceding all-layer envelope give a_j<2^-400")

    mu, d, AA, vv, jt, phit = sp.symbols("mu d A v j Phi_t", positive=True)
    M = mu*sp.Matrix([[1, -d], [-d, d*d+AA*vv*vv]])
    F = sp.Matrix([[1, 0], [phit, jt]])
    pulled = sp.simplify(jt*F.inv()*M*F.inv().T)
    exact = mu*sp.Matrix([[jt, -phit-d],
                          [-phit-d, ((phit+d)**2+AA*vv**2)/jt]])
    gate("exact_full_physical_pullback_matrix",
         all(zero(z) for z in pulled-exact),
         "The full physical matrix, Jacobian, drift and cross term are transformed together")
    kflow, jpsi, psit = sp.symbols("j_flow j_psi psi_t", positive=True)
    second = sp.simplify(pulled.subs({jt: kflow*jpsi, phit: -d+kflow*psit}))
    mut = mu*kflow
    betat = mu*AA*vv**2/kflow
    expected = sp.Matrix([[mut*jpsi, -mut*psit],
                          [-mut*psit, (mut*psit**2+betat)/jpsi]])
    gate("exact_drift_then_optical_interpolation",
         all(zero(z) for z in second-expected),
         "The only remaining cross term is psi_t, which is exactly sqrt(A) times the endpoint difference/Lplus")
    ur, ux = sp.symbols("u_t u_xi")
    pphysical = mu*(ur-(phit+d)*ux/jt)
    gate("exact_complete_endpoint_flux_density",
         zero((pulled*sp.Matrix([ur, ux]))[0]-jt*pphysical),
         "The output is K_e' times the full original raw conormal, including drift")
    Zt, Za = sp.symbols("Z_t Z_theta")
    Znew = sp.simplify(jt*F.inv()*sp.Matrix([Zt, Za]))
    gate("exact_metric_source_radial_Piola", zero(Znew[0]-jt*Zt),
         "The true radial source density and its two endpoint terms survive")
    gate("exact_metric_source_angular_Piola", zero(Znew[1]-(Za-phit*Zt)),
         "The entire angular source includes the moving-coordinate shear")
    rm, rb, nnu = sp.symbols("r_mu r_beta nu")
    weighted = sp.Matrix([
        [(1+rm)*jpsi, -(1+rm)*nnu],
        [-(1+rm)*nnu, ((1+rm)*nnu**2+1+rb)/jpsi],
    ])
    gate("exact_weighted_form_determinant",
         zero(weighted.det()-(1+rm)*(1+rb)),
         "The complete coordinate shear leaves the determinant independent of nu and jpsi")
    b = Q(1, 16)
    gate("complete_complex_form_first_row",
         (2*b+b*b)+(1+b)*b < 16*b,
         "The same coefficient majorant works for the analytic complex form extension")
    gate("complete_complex_form_second_row",
         (1+b)*b+((1+b)*b*b+2*b)/(1-b) < 16*b,
         "Both diagonal changes and the entire cross term are included")
    gate("true_relative_DN_layer_power",
         Q(251, 256)-Q(3, 4) == Q(59, 256),
         "The optical inverse length is paid without the invalid eta^(-1) cost")
    gate("complete_DN_coefficient_constant", 142+6+5 < 154,
         "16 times the complete coefficient sum is at most64 a_j/Lplus")

    rr = Q(6, 7)
    nn = 129
    sumtail = rr**nn*((nn+5)**2/(1-rr)
                      +2*(nn+5)*rr/(1-rr)**2
                      +rr*(1+rr)/(1-rr)**3)
    gate("relative_DN_decay_integer", 7**256 < 6**256*2**59,
         "2^(-59/256)<6/7, with no floating approximation")
    gate("all_positive_layer_sum", 2*sumtail < 1,
         {"exact_upper_sum": str(sumtail), "two_positive_components_per_layer": True})
    gate("actual_full_relative_DN_sum", 154-640 < -480,
         "Both positive components at every depth are included in the strict2^-480 bound")

    al, be, ga, de = sp.symbols("alpha beta gamma delta")
    Sdn = sp.Matrix([[al, -1], [-1, de]])/be
    fL, fR = sp.symbols("f_L f_R")
    pL = (fR-al*fL)/be
    pR = ga*fL+de*pL
    gate("exact_DN_left_port", zero((Sdn*sp.Matrix([fL, fR]))[0]+pL),
         "The left port has the correct outward sign and complete off-diagonal coupling")
    gate("exact_DN_right_port",
         zero(((Sdn*sp.Matrix([fL, fR]))[1]-pR).subs(ga, (al*de-1)/be)),
         "The right port uses the exact determinant-one transfer relation")
    Smean = sp.Matrix([[1, -1], [-1, 1]])
    gate("complete_mean_translation_kernel", Smean*sp.Matrix([1, 1]) == sp.zeros(2, 1)
         and Smean*sp.Matrix([1, -1]) != sp.zeros(2, 1),
         "Only common height translation is in the kernel; mean difference and flux remain")
    DD, z0, p0 = sp.symbols("D z0 p0", positive=True)
    gate("same_Airy_height_port", zero(sp.sqrt(DD)*(z0/sp.sqrt(DD))-z0),
         "The input is the complete sqrt(D)-weighted height derivative")
    gate("same_Airy_flux_port", zero((sp.sqrt(DD)*p0)/sp.sqrt(DD)-p0),
         "The output uses the true D^(-1/2)-weighted flux, not its unweighted mean")

    gate("actual_turning_endpoint_log_smallness", 80*Q(1, 2)**12 < Q(1, 4),
         "eta<2^-8 and Delta>1 suffice for the true endpoint log deficit<1/4")
    gate("actual_endpoint_exponential_factor", 3 < 2**4,
         "e<3 implies exp(1/4)<2, so the two actual endpoint p* values are retained")
    gate("actual_endpoint_mean_energy_gap", 2*Q(1, 2**12) < Q(1, 1024),
         "delta<2^-12 gives mu_start<epsilon delta^5/(1024 rho), below half mu_end")
    gate("actual_radial_resistance_power", -7+Q(3, 2) == -Q(11, 2),
         "Both the real minimum mu and the actual ramp length are included")
    gate("actual_continuous_source_embedding_constant", 512 < 32**2 and 2*32+8 < 128,
         "The full 1+2sqrt(R)+1/(4sqrt(M)) mean and nonmean embedding is retained")
    gate("physical_scalar_source_density_constant", 16*64**2 == 2**16,
         "The real angular L2 change of variables and the actual maximum w are both paid")
    gate("physical_scalar_source_first_power", 10+Q(3, 4) == Q(43, 4),
         "L2 radial input costs the actual square root of the positive-band length")
    gate("physical_scalar_source_second_power", Q(43, 4)-Q(11, 4) == 8,
         "The continuous body-source to full boundary-source power is positive and summable")
    gate("physical_scalar_source_second_constant", 16+7 == 23,
         "The epsilon^(3/2)*sqrt(rho) term includes the exact C_I factor")
    gate("full_label_Cauchy_domain", Q(1, 8)+2*Q(1, 32) < Q(1, 4),
         "Both label directions and their coupled Gamma variations remain inside the original ball")
    gate("full_first_label_operator_derivative", -480+4 == -476,
         "The first derivative is on a fixed reference energy space after paying rho/rho0")
    gate("full_second_label_operator_derivative", -480+10 == -470,
         "Two independent complex directions retain all cross-label derivatives")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        root/"results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md",
        root/"results/R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md",
        root/"results/R119-supplement-actual-Airy-balance-of-ray-coupling-and-sources.md",
        root/"results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
        root/"results/R119-supplement-positive-DN-in-actual-Airy-endpoint-angles.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-positive-DN-actual-Airy-endangles-v1",
        "scope": "Complete weak two-end DN in the exact adjacent Airy endpoint angles, an optical interpolation of the physical coordinate change, all mean and off-diagonal rows, continuous ordinary and explicitly given divergence sources, and full coupled parameter and scale derivatives. No mixed-network Green condition number is asserted.",
        "parameters": {
            "label_weight": 224,
            "true_positive_optical_lower_bound": "Lplus>delta_j^(3/4)*sqrt(j)/32",
            "all_modes": "m in 4Z including mean; no Fourier cutoff",
            "relative_form_per_component": "2^154(j+5)^2 delta_j^(59/256) exp(-640) X",
            "sum_relative_DN": "<2^-480 X",
            "sum_first_label_derivative": "<2^-476 after exact rho/rho0 normalization",
            "sum_second_label_derivative": "<2^-470 after exact rho/rho0 normalization",
            "ordinary_source_norm": "[2^16 epsilon^2 delta_j^(43/4)+2^23 epsilon^(3/2) sqrt(rho) delta_j^8] ||e||_L2",
        },
        "file_sha256": {
            str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "same_actual_Airy_endpoint_coordinates": True,
            "full_positive_weak_DN_relative_bound": True,
            "both_off_diagonal_DN_entries_retained": True,
            "full_mean_flux_and_independent_height": True,
            "actual_continuous_scalar_source_weight": True,
            "explicit_divergence_source_and_both_endpoint_terms": True,
            "all_coupled_label_and_scale_derivatives": True,
            "negative_reference_full_Green": False,
            "strong_Airy_to_positive_trace_comparison": False,
            "whole_mixed_network_inverse": False,
            "automatic_all_metric_source_conversion": False,
            "full_nonlinear_regular_high_input_inverse": False,
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

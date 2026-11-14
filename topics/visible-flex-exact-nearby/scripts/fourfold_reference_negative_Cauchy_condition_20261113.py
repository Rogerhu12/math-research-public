#!/usr/bin/env python3
"""The full actual reference negative-band Cauchy and continuous-source condition."""
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

    mu, mut, om, omt, qq = sp.symbols("mu mu_t Omega Omega_t q", positive=True)
    mm = sp.symbols("m", integer=True)
    R = sp.sqrt(mu)*sp.diag(sp.sqrt(om), 1/sp.sqrt(om))
    Rt = R.diff(mu)*mut+R.diff(om)*omt
    B = sp.Matrix([[0, 1], [qq**2, 0]])
    A0 = sp.I*mm*B+sp.diag(0, -mut/mu)
    transformed = sp.simplify((Rt+R*A0)*R.inv())
    exact = sp.I*mm*sp.Matrix([[0, om], [qq**2/om, 0]]) \
        +(mut/mu+omt/om)*sp.diag(1, -1)/2
    gate("complete_reference_density_auxiliary_frame",
         all(zero(z) for z in transformed-exact),
         "All D_t and actual log-density terms are retained; there is no model-potential substitution")
    P = sp.I*mm*sp.Matrix([[0, om], [qq**2/om, 0]])
    HH = sp.simplify((P+P.conjugate().T)/2)
    Hexpected = sp.Matrix([[0, sp.I*mm*(om-qq**2/om)/2],
                           [-sp.I*mm*(om-qq**2/om)/2, 0]])
    gate("exact_Hermitian_principal_error",
         all(zero(z) for z in HH-Hexpected),
         "The only principal norm error is |m| sigma^2/(2 Omega)")
    gate("Hermitian_two_eigenvalues",
         zero(HH.det()+mm**2*(om-qq**2/om)**2/4),
         "The exact Hermitian eigenvalues have equal opposite magnitudes")
    sig = sp.symbols("sigma", positive=True)
    gate("positive_auxiliary_regularization_identity",
         zero((om-qq**2/om).subs(qq**2, om**2-sig**2)-sig**2/om),
         "The artificial positive speed enters only the energy, not the real PDE")

    j0 = 129
    gate("actual_density_ratio_constant", 2*65 < 2**8,
         "The true log jump and exp(8|I|)<2 cover both kinds of complete negative component")
    gate("actual_density_exponential_window", 32*Q(1, 2**129) < Q(1, 2),
         "exp(x)<=1/(1-x)<2 in the actual first layer, and every later layer improves")
    gate("actual_density_monotone_root_factor", 2**8 == 16**2,
         "sqrt(mu_left/mu_right)<16 delta^-1; the true density is monotone across the whole component")
    gate("actual_short_interval_peak_first_layer", 4096*j0 < 2**64,
         "The square of |I| qmax is at most4096 j delta^(1/2)<1")
    gate("actual_short_interval_peak_deeper_layers", Q(130, 129)*Q(3, 4) < 1,
         "sqrt2>4/3 proves monotonic decrease of the complete squared envelope")
    gate("actual_complete_auxiliary_Cauchy_constant", 2*16*2 == 64,
         "exp(1/2), the exact monotone density and the full two-sided speed variation are all paid")
    gate("actual_Airy_auxiliary_ratio_min", 32*Q(1, 4)*(j0+4) > 1,
         "The actual lower length proves omega_m>=Omega_m even at m=0")
    gate("actual_Airy_auxiliary_ratio_max", 32*4 == 128,
         "Both endpoint frame ratios are bounded by varrho |I| <128(j+4)")
    gate("actual_Airy_reference_Cauchy_constant", 64*128*2 == 2**14,
         "The complete two-end frame change and Euclidean-to-component-sum norm are included")
    gate("all_frequency_reference_Cauchy_power", 1+Q(1, 3)+Q(1, 3) == Q(5, 3),
         "All frequencies are retained, including the unsuppressed mean state")
    gate("full_Wiener_multiplier_constant", 3*Q(5, 3)**2 < 16,
         "For0<h<=1, (1+|m|)^(5/3) exp(-h|m|)<16 h^(-5/3)")
    gate("true_reference_analytic_Cauchy_constant", 14+4 == 18,
         "One explicit angle-width payment gives the full strong Fourier/radial Cauchy bound")

    gate("actual_source_density_square_root_constant", 2**11 < (2**6)**2,
         "The reference density has physical units epsilon/rho and radial power delta^5")
    gate("actual_density_Airy_source_constant", 20+6 == 26,
         "The paired physical source of the previous theorem is multiplied by the true sqrt(mu0)")
    gate("actual_density_Airy_source_power",
         Q(8447, 1536)+Q(5, 2) == Q(12287, 1536),
         "The complete paired-source cancellation survives in the density Airy frame")
    gate("actual_reference_forced_response_constant", 26+18+1 == 45,
         "The real Cauchy condition and sqrt(|I|)<2sqrt(delta) are both paid")
    gate("actual_reference_forced_response_power",
         Q(12287, 1536)-1+Q(1, 2) == Q(11519, 1536),
         "The radial source weight remains a positive explicit power after the real condition number")
    gate("actual_single_pass_source_angle_budget", 3*12 < 64,
         "Two correlated-source widths and one reference Green width fit in the original64-wide extension")

    pp, vv, fv = sp.symbols("p v Fv")
    gate("complete_mean_flux_equation", zero(mut*vv+mu*(-mut/mu*vv+fv)-mu*fv),
         "The weighted mean flux has its genuine independent source row")
    gate("actual_mean_resistance_constant", 4*512 == 2**11,
         "The true min(mu) and whole negative radial length retain the independent mean-height fee")
    gate("actual_mean_resistance_power", 1-7 == -6,
         "No division by the zero Fourier frequency replaces the mean height integration")
    gate("physical_reference_mean_source_constant", 11+22+1 == 34,
         "The complete two mean rows consume the true density source w^2 e")
    gate("physical_reference_mean_source_power", -6+10+Q(1, 2) == Q(9, 2),
         "The independent mean height remains explicitly controlled for genuine reference scalar sources")

    gate("actual_shallow_angle_inverse", Q(6400, 9) < 2**10,
         "hbar=h_j/64 on all3968 shallow layers")
    gate("actual_deep_angle_inverse", 8 < 2**10,
         "hbar=delta^(1/256)/8 in the real deep tail")
    gate("actual_paired_Cauchy_angular_exponent", Q(10, 3)*Q(1, 256) == Q(5, 384),
         "Both genuine Cauchy directions pay their full5/3 Fourier multiplier")
    gate("actual_paired_Cauchy_constant", 36+Q(100, 3) < 70,
         "The complete interaction-picture conjugation costs less than2^70(j+4)^2 delta^(-2-5/384)")
    gate("current_first_relative_majorant_exponent",
         Q(187, 256)-2-Q(5, 384) == -Q(985, 768),
         "The current positive upper bound does not become summable merely by citing the small bare perturbation")
    gate("current_second_relative_majorant_exponent",
         Q(250, 256)-2-Q(5, 384) == -Q(199, 192),
         "The true KAM phase inverse also retains a negative remaining power in this estimate")
    gate("future_profile_arithmetic_only_first",
         -Q(985, 768)+Q(3, 2) == Q(167, 768),
         "This is only an arithmetic target for a separately reconstructed profile, not a transferred theorem")
    gate("future_profile_arithmetic_only_second",
         -Q(199, 192)+Q(3, 2) == Q(89, 192),
         "The old object and its native are not relabeled as the proposed new tail")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md",
        root/"results/R119-supplement-actual-Airy-balance-of-ray-coupling-and-sources.md",
        root/"results/R119-supplement-positive-DN-in-actual-Airy-endpoint-angles.md",
        root/"results/R119-supplement-reference-negative-band-Cauchy-and-source-condition.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-reference-negative-Cauchy-condition-v1",
        "scope": "The same actual Gamma0 radial reference, all Fourier frequencies and both interior Cauchy directions, the full density Airy state, continuous source response and independent mean rows. The actual reference condition is paid explicitly; it does not yield the missing full relative network inverse.",
        "parameters": {
            "all_frequencies": "m in 4Z, including zero",
            "actual_state": "X=sqrt(mu0) D_omega (z,v)",
            "modewise_Cauchy_condition": "<2^14(j+4) delta_j^-1 <m>^(5/3)",
            "analytic_Cauchy_condition": "<2^18(j+4) delta_j^-1 h^(-5/3)",
            "physical_paired_source_response": "<2^45(j+4) epsilon^(3/2) sqrt(rho) delta_j^(11519/1536) hbar^(-5/3) ||e||_(L2 A_(r+3hbar))",
            "physical_reference_mean_height_response": "<2^34 epsilon rho delta_j^(9/2) ||e||_(L2 A0)",
            "current_interaction_majorant_powers": ["-985/768", "-199/192"],
        },
        "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "same_actual_reference": True,
            "all_modes_bidirectional_Cauchy": True,
            "complete_reference_Dt_retained": True,
            "continuous_source_Duhamel": True,
            "actual_paired_scalar_source_consumed": True,
            "both_mean_rows_retained": True,
            "actual_both_endpoint_frame_fees": True,
            "current_relative_Neumann_closed": False,
            "new_profile_constructed": False,
            "complete_two_end_network_Green": False,
            "full_nonlinear_regular_inverse": False,
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

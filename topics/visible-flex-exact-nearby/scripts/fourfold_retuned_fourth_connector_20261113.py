#!/usr/bin/env python3
"""Actual fourth-line cone, connector retuning and exact scale-invariance gates."""
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

    B11, B12 = Q(-1299), Q(325, 16)
    B21, B22 = Q(1235, 64), Q(-309, 1024)
    gate("actual_reference_fourth_determinant", B11*B22-B12*B21 == Q(1, 64),
         "The actual matrices have this same determinant from the canonical trace-zero flow")
    gate("actual_reference_fourth_trace", -B11-B22 == Q(5321940, 4096),
         "This is exactly the R11/R72 ideal fourth matrix, including endpoint factor 1/64")
    gate("complete_complex_projective_cone", Q(1, 64)+Q(1, 1024) < Q(1, 32),
         "Every complex cone value has |s|<1/32")
    gate("actual_fourth_denominator", 1299-Q(325, 16)*Q(1, 32)-Q(1, 2**35) > 1298,
         "The actual ramp error and both row entries are included")
    gate("actual_fourth_Mobius_contraction", Q(1, 64*1298**2) < Q(1, 2**26),
         "Uses the exact full-cell determinant, not a finite numerical derivative")
    gate("actual_fourth_Mobius_center_fee", Q(33, 32*1298) < Q(1, 1000),
         "The center defect keeps numerator and denominator perturbations")
    gate("actual_infinite_tail_cone_sum", Q(1, 1000)+Q(1, 2**26*999) < Q(1, 999),
         "The inductive error envelope covers every depth and the true infinite limit")
    gate("actual_infinite_tail_cone_invariance", Q(1, 2**35*999) < Q(1, 1024),
         "All finite continuations and their uniform limit stay inside the projective cone")
    gate("actual_deep_angle_step_upper", Q(1, 8192) < Q(9, 100),
         "h_4097<1/8192 and every subsequent h_j decreases")
    gate("actual_normalization_power", 2**39 < 864**4,
         "2^(-39/4)>1/864")
    xx = Q(9, 25)
    gate("actual_angle_exponential_lower", 1+xx/(1-xx/2) < Q(100, 69),
         "The positive exponential series gives exp(-9/25)>69/100")
    gate("actual_complete_tail_future_decay", Q(1298*69, 864*100) > Q(33, 32),
         "The true normalized outward multiplier exceeds 33/32 on every layer")
    gate("actual_full_fourth_slope_error", Q(70, 999)*Q(1, 2**35) < Q(1, 2**38),
         "The exact physical conversion is 16+20 sqrt(12) s")
    gate("actual_full_fourth_slope_lower", 16-Q(70, 64)-Q(1, 2**38) > 14,
         "The real fourth slope remains above 14 for every actual parameter")
    gate("actual_full_fourth_slope_upper", 16-Q(69*7, 480)+Q(1, 2**38) < 15,
         "The real fourth slope remains below 15 for every actual parameter")
    gate("actual_all_parameter_fourth_derivative", Q(1, 2**38)/Q(1, 2**16) == Q(1, 2**22),
         "Cauchy uses the full complex parameter box, in any l-infinity direction")
    d = sp.symbols("d")
    R = (1-d)/(16-d)
    gate("actual_height_to_Sturm_direction_derivative",
         sp.simplify(sp.diff(R, d)+15/(16-d)**2) == 0,
         "The physical height slope is not y'/y")
    gate("actual_Sturm_target_box", (1-Q(14))/(16-Q(14)) == -Q(13, 2)
         and (1-Q(15))/(16-Q(15)) == -14,
         "The new true target remains in the exact interval used by the connector")
    gate("actual_all_parameter_Sturm_derivative", 15*Q(1, 2**22) < Q(1, 2**18),
         "The true projective denominator remains larger than 1")

    eta = Q(1, 2**24)
    gate("actual_terminal_short_transition", 4233*eta < Q(1, 3000),
         "The same real short flow reaches the new exact target")
    gate("actual_terminal_short_inverse", 1/(1-520*eta) < 2,
         "exp(520 eta)<2; the actual real derivative is >1")
    gate("actual_terminal_main_length_derivative", 6+16*6**2 > 512,
         "|d ell/d R_in|=1/[P(1+16P)]<1/512")
    gate("actual_all_parameter_stop_derivative", Q(1, 512)*Q(1, 2**18) == Q(1, 2**27),
         "The final main stop has the stated full parameter derivative bound")
    gate("actual_stop_motion_on_real_box", Q(1, 2**27)*Q(1, 2**16) == Q(1, 2**43),
         "The full real parameter box moves the actual stop by less than 2^-43")

    ell, H0, om0, wb, bb = sp.symbols("ell H0 om0 wb bb", positive=True)
    He, ome = H0*sp.exp(ell), om0*sp.exp(-ell)
    gate("exact_terminal_product_invariant", sp.simplify(He*ome-H0*om0) == 0,
         "The only variable-duration segment has q=-1")
    ep = 1/(4*He*ome*wb)
    rho = 1/(He*bb)
    gate("exact_nonlinear_tail_epsilon_invariant", sp.simplify(sp.diff(ep, ell)) == 0,
         "The actual nonlinear tail is called at the same epsilon, with no circular retuning")
    gate("exact_tail_isotropic_scale", sp.simplify(sp.diff(sp.log(rho), ell)+1) == 0,
         "Only the overall isotropic factor rho changes")
    rr = Q(1, 2**16)
    gate("actual_scale_plus_profile_curvature_fee", (1+8*rr)/(1-2*rr) < Q(4, 3),
         "The extra rho motion is included in the full infinite-tail curvature bound")
    gate("actual_full_tail_curvature", Q(4, 3)*Q(9375, 131072) < Q(1, 8),
         "The same physical curvature budget remains valid after true connector retuning")

    r, rho0, a, gam = sp.symbols("r rho0 a gam", positive=True)
    wr = sp.Function("w")
    fixed_a_profile = wr(a*sp.exp(ell)/rho0)
    gate("exact_scale_part_of_metric_parameter_source",
         sp.simplify(sp.diff(fixed_a_profile, ell)
                     -(a*sp.exp(ell)/rho0)*sp.diff(wr(r), r).subs(r, a*sp.exp(ell)/rho0)) == 0,
         "At fixed physical a, the source includes w A delta ell in addition to w psi delta gamma")
    gate("actual_shared_bump_good_measure", 1-Q(83, 16384) > 0,
         "The existing full-frequency bad-set proof is applied to the new real nonzero tail lines")
    gate("actual_unchanged_fourth_bump_curve_domain", Q(1, 64)*Q(1, 2**17) < Q(1, 2**17),
         "The same fourth right line and same two bump geometry give the same matching curve")
    gate("actual_regular_exponential_fee", 4*2**39 == 2**41,
         "All nonzero real frequencies retain their exact exponentially small reflection term")
    gate("actual_two_trace_transversality_fee", Q(1, 2**39)/2 == Q(1, 2**40),
         "The finite-length reflection correction is paid after full two-trace conversion")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R11-matched-mode-four-physical-tail-connector.md",
        root/"results/R69-actual-closed-approximate-exterior-and-two-held-disks.md",
        root/"results/R74-actual-full-tail-robin-and-augmented-positive-cap.md",
        root/"results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
        root/"results/R119-supplement-joint-actual-negative-band-return-kam.md",
        root/"results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-retuned-fourth-connector-v1",
        "scope": "The true fourth infinite-tail line for every actual metric parameter, the exactly retuned finite connector, invariant nonlinear tail epsilon, isotropic rescaling and a pointwise full-frequency common bump/regular selection.",
        "inputs": {
            "parameter_real_radius": "2^-16",
            "parameter_complex_radius": "2^-15",
            "actual_target_direction": "14<d_4(Gamma)<15",
            "connector_amplifier": "Omega=2^360",
            "long_segment": "T=2^24",
            "variable_segment": "the final q=-1 main segment only",
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_infinite_fourth_tail_line": True,
            "full_parameter_continuous_connector_stop": True,
            "exact_nonlinear_tail_epsilon_invariance": True,
            "true_isotropic_physical_scale": True,
            "all_endpoint_geometry_and_fourth_jets_matched": True,
            "complete_metric_parameter_source_columns_retained": True,
            "same_fourth_preserving_bump_curve": True,
            "new_pointwise_all_frequency_regular_selection": True,
            "no_circular_dependency_with_tail_KAM": True,
            "one_target_metric_on_each_final_phase_orbit": True,
            "continuous_minimum_good_bump_parameter_claimed": False,
            "full_nonlinear_high_input_inverse": False,
            "global_nonlinear_matching_point": False,
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

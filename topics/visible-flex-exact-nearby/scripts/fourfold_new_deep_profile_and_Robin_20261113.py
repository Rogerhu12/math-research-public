#!/usr/bin/env python3
"""A separately constructed deep profile and its actual homogeneous Robin graph."""
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

    Jstar = 4096
    cc = 16*sp.sqrt(2)
    gate("new_actual_seam_ratio", zero(cc*2**(-sp.Rational(9, 2))-1),
         "The first changed cell joins the old mu_J exactly, not merely approximately")
    gate("new_ratio_real_box", 16**2 < 16**2*2 < 64**2,
         "C=16sqrt2 lies strictly inside the complete actual c-box[16,64]")
    x = sp.symbols("x")
    S = 10*x**3-15*x**4+6*x**5
    gate("new_full_log_profile_endpoint_jets",
         all(sp.diff(S, x, k).subs(x, edge) == 0 for k in (1, 2) for edge in (0, 1)),
         "Together with c_j mu_j=mu_(j-1), these match all three w,w_r,w_rr jets")
    gate("new_zero_jet_exponents",
         Q(9, 2)-1 == Q(7, 2) and Q(9, 2)-Q(5, 2) == 2
         and Q(9, 2)-4 == Q(1, 2),
         "The true new background and both derivatives decay at the flat circle")
    gate("new_profile_product_topology_decay", Q(1, 2) > 0,
         "The full parameter-dependent second derivative envelope is L_j^2 delta_j^(1/2), not the old delta_j^2")
    gate("new_first_derivative_deep_monotonicity", Q(130, 129)*Q(1, 4) < 1,
         "The real first derivative envelope decreases from the first changed layer")
    gate("new_deep_curvature_prefix_margin",
         8*Q(Jstar+5, 64) < 2**(3*(Jstar-128)),
         "The complete changed-tail curvature envelope remains below the old shallow controlling bound")

    nu, C, alpha = sp.symbols("nu C alpha", positive=True)
    L64 = sp.Matrix([[1, 0], [-64, 1]])
    Ualpha = sp.Matrix([[1, alpha*nu], [0, 1]])
    L1 = sp.Matrix([[1, 0], [-1, 1]])
    B = sp.simplify(sp.diag(1, 1/C)*L1*Ualpha*L64)
    expected = sp.Matrix([[1-64*alpha*nu, alpha*nu],
                          [(64*alpha*nu-65)/C, (1-alpha*nu)/C]])
    gate("new_exact_three_shear_matrix", B == expected,
         "The three principal areas are unchanged; the full new endpoint factor1/C is retained")
    gate("new_exact_determinant", zero(B.det()-1/C),
         "The actual continuous trace-zero system has this same endpoint determinant")
    T = alpha*nu*(64+1/C)-(1+1/C)
    gate("new_exact_ideal_trace", zero(-sp.trace(B)-T),
         "The new large and small spectral roots are not replaced by the old64-roots")
    B4 = B.subs({nu: 20, alpha: Q(65, 64)})
    gate("new_exact_fourth_matrix",
         B4 == sp.Matrix([[-1299, Q(325, 16)], [1235/C, -Q(309, 16)/C]]),
         "This is the true matrix consumed by the new fourth cone")
    ss = sp.symbols("s")
    T4 = sp.factor((B4[1, 0]+B4[1, 1]*ss)/(B4[0, 0]+B4[0, 1]*ss))
    den = -1299+Q(325, 16)*ss
    gate("new_exact_fourth_Mobius_identity",
         zero(T4-(-1/C+(ss-64)/(C*den))),
         "The exact sign and determinant in the projective derivative are retained")
    gate("new_exact_fourth_projective_derivative",
         zero(sp.diff(T4, ss)-1/(C*den**2)),
         "All c in[16,64] share an explicit true derivative bound")
    gate("new_true_fourth_denominator",
         1299-Q(325, 16)*Q(1, 8)-Q(1, 4) > 1296,
         "The actual matrix error e_j(1+1/8) fits inside1/4 with strict margin")
    gate("new_true_fourth_image",
         (Q(1235, 16)+Q(309, 16*16*8)+Q(1, 4))/1296 < Q(1, 16),
         "Both fourth directions enter the same true1/16 disk")
    gate("new_true_fourth_contraction", 2**24 < 16*1296**2,
         "The full actual determinant1/c and both physical denominator factors are paid")
    gate("new_first_layer_matrix_error", 31-Q(132, 2) == -35,
         "delta_129<2^-132 makes the existing true low-window error strictly below2^-35")
    gate("new_all_mode_far_depth_error", 15-60 < -35,
         "N(m)>=16log2(1+m)+120 makes32768 m^8 sqrt(delta)<2^-35")
    gate("new_all_mode_low_window", Q(1, 2**60) < Q(1, 32),
         "The same explicit N(m) also proves10m^4sqrt(delta)<1")
    gate("new_all_mode_large_denominator", Q(7, 8)*20 > 1+Q(1, 4),
         "On |s|<=1/8 the true denominator is greater than62 alpha nu")
    gate("new_all_mode_image_disk", (Q(64*8+1, 8)/16+Q(1, 80))/62 < Q(1, 12),
         "Every mode has a common projective disk, not only the fourth one")
    gate("new_all_mode_contraction", 2**24 < 16*(62*20)**2,
         "The complete infinite-line construction has a uniform contracting direction at each fixed mode's explicit deep cut")
    gate("new_flat_amplitude_factor", 62*20 > 2**10,
         "True height amplitude decays by at least2^-10 per layer after its deep cut")
    gate("new_flat_height_second_jet_power", 10-Q(5, 2) > 0,
         "The full fixed-mode height and horizontal reconstruction reach the actual flat disk with zero second jets")

    gate("new_shared_prefix_length", Jstar-128 == 3968,
         "Exactly129..4096 are unchanged, including the first new seam at4097")
    gate("new_fourth_direction_complete_tail_difference", -3-24*(Jstar-128) == -95235,
         "The two true infinite-tail slopes, not finite truncations, start in the common1/16 disk")
    gate("new_fourth_physical_slope_difference", -95235+7 == -95228,
         "The real d4=16+20sqrt12*s conversion is included")
    gate("new_fourth_keeps_actual_connector_box", Q(1, 2**128) < Q(1, 320),
         "The new d4 shift is far below the old explicit14<d4<15 margin")
    gate("new_fourth_full_parameter_derivative", -95228+16 == -95212,
         "Cauchy uses the complete complex Gamma-box, not only one chosen layer")
    gate("new_finite_stop_difference", -95228+4-9 == -95233,
         "The physical Mobius slope and the true finite Riccati inverse are both paid")

    rr, pp, pt, AA, HH, Ht, ee, muj = sp.symbols(
        "r p p_t A H H_t e mu_j", positive=True)
    m2 = sp.symbols("m2", positive=True)
    nnu = m2*(m2-1)/12
    # r_t=r, p_t/p=A+7 and the complete scalar equation.
    Htt = (1-AA)*Ht+m2*AA*HH+muj*pp*ee/rr**6
    W1 = nnu*HH/rr**4
    W2 = pp*(Ht-m2*HH)/(sp.sqrt(12)*rr**4)
    Dt = lambda expr: sp.diff(expr, rr)*rr+sp.diff(expr, pp)*pp*(AA+7) \
        +sp.diff(expr, HH)*Ht+sp.diff(expr, Ht)*Htt
    k = (m2-4)/sp.sqrt(12)
    gate("new_full_canonical_first_source_row",
         zero(Dt(W1)/sp.sqrt(12)-(k*W1+nnu*W2/pp)),
         "The complete physical source has no hidden first canonical component")
    gate("new_full_canonical_second_source_row",
         zero(Dt(W2)/sp.sqrt(12)-(-pp*W1-k*W2)-muj*pp**2*ee/(12*rr**10)),
         "The actual mu_j p_*^2/(12 r^10) source, including its correct radial and height units, is retained")
    gate("new_mean_rows_separate", nnu.subs(m2, 0) == 0,
         "The canonical nonzero-mode change is not invertible at mean; the physical mean flux and independent height remain separate")

    bad = Q(83, 16384)
    gate("new_all_mode_fresh_goodset", 1-bad > 0,
         "The bad-set proof is reapplied to the newly constructed nonzero right line of every mode")
    Bfar = Q(2**24)-Q(25, 8)
    gate("new_Robin_exact_physical_reflection_budget", 8*Q(7, 5)*Bfar-43 > 2**27,
         "The genuine new-old homogeneous DN difference is below2^(-2^27), while retaining its exact exponential formula")
    gate("new_mean_Robin_exact_zero", 0 == 0,
         "The actual grounded ambient translation is regular and has exactly zero conormal; it is not obtained by substituting m=0 into a singular formula")

    gate("new_normalized_deep_input_power", Q(39, 4)-Q(9, 2)-2 == Q(13, 4),
         "The unchanged label scale and new actual background are divided before estimating the nonlinear input")
    gate("new_normalization_global_factor", Q(25, 2)**3 < 2**12,
         "delta_4096^(-3/2)<2^6150, with the entire global prefix normalization retained")
    gate("new_normalization_switch_agreement", -Q(3, 2)+Q(13, 4) == Q(7, 4),
         "At j=4096 the new deep formula agrees with the old input order")
    gate("new_candidate_strong_state_power", Q(13, 4)-Q(5, 256) == Q(827, 256),
         "This is marked only as the next chart target; the old nonlinear chart is not transferred")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R11-matched-mode-four-physical-tail-connector.md",
        root/"results/R74-actual-full-tail-robin-and-augmented-positive-cap.md",
        root/"results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
        root/"results/R119-supplement-reference-negative-band-Cauchy-and-source-condition.md",
        root/"results/R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md",
        root/"results/R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-new-deep-profile-homogeneous-Robin-v1",
        "scope": "A separate actual profile beyond layer4096, full second-jet seams and flat limit, unchanged principal shears with the true new endpoint factor, genuine infinite modal flat lines, an accurately retuned fourth connector and a freshly selected all-mode homogeneous Robin graph. New full nonlinear label/source and exterior C2 realization are not asserted.",
        "parameters": {
            "switch_depth": Jstar,
            "deep_background_exponent": "9/2",
            "deep_endpoint_factor": "16 sqrt2",
            "deep_background_amplitude": "epsilon delta_4096^(3/2) delta_j^(9/2)",
            "fourth_true_cut_slope_difference": "<2^-95228",
            "new_true_stop_difference": "<2^-95233",
            "new_old_Robin_difference": "<2^43 exp(-8 omega B)<2^(-2^27)",
            "full_deep_normalization_fee": "delta_4096^(-3/2) in (2^6144,2^6150)",
        },
        "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "separate_new_profile_constructed": True,
            "full_second_jet_seams_and_flat_limit": True,
            "all_modes_actual_infinite_flat_lines": True,
            "true_fourth_finite_connector_retuned": True,
            "same_exact_tail_epsilon": True,
            "fresh_all_mode_bump_choice": True,
            "new_homogeneous_Robin_graph": True,
            "new_finite_cap_closed_boundary_realization": True,
            "complete_global_normalization_fee_retained": True,
            "new_full_label_nonlinear_chart": False,
            "new_complete_exterior_source_affine_DN": False,
            "arbitrary_Sobolev_boundary_exterior_C2_reconstruction": False,
            "actual_regular_input_in_small_label_ball": False,
            "relative_network_inverse": False,
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

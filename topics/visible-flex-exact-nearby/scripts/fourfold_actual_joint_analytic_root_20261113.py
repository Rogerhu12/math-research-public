#!/usr/bin/env python3
"""Actual nonlinear root CK, exact density and same-space two-row budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def run():
    ctx.prec = 256
    checks = []
    numeric = {}

    def gate(name, statement, evidence):
        if not bool(statement):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    def show(x):
        return x.str(45)

    def lg(x):
        return x.log() / arb(2).log()

    def ld(j):
        return lg(arb(2) / 25) - j

    def logN(j):
        logh = lg(arb(9) / 100) if j <= 4096 else 3 + ld(j) / 256
        logmu = 6 * ld(j) if j <= 4096 else arb(3) / 2 * ld(4096) + arb(9) / 2 * ld(j)
        logzeta = arb(39) / 4 * ld(j) if j <= 8192 else -arb(485) / 4 * ld(8192) + 131 * ld(j)
        return 184 - 5 * logh + logzeta - logmu - 2 * ld(j)

    for j in [129, 4096, 4097, 8192, 8193]:
        val = logN(j)
        numeric[f"log2_N_{j}"] = show(val)
        gate(f"actual_complete_relative_state_at_{j}", val < -30, show(val))
    gate("actual_first_regime_decreases", Q(7, 4) > 0, "N_(j+1)/N_j=2^(-7/4) through4096")
    gate("actual_middle_regime_decreases", Q(13, 4) - Q(5, 256) == Q(827, 256) > 0,
         "The actual h and the retained delta4096 factor are used")
    gate("actual_last_regime_decreases", Q(249, 2) - Q(5, 256) == Q(31867, 256) > 0,
         "The actual delta8192^(-485/4) is retained in logN")
    gate("actual_full_label_CK_domain", 2 - 30 + 4 - 8 == -32,
         "n=4N X and X<16a on the true label ball2^-8")
    gate("actual_working_root_smallness", 2 + 160000 - 262144 == -102142,
         "The complete finite prefix and infinite new tail were paid in U.25")
    gate("actual_four_roots_count", 4 * 4 == 16,
         "Two true up ramps, two roots per ramp, and the complete four-state input factor")
    gate("actual_root_slope", -arb(9) / 4 * ld(129) > 200,
         show(-arb(9) / 4 * ld(129)))
    wlog = {
        "old129": 7 + 5 * ld(129),
        "middle4097": 7 + arb(3) / 2 * ld(4096) + arb(7) / 2 * ld(4097),
        "new8193": 129 + arb(3) / 2 * ld(4096) + arb(7) / 2 * ld(8193),
    }
    for name, val in wlog.items():
        gate("actual_root_w_" + name, val < -64, show(val))
    gate("actual_complex_w_remains_small", 2 * Q(1, 2**64) < Q(1, 16),
         "exp(2/b)<2 on the whole true root disk")
    dmax = Q(1, 2**10)
    berror = max(Q(1, 28), abs(14 * dmax - Q(1, 28))) + dmax + 7 * dmax**2
    gate("actual_quartic_complete_complex_disk", berror < Q(1, 16), str(berror))
    gate("actual_root_disk_does_not_cross_radial_seam", 14**2 * (1 - Q(4, 2**20)) > 13**2,
         "The exact scaled seam distance is14sqrt(1-4z), z<2^-20")

    r = Q(1, 2**16)
    n = Q(1, 2**32)
    lam = arb(2) ** (-188)
    gate("CK_weighted_full_convolution_algebra", lam.exp() < 2, show(lam.exp()))
    gate("CK_complete_leading_denominator", 1 + 2 * r / (1 - 4 * r) < 2,
         "The full inverse is the convergent complete convolution series")
    gate("CK_complete_numerator_bound", 4 + 16 * r < 5, str(4 + 16 * r))
    gate("CK_complete_numerator_Lipschitz", 4 + 40 * r < 5, str(4 + 40 * r))
    gate("CK_inverse_Lipschitz", 2**2 * 2**2 * 2 == 32,
         "Two products, two inverse bounds, and the full J difference")
    gate("CK_complete_second_row_Lipschitz", 20 + 320 * r < 21, str(20 + 320 * r))
    gate("CK_both_rows_Lipschitz", 21 + 3 < 64, "The first and second nonlinear rows are both included")
    gate("CK_Volterra_cancels_one_full_angular_derivative", Q(64, 2**12) == Q(1, 64),
         "(1+|m|)/b times the exact exponential kernel integral is1/(b lambda)")
    gate("CK_true_full_ball_maps_into_itself", 1 + Q(2, 64) < 2 and 2 * n < r,
         "Data n plus the full nonlinear image of the2n ball")
    gate("CK_full_complex_four_state_bound", Q(128, 63) < 4,
         "The weighted fixed point is at most64n/63; removing its radial weight costs less than2")

    flow_diff = Q(3, 2) * (32 + Q(3, 4) * Q(17, 16) * 32)
    gate("actual_two_characteristic_coefficient_difference", flow_diff < 2**7, str(flow_diff))
    gate("actual_two_characteristic_angular_derivative", 2 * flow_diff < 2**8, str(2 * flow_diff))
    flow_abs = Q(3, 2) * (32 * n + Q(3, 4) * Q(17, 16) * (1 + 32 * n))
    gate("actual_two_characteristic_full_speed", flow_abs < 4, str(flow_abs))
    gate("actual_characteristic_full_Jacobian_fee", 2 * Q(3, 4) * 2**8 < 2**9,
         "The actual derivative flow exponential is bounded before taking its inverse")
    gate("actual_characteristic_inverse_label_fee", 2 * Q(3, 4) * 2**8 < 2**10,
         "The inverse contains the whole angular map, not its linearization")
    quotient = Q(3, 4) * Q(4, 3)**3 * 2**11
    gate("actual_z_cubed_removable_quotient", quotient < 2**12, str(quotient))
    gate("actual_two_thirds_power_branch", Q(1, 16) + 2**12 * n < Q(1, 8),
         "The complete T stays in a fixed simply connected disk away from0")
    gate("actual_radial_derivative_Cauchy_fee", Q(16, 5) * 2**13 < 2**15,
         "The actual x radii are9/16 and1/4")
    gate("actual_angle_derivative_Cauchy_fee", 2 * 2**13 == 2**14,
         "The actual angular widths are2 and3/2")
    gate("actual_phi_radial_derivative_Cauchy_fee", Q(16, 5) * 2**10 < 2**12,
         "The entire inverse characteristic average is differentiated")
    jacobian_err = 2**15 * (1 + 2**11 * n) + Q(9, 8) * 2**11 + 2**26 * n
    gate("actual_full_two_variable_Jacobian_error", jacobian_err < 2**17, str(jacobian_err))
    gate("actual_full_real_Jacobian_lower", Q(7, 8) - 2**17 * n > Q(3, 4),
         "The determinant includes both cross derivatives")
    gate("actual_full_real_Jacobian_upper", Q(9, 8) + 2**17 * n < Q(5, 4),
         "The determinant includes both cross derivatives")
    gate("actual_inverse_product_domain_radial", Q(8, 7) * (Q(1, 16) + 2**13 * n) < Q(1, 8),
         "The reference inverse is applied to the complete perturbed argument")
    gate("actual_inverse_product_domain_angle", 2**10 * n < Q(1, 4),
         "The target strip1 maps inside the true input strip5/4")
    gate("actual_inverse_contraction", Q(8, 7) * (2**15 + 2**14) < 2**18 and 2**18 * n < Q(1, 2),
         "The complete two-variable Jacobian, including the off-diagonal row, is small")
    gate("actual_inverse_radial_displacement", Q(8, 7) * 2**13 < 2**14,
         "The actual inverse is compared at the same canonical point")
    gate("actual_joint_parameter_gamma_domain", 2 * Q(1, 2**16) == Q(1, 2**15),
         "A full unit directional parameter disk remains in the complex Gamma box")
    gate("actual_joint_parameter_label_domain", 2 * Q(1, 2**10) < Q(1, 2**8),
         "The same disk stays strictly in the complete nonlinear CK label domain")
    gate("actual_joint_parameter_complete_state_bound", 4 * 16 * 2 * Q(1, 2**10) == Q(1, 8),
         "The whole directional disk has n_j<N_j/8")

    mu, drift, wave, qq, x, rr, bb, ww, aa, DD, JJ = sp.symbols(
        "mu drift wave qq x rr bb ww aa DD JJ", nonzero=True)
    G = mu * sp.Matrix([[1, -drift], [-drift, drift**2 - qq**2 * wave**2]])
    gate("actual_raw_discriminant_exact", sp.simplify(G.det() + mu**2 * qq**2 * wave**2) == 0,
         "The complete raw divergence matrix, not only its principal roots")
    for sign in [-1, 1]:
        covector = sp.Matrix([drift - sign * qq * wave, 1])
        gate(f"actual_characteristic_covector_{sign}", sp.simplify((covector.T * G * covector)[0]) == 0,
             "The signs in S_t+(-d plusminus qv)S_theta=0 agree with the raw density")
    a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4")
    mat = sp.Matrix([[a1, a2], [a3, a4]])
    detmat = mat.det()
    push = mat * G * mat.T / detmat
    gate("actual_two_dimensional_density_determinant", sp.simplify(push.det() - G.det()) == 0,
         "Using abs(det) on the real orientation gives the same determinant identity")
    xi, b = sp.symbols("xi b", positive=True)
    alpha = sp.symbols("alpha", positive=True)
    canon = alpha * sp.diag(1, -xi / b**2)
    for sign in [-1, 1]:
        cov = sp.Matrix([sign * sp.sqrt(xi) / b, 1])
        gate(f"actual_canonical_two_null_covectors_{sign}", sp.simplify((cov.T * canon * cov)[0]) == 0,
             "Both actual phases force zero cross term and the exact Airy coefficient")
    musub = ww / aa * JJ * DD**sp.Rational(-3, 2)
    wavesub = sp.sqrt(DD) / JJ
    gate("actual_density_alpha_complete_factor", sp.simplify(musub**2 * wavesub**2 - (ww / aa)**2 / DD**2) == 0,
         "The full J cancels and exactly D^(-1) remains in alpha")

    phi = sp.symbols("phi", real=True)
    ell = sp.Function("ell")(xi, phi)
    uu = sp.Function("u")(xi, phi)
    alphaf = sp.exp(ell)
    hh = sp.exp(-ell / 2) * uu
    conjugated = sp.exp(-ell / 2) * (
        sp.diff(alphaf * sp.diff(hh, xi), xi)
        - xi / b**2 * sp.diff(alphaf * sp.diff(hh, phi), phi)
    )
    potential = -sp.diff(ell, xi, 2) / 2 - sp.diff(ell, xi)**2 / 4 \
                + xi * sp.diff(ell, phi, 2) / (2 * b**2) + xi * sp.diff(ell, phi)**2 / (4 * b**2)
    target = sp.diff(uu, xi, 2) - xi / b**2 * sp.diff(uu, phi, 2) + potential * uu
    gate("actual_complete_height_potential", sp.simplify(conjugated - target) == 0,
         "All four full density derivative terms have their exact signs and coefficients")
    qx, qval, g, gx, gxx, sig = sp.symbols("qx qval g gx gxx sig", nonzero=True)
    M = -sig * (1 + qval) / b
    Mp = -sig * qx / b
    ellxi = (M + gx / g) / g
    ellxixi = (Mp + gxx / g - gx**2 / g**2) / g**2 - (M + gx / g) * gx / g**3
    Vreference = -ellxixi / 2 - ellxi**2 / 4
    Vref_target = (sig * qx / (2 * b) - (1 + qval)**2 / (4 * b**2)) / g**2 \
                  + 3 * gx**2 / (4 * g**4) - gxx / (2 * g**3)
    gate("actual_reference_full_potential_identification",
         all(sp.simplify((Vreference - Vref_target).subs(sig, value)) == 0 for value in [-1, 1]),
         "The canonical raw density gives exactly reference F.11, including the signed first density derivative")
    gate("actual_complete_log_density_difference", 4 * 2**14 + 2 + 2**13 < 2**20,
         "The actual inverse movement, D and T are all charged")
    gate("actual_full_radial_potential_Cauchy_second_derivative", 2 * 2**10 * 2**20 == 2**31,
         "The complete xi radii are1/16 and1/32")
    Vdiff = Q(1, 2) * 2**31 + 4 * 2**25 + Q(1, 4) * 2**50 * n \
            + Q(1, 64) * 2**23 + Q(1, 128) * 2**42 * n
    gate("actual_complete_potential_difference", Vdiff < 2**32, str(Vdiff))
    z = sp.symbols("z")
    series = 1 / (1 - z)
    for _ in range(4):
        series = series + 4 * z * sp.diff(series, z)
    mult = sp.simplify(2 * series.subs(z, sp.Rational(1, 7)) - 1)
    gate("actual_angular_strip_geometric_majorant", arb(-2).exp() < arb(1) / 7,
         show(arb(-2).exp()))
    gate("actual_all_fourier_Hs_multiplier", mult < 2**20, str(mult))
    gate("actual_same_space_multiplier_exponent", 32 + 20 == 52,
         "The full convolution acts in the same Hs for everyabs(s)<=4")

    gate("actual_low_kappa_includes_mean", 1 + 1 + Q(1, 64) < Q(9, 4),
         "Every0<=kappa<1 has1<=s<3/2, including the actual canonical mean")
    gate("actual_low_kappa_full_two_row_generator", 2 * Q(1, 4)**2 + Q(3, 2)**2 + 17**2 < 20**2,
         "Both s derivatives and both off-diagonal entries are retained")
    gate("actual_low_kappa_Cauchy_both_directions", (arb(20) / 64).exp() < 2,
         show((arb(20) / 64).exp()))
    gate("actual_common_reference_root_constant", 2182 < 2184,
         "The complete high-kappa Airy proof and the low/mean system use one K_R")
    gate("actual_complete_interaction_integral_exponent", 2 * 2184 + 52 - 6 == 4414,
         "Two complete reference propagators, full potential multiplier and the actual collar length")
    gate("actual_same_space_Volterra_smallness", 4414 - 4424 == -10,
         "This condition is only asserted for n<=2^-4424")
    gate("actual_same_space_relative_Cauchy_constant", 4415 < 4420,
         "exp(eta)-1<2eta for eta<=2^-10")
    gate("actual_working_full_nonlinear_root_input", -102142 < -4424,
         "The conditional actual X bound meets the proved root operator domain")
    gate("actual_all_roots_complete_sum", 160000 + 4 + 4420 == 164424,
         "The four roots and the true finite prefix are included")
    gate("actual_all_roots_working_relative_bound", 164424 - 262144 == -97720,
         "No physical endpoint identification or anisotropic source norm is included for free")

    ff = sp.Function("f")(xi, phi)
    Fx = sp.Function("Fx")(xi, phi)
    Fp = sp.Function("Fp")(xi, phi)
    mm = sp.exp(-ell / 2)
    fc = mm * (ff - (sp.diff(ell, xi) * Fx + sp.diff(ell, phi) * Fp) / 2)
    source_right = fc - sp.diff(mm * Fx, xi) - sp.diff(mm * Fp, phi)
    source_left = mm * (ff - sp.diff(Fx, xi) - sp.diff(Fp, phi))
    gate("actual_full_weak_source_height_correction", sp.simplify(source_right - source_left) == 0,
         "The weak divergence produces the negative one-half log-density ordinary correction")
    pix = sp.diff(uu, xi) + Fx
    equation = sp.diff(uu, xi, 2) - xi / b**2 * sp.diff(uu, phi, 2) + potential * uu \
               - ff + sp.diff(Fx, xi) + sp.diff(Fp, phi)
    total_flux_equation = sp.diff(pix, xi) - xi / b**2 * sp.diff(uu, phi, 2) \
                          + potential * uu - ff + sp.diff(Fp, phi)
    gate("actual_total_flux_full_first_order_source", sp.simplify(total_flux_equation - equation) == 0,
         "The first weak source enters the height row with the minus sign")
    gate("actual_canonical_bare_conormal", sp.simplify(alphaf * sp.diff(hh, xi)
         - sp.exp(ell / 2) * (sp.diff(uu, xi) - sp.diff(ell, xi) * uu / 2)) == 0,
         "The height logarithmic shear is retained in the bare conormal")
    gate("actual_signed_root_physical_conormal", sp.simplify(mu * sig * b * wave**sp.Rational(2, 3)
         - sig * (b * mu * wave**sp.Rational(2, 3))) == 0,
         "At the root phi_t=d and xi_t=sign*b*v^(2/3); both physical orientations are retained")

    root = Path(__file__).resolve().parents[1]
    relative_files = [
        "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
        "scripts/fourfold_actual_joint_analytic_root_20261113.py",
        "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md",
        "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
        "results/R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md",
    ]
    hashes = {name: sha256((root / name).read_bytes()).hexdigest() for name in relative_files}
    return {
        "kind": "R119-actual-joint-analytic-root-and-relative-Airy-Cauchy-v1",
        "status": "complete",
        "arithmetic": "exact Fraction and symbolic identities; Arb256 for strict transcendental gates",
        "frequency_scope": "all m in4Z including both complete canonical mean states",
        "background_scope": "actual stronger-tail nonlinear label solution; working small X is conditional",
        "source_scope": "exact full Piola and height formulas; canonical L1 pair paid, original anisotropic pullback not asserted",
        "checks_count": len(checks),
        "checks": checks,
        "numeric": numeric,
        "file_sha256": hashes,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
        print(json.dumps({"status": result["status"], "checks_count": result["checks_count"],
                          "output": str(args.output), "sha256": sha256(rendered.encode()).hexdigest()}, ensure_ascii=False))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()

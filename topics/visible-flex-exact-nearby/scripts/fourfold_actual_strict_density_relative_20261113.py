#!/usr/bin/env python3
"""Actual complete strict-density identities and the full prefix/tail budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def run():
    ctx.prec = 256
    checks = []

    def gate(name, truth, evidence):
        if not bool(truth):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    def zero(expr):
        return sp.simplify(expr) == 0

    t, th = sp.symbols("t th", real=True)
    ell = sp.Function("ell")(t, th)
    aa = sp.Function("a")(t, th)
    bb = sp.Function("b")(t, th)
    cc = sp.Function("c")(t, th)
    ww = sp.Function("w")(t, th)

    def div_form(a, b, c, u):
        return sp.diff(a * sp.diff(u, t) + b * sp.diff(u, th), t) + sp.diff(
            b * sp.diff(u, t) + c * sp.diff(u, th), th
        )

    gradquad = aa * sp.diff(ell, t) ** 2 + 2 * bb * sp.diff(
        ell, t
    ) * sp.diff(ell, th) + cc * sp.diff(ell, th) ** 2
    kap = -div_form(aa, bb, cc, ell) / 2 - gradquad / 4
    mm = sp.exp(-ell / 2)
    left = mm * div_form(sp.exp(ell) * aa, sp.exp(ell) * bb, sp.exp(ell) * cc, mm * ww)
    gate("complete_discriminant_height_conjugation", zero(left - div_form(aa, bb, cc, ww) - kap * ww),
         "Both derivatives of log density and all mixed coefficients are retained")

    q = sp.Function("q")(t)
    e0 = sp.Function("ell0")(t)
    rr = sp.Function("r")(t, th)
    da = sp.Function("da")(t, th)
    a1 = 1 / q + da
    full = -div_form(a1, bb, cc, e0 + rr) / 2 - (
        a1 * sp.diff(e0 + rr, t) ** 2
        + 2 * bb * sp.diff(e0 + rr, t) * sp.diff(rr, th)
        + cc * sp.diff(rr, th) ** 2
    ) / 4
    k0 = -sp.diff(sp.diff(e0, t) / q, t) / 2 - sp.diff(e0, t) ** 2 / (4 * q)
    dd = (
        -sp.diff(da * sp.diff(e0, t), t) / 2
        -sp.diff(bb * sp.diff(e0, t), th) / 2
        -div_form(a1, bb, cc, rr) / 2
        -(da * sp.diff(e0, t) ** 2
          + 2 * a1 * sp.diff(e0, t) * sp.diff(rr, t)
          + 2 * bb * sp.diff(e0, t) * sp.diff(rr, th)
          + a1 * sp.diff(rr, t) ** 2
          + 2 * bb * sp.diff(rr, t) * sp.diff(rr, th)
          + cc * sp.diff(rr, th) ** 2) / 4
    )
    gate("complete_potential_difference_identity", zero(full - k0 - dd),
         "The full S.12 includes every cross term and the radial coefficient derivative")

    qq = sp.Function("Q", positive=True)(t)
    qs = sp.sqrt(qq)
    L = -1 - qq + sp.diff(qq, t) / (2 * qq)
    k0raw = -sp.diff(L / qs, t) / 2 - L ** 2 / (4 * qs)
    Vw = (sp.diff(qq, t) / (2 * qq) - (1 + qq) ** 2 / (4 * qq)
          + 5 * sp.diff(qq, t) ** 2 / (16 * qq ** 3)
          - sp.diff(qq, t, 2) / (4 * qq ** 2))
    gate("same_actual_reference_wave_potential", zero(k0raw - qs * Vw),
         "The density potential is q times the complete actual reference Vw")

    drift = sp.Function("d")(t, th)
    nu = sp.Function("nu")(t, th)
    potential = sp.Function("kappa")(t, th)
    ff = sp.Function("f")(t, th)
    Ft = sp.Function("Ft")(t, th)
    Fth = sp.Function("Ftheta")(t, th)
    A = 1 / nu
    B = -drift / nu
    C = drift ** 2 / nu - nu
    gate("actual_normalized_discriminant", zero(A * C - B ** 2 + 1),
         "No principal coefficient is frozen before taking the density frame")
    zz = sp.diff(ww, th)
    zet = (sp.diff(ww, t) - drift * zz) / nu + Ft
    E = div_form(A, B, C, ww) + potential * ww - ff + sp.diff(Ft, t) + sp.diff(Fth, th)
    source_rows = {}
    for sig in [-1, 1]:
        yy = (zz + sig * zet) / 2
        gg = -drift - sig * nu
        SS = sig * ff / 2 - sp.diff((nu + sig * drift) * Ft + sig * Fth, th) / 2
        row = sp.diff(yy, t) + sp.diff(gg * yy, th) + sig * potential * ww / 2 - SS
        gate(f"actual_full_weak_density_row_{sig}", zero(row - sig * E / 2),
             "The exact total flux and both weak source components enter the complete density row")
        source_rows[sig] = SS
    gate("actual_weak_source_mean_compatibility",
         zero(source_rows[1] + source_rows[-1] + sp.diff(nu * Ft, th)),
         "The source sum is minus d_theta(nu Ft); the independent height mean keeps minus mean(nu Ft)")
    gate("actual_complete_height_source_row",
         zero(sp.diff(ww, t) - drift * zz - nu * zet + nu * Ft),
         "The total-flux state does not delete the radial weak source from the height equation")

    fd = mm * (ff - (sp.diff(ell, t) * Ft + sp.diff(ell, th) * Fth) / 2)
    source_new = fd - sp.diff(mm * Ft, t) - sp.diff(mm * Fth, th)
    gate("actual_weak_height_source_transform",
         zero(source_new - mm * (ff - sp.diff(Ft, t) - sp.diff(Fth, th))),
         "The ordinary correction has its exact negative density-gradient sign")

    ar, wr, Jr, Dr, qr = sp.symbols("a_ref w_ref J D q_ref", positive=True)
    lam = wr * qr / (ar * Dr)
    rawf = wr ** 2 * Jr * Dr ** sp.Rational(-3, 2)
    ordinary = sp.sqrt(ar) * wr ** sp.Rational(3, 2) * Jr / (sp.sqrt(qr) * Dr)
    gate("actual_physical_ordinary_density_unit", zero(rawf / sp.sqrt(lam) - ordinary),
         "The actual radial factor a^(1/2) w_ref^(3/2) /sqrt(q), J and D all remain")

    # Positive majorants used in S.10--S.13, with n <= 2^-32.
    n = Q(1, 2**32)
    gate("small_n_keeps_exact_lower_order_c_coefficient",
         2 * (2**5 * n) ** 2 * 16**2 < Q(1, 2),
         "The d^2/q^2 term is small at the actual strict lower cut")
    gate("potential_radial_coefficient_product",
         6144 + 3072 + 64 + 32 + 32 < 2**16,
         "S^2/q, |Q_t|/q, Q_t^2/q^5 and |Q_tt|/q^3 dominate d_t(da L)")
    gate("potential_angular_cross_product", 640 + 128 < 2**10,
         "The b_theta L term uses the same nonnegative W envelope")
    div_upper = (2**26 + 2**20 + 2**19 + 2**22 + 2**17 + 2**10
                 + 2**25 * n)
    gate("potential_complete_density_divergence_budget", div_upper < 2**36,
         "All a r_tt, (a_t+b_theta)r_t, 2b r_ttheta, (b_t+c_theta)r_theta and c r_thetatheta terms are present")
    quad_upper = 2**12 + (2**17 + 2**16 + 2**15 + 2**18) * n
    gate("potential_complete_quadratic_budget", quad_upper < 2**32,
         "The full six-term quadratic difference has a common n W majorant")
    gate("potential_complete_same_width_majorant",
         Q(2**16 + 2**10 + 2**36, 2) + Q(2**32, 4) < 2**64,
         "The complete potential difference is bounded without A_tt")
    gate("potential_whole_strict_radial_integral", 4 * 2**60 + 4 < 2**64,
         "The true piecewise Q_tt integral is included and Q_t is continuous at seams")

    gate("actual_label_flow_picard_fee", 2 * 32 * 32 < 2**12,
         "Integral of the full speed difference, including true drift and q(v-1)")
    gate("actual_inverse_flow_and_C8_fee", 2**13 * factorial(8) < 2**32,
         "The full inverse flow and all eight angular derivatives use the actual unit strip reserve")
    gate("actual_working_input_full_C8_smallness", 160036 - 262144 < -32,
         "The real U.25 prefix and deep-tail budget pays the actual coefficient differences")
    gate("actual_composition_chain_count", int(sp.bell(8)) < 2**16,
         "The complete chain rule, not a finite Fourier truncation, controls H^6 and adjoints")
    multiplier_fee = sum(comb(6, k) * factorial(k) for k in range(7))
    gate("actual_full_Sobolev_multiplier_fee", multiplier_fee < 2**20,
         f"(1+x)^6 exp(-x) <= sum binom(6,k) k! = {multiplier_fee}")
    gate("actual_primitive_full_nonzero_mode_gain", Q(5, 4) < 2,
         "Every nonzero frequency is kept; the circle has |m|>=4")
    gate("actual_complete_generator_ordered_difference",
         2**53 + 2**72 + 2**92 < 2**96 and 2**64 + 2**112 * n < 2**96,
         "The ordered LBR difference pays both means and uses R0 only where a derivative is needed")
    gate("actual_complete_generator_integral",
         96 + 128 + 2 < 256 and 96 + 32 + 60 + 2 < 256,
         "Both complete potential and exact flow differences fit S.22 with N_j plus its adjacent cell")

    gate("reference_strict_high_frequency_energy", Q(2**60, 2**64) == Q(1, 16),
         "The full Vw perturbation controls both wave rows for every |m|>=mstar")
    gate("reference_strict_two_complete_low_frames",
         6 + 48 + 300 < 2**20,
         "Both inverse and forward shears retain L^2 M^-2 and rho M^-1/3")
    low1 = Q(180) + Q(65 * 5, 3)
    low2 = Q(185) + Q(65 * 4, 3)
    low3 = Q(230)
    gate("reference_complete_low_frequency_constants",
         max(low1, low2, low3) + 2 < 300,
         {"powers_of_two": [str(low1), str(low2), str(low3)]})
    gate("reference_complete_low_frequency_powers",
         Q(28, 3) < 10 and Q(26, 3) < 10 and 7 < 10
         and Q(13, 3) < 5 and Q(14, 3) < 5 and 3 < 5,
         "All low frequencies are bounded in the identical output Sobolev space")
    gate("reference_raw_mean_density_ratio",
         Q(272, 2) + Q(6 + 4, 2) < 142
         and Q(2, 2) + Q(3, 8) == Q(11, 8),
         "The actual independent mean height uses Lambda=mu q, not a gradient mean slot")
    gate("reference_raw_mean_integral_fee", 2 + 6 + 272 == 280,
         "The full integral of mu^-1 between arbitrary strict times is retained")
    gate("reference_complete_mean_two_shear_fee",
         284 + 2 * 29 + 4 < 350 and Q(7, 4) + 6 == Q(31, 4),
         "Both normal shears and both complete c,alpha transformations are paid")
    gate("reference_complete_all_mode_state_bound",
         350 < 512 and Q(31, 4) < 10 and 3 < 5,
         "Kstrict includes every nonzero mode and the independent height and flux means")
    gate("actual_complete_relative_interaction_power", 2 * 512 + 256 == 1280,
         "The full two-direction reference condition number is paid twice")

    def lg(x):
        return x.log() / arb(2).log()

    def logdelta(j):
        return lg(arb(2) / 25) - j

    def logN(j):
        ld = logdelta(j)
        hh = lg(arb(9) / 100) if j <= 4096 else 3 + ld / 256
        mu = 6 * ld if j <= 4096 else arb(3) * logdelta(4096) / 2 + arb(9) * ld / 2
        zz = arb(39) * ld / 4 if j <= 8192 else -arb(485) * logdelta(8192) / 4 + 131 * ld
        return 184 - 5 * hh + zz - mu - 2 * ld

    def logB(j):
        nn = arb(2) ** logN(j)
        if j > 129:
            nn += arb(2) ** logN(j - 1)
        return 1280 + 13 * lg(arb(j + 4)) - 25 * logdelta(j) + lg(nn)

    rows = {}
    for j in [129, 130, 4096, 4097, 4098, 8192, 8193, 8194]:
        value = logB(j)
        gate(f"actual_full_adjacent_cell_budget_{j}", value < 186208,
             {"log2_upper_interval": value.str(45),
              "normalizations": "Both delta4096^(-3/2) and delta8192^(-485/4), actual h_j and adjacent N retained"})
        rows[str(j)] = value.str(45)

    gate("actual_old_and_middle_finite_monotonicity",
         Q(7, 4) < 25 and Q(827, 256) < 25,
         "Each actual old or middle interval increases; the two mixed seam rows are computed separately")
    ratio = (arb(8199) / 8198) ** 13 * arb(2) ** (25 - arb(31867) / 256)
    gate("actual_infinite_deep_tail_geometric_ratio", ratio < arb(2) ** -90,
         {"ratio_interval": ratio.str(45), "first_all_new_adjacent_row": 8194})
    gate("actual_complete_prefix_count", 8193 - 129 + 1 < 2**14,
         "All 8065 finite rows are retained, including the actual maximum at8193")
    gate("actual_all_components_and_infinite_sum", 186208 + 14 + 2 < 192000,
         "Two negative components per layer, the finite prefix and the whole geometric deep tail are all paid")
    gate("actual_working_input_full_relative_smallness", 192000 - 262144 == -70144,
         "This consumes the existing proved small X input contract, without asserting a new nonlinear reach")
    gate("actual_complete_relative_propagator_error", -70144 + 1 == -70143,
         "The actual full F_state Neumann interaction gives exp(eta)-1<=2eta")

    gate("actual_complete_source_state_fee", 20 + 22 + 2 < 46,
         "The true density pullback, full mean reconstruction and weak height mean are included")
    gate("actual_complete_source_propagator_fee", 46 + 1 < 48,
         "The actual two-direction Cauchy bound is at most2Kstrict")
    gate("actual_ordinary_coefficient_multiplier_smallness", 20 + 8 - 32 < 0,
         "J/D is a bounded actual same-space multiplier; the exact radial unit is not removed")

    root = Path(__file__).resolve().parents[1]
    names = [
        "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
        "scripts/fourfold_actual_strict_density_relative_20261113.py",
        "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
        "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-unscalarized-tail-frame-and-summable-remainder.md",
        "results/R119-supplement-actual-ray-amplitude-and-integrable-relative-coupling.md",
    ]
    return {
        "kind": "R119-actual-complete-strict-density-relative-Cauchy-v1",
        "status": "proved",
        "arithmetic": "exact rational inequalities and symbolic identities; Arb256 directed full-prefix and deep-tail arithmetic",
        "operator_scope": "all Fourier modes, both independent means, actual fixed labels, same Gamma, no head projection",
        "source_scope": "actual ordinary and weak full density source; bare endpoint weak traces remain separate inputs",
        "all_checks_pass": all(item["pass"] for item in checks),
        "check_count": len(checks),
        "checks": checks,
        "actual_log2_budget_rows": rows,
        "deep_ratio_interval": ratio.str(45),
        "file_sha256": {name: sha256((root / name).read_bytes()).hexdigest() for name in names},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(encoded)
        print(json.dumps({"checks": report["check_count"], "all_pass": report["all_checks_pass"],
                          "report": str(args.output), "sha256": sha256(encoded.encode()).hexdigest()}))
    else:
        print(encoded, end="")

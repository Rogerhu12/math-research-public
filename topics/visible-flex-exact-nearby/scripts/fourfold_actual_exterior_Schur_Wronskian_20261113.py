#!/usr/bin/env python3
"""Exact algebra and new scalar budgets for the actual R119 exterior Schur.

No finite-mode experiment is used to replace the proof's full-frequency
estimates.  The calculation checks the new identities and their constants.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ctx.prec = 192
TOPIC = Path(__file__).resolve().parents[1]
PROOF = TOPIC / "results/R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md"
DEFAULT_OUTPUT = TOPIC / "notes/2026-11-13-R119-actual-exterior-Schur-Wronskian-budget.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    gates: list[dict[str, object]] = []

    def gate(name: str, condition: object, detail: str) -> None:
        ok = bool(condition)
        gates.append({"name": name, "passed": ok, "detail": detail})
        if not ok:
            raise AssertionError(name)

    m, r, muj, pp, A = sp.symbols("m r muj pp A", nonzero=True)
    F, Fy, Ftang, src = sp.symbols("F Fy Ftang src")
    H, Ht = sp.symbols("H Ht")
    root12 = sp.sqrt(12)
    nu = m**2 * (m**2 - 1) / 12
    k = (m**2 - 4) / root12
    mu = muj * pp / r**8
    c = r**4 / (root12 * muj)
    q = r**4 / (12 * muj)
    matrix = sp.Matrix([[k, nu / pp], [-pp, -k]])
    W = sp.Matrix([nu * H / r**4, pp * (Ht - m**2 * H) / (root12 * r**4)])
    # t = log r, y = sqrt(12) t, (log p*)_t = A + 7.
    Htt = (1-A)*Ht + A*m**2*H + (src-root12*Fy-sp.I*m*Ftang)/mu
    dWdy = sp.Matrix([
        nu * (Ht-4*H)/(root12*r**4),
        pp*((A+3)*(Ht-m**2*H) + Htt-m**2*Ht)/(12*r**4),
    ])
    unshifted = sp.simplify(dWdy-matrix*W)
    gate("unshifted_source_first_row", unshifted[0] == 0, str(unshifted[0]))
    gate("unshifted_source_second_row", sp.simplify(unshifted[1]-q*(src-root12*Fy-sp.I*m*Ftang)) == 0,
         str(unshifted[1]))
    shifted = sp.simplify(unshifted + sp.Matrix([0, 4*c*F/root12+c*Fy]) - matrix*sp.Matrix([0,c*F]))
    expected = sp.Matrix([-nu*c*F/pp, q*(src-sp.I*m*Ftang+m**2*F)])
    gate("total_flux_weak_two_rows", sp.simplify(shifted-expected) == sp.zeros(2,1), str(expected))
    gate("no_radial_derivative_of_F", all(v.diff(Fy) == 0 for v in shifted), str(shifted))
    gate("canonical_charge_from_raw_flux", sp.simplify(pp/(root12*r**4*mu)-c) == 0, str(c))
    gate("remaining_radial_charge", sp.simplify(4*c/root12+k*c-m**2*q) == 0, "c_y+k*c=m^2*q")
    e = sp.symbols("e")
    w = muj*pp/r**7
    gate("ordinary_source_identity", sp.simplify(q*w**2*e-muj*pp**2*e/(12*r**10)) == 0,
         "q*w^2*e=mu_j*p_*^2*e/(12*r^10)")

    om, ar74 = sp.symbols("omega A_R74", positive=True)
    G = sp.Matrix([[ar74,-4/m**2],[-1,4/ar74]])
    R = sp.Matrix([[4*om,-4/m**2],[1,-1/om]])
    gate("grounded_two_trace_determinant", sp.simplify(G.det()-4*(1-m**-2)) == 0, str(G.det()))
    gate("raw_two_trace_determinant", sp.simplify(R.det()+4*(1-m**-2)) == 0, str(R.det()))
    gate("opposite_Wronskian_sign", sp.simplify(G.det()+R.det()) == 0, "W_grounded=-W_raw")
    hq, pq, hh, ph, mm, coeff = sp.symbols("hq pq h ph mu coeff", nonzero=True)
    # Physical equation: (mu*h_t+F^t)_t=mu*A*m^2*h+s-im*Ftheta.
    wrprime = (pq/mm)*ph + hq*(mm*coeff*m**2*hh+src-sp.I*m*Ftang) \
        - (mm*coeff*m**2*hq)*hh - pq*(ph-F)/mm
    wrtarget = hq*(src-sp.I*m*Ftang)+(pq/mm)*F
    gate("full_weak_Wronskian_source", sp.simplify(wrprime-wrtarget) == 0, str(wrtarget))
    rho = sp.symbols("rho", nonzero=True)
    gate("physical_height_scaling", sp.simplify((w/(rho*r))*(rho*Ht) - (w/r)*Ht) == 0,
         "physical and dimensionless total raw flux have the same unit")

    al, be, de = sp.symbols("alpha beta_T delta", nonzero=True)
    ga = (al*de-1)/be
    hL, hR, pL, pR = sp.symbols("hL hR pL pR")
    rh = hR-al*hL-be*pL
    rp = pR-ga*hL-de*pL
    qL = -pL-(al*hL-hR)/be
    qR = pR-(-hL+de*hR)/be
    gate("DN_left_from_Cauchy", sp.simplify(qL-rh/be) == 0, "q_L=r_h/beta_T")
    gate("DN_right_from_Cauchy", sp.simplify(qR-rp+de*rh/be) == 0,
         "q_R=r_p-delta*r_h/beta_T")
    gate("Cauchy_from_DN_two_rows", sp.simplify(be*qL-rh) == 0 and sp.simplify(qR+de*qL-rp) == 0,
         "r_h=beta_T*q_L; r_p=q_R+delta*q_L")

    tau = Fraction(5177,400)
    loss = Fraction(88823,400)
    sigma224 = Fraction(224)-loss
    margin = Fraction(2080)-loss-Fraction(1850)
    gate("actual_connector_loss", Fraction(235)-tau == loss, str(loss))
    gate("actual_224_positive_width", sigma224 == Fraction(777,400), str(sigma224))
    gate("full_Schur_width_margin", margin == Fraction(3177,400), str(margin))
    gate("outer_Wronskian_fee", 41-447+16 == -390, "2^41 * 2^-447 * 2^16 = 2^-390")
    gate("continuous_outer_fee", -390+450 == 60, "2^-390 * 2^450 = 2^60")
    gate("nonmean_Schur_row_fee", -447+16+1 == -430, "two retained traces cost at most 2")
    gain = (-arb(4)*arb(margin.numerator)/arb(margin.denominator)).exp()/16
    gate("true_2080_inverse_margin", gain < arb(2)**(-49), str(gain))
    gate("full_reference_Green_fee", arb(2)**16 + 9*arb(2)**(-479) < arb(2)**17,
         "2^16 + 9*2^-479 < 2^17")
    gate("all_beta_outer_width_positive", Fraction(24514072)-loss > 0,
         str(Fraction(24514072)-loss))
    # Actual long length lower bound from the existing directed theorem.
    Lmin = arb("24514072.626868956")
    coth_excess = 2/((8*Lmin).exp()-1)
    gate("coth_full_actual_long", coth_excess < arb(2)**(-100), str(coth_excess))
    gate("mean_not_using_canonical_nu_zero", sp.simplify(nu.subs(m,0)) == 0,
         "mean is retained through pi_0'=s_0, H_0'=(pi_0-F0^t)/mu")

    dependencies = [
        PROOF,
        TOPIC / "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        TOPIC / "results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md",
        TOPIC / "results/R119-supplement-balanced-connector-label-domain-224.md",
        TOPIC / "results/R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md",
        TOPIC / "results/R74-actual-full-tail-robin-and-augmented-positive-cap.md",
        Path(__file__).resolve(),
    ]
    report = {
        "status": "proved_new_algebra_and_scalar_budgets",
        "object": "actual fixed Gamma0 stronger-tail reference, same true good bump",
        "passed": all(g["passed"] for g in gates),
        "gate_count": len(gates),
        "gates": gates,
        "exact_widths": {
            "connector_loss": str(loss), "width_at_beta224": str(sigma224),
            "Schur_2080_margin": str(margin), "outer_width": "L+beta-88823/400",
        },
        "operator_scope": {
            "outer_affine_source": "F_beta to dotA1_(L+beta-88823/400), norm < 2^-390",
            "continuous_weak_source": "S1_beta(J) to same external space, norm < 2^60",
            "reference_internal_Green": "F_(beta+2080) to X_beta, norm < 2^17",
            "unpaid_relative_gate": "D0^-1 E G deltaL_a on the same X_beta",
            "means": "independent total flux integral and one raw height constant retained",
            "weak_C2": "requires effective ordinary S1/S2 and actual boundary traces",
        },
        "file_sha256": {str(p.relative_to(TOPIC)): sha(p) for p in dependencies},
    }
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"passed": report["passed"], "gate_count": len(gates),
                      "report": str(args.output), "report_sha256": sha(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

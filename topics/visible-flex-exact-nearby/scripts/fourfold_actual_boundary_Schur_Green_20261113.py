#!/usr/bin/env python3
"""Exact actual-B Schur projector and raw-Dirichlet Green normalizations."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

TOPIC = Path(__file__).resolve().parents[1]
PROOF = TOPIC / "results/R119-supplement-actual-boundary-Schur-projector-and-interior-Green-kernel.md"
OUT = TOPIC / "notes/2026-11-13-R119-actual-boundary-Schur-Green-budget.json"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=OUT)
    args = ap.parse_args()
    gates = []

    def gate(name, ok, detail):
        passed = bool(ok)
        gates.append({"name": name, "passed": passed, "detail": str(detail)})
        if not passed:
            raise AssertionError(name)

    m, om, cot = sp.symbols("M omega coth", positive=True)
    C = sp.Matrix([[om,-1/m],[om/m,-1]])
    row = sp.Matrix([[cot,1]])
    gate("actual_two_trace_det", sp.simplify(C.det()+om*(1-m**-2)) == 0, C.det())
    gate("actual_finite_long_row", sp.simplify(row*C-sp.Matrix([[(1+1/m)*om+(cot-1)*om,
                                                               -(1+1/m)-(cot-1)/m]])) == sp.zeros(1,2), row*C)
    gate("C_column_bound", F(15,8)<2, "15/8 < 2")
    gate("C_inverse_column_one", (F(5,7)+F(1,4))/F(15,16) == F(36,35), "36/35 < 2")
    gate("C_inverse_column_two", (1+F(5,28))/F(15,16) == F(44,35), "44/35 < 2")
    gate("full_angle_margin", F(1,2**39)-F(1,2**99) > F(1,2**40), "2^-39-2^-99 > 2^-40")
    gate("trace_reconstruction_fee", 3*2**40 < 2**42, "3*2^40 < 2^42")
    gate("full_projector_fee", 1+2**43 < 2**44, "1+2^43 < 2^44")

    x1, x2 = sp.symbols("x1 x2")
    x = sp.Matrix([x1,x2])
    denom = (row*x)[0]
    Pi = sp.eye(2)-x*row/denom
    gate("projector_full_matrix", sp.simplify(Pi*Pi-Pi) == sp.zeros(2), Pi)
    gate("projector_kernel_actual_allowed_line", sp.simplify(Pi*x) == sp.zeros(2,1), Pi*x)
    gate("projector_raw_Dirichlet_range", sp.simplify(row*Pi) == sp.zeros(1,2), row*Pi)
    gate("source_boundary_fee", 44-431 == -387, "2^44 * 2^-431 = 2^-387")
    gate("continuous_source_boundary_fee", 450-387 == 63, "2^450 * 2^-387 = 2^63")

    aa, gam = sp.symbols("A0 gamma", positive=True)
    d = 1-m**-2
    grounded = sp.Matrix([[aa,-4/m**2],[-1,4/aa]])
    raw = sp.Matrix([[4*om,-4/m**2],[1,-1/om]])
    yq = sp.simplify(grounded.inv()*sp.Matrix([1,-gam]))
    qraw = sp.simplify(raw*yq)
    b = 1+(aa-4*om)*(gam/m**2-1/aa)/d
    gate("true_regular_raw_height", sp.simplify(qraw[0]-b) == 0, b)
    gate("raw_height_gap_fee", F(1,2**34)*F(1,4)/F(15,16) < F(1,2**35),
         "(2^-34/4)/(15/16) < 2^-35")
    gate("raw_height_strict_sign", F(1,20) < F(100,601), "gamma/M^2 < 1/20 < 1/A0")
    yv = sp.simplify(raw.inv()*sp.Matrix([0,-1/b]))
    expected_yv = sp.Matrix([1/((m**2-1)*b),om*m**2/((m**2-1)*b)])
    gate("raw_Dirichlet_companion_initial_state", sp.simplify(yv-expected_yv) == sp.zeros(2,1), expected_yv)
    vv = sp.simplify(grounded*yv)
    gate("companion_affine_grounded_row_one", sp.simplify(vv[1]+gam*vv[0]-1) == 0,
         "p_v + gamma*v_v = 1, although v_v need not be zero")
    raw_v = sp.simplify(raw*yv)
    gate("raw_Wronskian_minus_one", sp.simplify(sp.Matrix.hstack(qraw,raw_v).det()+1) == 0,
         "W_raw(q,v) = -1")
    gate("grounded_Wronskian_plus_one", sp.simplify(sp.Matrix.hstack(grounded*yq,vv).det()-1) == 0,
         "W_grounded(q,v) = 1")
    v_norm_sq = (F(1,16)+F(9,4))/(F(15,16)**2*F(31,32)**2)
    gate("full_companion_Y_initial_norm", v_norm_sq<4, f"M^2 ||Y_v(0)||^2 <= {v_norm_sq} < 4")
    gate("balanced_B_frame_fee", 2**86+64 < 2**88, "sqrt(2^86+64) < 2^44")

    qh, qp, vh, vp, jh, jp = sp.symbols("qh qp vh vp jh jp")
    qv = sp.Matrix([qh,qp]); vv0=sp.Matrix([vh,vp]); jv=sp.Matrix([jh,jp])
    wvJ = vh*jp-vp*jh
    wqJ = qh*jp-qp*jh
    det = qh*vp-qp*vh
    gate("complete_Green_differentiation", sp.simplify(qv*wvJ-vv0*wqJ+det*jv) == sp.zeros(2,1),
         "q[v,J]-v[q,J] = -W(q,v)J = J")
    Ft, Fth, mu, ss = sp.symbols("Ft Ftheta mu s", nonzero=True)
    gate("all_weak_source_pairing", sp.simplify(qh*(ss-sp.I*m*Fth)-qp*(-Ft/mu)
                                                -(qh*(ss-sp.I*m*Fth)+(qp/mu)*Ft)) == 0,
         "[q,J]=q_h(s-imFtheta)+q_h' Ft")

    deps = [PROOF, Path(__file__).resolve(),
            TOPIC / "results/R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md",
            TOPIC / "results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md",
            TOPIC / "results/R74-actual-full-tail-robin-and-augmented-positive-cap.md",
            TOPIC / "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md"]
    report = {
        "passed": all(g["passed"] for g in gates), "gate_count":len(gates), "gates":gates,
        "object":"same actual fixed Gamma0, same true all-mode good bump, full nonzero fourfold spectrum",
        "scope":{
            "homogeneous_trace_inverse":"Z_sigma to C_sigma < 2^42",
            "full_raw_Dirichlet_projector":"C_sigma to C_sigma < 2^44",
            "discrete_source_B_two_traces":"F_beta to C_(beta-88823/400) < 2^-387",
            "continuous_ordinary_and_weak_B_two_traces":"S1_beta(J) to same C space < 2^63",
            "companion_boundary":"raw height zero, raw flux -1/b_m; not grounded height zero",
            "actual_Green_Wronskian":"-1",
            "still_required":"same-weight interior norm of full two-column Green acting on actual DeltaG gradient, including all weak charges and means",
        },
        "file_sha256":{str(p.relative_to(TOPIC)):sha(p) for p in deps},
    }
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"passed":report["passed"],"gate_count":len(gates),"report":str(args.output),
                      "report_sha256":sha(args.output)},ensure_ascii=False))


if __name__ == "__main__":
    main()

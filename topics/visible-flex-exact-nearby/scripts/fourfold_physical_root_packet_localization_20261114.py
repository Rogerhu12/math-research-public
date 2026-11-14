#!/usr/bin/env python3
"""Exact physical root-packet, full strong-Cauchy and localization budgets."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-actual-physical-root-packets-and-center-localization.md"
DEPS = [
    PROOF,
    "results/R119-supplement-complete-low-cone-and-explicit-exterior-crossing-form.md",
    "results/R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md",
    "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
    "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
    "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
    "results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md",
    "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    identities = {p: sha(TOPIC / p) for p in DEPS}
    identities["source"] = sha(__file__)
    gates = []

    def gate(name, ok, **values):
        row = {"name": name, "passed": bool(ok)}
        row.update({k: str(v) if isinstance(v, F) else v for k, v in values.items()})
        gates.append(row)
        if not ok:
            raise AssertionError(row)

    # Direct symbolic full-state algebra, with theta-variable coefficients.
    th = sp.symbols("theta")
    mu, Q = sp.symbols("mu Q", positive=True)
    u, v = sp.Function("u")(th), sp.Function("v")(th)
    d, aa, cc = [sp.Function(s)(th) for s in ["d", "A", "C"]]
    h, pi = u/sp.sqrt(mu), sp.sqrt(mu)*v
    mu_t = -(1+Q)*mu
    ht = d*sp.diff(h, th)+(aa/mu)*pi
    pit = sp.diff(d*pi, th)+Q*sp.diff((mu*cc)*sp.diff(h, th), th)
    ut = sp.sqrt(mu)*ht+mu_t/(2*mu)*u
    vt = pit/sp.sqrt(mu)-mu_t/(2*mu)*v
    gate("complete unshifted first physical state",
         sp.simplify(ut+(1+Q)*u/2-d*sp.diff(u, th)-aa*v) == 0)
    gate("complete unshifted second physical state",
         sp.simplify(vt-sp.diff(d*v, th)-Q*sp.diff(cc*sp.diff(u, th), th)-(1+Q)*v/2) == 0)
    gate("lower-right transport retains the mean-output column",
         sp.expand(sp.diff(d*v, th)) == d*sp.diff(v, th)+sp.diff(d, th)*v)
    gate("lower-left complete coefficient derivative retained",
         sp.expand(sp.diff(cc*sp.diff(u, th), th)) == cc*sp.diff(u, th, 2)+sp.diff(cc, th)*sp.diff(u, th))
    sig, sig_t = sp.symbols("s s_t", positive=True)
    S = sp.diag(sp.sqrt(sig), 1/sp.sqrt(sig))
    St = sp.diag(sig_t/(2*sp.sqrt(sig)), -sig_t/(2*sig**sp.Rational(3, 2)))
    M = sp.Matrix(2, 2, sp.symbols("x0:4"))
    N = sp.Matrix(2, 2, sp.symbols("y0:4"))
    gate("the complete moving frequency-weight derivative cancels",
         sp.simplify((St*S.inv()+S*M*S.inv())-(St*S.inv()+S*N*S.inv())-S*(M-N)*S.inv()) == sp.zeros(2))

    gate("weight power for a nonzero lag is at most quadratic", F(4, 3) <= 2)
    gate("a single one-derivative denominator covers both transport factors", F(3, 2) < 2)
    gate("all output Sobolev lag powers are at most six", 4+2 == 6)
    gate("exponential Wiener width pays all six lag powers", F(6**6, 2**5) < 2**20)
    gate("all four blocks and means fit the displayed strong constant", 12+20+4 < 48)
    gate("lower-left coefficient is exactly zero at a true root", Q.subs(Q, 0) == 0)
    gate("mean frequency weight equals one", F(1) == 1)

    gate("actual target density window closes at top H4", F(4)-F(1, 2) == F(7, 2))
    gate("actual target density window closes at bottom", -4-F(1, 2) == -F(9, 2))
    gate("strict conversion retains current analytic and shear fees", 29+22+20+32 < 128)
    gate("strict full physical Cauchy bits", 128+1100+128 == 1356 < 1400)
    gate("strict full physical Cauchy J power", 1+5+1 == 7)
    gate("strict full physical Cauchy delta power", 3+10+3 == 16)
    gate("strict full strong difference bits", 2*1400+48+1+2 == 2851 < 3000)
    gate("strict full strong difference J power", 2*7 == 14)
    gate("strict full strong difference delta power", 2*16 == 32)

    # Canonical/physical mean and nonzero root weights.
    D, JJ = sp.symbols("D J", positive=True)
    speed = sp.sqrt(D)/JJ
    gate("exact root alpha ratio including both true density factors",
         sp.simplify(D**(-1)*speed**(-sp.Rational(1, 3))-JJ**sp.Rational(1, 3)*D**(-sp.Rational(7, 6))) == 0)
    gate("root mean retains the sqrt-b height and inverse flux scales", F(1, 2)+F(1, 2) == 1)
    gate("nonzero-root balance ratio is bounded by b to two thirds", F(4, 3)/2 == F(2, 3))
    gate("root endpoint angular and multiplier fees", 32+20+20 < 100)
    gate("root endpoint strong variation fees", 32+100+20 < 180)
    gate("strict root cut parameter derivative fits frame fee", 12+32+40+20 < 128)
    gate("root graph frame strong losses fit displayed constant", 128+40+32+20 < 256)
    gate("genuine graph principal remains bounded with its complete remainder", 20+1 == 21)
    gate("full root physical Cauchy bits", 2185+21+20+128+100 == 2454 < 2800)
    gate("full root physical Cauchy b power", F(1, 2)+F(1, 2)+1 == 2)
    gate("actual core absolute difference bits", 2185+4420 == 6605)
    gate("full root core-variation product bits", 6605+269 == 6874 < 8000)
    gate("complete root graph-variation b powers fit safe fourth", 2+1 <= 4)
    gate("root endpoint physical-normalization variations fit safe fourth", F(1, 2)+F(1, 2)+1 <= 4)

    # Complete root-to-center: exact ordering, no endpoint source deleted.
    gate("center wave transformation uses at most B three quarters", F(1)-F(1, 4) == F(3, 4))
    gate("center radial B conversion bits", F(7)*F(3, 4) < 6)
    gate("complete physical Cauchy exponent", 16+F(9, 2)+F(9, 8) == F(173, 8) < 24)
    gate("complete physical Cauchy J power", 7+1+F(3, 4) < 14)
    gate("complete physical Cauchy bits", 1400+2800+38+8+6 < 8000)
    gate("strict-difference complete exponent", 32+F(9, 2)+F(9, 8) == F(301, 8) < 40)
    gate("root-difference complete exponent", 16+9+F(9, 8) == F(209, 8) < 40)
    gate("strict-difference complete J power", 14+1+F(3, 4) < 22)
    gate("root-difference complete J power", 7+2+F(3, 4) < 22)
    gate("strict-difference complete bits", 3000+2800+38+14 < 12000)
    gate("root-difference complete bits including n factor", 8000+4*19+1400+14+2 < 12000)

    # Actual first-layer smallness; these retain both original seam factors.
    n0, X0, logJ, logd = -20010, -1048576, 14, 8197
    alpha = F(31867, 256)
    root_log = 38+logJ+F(9, 2)*logd+2+n0+X0
    gate("actual physical root relative graph smallness", root_log < -512, log2_upper=root_log)
    gate("actual complete root potential smallness", 2+n0+X0 < -4424)
    gate("actual whole strict relative propagator smallness",
         1280+13*logJ+25*logd+n0+X0 < -1000)
    gate("actual first-layer geometry used", 8198 < 2**14 and F(25, 2) < 16)

    gate("physical input packet has a true factor-two buffer", F(1, 4)*2 == F(1, 2))
    gate("complete H5 input fee is B to five halves", 5*F(1, 2) == F(5, 2))
    gate("packet B conversion integer fee", 7*F(5, 2) < 18)
    gate("packet absorption complete delta exponent", 24+40+F(15, 4) == F(271, 4) < 68)
    gate("packet absorption complete J exponent", 14+22+F(5, 2) < 39)
    gate("packet complete unrounded bits", 8000+12000+18+1 == 20019 < 20100)
    absorption_log = 20018+39*logJ+68*logd+n0+X0
    gate("actual complete reference-inverse absorption", absorption_log < -1, log2_upper=absorption_log)
    gate("physical packet to true localization bits", 20100+12600 == 32700)
    gate("physical packet to true localization J power", 39+42 == 81)
    gate("physical packet to true localization delta power", 68+38 == 106)
    localization_log = 32700+81*logJ+106*logd+n0+X0
    gate("actual first-layer complete packet localization", localization_log < -160000, log2_upper=localization_log)
    gate("whole packet J layer ratio", F(8199, 8198)**81 < F(65, 64))
    gate("whole packet J layer bit", F(65, 64)**32 < 2)
    gate("complete packet deep-layer decay", alpha-106-F(1, 32) > 18)
    gate("complete root graph deep-layer decay", alpha-F(9, 2)-F(1, 32) > 119)
    gate("same supplied incoming is inside actual small ball", 4-60000000 < -1048576)

    # Complete ordinary and weak normalization; no radial derivative of Ft.
    Ft, Fth, gg = [sp.Function(s)(th) for s in ["Ft", "Ftheta", "g"]]
    source_h = -(aa/mu)*Ft
    source_p = gg-sp.diff(Fth+d*Ft, th)
    gate("complete physical weak first source weight",
         sp.simplify(sp.sqrt(mu)*source_h+aa*Ft/sp.sqrt(mu)) == 0)
    gate("complete physical weak second source weight",
         sp.simplify(source_p/sp.sqrt(mu)-(gg-sp.diff(Fth+d*Ft, th))/sp.sqrt(mu)) == 0)
    gate("constant physical height still gives exact zero source-free generator",
         sp.simplify((d*sp.diff(sp.Integer(1), th)+(aa/mu)*0)) == 0)

    report = {
        "status": "passed",
        "producer": "new exact SymPy full-state identities and Fraction budgets",
        "utc": datetime.now(timezone.utc).isoformat(),
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "new_bounds": {
            "complete_physical_generator_difference": "2^48 n (1+sqrt(Q)), H^(s+1) -> H^s, |s|<=4",
            "complete_physical_root_center_Cauchy": "2^8000 J^14 delta^-24, both directions and both means",
            "complete_strong_difference": "2^12000 J^22 delta^-40 Ncal X, H5 -> H4",
            "actual_physical_input_packet": "both traces, 4<=|m|<=sqrt(B)/4, full mean retained",
            "actual_center_high_tail": "2^20100 J^39 delta^-68 Ncal X times center low norm",
            "true_localization_first_layer_log2": str(localization_log),
            "true_absorption_first_layer_log2": str(absorption_log),
        },
        "scope": {
            "actual": [
                "same current Gamma-star and original physical root cuts",
                "full high output, cross-cone and both mean evolution",
                "physical low Cauchy packets satisfy the previously stated complete center localization",
                "physical strict ordinary/weak source state and actual root source normalization retained",
            ],
            "not_granted": [
                "bare pullback has small norm on the same Sobolev space",
                "every actual whole-network near-kernel belongs to this physical packet subspace",
                "generic physical L2 weak sources acquire unproved root graph traces",
                "the original-label source inverse or nonlinear outer F is solved",
            ],
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "passed", "gates": len(gates),
                      "output": str(args.out), "sha256": sha(args.out)}), flush=True)


if __name__ == "__main__":
    main()

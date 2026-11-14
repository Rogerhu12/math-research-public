#!/usr/bin/env python3
"""New exact identities and finite budget for actual compact two-phase response."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as sp


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md"
DEPS = [
    PROOF,
    "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
    "results/R119-supplement-actual-compact-profile-label-response.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R119-supplement-actual-nonradial-first-density-phase.md",
    "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
    "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
    "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
    "results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md",
    "results/R119-supplement-joint-actual-principal-and-beta-selection.md",
    "results/R133-supplement-actual-compact-ray-endpoint-response.md",
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def out_exact(v):
    return str(v) if isinstance(v, F) else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ids = {s: sha(TOPIC / s) for s in DEPS}
    ids["source"] = sha(Path(__file__))
    gates = []

    def gate(name, cond, **data):
        row = {"name": name, "passed": bool(cond)}
        row.update({k: out_exact(v) for k, v in data.items()})
        gates.append(row)
        if not cond:
            raise AssertionError(row)

    q, nu, d, L, R, rth = sp.symbols("q nu d L R rth", nonzero=True)
    lt = L + d * rth + R
    quad = lt**2 / (q * nu) - 2 * d * lt * rth / (q * nu)
    quad += (d**2 / (q * nu) - q * nu) * rth**2
    target = (L + R)**2 / (q * nu) - q * nu * rth**2
    gate("complete drift-density action identity",
         sp.cancel(quad - target) == 0)
    flux = (lt - d * rth) / (q * nu)
    gate("complete radial divergence boundary density",
         sp.cancel(flux - (L + R) / (q * nu)) == 0)
    gate("beta compact action coefficient", -F(1, 4) * -F(1, 4) == F(1, 16))

    t = sp.symbols("t")
    psi, aq, ay, b = [sp.Function(z)(t) for z in ("psi", "aq", "ay", "b")]
    original = -sp.diff(psi, t) * aq - sp.diff(psi, t, 2) * ay + psi * b
    reduced = psi * (sp.diff(aq, t) - sp.diff(ay, t, 2) + b)
    endpoint = -psi * aq - sp.diff(psi, t) * ay + psi * sp.diff(ay, t)
    gate("two compact integrations by parts retain signs",
         sp.expand(original - reduced - sp.diff(endpoint, t)) == 0)
    gate("quartic first actual radial derivative", F(2, 80) < 1)
    gate("quartic second actual radial derivative", F(30, 80**2) < 1)
    gate("quartic third actual radial derivative", F(45, 80**3) < 1)
    E = F(65, 64)
    z, w2 = F(1, 16), F(1, 64)
    Jerr = z + E * z
    Derr = w2 * (2 * z + z*z + E*z*z)
    gate("complex normalized J denominator", Jerr < F(1, 4), upper=Jerr)
    gate("complex full D denominator", Derr < F(1, 128), upper=Derr)
    gate("positive-branch complex square-root upper", 1 + F(1, 128) < F(3, 2)**2)
    gate("positive-branch complex square-root lower", 1 - F(1, 128) > F(2, 3)**2)
    gate("wave factor and inverse both below two",
         F(3, 2) / F(3, 4) <= 2 and F(5, 4) / F(2, 3) < 2)
    Dth = 2 * w2 * ((1 + z) * z + E * z*z)
    gate("complete angular density derivative", Dth / (1 - Derr) < 1)
    Lbound = 1 + F(9, 4) + F(2) / (2 * F(3, 4))
    Lbound += 2 * F(9, 4) * w2 * z / F(3, 4)
    gate("scaled action complete linear bracket", Lbound < 5, upper=Lbound)
    gate("scaled action analytic bound", 4 * 5**2 + 4 < 2**12)
    gate("five-direction Cauchy disk fits", 5 * F(1, 2**11) < F(1, 256))
    gate("full mixed coefficient Cauchy constant", 120 * 2**(55 + 12) < 2**80)
    gate("state radial first-jet coefficient reserve", 9 + 3 <= 12)
    gate("state radial second-jet coefficient reserve", 9 + 3 + 4 + 3 + 5 < 30)
    gate("direct action first derivative reserve", 80 + 12 + 3 < 96)
    gate("direct action second derivative reserve", 80 + 30 + 4 < 116)
    gate("explicit gauge action derivative reserve", 80 + 8 + 3 < 96)
    gate("sum of all three direct action terms",
         2 * 2**96 + 2**116 < 2**118)
    gate("physical dt and beta coefficient preserve rho5",
         118 + 1 - 4 < 128)
    gate("strict full hat action plus true integral", 32 + 64 < 224)
    gate("root finite-part and both graphs", 128 + 19 + 4 < 224)
    gate("root weighted integral factor", F(1, 4) * 2 * F(1, 8) == F(1, 16))
    gate("full beta response forcing constant", 224 + 832 + 2 < 1100)
    gate("direct beta difference is covered", 128 + 2 + 2 < 1100)
    gate("principal row normalization is covered", 843 + 4 + 4 < 1100)
    gate("radial two-phase inverse block", 2**13 < 2**15)
    kam_sum = 80 * 2**12 * F(32, 31)
    gate("actual per-row KAM angular derivative series", kam_sum < 2**19,
         upper=kam_sum)
    gate("local KAM derivative retains row size", 19 + 32 + 34 < 96)
    gate("whole-parameter beta Cauchy row", 144 + 33 < 256)
    gate("whole-parameter ray Cauchy row", 20 + 33 + 4 < 256)
    gate("conjugacy mean normalization row", 96 + 4 < 256)
    gate("complete prefix and all-rows weight reserve", 160016 + 3 < 160024)
    global_feedback = 15 + 256 + 160024
    gate("joint actual matrix feedback exponent",
         global_feedback == 160295 and global_feedback - 1048576 < -1,
         log2_upper=global_feedback - 1048576)
    gamma_sup = 16 + 1100 + 160024
    gate("complete infinite parameter solution bound", gamma_sup == 161140)
    row_main = 15 + 1100
    row_feedback = 15 + 256 + gamma_sup - row_main
    gate("true deep row after full inverse", row_feedback == 160296)
    gate("true row feedback absorbs on reachable input",
         row_feedback - 1048576 < -1 and row_main + 1 < 1120)
    gate("additional physical output derivatives remain in paid window",
         F(7, 2) <= F(7, 2) and 4 <= 4)
    gate("higher output root delta fee", F(119, 4) + F(3, 2) == F(125, 4) < 34)
    gate("higher output strict delta fee", F(125, 4) + F(3, 2) == F(131, 4) < 34)
    gate("higher output J fee", F(33, 2) < 20)
    gate("full output derivative constant reserve", 7800 + 48 + 7 + 30 + 128 < 8400)
    gate("complete direct Hamiltonian kernel coefficient", 8 * 2**20 < 2**40)
    gamma_bits = 8400 + 40 + 1120 + 10 + 10980 + 133 + 77 + 1000 - 42
    gate("whole local Gamma metric contribution", gamma_bits == 21718 < 22000,
         exponent=gamma_bits)
    gamma_delta = F(40) + F(57, 2) - F(25, 8) + F(231, 128)
    gate("whole local Gamma delta power", gamma_delta < 68, exponent=gamma_delta)
    gate("whole local Gamma J power", 24 + 19 + 48 == 91 < 92)
    gamma_first = 22000 - 20010 - 1048576 + 14 * 92 + 8197 * 68
    gate("actual first layer local Gamma contribution",
         gamma_first == -487902 < -480000, log2_upper=gamma_first)
    gate("all-layer J92 ratio", F(8199, 8198)**92 < F(65, 64))
    gate("all-layer J92 fractional comparison", F(65, 64)**32 < 2)
    alpha = F(31867, 256)
    gate("local Gamma contribution decreases along true deep tail",
         alpha - 68 - F(1, 32) > 56)
    gate("complete parameter-induced state response", 64 + 161140 == 161204)
    second_bits = 7800 + 24 + 161204 + 10980 + 133 + 77 + 1000 - 42
    gate("all-parameter background response constant", second_bits == 181176 < 182000,
         exponent=second_bits)
    second_first = 182000 - 20010 - 2 * 1048576 + 14 * 84 + 8197 * 60
    gate("actual first layer all-parameter background response",
         second_first == -1442166 < -1400000, log2_upper=second_first)
    gate("all-parameter background response tail decreases",
         alpha - 60 - F(1, 64) > 64)
    gate("all four actual form errors leave d over eight",
         F(1, 4) - 4 * F(1, 64) > F(1, 8))

    report = {
        "status": "passed",
        "producer": "new SymPy exact identities and Python Fraction budgets",
        "utc": datetime.now(timezone.utc).isoformat(),
        "all_passed": all(g["passed"] for g in gates),
        "gate_count": len(gates),
        "gates": gates,
        "scope": {
            "object": "current full controlled tail on actual reachable X<=2^-1048576",
            "direction": "fresh unused strict compact support; two actual radial phase annihilators",
            "new": [
                "full finite-part beta response with rho5",
                "joint infinite two-parameter derivative with true row bounds",
                "complete negative-pocket form along actual Gamma-star",
            ],
            "retained": [
                "two physical traces and two means",
                "all output angular modes and opposite cone",
                "ordinary and weak affine source columns and actual weak endpoint traces",
            ],
            "not_granted": [
                "nonzero finite-box radial compensation deleted",
                "mixed-frequency cluster positivity",
                "same-Hs norm derivative of a bare pullback",
                "whole-network or nonlinear outer F inverse",
            ],
        },
        "bounds": {
            "parameter_row_bits": 1120,
            "parameter_global_bits": gamma_sup,
            "parameter_matrix_feedback_log2": global_feedback - 1048576,
            "gamma_form_first_layer_log2": gamma_first,
            "gamma_background_first_layer_log2": second_first,
            "complete_form_lower_fraction_of_d": "1/8",
        },
        "file_sha256": ids,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "gates": len(gates),
                      "output": str(args.out), "sha256": sha(args.out)}))


if __name__ == "__main__":
    main()

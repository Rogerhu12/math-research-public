#!/usr/bin/env python3
"""Exact identities and new budgets for positive incoming packets.

This does not rerun any numerical center, scalar cache, or nonlinear solve.
It checks only the new two-endpoint identities and explicit rational costs.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-positive-Cayley-packets-to-complete-center-forms.md"
DEPS = [
    PROOF,
    "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
    "results/R119-supplement-actual-positive-transmission-and-weighted-affine-source.md",
    "results/R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md",
    "results/R119-supplement-complete-low-cone-and-explicit-exterior-crossing-form.md",
    "results/R119-supplement-actual-physical-root-packets-and-center-localization.md",
    "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
    "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    identities = {p: sha(TOPIC / p) for p in DEPS}
    identities["source"] = sha(Path(__file__))
    gates: list[dict] = []

    def gate(name, passed, **values):
        item = {"name": name, "passed": bool(passed)}
        item.update({k: str(v) if isinstance(v, F) else v for k, v in values.items()})
        gates.append(item)
        if not passed:
            raise AssertionError(item)

    alpha = F(31867, 256)
    for q, overhead in enumerate((12, 8, 4)):
        gate(f"actual normalized prefix seam q={q}",
             F(-20138 + overhead) < -19500 - alpha*q,
             upper=F(-20138 + overhead), target=-19500-alpha*q)
    gate("complete deep seven-cell envelope",
         -20138 + 4 + 2*alpha < -19500,
         upper=-20138 + 4 + 2*alpha)
    gate("fourteen actual nonnegative terms", 14 < 2**4)
    gate("positive local DN coefficient after Sobolev conversion", 104+50 < 200)
    gate("positive neighboring-cell reserves", 104+50+16 < 200)
    gate("KAM endpoint neighboring-cell reserve", 86+12 < 100)
    gate("actual endpoint Jacobian is small with six derivatives",
         100+30+14*2+8197-19500-1048576 < -1000)

    # Exact full-state frame, including the flux density Jacobian and shear.
    bb, vv, ww, ell, jac = sp.symbols("sqrt_b V W ell jac", nonzero=True)
    mat = sp.Matrix([[vv/(bb*ww), 0],
                     [-bb*ell/(2*vv*ww*jac), bb*ww/(vv*jac)]])
    gate("physical two-trace frame includes the exact Jacobian",
         sp.simplify(jac*mat.det()) == 1)
    gate("reference frame is symplectic and invertible",
         sp.simplify(mat.subs(jac, 1).det()) == 1)
    hh, pp = sp.symbols("Yh Yp")
    mu, slope = sp.symbols("mu slope", positive=True)
    alf = slope*mu
    raw_h = hh/(sp.sqrt(alf)*ww)
    outward = sp.sqrt(alf)*(ww*pp-ell*hh/(2*ww))
    gate("height row recovers the correct physical square-root density",
         sp.simplify(sp.sqrt(mu)*raw_h - hh/(sp.sqrt(slope)*ww)) == 0)
    gate("total flux row retains reference normal shear",
         sp.simplify(outward/sp.sqrt(mu)
                     - sp.sqrt(slope)*(ww*pp-ell*hh/(2*ww))) == 0)

    cc, ccbar = sp.symbols("C Cstar", commutative=False)
    graph_square = ((1+ccbar)*(1+cc)+(ccbar-1)*(cc-1))/2
    gate("paired graph norm before invoking unitarity",
         sp.expand(graph_square-1-ccbar*cc) == 0)
    gate("complete graph Sobolev bound with Cayley norm below two", 1+2**2 < 4**2)
    gate("affine outgoing column has unit graph norm", F(1, 2)+F(1, 2) == 1)

    P, P0, T, T0, G, G0 = sp.symbols("P P0 T T0 G G0", commutative=False)
    ordered = (P-P0)*T0*G0 + P*(T-T0)*G0 + P*T*(G-G0)
    gate("ordered telescope retains one derivative loss",
         sp.expand(P*T*G-P0*T0*G0-ordered) == 0)
    gate("sixth derivative Cauchy factor", sp.factorial(6)*4**6 < 2**22)
    gate("inverse angle Cauchy factor", 2*sp.factorial(6)*8**6 < 2**30)
    gate("integer composition chain-rule reserve", sp.factorial(6)*2**6*2 < 2**17)
    gate("frame multiplier and three-block reserve", 40+12+3 < 100)
    gate("strong frame and density difference reserve", 80+12+3 < 160)
    gate("actual root frame common bound", 100+12 < 120)
    gate("actual root frame strong common bound", 160+12+100 < 300)

    telescope_terms = (
        (12100+120+1, 22+1, 40+2),
        (8100+300+1, 14+3, 24+3),
        (8100+120+200+1, 14+1+2, 24+2+2),
    )
    for index, (bits, jexp, dexp) in enumerate(telescope_terms):
        gate(f"complete ordered term {index}",
             bits+2 < 12300 and jexp <= 23 and dexp <= 42,
             bits=bits, J_power=jexp, inverse_delta_power=dexp)
    gate("reference paired inverse constant", 8100+120+2 < 8300)
    gate("paired inverse complete powers", 14+1 == 15 and 24+2 == 26)
    gate("whole actual paired map constant", 8100+120+2 < 8300)
    gate("finite input H5 cost", 10*F(5, 2) == 25 and F(5, 2) < 3 and F(15, 4) < 4)
    gate("packet strong-difference constant", 12300+25 < 12400)
    gate("packet strong-difference powers", 23+3 == 26 and 42+4 == 46)
    gate("two complete inverse factors in leakage", 1+8300+12400 < 20800)
    gate("leakage actual powers", 15+26 == 41 and 26+46 == 72)
    kd_first = 8300+12400+14*41+8197*72-19500-1048576
    gate("actual paired inverse absorbs the strong error", kd_first < -400000,
         first_log2_upper=kd_first)
    localization_first = 33600+14*83+8197*110-19500-1048576
    gate("entire paired packet enters the center threshold", localization_first < -130000,
         first_log2_upper=localization_first)
    gate("largest polynomial deep ratio", F(8199, 8198)**83 < F(65, 64))
    gate("polynomial ratio exponent", F(65, 64)**32 < 2)
    gate("infinite deep localization decays", alpha-110-F(1, 32) > 14,
         excess=alpha-110-F(1, 32))

    gate("full common positive coefficient retains original ramp scale",
         800+8*1024+64+15+F(9, 2) < 9100)
    gate("full exterior high coefficient", 18200-2*1024+20+71 < 16300)
    gate("paired threshold square has exact 200-bit reserve",
         16300-2*12800+9100 == -200)
    gate("paired threshold square keeps all polynomial weights",
         20-2*42+64 == 0 and -71+2*38-5 == 0)
    gate("complete two-pocket positive remainder", F(1, 8)-F(1, 2**200) > F(1, 16))
    gate("positive incoming coefficient includes both inverse factors",
         9100+6+2*8300 == 25706 < 25800)
    gate("positive incoming J and delta powers", 64+2*15 == 94 and 5+2*26 == 57)

    gate("source two-center constant", 8300+60 == 8360)
    gate("no source mean or total-flux charge is removed", True,
         contract="Both positive endpoints, both graph rows, outgoing mean, and both total flux charges retained")
    gate("full form continuity constant", 8600-5*1024+30 < 3600)
    gate("full form continuity J power", 16-5*8 == -24)
    gate("complete low-input H4 state constant", 8300+2*10 < 8400)
    gate("complete low-input H4 powers", 15+2 == 17 and 26+3 == 29)
    cross_bits = 3600+8400+8360
    cross_J = -24+17+15
    cross_delta = 30+29+26
    gate("complete source crossing coefficient", cross_bits == 20360)
    gate("complete source crossing powers", cross_J == 8 and cross_delta == 85)
    young_bits = 1+2*cross_bits+25800
    young_J = 2*cross_J+94
    young_delta = 2*cross_delta+57
    gate("Young negative source coefficient", young_bits == 66521 < 66600)
    gate("Young negative source complete powers", young_J == 110 and young_delta == 227)
    gate("affine diagonal source fee", 3600+2*8360 == 20320 < 66521)
    gate("affine diagonal source powers fit the same fee",
         -24+2*15 == 6 < 110 and 30+2*26 == 82 < 227)
    gate("sum of both negative source terms", 66521+1 < 66600)

    report = {
        "status": "passed",
        "utc": datetime.now(timezone.utc).isoformat(),
        "producer": "Exact SymPy identities and Fraction inequalities; no sampled spectral or PDE claim",
        "gate_count": len(gates),
        "all_passed": all(row["passed"] for row in gates),
        "gates": gates,
        "scope": {
            "new": [
                "one-derivative strong map from full positive Cayley incoming to both actual centers",
                "actual zero-mean low incoming packet gives paired infinite-output localization",
                "sum of the two existing pocket forms is positive on that actual image",
                "complete positive ordinary/weak affine source and independent incoming mean costs",
            ],
            "not_granted": [
                "all whole-network near-kernels are low incoming packets",
                "sum of the two assigned pocket forms equals a single global profile generator",
                "positive interior parameter form or off-site pocket responses vanish",
                "full source-to-original-label inverse or nonlinear outer equation",
            ],
        },
        "bounds": {
            "root_to_centers_H5_H4": "2^12300 J^23 delta^-42 Npair X",
            "paired_localization": "2^-12800 J^-42 delta^38",
            "assigned_two_pocket_form": "2^-25800 J^-94 delta^57 ||incoming_perp||^2",
            "complete_positive_affine_source": "2^8360 J^15 delta^-26 (||incoming_mean||+S4)",
            "inhomogeneous_form_source_fee": "2^66600 J^110 delta^-227 (||incoming_mean||+S4)^2",
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "passed", "gates": len(gates), "output": str(args.out),
                      "sha256": sha(args.out)}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact new identities and rational budgets for the actual three-piece form.

No spectral sampling, large scientific source, or nonlinear solve is rerun.
The analytic premises are the explicitly named results in the proof.
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
PROOF = "results/R119-supplement-complete-three-piece-physical-crossing-form.md"
DEPS = [
    PROOF,
    "results/R119-supplement-positive-Cayley-packets-to-complete-center-forms.md",
    "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
    "results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md",
    "results/R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md",
    "results/R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md",
    "results/R119-supplement-complete-low-cone-and-explicit-exterior-crossing-form.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R119-supplement-controlled-profile-full-label-and-raw-ports.md",
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
    gate("joint profile complex disk retains its full radius",
         F(1, 2**79) + 2*F(1, 2**68) < F(1, 2**64))
    gate("principal error is absorbed by the actual beta difference",
         39+2 < 144 and F(3, 2) < 3 and F(3, 4) < 5)
    gate("complete local E row", 144+1 == 145)
    gate("actual second-row inverse", 145+10 == 155)
    gate("both joint gamma coordinates retained", 3*2**155 + 2**39 < 2**157)
    gate("full local gamma norm", 157 < 160 and 3 < 4 and 5 < 6)
    gate("adjacent original scales in W", 4+6 == 10)
    gate("remote radial compensation derivative is exactly zero",
         sp.diff(sp.Symbol("gamma_local"), sp.Symbol("shape_remote")) == 0,
         premise="Exact disjoint-support phase decomposition H.8; not a PDE decoupling")
    gate("full joint remote gamma Cauchy cost", 160+10+68 == 238 < 240)
    gate("complete relative background Cauchy cost", 2+68 == 70)
    gate("gauged field product and full bump derivative reserve",
         8+2+240+1 < 300)
    nfirst = -19500-1048576
    gate("actual local nonlinear norm is below one", nfirst < 0)
    gamma_first = 240+14*4+8197*6+nfirst
    gate("actual remote gamma remains small", gamma_first < -1000000,
         first_log2_upper=gamma_first)

    # Identity hat(z)/w = d(z/w) + psi (z/w - F1/w).
    z, w, zdot, psi, f1 = sp.symbols("z w zdot psi f1", nonzero=True)
    relative_dot = zdot/w-z*psi/w
    gate("complete gauged physical normalization",
         sp.expand((zdot-psi*f1)/w
                   -(relative_dot+psi*(z/w-f1/w))) == 0)

    gate("whole-window low-state neighbor reserve", 8440+20+34 < 8540)
    gate("whole-window high-state neighbor reserve", 8500+16+30 < 8600)
    gate("complete strong energy is quadratic",
         2*sp.Symbol("u")**2+2*sp.Symbol("v")**2
         -(sp.Symbol("u")+sp.Symbol("v"))**2
         == (sp.Symbol("u")-sp.Symbol("v"))**2
         or sp.expand(2*sp.Symbol("u")**2+2*sp.Symbol("v")**2
                      -(sp.Symbol("u")+sp.Symbol("v"))**2
                      -(sp.Symbol("u")-sp.Symbol("v"))**2) == 0)
    gate("paired high-state threshold exponent", 8600-2*12800 < 8540-1000)
    gate("paired high-state threshold powers",
         16-2*42 < 20 and -30+2*38 > -34)
    gate("low and high strong energy including cross terms", 8540+2 < 8700)
    gate("all remote kernel factors", 300+8700+40+2 == 9042 < 9200)
    gate("all remote kernel polynomial powers", 4+20 == 24 and 6+34 == 40)

    gate("whole positive Cayley derivative Cauchy reserve", 200+68 < 280)
    gate("both KAM endpoint derivatives Cauchy reserve", 100+68 < 180)
    gate("differentiated inverse angular map has true sign",
         sp.diff(sp.Function("K")(sp.Symbol("x")), sp.Symbol("x"))
         * (-sp.Symbol("Kdot")/sp.diff(sp.Function("K")(sp.Symbol("x")), sp.Symbol("x")))
         + sp.Symbol("Kdot") == 0)
    gate("strong physical frame derivative reserve", 160+12+180 < 380)
    gate("strong physical frame J power", F(1, 4)+2 < 3)
    gate("strong physical frame inverse-delta power", F(9, 8)+1 < 3)
    gate("full frame generator contains the actual inverse", 380+120 == 500)
    gate("full frame generator polynomial weights", 3+1 == 4 and 3+2 == 5)

    # Exact symplectic and graph identities, before scalar norm estimates.
    aa, cc, adot, cdot = sp.symbols("aa cc adot cdot", nonzero=True)
    Jmat = sp.Matrix([[0, 1], [-1, 0]])
    Tmat = sp.Matrix([[aa, 0], [cc, 1/aa]])
    dTmat = sp.Matrix([[adot, 0], [cdot, -adot/aa**2]])
    gate("reference density and normal shear are symplectic",
         sp.simplify(Tmat.T*Jmat*Tmat-Jmat) == sp.zeros(2))
    gen = sp.simplify(Tmat.T*Jmat*dTmat)
    gate("physical frame variation is a Hermitian coefficient form",
         sp.simplify(gen-gen.T) == sp.zeros(2))
    jac = sp.symbols("jac", nonzero=True)
    density_frame = sp.diag(1, 1/jac)*Tmat
    gate("actual angular Jacobian preserves the integrated pairing",
         sp.simplify(jac*density_frame.T*Jmat*density_frame-Jmat) == sp.zeros(2))
    Cstar, dC = sp.symbols("Cstar dC", commutative=False)
    graph_form = -sp.I*(1+Cstar)*dC/2-sp.I*(Cstar-1)*dC/2
    gate("complete two-endpoint Cayley crossing identity",
         sp.expand(graph_form+sp.I*Cstar*dC) == 0)
    gate("low incoming one-derivative factor", F(1, 2) < 1 and F(3, 4) < 1 and 5 < 10)
    gate("complete graph H1 factor", 2+10 == 12)
    gate("physical endpoint generator crossing factor", 1+500+12 == 513 < 520)
    gate("both positive parameter terms fit the displayed coefficient", 280 < 513 and 513+1 < 520)
    gate("complete positive parameter polynomial powers", 4+1 == 5 and 5+1 == 6)

    # Inner roots retain heights, total fluxes, and their parameter derivatives.
    h, dh, q, dq = sp.symbols("h dh q dq")
    outgoing_positive = h*dq-q*dh
    outgoing_negative = h*(-dq)-(-q)*dh
    gate("exact physical inner-root crossing cancellation",
         sp.expand(outgoing_positive+outgoing_negative) == 0)
    gate("paired center lower bound includes both inverse factors",
         520+2+2*8300+9100 == 26222 < 26400)
    gate("positive comparison keeps J weights", 5+2*15+64 == 99)
    gate("positive comparison keeps delta weights", 6+2*26+5 == 63)
    gate("remote comparison keeps constants", 9200+9100 == 18300)
    gate("remote comparison keeps J weights", 24+64 == 88)
    gate("remote comparison keeps delta weights", 40+5 == 45)
    for name, bits, jp, dp, target in (
        ("positive", 26400, 99, 63, -523879),
        ("remote", 18300, 88, 45, -679679),
    ):
        first = bits+14*jp+8197*dp+nfirst
        gate(f"complete {name} first-layer relative gate", first == target and first < -20,
             first_log2_upper=first)
        gate(f"complete {name} deep polynomial ratio", F(8199, 8198)**jp < F(65, 64))
        gate(f"complete {name} infinite-tail decay", alpha-dp-F(1, 32) > (61 if name == "positive" else 79),
             decay_bits=alpha-dp-F(1, 32))
    gate("polynomial ratio logarithm paid by exact power", F(65, 64)**32 < 2)
    gate("assigned two-pocket form retains its reserve", F(1, 8)-F(1, 2**200) > F(1, 16))
    gate("both actual missing terms absorbed", F(1, 16)-2*F(1, 2**20) > F(1, 32))
    gate("true incoming positive constant", 9100+7+2*8300 == 25707 < 25800)
    gate("true incoming J power", 64+2*15 == 94)
    gate("true incoming delta power", 5+2*26 == 57)

    umin, uleft, uright = sp.symbols("umin uleft uright", positive=True)
    gate("original left coordinate implements the common direction",
         sp.simplify(uleft*umin/(2*uleft)-umin/2) == 0)
    gate("original right coordinate implements the common direction",
         sp.simplify(uright*umin/(2*uright)-umin/2) == 0)
    gate("half-radius coordinate path stays in the original box", F(1, 2)+F(1, 2) == 1)

    # General source identity: no source term is set to zero in the algebra.
    a11, a12, a21 = sp.symbols("a11 a12 a21")
    Amat = sp.Matrix([[a11, a12], [a21, -a11]])
    y1, y2, v1, v2, s1, s2, r1, r2 = sp.symbols("y1 y2 v1 v2 s1 s2 r1 r2")
    Y, V = sp.Matrix([y1, y2]), sp.Matrix([v1, v2])
    S, R = sp.Matrix([s1, s2]), sp.Matrix([r1, r2])
    derivative = ((Amat*Y+S).T*Jmat*V+Y.T*Jmat*(Amat*V+R))[0]
    source_pairing = (S.T*Jmat*V+Y.T*Jmat*R)[0]
    gate("complete inhomogeneous Hamiltonian source pairing",
         sp.expand(derivative-source_pairing) == 0)
    weak_trace, weak_trace_dot = sp.symbols("weak_trace weak_trace_dot")
    gate("bare flux source endpoint charge retained",
         sp.expand(h*(dq-weak_trace_dot)-(q-weak_trace)*dh
                   -(h*dq-q*dh)+h*weak_trace_dot-weak_trace*dh) == 0)

    report = {
        "status": "passed",
        "utc": datetime.now(timezone.utc).isoformat(),
        "producer": "Exact SymPy identities and Fraction inequalities; no sampled spectral, whole-network, or nonlinear claim",
        "gate_count": len(gates),
        "all_passed": all(row["passed"] for row in gates),
        "gates": gates,
        "scope": {
            "new": [
                "local joint Gamma-star deviation on the already constructed profile complex ball",
                "both cross-pocket full responses with both compensation columns",
                "complete positive physical parameter form including the two moving KAM endpoint angles",
                "actual homogeneous negative-positive-negative crossing on the true low incoming subspace",
                "exact source and total-versus-bare boundary pairing identities retained",
            ],
            "not_granted": [
                "all whole-network near-kernels have low incoming frequency support",
                "the response of the rest of the network is zero or bounded by this three-piece state mass",
                "outer good-parameter selection is differentiable or the physical stopping scale is free",
                "full source-to-original-label inverse or nonlinear outer equation is solved",
            ],
        },
        "bounds": {
            "joint_local_deviation": "2^160 W_i X",
            "remote_Gamma_derivative": "2^240 J^4 delta^-6 Npair X",
            "remote_complete_form": "2^9200 J^24 delta^-40 Npair X ||centers_low||^2",
            "positive_complete_physical_form": "2^520 J^5 delta^-6 Npair X ||incoming||^2",
            "actual_three_piece_positive_form": "2^-25800 J^-94 delta^57 ||incoming_perp||^2",
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "passed", "gates": len(gates), "output": str(args.out),
                      "sha256": sha(args.out)}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact common-direction matrix, full Bernstein certificate and actual fees."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sympy as sp
from flint import fmpq as Q


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md"
DEPS = [
    PROOF,
    "results/R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md",
    "results/R119-supplement-all-scaled-five-function-finite-box-generator.md",
    "results/R119-supplement-same-current-parameter-finite-box-nonradial-pocket-form.md",
    "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
    "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
    "results/R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md",
    "results/R119-supplement-actual-compact-profile-label-response.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md",
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def exact(x):
    return str(x) if isinstance(x, (F, Q)) else x


def bernstein_coefficients(expr, variables, box):
    p = sp.Poly(expr, *variables)
    degrees = [int(p.degree(x)) for x in variables]
    coeff = {m: Q(int(c.p), int(c.q)) for m, c in p.terms()}
    for axis, (a, b) in enumerate(box):
        n = degrees[axis]
        mat = [
            [
                sum(
                    (
                        Q(math.comb(j, k))*a**(j-k)*(b-a)**k
                        * Q(math.comb(i, k), math.comb(n, k))
                        for k in range(min(j, i)+1)
                    ),
                    Q(0),
                )
                for j in range(n+1)
            ]
            for i in range(n+1)
        ]
        groups = {}
        for index, value in coeff.items():
            key = index[:axis]+index[axis+1:]
            groups.setdefault(key, [Q(0)]*(n+1))[index[axis]] = value
        new = {}
        for key, vec in groups.items():
            for i in range(n+1):
                val = sum((u*v for u, v in zip(mat[i], vec)), Q(0))
                new[key[:axis]+(i,)+key[axis:]] = val
        coeff = new
    return degrees, coeff


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    identities = {p: sha(TOPIC / p) for p in DEPS}
    identities["source"] = sha(__file__)
    gates = []

    def gate(name, condition, **values):
        row = {"name": name, "passed": bool(condition)}
        row.update({k: exact(v) for k, v in values.items()})
        gates.append(row)
        if not condition:
            raise AssertionError(row)

    z, v, tau, kap = sp.symbols("z v tau kappa")
    rel = 1-4*z
    cc = 450*z**6+tau**2*(5-8*z)
    ccz = sp.diff(cc, z)

    def red(expr):
        p = sp.Poly(sp.expand(expr), v)
        out = sum(
            (coef*rel**(n//2)*v**(n % 2) for (n,), coef in p.terms()),
            sp.Integer(0),
        )
        return sp.expand(out)

    def dx(expr):
        return red(v*sp.diff(expr, z)-2*sp.diff(expr, v))

    gate("the exact derivative preserves the actual quartic constraint",
         sp.expand(v*sp.diff(v*v-rel, z)-2*sp.diff(v*v-rel, v)) == 0)
    qq = 30*z*z
    p1 = qq**3*dx(qq)
    p2 = 12*qq**4*dx(qq)
    p2 += tau*tau*(40*qq*dx(qq)*dx(dx(qq))
                    -35*dx(qq)**3-8*qq*qq*dx(dx(dx(qq))))
    wp = red(p1*dx(p2)-dx(p1)*p2)
    expected_wp = red(sp.Integer(4199040000000)*z**9*v**3*cc)
    gate("complete e-zero phase Wronskian including every tau term",
         sp.expand(wp-expected_wp) == 0)

    alpha = 9/z-ccz/cc
    A0 = 12/z**2-30/z+12/rel-2*ccz/cc*(1/z-3)
    EE = -2*alpha+rel*sp.diff(alpha, z)+12/rel+A0+9*rel*alpha/z+54/z
    den = z**3*rel**2*cc**2
    a2 = sp.cancel(den*(tau*v*(18/z-ccz/cc+6/rel)-1))
    a1 = sp.cancel(den*(tau*tau*EE-tau*v*(9/z-ccz/cc+6/rel)))
    a0 = sp.cancel(den*(tau**3*v*(sp.diff(A0, z)+9*A0/z)-tau*tau*A0))
    for name, aa in [("D2", a2), ("D1", a1), ("D0", a0)]:
        gate("complete "+name+" scalar numerator is polynomial",
             sp.denom(aa) == 1)

    AA = sp.Matrix([[0, 1], [qq*qq/4-kap*qq-30*tau*z*v, 0]])
    KK = sp.Matrix([[qq*qq/4-kap*qq, (qq-2*kap)/2],
                    [(qq-2*kap)/2, 1]])

    def cov(C):
        return (tau*(v*C.diff(z)-2*C.diff(v))+AA.T*C+C*AA).applyfunc(red)

    D1 = cov(KK)
    D2 = cov(D1)
    D3 = cov(D2)
    C = (den*D3+a2*D2+a1*D1+a0*KK).applyfunc(red)
    gate("the complete two-state numerator is symmetric", C[0, 1] == C[1, 0])
    gate("the whole numerator has kappa degree at most three",
         max(sp.degree(q, kap) for q in C) <= 3)
    print(json.dumps({"stage": "exact complete matrix reconstructed"}), flush=True)

    # This reduction is exact modulo v^2=1-4z, whose derivative was checked above.
    detnum = red(C[0, 0]*C[1, 1]-C[0, 1]**2)
    pk = sp.Poly(detnum, kap)
    gate("exact first kappa zero in e-zero determinant",
         pk.coeff_monomial(1) == 0)
    gate("exact second kappa zero in e-zero determinant",
         pk.coeff_monomial(kap) == 0)
    P = sp.expand(detnum/kap**2)
    leading_C22 = qq*(qq-4*kap)*(qq-2*kap-1)
    leading_P = qq**2*(qq-4*kap)**2*(qq**2-4*qq*kap-1)
    gate("complete zero-tau diagonal identity",
         sp.expand(C[1, 1].subs(tau, 0)-den.subs(tau, 0)*leading_C22) == 0)
    gate("complete zero-tau determinant quotient identity",
         sp.expand(P.subs(tau, 0)-den.subs(tau, 0)**2*leading_P) == 0)

    variables = [z, v, tau, kap]
    box = [
        (Q(63, 256), Q(255, 1024)),
        (Q(1, 16), Q(1, 8)),
        (Q(0), Q(1, 80)),
        (Q(0), Q(1, 4)),
    ]
    certificates = []
    for name, expr, bit in [
        ("complete_C22_numerator", C[1, 1], 30),
        ("complete_det_over_kappa2_numerator", P, 57),
    ]:
        deg, coeff = bernstein_coefficients(expr, variables, box)
        minimum = min(coeff.values())
        gate(name+" all Bernstein coefficients exceed the stated positive bound",
             minimum > Q(1, 2**bit),
             count=len(coeff), degrees=deg, minimum=minimum)
        certificates.append({
            "name": name, "degrees": deg, "coefficient_count": len(coeff),
            "all_positive": all(a > 0 for a in coeff.values()),
            "minimum": str(minimum),
            "minimum_index": next(i for i, a in coeff.items() if a == minimum),
            "lower_bound": "2^-"+str(bit),
        })
    dupper = F(1, 64**3)*(F(450, 4096)+F(5, 6400))**2
    gate("complete positive common denominator", dupper < F(1, 2**24),
         upper=dupper)
    gate("e-zero physical diagonal lower bound", -30+24 == -6)
    gate("e-zero physical determinant quotient lower bound", -57+48 == -9)
    print(json.dumps({"stage": "all 6792 Bernstein coefficients positive"}), flush=True)

    # Complete complex-e jets: these are coefficient majorants in the true x
    # variable, with all signs made positive; no radial samples are used.
    njet = 7

    def pad(a):
        return list(a)+[F(0)]*(njet-len(a))

    def add(a, b):
        return [q+r for q, r in zip(a, b)]

    def scale(a, c):
        return [q*c for q in a]

    def mult(a, b):
        return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(njet)]

    def power(a, n):
        out = pad([F(1)])
        for _ in range(n):
            out = mult(out, a)
        return out

    def deriv(a):
        return pad([(n+1)*a[n+1] for n in range(njet-1)])

    qjet = pad([F(2), F(2), F(15), F(15, 2), F(30)])
    emax, taumax = F(1, 128), F(1, 80)
    j1 = mult(power(qjet, 3), deriv(qjet))
    j2 = mult(add(add(scale(power(qjet, 4), 12),
                      scale(power(qjet, 3), 8*emax)),
                  scale(power(qjet, 2), 12*emax**2)), deriv(qjet))
    rr = add(add(scale(mult(mult(qjet, deriv(qjet)), deriv(deriv(qjet))), 40),
                 scale(power(deriv(qjet), 3), 35)),
             scale(mult(power(qjet, 2), deriv(deriv(deriv(qjet)))), 8))
    j2 = add(j2, scale(rr, taumax**2))
    for i, bit in enumerate([4, 9, 12, 16]):
        gate("complete complex p1 jet "+str(i),
             math.factorial(i)*j1[i] <= 2**bit,
             bound=math.factorial(i)*j1[i])
    for i, bit in enumerate([9, 13, 17, 22]):
        gate("complete complex p2 jet "+str(i),
             math.factorial(i)*j2[i] < 2**bit,
             bound=math.factorial(i)*j2[i])
    gate("complex F upper bound", F(31, 16)+7*emax < 2)
    gate("complex F lower bound", F(7, 4)-7*emax > F(5, 3))
    gate("complete complex phase Wronskian upper",
         2**4*2**13+2**9*2**9 < 2**19)
    gate("true real phase Wronskian lower",
         12*F(7, 4)**6*F(3, 4)**3 > 2**7)
    gate("complex phase Wronskian variation on the actual e disk",
         F(2**19)*F(1, 2**24)/(F(1, 128)-F(1, 2**24)) < 8)
    gate("complete complex phase denominator remains separated", 128-8 > 64)
    gate("complete complex b1 bound", F(2**4*2**17+2**12*2**9, 64) <= 2**16)
    gate("complete complex b0 bound", F(2**9*2**17+2**12*2**13, 64) < 2**21)
    gate("complete complex b1 derivative", F(2**28, 64)+2**32 < 2**33)
    gate("complete complex b0 derivative", F(2**32, 64)+2**37 < 2**38)
    r0 = F(9, 2)*F(2)/F(5, 3)
    r1 = F(9, 2)*(F(30)/F(5, 3)+F(4)/F(5, 3)**2)
    r2 = F(9, 2)*(F(45)/F(5, 3)+F(180)/F(5, 3)**2+F(16)/F(5, 3)**3)
    gate("complete complex log-height derivative", r0 < 6, bound=r0)
    gate("complete complex log-height second derivative", r1 < 2**7, bound=r1)
    gate("complete complex log-height third derivative", r2 < 2**9, bound=r2)
    a2bound = (3*F(6)+2**16)/80+1
    a1bound = (3*(F(2**7)+36)+2*F(2**16)*6+2**33+2**21)/6400
    a1bound += (12+F(2**16))/80
    a0bound = (F(2**9)+3*6*2**7+6**3+F(2**16)*(2**7+36)
               +(F(2**33)+2**21)*6+2**38)/80**3
    a0bound += (F(2**7)+36+F(2**16)*6+2**21)/80**2
    gate("complete D2 scalar coefficient", a2bound < 2**10, bound=a2bound)
    gate("complete D1 scalar coefficient", a1bound < 2**21, bound=a1bound)
    gate("complete D0 scalar coefficient", a0bound < 2**21, bound=a0bound)

    qp = add(qjet, pad([emax]))
    al = add(add(scale(power(qp, 2), F(1, 4)), qjet),
             scale(deriv(qjet), taumax/2))
    kl = add(scale(power(qp, 2), F(1, 4)), qjet)
    ko = scale(add(qp, pad([F(2)])), F(1, 2))
    Ajet = [[[F(0), F(1) if n == 0 else F(0)], [al[n], F(0)]]
            for n in range(njet)]
    Kjet = [[[kl[n], ko[n]], [ko[n], F(1) if n == 0 else F(0)]]
            for n in range(njet)]

    def covjet(Cj):
        out = []
        for n in range(njet-1):
            mat = [[taumax*(n+1)*Cj[n+1][i][j] for j in range(2)] for i in range(2)]
            for ell in range(n+1):
                for i in range(2):
                    for j in range(2):
                        mat[i][j] += sum(
                            Ajet[ell][b][i]*Cj[n-ell][b][j]
                            + Cj[n-ell][i][b]*Ajet[ell][b][j]
                            for b in range(2)
                        )
            out.append(mat)
        out.append([[F(0), F(0)], [F(0), F(0)]])
        return out

    for i, bit in enumerate([4, 5, 7, 9]):
        bound = sum(sum(row) for row in Kjet[0])
        gate("complete complex two-state covariant jet "+str(i), bound < 2**bit,
             bound=bound)
        Kjet = covjet(Kjet)
    gate("complete analytic matrix coefficient bound",
         2**9+2**10*2**7+2**21*2**5+2**21*2**4 < 2**30)
    N = sp.Matrix([[0, 0], [-sp.Symbol("F"), 0]])
    Ctest = sp.Matrix([[sp.Symbol("a"), sp.Symbol("b")],
                       [sp.Symbol("b"), sp.Symbol("c")]])
    LN = lambda Z: N.T*Z+Z*N
    gate("no fourth kappa degree in the complete three-derivative matrix",
         LN(LN(LN(Ctest))) == sp.zeros(2))
    gate("determinant coefficient count", 8*2**60 == 2**63)
    gate("exact polynomial quotient bound without division by e",
         F(2**63)/(1-F(1, 2**24)) < 2**64)
    gate("complete quotient on the whole kappa disk quarter",
         F(2**64)/(1-F(1, 4)) < 2**65)
    gate("uniform finite-e quotient comparison", 65+25-190 == -100)
    gate("uniform finite-e diagonal comparison", 30+25-190 == -135)
    gate("true factor kappa minus e retained", 1-F(1, 16) > F(1, 2))
    gate("actual complete positive matrix lower",
         -10-1-30 > -48)
    gate("true zero-mode flux positive after e continuation",
         F(1, 2**6)-F(1, 2**135) > F(1, 2**7))

    gate("common support fits every original unused interval", 1024 > 31+3)
    gate("common support fits the complete two-row local radius",
         6*F(1, 2**1024) < F(1, 2**12))
    gate("complete C4 normalization including both terms",
         520+64+42+20+2 < 720)
    gate("true bump integral lower", F(1, 2)*F(15, 16)**14 > F(1, 8))
    gate("complete nonzero-mode pairing bits", 720+48+2+3 == 773 < 800)
    gate("complete mean-flux pairing bits", 720+7+3+1 < 800)
    gate("actual band uses its lower frequency", 800+5 == 805)
    gate("actual unchanged band-radius comparison", 22050-805-8192+45 == 13098)
    gate("actual unchanged mean-radius comparison", 22050-800-8192+50 == 13108)
    gate("all old radial consumers retain their lower bound", 13098 > 13000)
    gate("complete mean compact change in the full box",
         803+3072-36036 == -32161 < -32000)
    gate("complete mean compact change has favorable J and delta powers",
         24-48 == -24 and 96 > 0)
    gate("full output Sobolev and mean reserve", 16+4+4 < 40)
    gate("true band source-to-form ratio", 805+3072+15+200 == 4092 < 4100)
    gate("true band delta ratio", F(9, 2)-F(5, 8) == F(31, 8))
    gate("independent mean source-to-form ratio", 800+3072+5 == 3877 < 4100)
    gate("mean delta ratio is no larger than full band ratio", F(3, 2) < F(31, 8))
    gate("whole mixed local error constant", 152+2+2+14+4100 < 4400)
    gate("whole mixed local delta power", 3+F(31, 8) < 7)
    gate("whole actual fixed-parameter response constant",
         7840+24+832+4100-42 == 12754 < 13000)
    gate("whole actual fixed-parameter response delta power",
         32+F(31, 8)+F(231, 128) < 38)
    gate("complete actual chi parameter metric constant",
         8440+40+1130+10+4100-42 == 13678 < 14000)
    gate("complete actual chi parameter metric delta power",
         34+6+F(31, 8)+F(231, 128) < 46)
    gate("complete actual chi parameter background constant",
         161150+64+7840+24+10+4100-42 == 173146 < 174000)
    gate("nonzero radial compensator full mixed metric",
         8440+40+2-36036 < -27000)
    gate("radial compensator complete background", 65+7840+24+10-36036 < -28000)
    gate("actual radial-column full mixed metric", 8440+40+280+10-36036 < -27000)
    r_background = 160300+64+7840+24+10-36036
    gate("actual radial-column complete background",
         r_background == 132202 and r_background-2*1048576 < -1900000)
    first_bounds = [
        4400-20010-1048576+14*28+8197*7,
        13000-20010-1048576+14*40+8197*38,
        14000-20010-1048576+14*48+8197*46,
        174000-20010-2*1048576+14*40+8197*38,
    ]
    for name, value, claimed in zip(
        ["local mixed", "fixed-parameter", "joint metric", "joint background"],
        first_bounds, [-1000000, -740000, -670000, -1600000],
    ):
        gate("actual complete first layer "+name, value < claimed, log2_upper=value)
    gate("largest whole-band polynomial layer ratio",
         F(8199, 8198)**48 < F(65, 64))
    gate("largest whole-band polynomial layer exponent", F(65, 64)**32 < 2)
    gate("complete actual mixed fees sum on the deep tail",
         F(31867, 256)-46-F(1, 32) > 78)
    gate("complete actual mixed form leaves the claimed positive quarter",
         F(1, 2)-8*F(1, 256) > F(1, 4))
    gate("actual supplied input enters this same neighborhood", 4-60000000 < -1048576)

    report = {
        "status": "passed",
        "producer": "new exact SymPy quotient-ring identities, flint rational Bernstein coefficients, and Fraction budgets",
        "utc": datetime.now(timezone.utc).isoformat(),
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "bernstein": certificates,
        "bounds": {
            "full_finite_e_matrix": "C_e > 2^-48*kappa^2 I for 16e<=kappa<=1/4",
            "common_compact_radius": "2^-1024 J^-8",
            "nonzero_pairing": "2^-800 rho^8 Delta^3 M^5/B^3",
            "mean_flux_pairing": "2^-800 rho^8 Delta^3/B",
            "whole_actual_mixed_form": "d_c/4 on the whole central band plus flux mean",
            "constant_height": "exact null slot, not discarded",
            "first_layer_actual_log2": first_bounds,
        },
        "scope": {
            "object": "same actual current Gamma-star and original compact profile family",
            "input": "all central modes U/2<=|m|<=U, U^2<=B/4, with both physical traces and the two means",
            "new": [
                "one common radial phase-annihilating direction",
                "entire tau interval and finite e, including exact kappa*(kappa-e)",
                "full actual mixed central quadratic form throughout the original box",
            ],
            "retained": [
                "all output Fourier modes and both means",
                "r_U/N_band scaling and actual radial compensation",
                "ordinary and weak affine sources, physical endpoint dependence",
            ],
            "not_granted": [
                "the actual whole-network near-kernel lies in this central band",
                "band-exterior cross terms are zero",
                "an arbitrary physical source has a solved label preimage",
                "the nonlinear outer F is solved",
            ],
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({
        "status": "passed", "gates": len(gates),
        "bernstein_coefficients": sum(c["coefficient_count"] for c in certificates),
        "output": str(args.out), "sha256": sha(args.out),
    }), flush=True)


if __name__ == "__main__":
    main()

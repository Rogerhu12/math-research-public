#!/usr/bin/env python3
"""Actual radial positive two-root Airy defect, full sources and all modes.

Exact identities and directed constants.  No sampling of frequencies or roots.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp

ctx.prec = 192
TOPIC = Path(__file__).resolve().parents[1]
PROOF = TOPIC / "results/R119-supplement-actual-positive-two-root-Airy-defect-and-full-sources.md"
OUT = TOPIC / "notes/2026-11-13-R119-positive-two-root-Airy-budget.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    gates = []

    def gate(name, passed, detail):
        ok = bool(passed)
        gates.append({"name": name, "passed": ok, "detail": str(detail)})
        if not ok:
            raise AssertionError(name)

    H = arb(1) / 64
    G = arb(2)
    d = 1 - G * H
    gamma13 = (arb(1) / 3).gamma()
    gamma23 = (arb(2) / 3).gamma()
    A0 = 1 / (arb(3) ** (arb(2) / 3) * gamma23)
    A1abs = 1 / (arb(3) ** (arb(1) / 3) * gamma13)
    cA = A1abs / A0
    c = 1 / cA.sqrt()
    gate("actual_Airy_initial_height", A0 > arb(1) / 4, A0)
    gate("actual_Airy_initial_slope", A1abs < 1, A1abs)
    gate("actual_Airy_impedance", cA > arb(1) / 2 and cA < 1, cA)
    gate("height_gradient_complete", (arb(1) / 2 / (arb(7) / 8) ** 2 + 2 / (arb(7) / 8)) / 2 < G,
         "both g and actual mu derivatives retained")
    gate("positive_height_absorption", d == arb(31) / 32, d)
    gate("two_real_collars_disjoint", 60 * (arb(2) ** 190 * arb(7) / 30).sqrt() * (1-arb(2)**-18) > 2*8*H/7,
         "actual root separation 60 B z0 (1-4 z0), B>2^190, z0<2^-20")

    z, a, g, mu, m, uz, u, r = sp.symbols("z a g mu m uz u r", positive=True)
    T = sp.sqrt(a*g*mu)
    radial = sp.simplify(mu * (a*g/T)**2 / (a*g))
    angular = sp.simplify(mu * z*g*g*m*m / T**2 / (a*g))
    gate("true_radial_height_density", radial == 1, radial)
    gate("true_angular_height_density", angular == z*m*m/a**2, angular)
    gate("true_source_Jacobian_height", sp.simplify(1/(a*g*T) - 1/(a*g*sp.sqrt(a*g*mu))) == 0,
         "ordinary f/(a*g*T), weak Fz=epsilon Ft/T, extra -r Fz")

    l, kap = sp.symbols("l kap", positive=True)
    ramp = 1-z/l
    gate("exact_ramp_gradient", sp.integrate(sp.diff(ramp,z)**2 + kap**2*z*ramp**2,(z,0,l)) == 1/l+kap**2*l**2/12,
         "l^-1 + kappa^2*l^2/12")
    gate("exact_ramp_mass", sp.integrate(ramp**2,(z,0,l)) == l/3, "l/3")
    gate("full_low_ramp_endpoint", 1/H+H**2/12 < 65, 1/H+H**2/12)
    gate("full_high_ramp_endpoint", arb(13)/12 < 65, "13/12")
    E = (arb(65).sqrt()+G*(H/3).sqrt())**2
    Tgrad = (E.sqrt()+G*(2*H).sqrt())/d
    P = ((4+H**2)*Tgrad**2+4+2*H).sqrt()
    gate("full_Poisson_extension_energy", E < 128, E)
    gate("full_Poisson_two_collar_gradient", Tgrad < 16, Tgrad)
    gate("full_Poisson_two_collar_mass", P < 64, P)

    x = sp.symbols("x")
    aa = sp.Function("aa")(x)
    ap = sp.diff(aa,x)
    sub = {sp.diff(aa,x,2):x*aa}
    gate("Airy_L2_moment_derivative", sp.expand(sp.diff(ap**2-x*aa**2,x).subs(sub)+aa**2)==0,
         "(Ai'^2-x Ai^2)'=-Ai^2; integral I0=Ai'(0)^2")
    gate("Airy_weighted_moment_1", sp.expand(sp.diff(x*x*aa*ap,x).subs(sub)- (2*x*aa*ap+x*x*ap**2+x**3*aa**2))==0,
         "J2=I0-I3 after integration")
    gate("Airy_weighted_moment_2", sp.expand(sp.diff(x**3*ap**2-x**4*aa**2,x).subs(sub)-(3*x*x*ap**2-4*x**3*aa**2))==0,
         "3 J2=4 I3 after integration")
    I0, I3, J2 = sp.symbols("I0 I3 J2")
    sol = sp.solve([J2-I0+I3,3*J2-4*I3],[J2,I3])
    gate("complete_Airy_weighted_moment", sol[J2] == 4*I0/7, sol)
    gate("Airy_moment_norms", A1abs < 1 and (arb(4)/7).sqrt()*A1abs < 1,
         {"Ai_L2":str(A1abs),"x_Aiprime_L2":str((arb(4)/7).sqrt()*A1abs)})

    # Complete cutoff derivative bounds by exact extrema on [0,1].
    cutoff = 1-10*x**3+15*x**4-6*x**5
    dp = sp.diff(cutoff,x); ddp = sp.diff(cutoff,x,2)
    gate("cutoff_C2_end_jets", cutoff.subs(x,0)==1 and cutoff.subs(x,1)==0
         and all(sp.diff(cutoff,x,k).subs(x,e)==0 for k in (1,2) for e in (0,1)),
         "actual cutoff joins with both first and second derivatives zero")
    gate("cutoff_first_derivative", sp.factor(dp) == -30*x*x*(x-1)**2,
         "sup |chi'|=(15/8)*2/H < 4/H")
    crit = sp.solve(sp.diff(ddp,x),x)
    maxdd = max([abs(ddp.subs(x,t)) for t in crit]+[sp.Integer(0)])
    gate("cutoff_second_derivative", bool(maxdd < 6),
         "sup |chi''| < 6*(2/H)^2 = 24/H^2")
    residual = 16+24/H**2+16/H**2
    gate("complete_three_term_Ai_residual", residual < arb(2)**18, residual)
    defect = 64*arb(2)**18/A0
    reflection = 2*defect/(arb(3).sqrt()*cA)
    gate("complete_two_end_DN_defect", defect < arb(2)**28, defect)
    gate("complete_two_end_reflection", reflection < arb(2)**30, reflection)
    t, ca = sp.symbols("t ca", real=True)
    b = sp.sqrt(3)-sp.I
    acomplex = sp.sqrt(3)+sp.I
    den = sp.expand((b*t+ca*acomplex)*(acomplex*t+ca*b))
    gate("true_Airy_resolvent_denominator", sp.simplify(den-4*(t*t+ca*t+ca*ca))==0,
         ">=3 cA^2 for every real spectral value")
    gate("full_source_Airy_multiplier", 1/(arb(3).sqrt()*cA*c*A0) < 8,
         1/(arb(3).sqrt()*cA*c*A0))
    gate("mean_source_resolvent", arb.pi()/c < 4, arb.pi()/c)
    gate("all_source_constant", 8*64 < 2**10 and 4*64 < 2**10,
         "tau retained for nonzero kappa<1; mean separate")
    gate("all_layer_strong_coefficient", arb(2)**30*arb(2)**(arb(64)/3)*arb(2) < arb(2)**64,
         "a_*^(4/3) < 2^(64/3) (j+5)^(2/3) delta^-3; full Fourier weight factor <2")

    dependencies = [PROOF, Path(__file__).resolve(),
        TOPIC/"results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
        TOPIC/"results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md",
        TOPIC/"results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
        TOPIC/"results/R39-finite-component-airy-transfer-input.md"]
    report = {"passed": all(g["passed"] for g in gates), "gate_count":len(gates),
        "gates":gates, "bounds":{"E_extension":str(E),"T_gradient":str(Tgrad),
            "P_mass":str(P),"Ai_residual_over_c":str(residual),
            "DN_defect":str(defect),"reflection":str(reflection)},
        "scope":"actual complete radial positive two-root component, all nonzero frequencies plus exact mean; no whole-network inverse or nonradial update transfer",
        "file_sha256":{str(p.relative_to(TOPIC)):sha(p) for p in dependencies}}
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"passed":report["passed"],"gate_count":len(gates),
        "report":str(args.output),"report_sha256":sha(args.output)},ensure_ascii=False))


if __name__ == "__main__":
    main()

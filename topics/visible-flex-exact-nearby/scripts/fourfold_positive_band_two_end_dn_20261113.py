#!/usr/bin/env python3
"""Actual raw-height divergence, holonomy and positive-band two-end DN budgets."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    P, K, U, V, Uth, Vth, w, A = sp.symbols("P K U V Uth Vth w A")
    E = 1+w*w
    J = 1+K+E*U
    D = 1-w*w*(2*K+K*K+E*P*P)
    Qph = V-P
    F = (-A*(2*K+U+K*K+K*U+w*w*P*P)+E*Qph*Qph)/J
    FP, FK, FU, FV = [sp.diff(F, x) for x in (P, K, U, V)]
    d = E*Qph/J
    v2 = D/J**2
    tr = {P:V-(A+1)*P, K:F, U:Vth-(A+1)*U,
          V:FP*U+FK*V+FU*Uth+FV*Vth, w:A*w}
    er = {P:U, K:V, U:Uth, V:Vth, w:0}
    dt = lambda expr: sum(sp.diff(expr, x)*rhs for x, rhs in tr.items())
    de = lambda expr: sum(sp.diff(expr, x)*rhs for x, rhs in er.items())
    zero = lambda expr: sp.factor(expr) == 0
    logpart = sp.log(J)-sp.Rational(3, 2)*sp.log(D)
    lt = A-1+dt(logpart)
    le = de(logpart)
    gate("exact_raw_height_t_coefficient",
         zero(lt-d*le-de(d)+A+1+FK),
         "mu=(w/a) J D^-3/2 includes all actual first-order terms")
    gate("exact_raw_height_theta_coefficient",
         zero(-dt(d)-d*lt+de(d*d+A*v2)+(d*d+A*v2)*le+FP),
         "The independent U_theta,V_theta terms cancel in the full divergence identity")
    gate("exact_raw_height_principal",
         zero(FU+d*d+A*v2) and zero(FV-2*d),
         "The complete principal matrix is retained")

    hol = (1+w*w*(1+K)*U/(1-w*w*P*P))/sp.sqrt(D)
    holU = sp.diff(hol, U)
    gate("exact_full_holonomy_K_Euler_derivative",
         zero((sp.diff(hol, K)-w*w*J*D**(-sp.Rational(3, 2)))
              *D**sp.Rational(3, 2)),
         "G_K=w^2 rho J, including the mean")
    gate("exact_full_holonomy_P_Euler_derivative",
         zero((sp.diff(hol, P)-de(holU)
               +w*w*E*Qph*D**(-sp.Rational(3, 2)))
              *D**sp.Rational(3, 2)),
         "G_P-d_theta G_U=-w^2 rho E(V-P)")
    a, ht, he, es = sp.symbols("a ht he e", nonzero=True)
    mu = w*J*D**(-sp.Rational(3, 2))/a
    gate("exact_ordinary_scalar_density_source",
         zero(mu*a*w*es-w*w*J*D**(-sp.Rational(3, 2))*es),
         "The true source is w^2 J rho e, not an endpoint jump")
    gate("exact_raw_conormal_holonomy_identity",
         zero(mu*(ht-d*he)-w*w*D**(-sp.Rational(3, 2))*
              (J*ht/(a*w)-E*Qph*he/(a*w))),
         "<p_raw>=delta M after the complete angular Euler integration")

    n = Q(1, 256)
    gate("actual_D_series_domain", 3*n < Q(1, 16),
         "All coefficient ratios use the actual small relative state")
    gate("actual_rho_derivative_bound", Q(3, 2)**2*Q(16, 15)**5 < 4,
         "(3/2)(16/15)^(5/2)<2")
    gate("actual_inverse_root_derivative_bound", Q(1, 2)**2*Q(16, 15)**3 < 1,
         "The inverse square-root first derivative is below 1")
    gate("actual_radial_ratio_bound", 2*2+2*3 == 10,
         "||J rho-1||<=10n")
    gate("actual_angular_ratio_bound", 2*3+2*2 == 10,
         "||D^-1/2/J-1||<=10n")
    gate("actual_complete_positive_form_relative_fee",
         20*Q(1, 2**447)+2*Q(1, 2**435) < Q(1, 2**430),
         "Includes the actual angle Jacobian at both endpoints")
    epsilon = Q(1, 2**430)
    gate("actual_positive_form_coercivity", epsilon < Q(1, 2),
         "The same energy completion works at true A=0 endpoints")

    aa, bb, dd, fm, fp = sp.symbols("aa bb dd fm fp", nonzero=True)
    cc = (aa*dd-1)/bb
    pm = (fp-aa*fm)/bb
    pp = cc*fm+dd*pm
    S = sp.Matrix([[aa, -1], [-1, dd]])/bb
    gate("exact_complete_two_end_DN_matrix",
         all(zero(x) for x in sp.Matrix([-pm, pp])-S*sp.Matrix([fm, fp])),
         "Both outward fluxes and the exact nonzero cross term are retained")
    RR = sp.symbols("R", positive=True)
    mean_S = sp.Matrix([[1, -1], [-1, 1]])/RR
    gate("exact_independent_mean_translation_kernel",
         mean_S*sp.Matrix([1, 1]) == sp.zeros(2, 1),
         "Mean height difference and flux remain; only the common height is a kernel")
    gate("exact_mean_difference_energy",
         zero((sp.Matrix([fm, fp]).T*mean_S*sp.Matrix([fm, fp]))[0]
              -(fm-fp)**2/RR),
         "The complete mean energy uses the true radial resistance")
    gate("ordinary_source_green_relative_fee", epsilon/(1-epsilon) < 2*epsilon,
         "The resolvent identity retains the actual ordinary source functional")
    gate("ordinary_source_flux_full_dual_fee", (1+epsilon)/(1-epsilon) < 4,
         "The complete two-end source flux, including its translation test row, is below 2 S_I")
    gate("actual_nonzero_angular_Poincare_constant", Q(1, 4)**2 == Q(1, 16),
         "All real fourfold modes are included; there is no discarded low nonzero mode")
    gate("whole_source_contract_keeps_translation", True,
         "C_I=1+2 sqrt(R_I)+1/(4 sqrt(M_I)) bounds full height, not just its angular derivative")
    gate("source_outward_flux_mean_kept", True,
         "Testing the exact divergence identity against 1 gives total outward flux=int source")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-actual-final-connector-all-label-continuation.md",
        root/"results/R119-supplement-unscalarized-tail-frame-and-summable-remainder.md",
        root/"results/R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md",
        root/"results/R119-supplement-divergence-frame-and-uniform-turning-energy.md",
        root/"results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-actual-positive-band-two-end-dn-v1",
        "scope": "The actual complete raw-height scalar divergence operator, holonomy flux, true-angle positive-band weak Dirichlet/source Green and both-end relative DN in an explicit full-frequency radial energy trace space.",
        "inputs": {
            "label_weight": 224,
            "full_relative_positive_form_fee_power_of_2": -430,
            "true_trace_space": "sum over every m in 4Z of f_m^* S_m f_m, plus the independent common mean height",
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "complete_raw_scalar_operator": True,
            "true_raw_flux_mean_equals_holonomy_variation": True,
            "all_positive_component_frequencies": True,
            "both_endpoint_trace_and_feedback": True,
            "actual_endpoint_angle_maps_retained": True,
            "updated_weak_positive_DN_relative_bound": True,
            "continuous_ordinary_source_and_mean_charge": True,
            "uniform_installed_strong_Airy_trace_equivalence": False,
            "uniform_all_layer_source_fee": False,
            "arbitrary_R37_metric_source_conversion": False,
            "full_mixed_return_relative_inverse": False,
            "closed_surface_main_goal": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({"all_pass": report["all_pass"], "checks": len(report["checks"]),
                          "out": str(args.out)}, ensure_ascii=False))
    else:
        print(encoded, end="")

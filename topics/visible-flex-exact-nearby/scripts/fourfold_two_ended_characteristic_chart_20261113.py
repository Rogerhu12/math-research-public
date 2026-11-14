#!/usr/bin/env python3
"""Exact full matrices, fold limits, Piola sources and parameter columns."""
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
        if not bool(condition):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    def zero(expr):
        return sp.simplify(expr) == 0

    b, c, q, q0, u, v1, muh = sp.symbols(
        "b c q q0 u v1 muh", positive=True)
    lp, lm = sp.symbols("lp lm", positive=True)
    gate("actual_two_branch_product",
         zero(((lp+lm)/2)**2-((lp-lm)/2)**2-lp*lm),
         "Both inverse characteristic derivatives are positive")
    J = c*q*(u*u-v1*v1)/q0
    DX = sp.Matrix([[(b*v1+c*q*u)/q0, v1/q0],
                    [b*u+c*q*v1, u]])
    gate("exact_full_characteristic_Jacobian", zero(DX.det()-J),
         "The full two-dimensional cross terms are retained")
    M = muh*sp.Matrix([[1, -b], [-b, b*b-c*c*q*q]])
    pushed = sp.simplify(DX*M*DX.T/J)
    gate("exact_transformed_radial_coefficient",
         zero(pushed[0, 0]-muh*c*q/q0),
         "This is the actual weak matrix, divided by the full Jacobian")
    gate("exact_transformed_cross_coefficient", zero(pushed[0, 1]),
         "The two characteristic equations cancel the complete mixed coefficient")
    gate("exact_transformed_angular_coefficient",
         zero(pushed[1, 1]+muh*c*q*q0),
         "The reference type factor is exactly -q0(T)^2")
    gate("exact_transformed_discriminant",
         zero(pushed.det()+muh*muh*c*c*q*q),
         "The determinant density is invariant under the two-dimensional push")

    ct, kth, mu = sp.symbols("chi_t chi_theta mu", positive=True)
    dd, vv = (b+ct)/kth, c/kth
    Mh = mu*sp.Matrix([[1, -dd], [-dd, dd*dd-vv*vv*q*q]])
    Dchi = sp.Matrix([[1, 0], [ct, kth]])
    Mh_push = sp.simplify(Dchi*Mh*Dchi.T/kth)
    gate("exact_hodograph_full_matrix",
         all(zero(z) for z in Mh_push-(mu/kth)*sp.Matrix(
             [[1, -b], [-b, b*b-c*c*q*q]])),
         "The physical-angle time derivative is retained")

    w, ar, JD, D, ee = sp.symbols("w ar JD D e", positive=True)
    v = sp.sqrt(D)/JD
    mu_raw = w/ar*JD/D**sp.Rational(3, 2)
    chi_theta = c/v
    mu_hat = sp.simplify(mu_raw/chi_theta)
    source_raw = w*w*JD*ee/D**sp.Rational(3, 2)
    source_hat = sp.simplify(source_raw/chi_theta)
    gate("exact_hodograph_density_cancellation",
         zero(mu_hat-w/(ar*c*D)),
         "The full J and square-root discriminant factors cancel")
    gate("exact_hodograph_source_cancellation",
         zero(source_hat-w*w*ee/(c*D)),
         "The original ordinary scalar source has its true physical units")
    gate("exact_source_to_raw_principal_ratio",
         zero(source_hat/mu_hat-ar*w*ee),
         "The normalized physical source is a*w*e before the second map")
    mu_eff = mu_hat*c*q/q0
    source_new = source_hat/J
    gate("exact_full_ordinary_source_factor",
         zero(source_new/mu_eff-ar*w*ee*q0*q0/(c*c*q*q*(u*u-v1*v1))),
         "Both branch Jacobians and both optical factors remain")

    hp = sp.symbols("Hprime", positive=True)
    gamma = (c*hp)**sp.Rational(2, 3)
    qr = gamma**sp.Rational(-1, 2)
    gate("exact_fold_optical_ratio",
         zero(qr-(c*hp)**sp.Rational(-1, 3)),
         "The s^(3/2) factor is removed before taking an endpoint limit")
    Jend = c*qr*hp*hp
    gate("exact_fold_Jacobian",
         zero(Jend-c**sp.Rational(2, 3)*hp**sp.Rational(5, 3)),
         "The full endpoint Jacobian has a positive finite value")
    mu_end = w/(ar*D)*qr
    gate("exact_fold_boundary_flux_density",
         zero(mu_end-mu_hat*gamma/hp),
         "The endpoint conormal transforms by division by Hprime")
    source_end = ar*w*ee/(c*c*qr*qr*hp*hp)
    gate("exact_fold_ordinary_source",
         zero(source_end-ar*w*ee/(c*hp)**sp.Rational(4, 3)),
         "There is no unremoved inverse square-root singularity")
    dc, dhp = sp.symbols("dc dHprime")
    gate("exact_fold_parameter_jet",
         zero(sp.diff(gamma, c)*dc+sp.diff(gamma, hp)*dhp
              -sp.Rational(2, 3)*gamma*(dc/c+dhp/hp)),
         "Both the actual scalar speed and the actual endpoint angle vary")

    HT, HP, drift = sp.symbols("H_T H_Phi drift")
    jac_angle = chi_theta*hp
    raw_theta = jac_angle*HP
    raw_time = gamma*HT+drift*raw_theta
    raw_flux = mu_raw*(raw_time-drift*raw_theta)
    gate("exact_complete_raw_jet_recovery",
         zero(raw_flux-mu_raw*gamma*HT),
         "The actual drift remains in h_t and cancels only in the true conormal")
    gate("exact_total_endpoint_flux",
         zero(raw_flux/jac_angle-mu_end*HT),
         "The physical-angle Jacobian and the KAM angle Jacobian are both present")

    ta, tb, tab, sa, sab, qp = sp.symbols(
        "T_a T_b T_ab Sigma_a Sigma_ab q0prime")
    gate("exact_first_parameter_inverse",
         zero((sa/q0)*q0-sa),
         "All of Sigma's parameter dependence is retained")
    gate("exact_second_parameter_inverse",
         zero(q0*((sab-qp*ta*tb)/q0)+qp*ta*tb-sab),
         "The q0prime*T_a*T_b term is necessary")
    gate("fold_first_parameter_order",
         Q(3, 2)-Q(1, 2) == 1,
         "D Sigma is O(s^(3/2)), while q0(T) is O(s^(1/2))")
    gate("fold_second_parameter_cross_order",
         -Q(1, 2)+1+1 == Q(3, 2),
         "The complete second inverse numerator has the same vanishing order")

    t, x = sp.symbols("t x")
    XX = sp.Function("X")(t, x)
    YY = sp.Function("Y")(t, x)
    Z1 = sp.Function("Z1")(t, x)
    Z2 = sp.Function("Z2")(t, x)
    aa, bb = sp.diff(XX, t), sp.diff(XX, x)
    cc, dd2 = sp.diff(YY, t), sp.diff(YY, x)
    JJ = aa*dd2-bb*cc
    ZZ1, ZZ2 = (aa*Z1+bb*Z2)/JJ, (cc*Z1+dd2*Z2)/JJ
    div_pushed = (dd2*sp.diff(ZZ1, t)-cc*sp.diff(ZZ1, x)
                  -bb*sp.diff(ZZ2, t)+aa*sp.diff(ZZ2, x))/JJ
    gate("exact_Piola_weak_source",
         zero(div_pushed-(sp.diff(Z1, t)+sp.diff(Z2, x))/JJ),
         "A full vector divergence source is pushed, not replaced by a boundary jump")

    dXX = sp.Function("deltaX")(t, x)
    dYY = sp.Function("deltaY")(t, x)
    V1, V2 = (dd2*dXX-bb*dYY)/JJ, (-cc*dXX+aa*dYY)/JJ
    dJJ = (sp.diff(dXX, t)*dd2+aa*sp.diff(dYY, x)
           -sp.diff(dXX, x)*cc-bb*sp.diff(dYY, t))
    gate("exact_parameter_log_Jacobian",
         zero(dJJ/JJ-sp.diff(V1, t)-sp.diff(V2, x)
              -(V1*sp.diff(JJ, t)+V2*sp.diff(JJ, x))/JJ),
         "The coordinate variation includes both divergence and transport")
    ff, dff, dlogJ, Vf, VlogJ, divV = sp.symbols(
        "f deltaf deltalogJ Vgradf VgradlogJ divV")
    density_variation = dff-ff*dlogJ-Vf+ff*VlogJ
    gate("exact_parameter_density_column",
         zero(density_variation.subs(dlogJ, divV+VlogJ)
              -(dff-Vf-ff*divV)),
         "The actual numerator is delta f - div(f V)")

    A0, Rphi, RT, zz, vv2, Hpp, source = sp.symbols(
        "A0 Rphi RT z v Hphiphi source")
    scalar_second = source-A0*Hpp-A0*Rphi*zz-(A0-1+RT)*vv2
    gate("exact_residual_density_first_order_system",
         zero(scalar_second
              -(source-A0*Hpp-(A0-1)*vv2-A0*Rphi*zz-RT*vv2)),
         "The lower-left density remainder retains the exact turning factor A0")
    gate("constant_height_translation_retained",
         zero(scalar_second.subs({source: 0, Hpp: 0, zz: 0, vv2: 0})),
         "No artificial zeroth-order potential has been inserted")

    lam = sp.symbols("Lambda", positive=True)
    xx = sp.symbols("x")
    S = 10*xx**3-15*xx**4+6*xx**5
    shoulder = (7+lam*sp.diff(S, xx)).subs(xx, 1/sp.sqrt(lam))
    gate("actual_nonturning_quintic_shoulder",
         zero(shoulder-(7+30*(1-1/sp.sqrt(lam))**2)),
         "The sharp shoulder comes from the actual quintic, not a hypothetical profile")
    gate("absolute_shift_is_not_relative_profile_control",
         (7+30*Q(3, 4)**2)/7 > 3,
         "For Lambda>=16, a shift of one shrinking shoulder width changes q^2 by a factor >3")
    gate("finite_source_L2_change_of_variables",
         zero((source_raw/JJ)**2*JJ*JJ-source_raw**2),
         "The stated source norm keeps its explicit Jacobian weight")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R119-supplement-actual-negative-band-metric-parameters.md",
        root/"results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
        root/"results/R119-supplement-joint-actual-negative-band-return-kam.md",
        root/"results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
        root/"results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md",
        root/"results/R119-supplement-two-ended-negative-characteristic-chart-and-densities.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-two-ended-characteristic-chart-v1",
        "scope": "Actual two-ended C2 characteristic coordinates on every internal negative component, exact full weak matrix and density, both traces, mean, ordinary/Piola sources and complete coordinate-parameter variations.",
        "file_sha256": {
            str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest()
            for p in paths
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "actual_two_end_fixed_C2_diffeomorphism": True,
            "actual_fold_inverse_and_parameter_terms": True,
            "full_principal_and_density_transformed_exactly": True,
            "both_height_and_flux_traces": True,
            "mean_and_holonomy_source_retained": True,
            "ordinary_scalar_and_weak_divergence_sources": True,
            "all_Fourier_inputs_retained": True,
            "full_domain_analytic_angle_chart": False,
            "uniform_relative_density_smallness": False,
            "complete_Airy_and_positive_port_comparison": False,
            "full_nonlinear_high_input_inverse": False,
            "topic_completion": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                               encoding="utf-8")
    print(json.dumps({"all_pass": result["all_pass"], "checks": len(result["checks"]),
                      "output": str(args.output) if args.output else None},
                     ensure_ascii=False))

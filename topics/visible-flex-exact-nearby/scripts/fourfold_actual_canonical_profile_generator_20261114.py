#!/usr/bin/env python3
"""New exact computation for the full physical compact-profile generator.

This checks rational jet identities and differential-operator order/signs.
No finite Fourier model is substituted for the PDE or its Cauchy map.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path

import sympy as s


def compute() -> dict:
    gates = []

    def gate(name, passed, **data):
        if not passed:
            raise ArithmeticError(name)
        gates.append({"name": name, "passed": True, **data})

    def ident(name, expr):
        numerator = s.fraction(s.cancel(expr))[0]
        gate(name, numerator == 0, residual=str(numerator))

    def qgate(name, left, relation, right):
        left, right = F(left), F(right)
        passed = {"<": left < right, "<=": left <= right, "=": left == right}[relation]
        gate(name, passed, left=str(left), relation=relation, right=str(right))

    w, p, k, q, kt, ptt, ktt = s.symbols("w p k q kt ptt ktt")
    E = 1 + w**2
    T = 1 - p**2
    K = w + k
    J = K + E*q
    D = E*T - K**2
    z = kt-p
    zt = ktt-q
    f = w*(-k-q+w*(k*q-p**2))/J
    d = E*z/J

    def theta(expr):
        return sum(s.diff(expr, x)*y for x, y in ((p,q),(k,kt),(q,ptt),(kt,ktt)))

    def control(expr):
        return w*s.diff(expr,w)+f*s.diff(expr,k)+theta(f)*s.diff(expr,kt)

    def velocity(expr):
        return sum(s.diff(expr,x)*y for x,y in ((p,z),(k,E*z*z/J),(q,zt)))

    fk = s.diff(f,k)
    BJ = control(J)
    BD = control(D)
    ident("actual_f_k",fk-w*w*(E*q*q-T)/(J*J))
    ident("control_J",BJ-w*w*(T+K*q+2*q*J)/J)
    ident("control_D",BD-2*w*w*q*D/J)
    ident("control_inverse_density_Ba_over_a",-(BJ/J-s.Rational(3,2)*BD/D)-fk)
    ident("U_D_minus_d_Dtheta",velocity(D)-d*theta(D))
    ident("U_J_minus_d_Jtheta",velocity(J)-d*theta(J)-J*theta(d)-E*z*z/J)
    logc_U = -velocity(J)/J-velocity(D)/(2*D)
    logc_theta = -theta(J)/J-theta(D)/(2*D)
    ident("complete_advective_c_identity",logc_U-d*logc_theta+theta(d)+d*d/E)
    # c_t/c = logc_U - Q*(Bc/c) - 1; the last -1 is r_t/r.
    Q=s.symbols("Q")
    Bc_over_c=2-BJ/J-BD/(2*D)
    ct_over_c=logc_U-Q*Bc_over_c-1
    ident("actual_c_t_plus_Q_Bc_and_commutator",ct_over_c+Q*Bc_over_c+theta(d)-d*logc_theta+1+d*d/E)
    # B(K/(T sqrt D)) = w^2/(J sqrt D), after clearing T sqrt D.
    ident("pointwise_flux_shear_from_holonomy",control(K)-K*BD/(2*D)-w*w*T/J)

    x=s.symbols("theta", real=True)
    af,cf,df,bf,hf,pif = [s.Function(name)(x) for name in ("a","c","d","bd","h","pi")]
    deriv=lambda expr:s.diff(expr,x)
    L=lambda coeff,expr:deriv(coeff*deriv(expr))
    def A(Y):
        h,pi=Y
        return (df*deriv(h)+af*pi,Q*L(cf,h)+deriv(df*pi))
    def B(Y):
        h,pi=Y
        return (s.S.Zero,-L(cf,h))
    AB=A(B((hf,pif))); BA=B(A((hf,pif)))
    comm=(s.expand(AB[0]-BA[0]),s.expand(AB[1]-BA[1]))
    ident("full_commutator_upper_row",comm[0]+af*L(cf,hf))
    ident("full_commutator_lower_row",comm[1]-L(cf*deriv(df)-df*deriv(cf),hf)-L(cf,af*pif))
    gate("commutator_no_third_angle_jet",not any(expr.has(s.diff(hf,x,3)) for expr in comm))
    # Exact local Hamiltonian adjoint identity, before any mean projection.
    ut,vt=s.Function("u")(x),s.Function("v")(x)
    top=lambda h:bf*deriv(h)-af*L(cf,h)
    negative_adjoint=lambda pi:deriv(bf*pi)+L(cf,af*pi)
    boundary=bf*ut*vt-cf*(af*ut*deriv(vt)-deriv(af*ut)*vt)
    # <u,(bd d-a Lc)v>+<(d bd+Lc a)u,v> is a total derivative.
    ident("Hamiltonian_diagonal_complete_boundary",ut*top(vt)+negative_adjoint(ut)*vt-deriv(boundary))
    # The weak source gauge adds only angular derivatives.
    Ft,Fs,gg=s.Function("Ft")(x),s.Function("Ftheta")(x),s.Function("g")(x)
    src=(-af*Ft,gg-deriv(Fs+df*Ft))
    ident("weak_gauge_second_component",-B(src)[1]+L(cf,af*Ft))
    ident("weak_flux_mean_is_angular_divergence",src[1]-gg+deriv(Fs+df*Ft))

    mu0, M, ht, hh = s.symbols("mu0 M ht h")
    pi=mu0*ht
    radial=mu0*M*M*hh*hh-2*M*M*hh*pi+pi*pi/mu0
    ident("actual_radial_kernel_all_M",radial-mu0*(ht*ht-2*M*M*hh*ht+M*M*hh*hh))
    ident("radial_free_flux_mean",radial.subs(M,0)-mu0*ht*ht)

    # Independent exact arithmetic for the full analytic/jet/Sobolev fees.
    R=F(1,64); centre=R/4; direction=R/4
    qgate("two_complex_directions_stay_inside",centre+2*direction,"<",R)
    qgate("R_map_complex_sup",(2**10)*R,"=",16)
    qgate("R_second_derivative_Cauchy",16/direction**2,"=",2**20)
    qgate("F_second_derivative_Cauchy",(4*R)/direction**2,"=",2**12)
    qgate("F1_first_derivative_Cauchy",(8*R)/(R/2),"=",16)
    multiplier=sum(comb(4,j)*factorial(j) for j in range(5))
    qgate("complete_signed_Sobolev_multiplier",multiplier,"=",65)
    qgate("multiplier_binary_fee",multiplier,"<",2**7)
    qgate("R_full_jet_and_both_output_fee",2**20*2**4*2**7,"<",2**32)
    qgate("F_full_jet_and_both_output_fee",2**12*2**4*2**7,"<",2**24)
    n=F(1,2**32)
    qgate("true_J_complex_inverse_margin",3*n,"<",F(1,8))
    qgate("true_D_complex_inverse_margin",3*n,"<",F(1,8))
    qgate("coefficient_product_error",2**10*(2+2**10*n),"<",2**12)
    qgate("complete_quadratic_sum_fee",8*2**12,"<",2**16)
    qgate("strict_material_integral_fee",4*16,"=",64)
    qgate("response_complete_strong_fee",2**24*2**832*64,"<",2**863)
    qgate("direct_complete_strong_fee",2**32*4*2,"<",2**36)
    qgate("both_complete_strong_fees",2**863+2**36,"<",2**872)
    qgate("profile_direct_form_rho5_fee",2**16*2,"=",2**17)
    qgate("profile_response_form_integral_fee",2**16*16,"=",2**20)

    here=Path(__file__).resolve()
    topic=here.parent.parent
    inputs=[
        here,
        topic/"results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
        topic/"results/R119-supplement-actual-compact-profile-flux-gauge-and-principal-port-derivative.md",
        topic/"results/R119-supplement-actual-compact-profile-label-response.md",
        topic/"results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
        topic/"results/R119-supplement-high-oscillation-polynomial-phase-preserving-control.md",
    ]
    return {
        "schema":"visible-exact-R119-actual-canonical-profile-generator-v1",
        "implementation":"new exact SymPy rational-jet and Fraction computation; no recovered native",
        "scope":"Actual full raw height/total-flux profile gauge, complete Hamiltonian kernel, both means, real-background response and ordinary/weak source strong variation",
        "file_sha256":{str(p.relative_to(topic)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        "gate_count":len(gates),"all_passed":all(g["passed"] for g in gates),"gates":gates,
        "retained":["all Fourier modes","both physical means","current Gamma","actual background response","ordered full Cauchy factors","total/bare weak endpoint charges"],
        "not_claimed":["same-order operator-norm derivative of a naked pullback","nonradial cluster positivity","full same-weight network inverse","solution of the nonlinear F equation"]
    }


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=compute()
    raw=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(raw,encoding="utf-8")
        print(json.dumps({"output":str(args.output),"gates":report["gate_count"],"all_passed":report["all_passed"],"sha256":hashlib.sha256(raw.encode()).hexdigest()}))
    else:
        print(raw,end="")

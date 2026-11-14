#!/usr/bin/env python3
"""R81 actual finite angular windows and balanced positive-cap reflection.

Consumes the same-object complete R69/R74/R76 certificates. Every angular
form derivative comes from the paid analytic coefficient/common-translation
tubes. The true physical regular mean, its differentiated row and multiplier
column are retained. Complex root Robin coercivity pays the actual balanced
reflection and its inverse; no central feedback or Airy-coordinate jet is
silently supplied by these constants.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import arb, ctx


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def lo(value):
    return arb(value["lower"]).lower()


def hi(value):
    return arb(value["upper"]).upper()


def rec(value):
    value = arb(value)
    if not value.is_finite():
        raise ValueError("nonfinite directed constant")
    return dict(ball=value.str(40), lower=value.lower().str(40),
                upper=value.upper().str(40))


def first_moment(modulus, width):
    return (2*modulus*(-width/2).exp()/(-(-width/2).expm1())**2).upper()


def U(value):
    return arb(value).upper()


def binomial_norm(values, k):
    return U(sum((math.comb(k,j)*values[j]**2 for j in range(k+1)),arb(0)).sqrt())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--weighted",type=Path,
        default=Path("notes/2026-11-12-actual-weighted-exterior-robin-certificate.json"))
    ap.add_argument("--closed",type=Path,
        default=Path("notes/2026-11-12-actual-closed-approximate-exterior.json"))
    ap.add_argument("--robin",type=Path,
        default=Path("notes/2026-11-12-actual-exterior-robin-certificate.json"))
    ap.add_argument("--order",type=int,default=12)
    ap.add_argument("--bits",type=int,default=256)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.order<1 or args.order>128 or args.bits<128:
        raise ValueError("supply a finite positive window and sufficient precision")
    ctx.prec=args.bits
    weighted,closed,robin=[json.loads(p.read_text()) for p in
                           (args.weighted,args.closed,args.robin)]
    if not all(r.get("complete") for r in (weighted,closed,robin)):
        raise ValueError("all three actual inputs must be complete")
    for key in ("exact_parameter_interval","origin_inputs_sha256","direction_sha256"):
        if any(r[key]!=weighted[key] for r in (closed,robin)):
            raise ValueError("a finite angular window changed the actual object")
    for p in (args.closed,args.robin):
        if weighted["input_sha256"].get(str(p))!=sha(p):
            raise ValueError("R76 does not bind this complete exterior input")
    weighted_source=Path(__file__).with_name("fourfold_phase_weighted_exterior_robin.py")
    if weighted["source_sha256"]!=sha(weighted_source):
        raise ValueError("the paid weighted exterior source changed")

    op=closed["complete_finite_positive_operator"]
    rop=robin["actual_augmented_positive_operator"]
    flow=weighted["refined_actual_flow"]
    comm=weighted["actual_commutators"]
    base=weighted["actual_weighted_solution"]
    rho=lo(flow["sheared_angular_strip"])
    radius=lo(flow["common_translation_strip"])
    M=hi(flow["complex_derivative_and_inverse"])
    MC=hi(comm["improved_matrix_modulus"])
    boundary=weighted["actual_boundary_kernel"]
    mu=lo(flow["derivative_real_part_lower"])
    if not mu>0 or not hi(flow["derivative_sector_slope_upper"])<arb(1)/4:
        raise ValueError("the actual full-kernel sector gate is not paid")
    # Entire |D| boundary energy, rather than its order-zero difference:
    # |K_H(x,y)| <= (4 M^2/mu^2) csc^2((x-y)/2).
    boundary_energy_factor=U(4*M**2/mu**2)
    MB=U(hi(boundary["stable_line_c0_upper"])*boundary_energy_factor
         +hi(boundary["stable_line_c1_upper"])*(M+hi(boundary["pulled_resolvent"]))
         +hi(boundary["true_tail_operator"]))
    if not MB<435:
        raise ValueError("the stated complete boundary-energy modulus failed")
    Ct=hi(op["trace_squared"])
    Ce=hi(op["extension_squared"])
    CI=hi(op["interior_two_thirds_gain"])
    trace=U(Ct.sqrt()); lift=U(Ce.sqrt())
    weight=arb(2)**(-67)
    if not weight<min(rho/4,radius/4):
        raise ValueError("coefficient differentiation leaves the weighted Cauchy tube")
    qC=U(1+weight*first_moment(arb(1),rho/2))
    qB=U(1+weight*first_moment(arb(1),radius/2))
    if not qC<2 or not qB<2:
        raise ValueError("the actual derivative-conjugation factors are not bounded")
    # Repeat the full actual mean-preserving inverse gate with the sharper
    # whole-form boundary modulus. This does not extrapolate R76's old weight.
    Mstar=hi(rop["full_form_norm"])
    NC=first_moment(MC,rho)
    NB=first_moment(MB,radius)
    NJ=first_moment(M,rho)
    T0=U((Ct*Ce).sqrt()*NJ)
    N0=U(NC+Ct*NB)
    Nstar=U(2*N0+3*Mstar*T0)
    Tnorm=U(1+weight*T0)
    g=hi(rop["one_Dirichlet_coercive_inverse"])
    dirichlet_ratio=U(g*weight*Nstar)
    if not weight*T0<arb(1)/4 or not dirichlet_ratio<arb(1)/2:
        raise ValueError("the improved actual Dirichlet mean-transport gate failed")
    B0=U(Mstar+weight*N0)
    B=U(2*g*Tnorm**2)
    A=U(lift*(1+B*B0))
    LD=U(lift*B0*A)
    LF=U(lift*(B0*B+1))
    form_derivatives=[B0]
    mean_derivatives=[arb(0)]
    for j in range(1,args.order+1):
        factorial=arb(math.factorial(j))
        form_derivatives.append(U(factorial*(qC*MC*(2/rho)**j
                                                +Ct*qB*MB*(2/radius)**j)))
        # W_{+/-s} J^(j) phi_0: Hardy/Parseval on two strip boundaries.
        mean_derivatives.append(U(2*M*factorial*(2/rho)**j))

    P=[A]; Q=[B]
    ZP=[LD]; ZQ=[LF]
    derivative_rows=[]
    for k in range(1,args.order+1):
        Jk=mean_derivatives[k]
        cp=sum((math.comb(k,j)*form_derivatives[j]*P[k-j]
                for j in range(1,k+1)),arb(0))
        cq=sum((math.comb(k,j)*form_derivatives[j]*Q[k-j]
                for j in range(1,k+1)),arb(0))
        # Mean of D^k U is (-1)^k <U,W_-s J^(k) phi_0>;
        # the differentiated multiplier column is lambda W_s J^(k) phi_0.
        P.append(U(A+A*trace*Jk*P[0]+B*(cp+trace*Jk*LD)))
        Q.append(U(A*trace*Jk*Q[0]+B*(1+cq+trace*Jk*LF)))
        ZP.append(U(lift*sum((math.comb(k,j)*form_derivatives[j]*P[k-j]
                              for j in range(k+1)),arb(0))))
        ZQ.append(U(lift*(1+sum((math.comb(k,j)*form_derivatives[j]*Q[k-j]
                                 for j in range(k+1)),arb(0)))))

    # Actual full root Robin form b +/- i ||<D>^(1/3) trace_0||^2.
    # The regular physical mean remains constrained; its lift has root trace 0.
    L=hi(op["length_upper"])
    ellipticity=lo(op["matrix_lower"])
    mass_cost=U(max(2*L,(1+L**2)/ellipticity))
    robin_inverse=U(arb(2).sqrt()*mass_cost)
    robin_neumann=U(robin_inverse*weight*Nstar)
    if not weight*T0<arb(1)/4 or not robin_neumann<arb(1)/2:
        raise ValueError("the actual complex root-Robin inverse gate failed")
    BR=U(2*robin_inverse*Tnorm**2)
    AR=U(lift*(1+BR*B0))
    incoming_force=U((2*Ct).sqrt())
    PR=[U(BR*incoming_force)]; QR=[BR]
    lambda_R_data=U(lift*B0*PR[0])
    lambda_R_source=U(lift*(B0*BR+1))
    for k in range(1,args.order+1):
        Jk=mean_derivatives[k]
        cp=sum((math.comb(k,j)*form_derivatives[j]*PR[k-j]
                for j in range(1,k+1)),arb(0))
        cq=sum((math.comb(k,j)*form_derivatives[j]*QR[k-j]
                for j in range(1,k+1)),arb(0))
        PR.append(U(BR*incoming_force+AR*trace*Jk*PR[0]
                    +BR*(cp+trace*Jk*lambda_R_data)))
        QR.append(U(AR*trace*Jk*QR[0]
                    +BR*(1+cq+trace*Jk*lambda_R_source)))

    windows=[]
    for k in range(args.order+1):
        pbar=binomial_norm(P,k);qbar=binomial_norm(Q,k)
        zpbar=binomial_norm(ZP,k);zqbar=binomial_norm(ZQ,k)
        prbar=binomial_norm(PR,k);qrbar=binomial_norm(QR,k)
        windows.append(dict(integer_order=k,
            energy_Poisson=rec(pbar),energy_source_per_combined_norm=rec(qbar),
            L2_Poisson_gain_two_thirds_positive_window=rec(U(CI*pbar)),
            L2_Poisson_gain_two_thirds_negative_window=rec(U(CI*zqbar)),
            DN_root_and_regular_mean_both_sign_windows=rec(zpbar),
            ordinary_source_contact_positive_window=rec(U(CI*zqbar)),
            ordinary_source_contact_negative_window=rec(U(CI*pbar)),
            regular_boundary_source_contact_positive_window=rec(U(trace*zqbar)),
            regular_boundary_source_contact_negative_window=rec(U(trace*pbar)),
            balanced_reflection_and_inverse_both_sign_windows=rec(U(1+incoming_force*prbar)),
            root_Robin_energy_data=rec(prbar),root_Robin_energy_source=rec(qrbar),
            root_Robin_affine_outgoing_positive_window=rec(U(incoming_force*qrbar))))
        derivative_rows.append(dict(order=k,
            actual_form_derivative=rec(form_derivatives[k]),
            actual_mean_derivative=rec(mean_derivatives[k]),
            Poisson_derivative=rec(P[k]),source_derivative=rec(Q[k]),
            Poisson_contact_derivative=rec(ZP[k]),source_contact_derivative=rec(ZQ[k]),
            root_Robin_data_derivative=rec(PR[k]),root_Robin_source_derivative=rec(QR[k])))

    report=dict(kind="actual_full_exterior_finite_angular_windows_and_balanced_reflection",
        complete=True,source_sha256=sha(__file__),bits=args.bits,
        input_sha256={str(p):sha(p) for p in (args.weighted,args.closed,args.robin)},
        dependency_sha256={weighted_source.name:sha(weighted_source)},
        origin_inputs_sha256=weighted["origin_inputs_sha256"],
        direction_sha256=weighted["direction_sha256"],
        exact_parameter_interval=weighted["exact_parameter_interval"],
        angular_convention="physical sheared phi, period 2*pi; true operator restricted to 4Z",
        signed_weight="1/147573952589676412928",
        weight_types=weighted["weight_types"],maximum_integer_window=args.order,
        actual_base={k:rec(v) for k,v in dict(
            interior_gain=CI,trace_squared=Ct,extension_squared=Ce,
            sheared_coefficient_strip=rho,common_boundary_translation_strip=radius,
            coefficient_modulus=MC,normalized_boundary_modulus=MB,mean_density_modulus=M,
            full_absD_boundary_energy_factor=boundary_energy_factor,
            matrix_first_lag_moment=NC,boundary_first_lag_moment=NB,
            mean_density_first_lag_moment=NJ,mean_transport_rate=T0,
            untransported_form_rate=N0,transported_form_rate=Nstar,
            weighted_Dirichlet_Neumann_ratio=dirichlet_ratio,
            differentiated_coefficient_weight_factor=qC,
            differentiated_boundary_weight_factor=qB,weighted_form=B0,
            base_Poisson=A,base_Vdual_source=B,base_contact_data=LD,base_contact_source=LF).items()},
        actual_complex_root_Robin={k:rec(v) for k,v in dict(
            radial_length_upper=L,ellipticity_lower=ellipticity,
            mass_and_gradient_cost=mass_cost,unweighted_coercive_inverse=robin_inverse,
            mean_transport_norm=Tnorm,weighted_Neumann_ratio=robin_neumann,
            weighted_Vdual_inverse=BR,regular_mean_lift=AR,incoming_force=incoming_force,
            physical_mean_data_output=lambda_R_data,
            physical_mean_source_output=lambda_R_source).items()},
        derivative_rows=derivative_rows,windows=windows,
        source_norm_convention="N_k=CI*||W_s f||L2(H^(k-2/3))+sqrt(Ct)*||W_s d||H^(k-1/2)",
        scope=[
            "The actual full R74 tail and physical regular mean multiplier remain in every window.",
            "All finite angular windows use only paid uniform angular analyticity, not high radial smoothness.",
            "Signed source-contact windows use K_s=-H_-s^* and the true full regular-trace adjoint.",
            "The balanced reflection uses Q=<D_phi>^(1/3), x=Qa,y=Q^-1 p, incoming=(x+i y)/sqrt(2).",
            "Root-Robin sign reversal gives the inverse; both are actual onto operators including the root mean.",
            "The root reflection uses regular mean value zero and carries its mean-flux compatibility output separately.",
            "Airy-coordinate/height jets, their exact canonical boundary factors and the central low Schur block remain separate inputs.",
            "Large finite constants do not certify a chosen high-frequency cutoff or a central finite block.",
            "The affine parameter statement is pointwise-uniform and does not prove continuity of the far-bump selection."
        ])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(complete=True,report_sha256=sha(args.out),order=args.order,
                         root_Robin_ratio=float(robin_neumann),
                         base_root_Robin_inverse=float(BR),
                         log10_order_last_contact=float(hi(windows[-1]["ordinary_source_contact_positive_window"]).log()/arb(10).log()))),flush=True)


if __name__=="__main__":
    main()

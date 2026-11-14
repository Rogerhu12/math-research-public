#!/usr/bin/env python3
"""Actual complete bidisk bound for the negative characteristic cancellation.

For k=1/(2 U0), F_sigma=k*T_sigma,theta obeys
  D_sigma F_sigma=2 s C F_sigma, C=-(U0_rho+q U0_theta)/U0-q_theta,
with exact initial F_sigma=1. This source pays C, q and k on a true closed
complex bidisk using every degree-80 Fourier/Taylor coefficient, every cell
gap and the whole actual parameter transfer error.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb,arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import CBox,Box,zeros,DirectedFFT,arb_box
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_subprincipal_root_parameter_transfer import load_transferred
from fourfold_negative_collar_root_fourier_budget import record


def modulus(z):return arb(float(np.max(z.magnitude_upper()))).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fields",type=Path,default=Path("notes/2026-11-13-R106-seven-field-full-parameter-transfer.json"))
    p.add_argument("--root-variation",type=Path,default=Path("notes/2026-11-12-actual-root-complex-potential-variation.json.gz"))
    p.add_argument("--rho-radius",type=Fraction,default=Fraction(13,50000))
    p.add_argument("--physical-strip",type=Fraction,default=Fraction(1,500))
    p.add_argument("--radial-angles",type=int,default=128)
    p.add_argument("--angles",type=int,default=2048)
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new actual cancellation output required")
    ctx.prec=a.bits;tick=time.monotonic()
    d,rows,scale=load_transferred(a.fields)
    outer=read(a.root_variation)
    if (not outer.get("proved") or outer["failed_cells"] or outer["pending"] or
        outer["source_sha256"]!=sha(Path(__file__).with_name("fourfold_phase_root_potential_complex_variation.py"))):
        raise ValueError("complete actual root-angle lower bound is missing")
    for key in ("center_object_sha256","origin_inputs_sha256","direction_sha256","exact_center_parameter"):
        if d["identity"][key]!=outer["object"][key]:raise ValueError("root angle belongs to another actual family")
    lp,hp=map(Fraction,d["identity"]["exact_parameter_interval"])
    lo,ho=map(Fraction,outer["object"]["exact_parameter_interval"])
    if not lo<=lp<hp<=ho:raise ValueError("root-angle certificate has a smaller parameter interval")
    R,S=exact_arb(a.rho_radius),exact_arb(a.physical_strip)
    R0,S0=exact_arb(Fraction(d["working_rho_radius"])),exact_arb(Fraction(d["working_physical_angle_strip"]))
    if not 0<R<R0 or not 0<S<S0:raise ValueError("actual Cauchy derivative margins missing")
    Nr,Nt=a.radial_angles,a.angles
    if (Nr&(Nr-1) or Nt&(Nt-1) or Nr<=d["degree"] or Nt<=2*d["K"]):
        raise ValueError("insufficient exact two-dimensional Fourier evaluation grids")
    names=("U0","q","U0_rho","U0_theta","q_theta")
    data=zeros((Nr,Nt,len(names)));movement={name:arb(0) for name in names}
    root_u0=arb(0);radial_gap=arb.pi()/Nr;angular_gap=arb.pi()/Nt
    for name,base,ar,at in (("U0","U0",0,0),("q","q",0,0),
                           ("U0_rho","U0",1,0),("U0_theta","U0",0,1),
                           ("q_theta","q",0,1)):
        column=names.index(name)
        for n,row in enumerate(rows[base]):
            if n<ar:continue
            radial_frequency=n-ar
            radial=(R/scale)**n
            if ar:radial*=n/R
            for k,c in row.items():
                angular=(-4*int(k)*S).exp()
                z=c*radial*angular*(acb(0,4*int(k)) if at else 1)
                data[radial_frequency%Nr,int(k)%Nt,column]=CBox.from_acb(z)
                movement[name]+=abs(z).upper()*(radial_frequency*radial_gap+abs(int(k))*angular_gap)
                if name=="U0" and n==0:root_u0+=abs(c).upper()*(4*abs(int(k))*S).exp()
    errors={name:stored(d["complete_approximant_errors"][name]["complete_sup_error"]).upper()
            for name in ("U0","q")}
    tails={"U0":errors["U0"],"q":errors["q"],"U0_rho":errors["U0"]/(R0-R),
           "U0_theta":errors["U0"]/(S0-S),"q_theta":errors["q"]/(S0-S)}
    fft=DirectedFFT();data=fft.fft(data,inverse=True)*Nr
    data=fft.fft(data,axis=1,inverse=True)*Nt
    enclosed={name:data[...,j].pad(arb_box((movement[name]+tails[name]).upper()))
              for j,name in enumerate(names)}
    U,q,Ur,Ut,qt=(enclosed[name] for name in names)
    real_lower=arb(float(np.min(U.real.lo))).lower()
    if not real_lower>0:raise ValueError("complete U0 bidisk does not certify a nonzero denominator")
    C=-(Ur+q*Ut)/U-qt;k=1/(2*U)
    bound_C,bound_q,bound_k=map(modulus,(C,q,k))
    Y=(2*(root_u0+errors["U0"])).upper()
    m=stored(outer["uniform_bounds"]["Y_prime_real_lower"]).lower()
    if not m>0 or not a.physical_strip<=Fraction(outer["exact_physical_angle_strip"]):
        raise ValueError("actual initial angle inverse domain is missing")
    out=dict(kind="actual_negative_characteristic_complete_cancellation_bidisk",
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(a.fields):sha(a.fields),str(a.root_variation):sha(a.root_variation)},
        identity=d["identity"],root=d["root"],rho_radius=str(a.rho_radius),
        physical_angle_strip=str(a.physical_strip),radial_phase_cells=Nr,angular_cells=Nt,
        exact_input_radial_degree=d["degree"],complete_input_positive_angle_modes=d["K"],
        all_modes_all_parameter_errors_and_all_closed_cell_gaps_retained=True,
        actual_identity="C=-(U0_rho+q*U0_theta)/U0-q_theta; kstar=1/(2*U0)",
        actual_flow_identity="(partial_s+(2*s*q-2*sigma*s*s*kstar)*partial_theta)(kstar*T_sigma_theta)=2*s*C*(kstar*T_sigma_theta)",
        actual_initial_condition="kstar(0,theta)*Y0_prime(theta)=1",
        complete_complex_moduli={"C":record(bound_C),"q":record(bound_q),"kstar":record(bound_k),
                                 "root_Y0_prime":record(Y)},
        complete_U0_real_lower=record(real_lower),root_Y0_prime_real_lower=record(m),
        complete_finite_cell_movement={name:record(v.upper()) for name,v in movement.items()},
        complete_true_Cauchy_derivative_tails={name:record(v.upper()) for name,v in tails.items()},
        maximum_principle="Full rho-circle/upper-angle closed cells; Schwarz reflection fills lower angle boundary, then successive maximum principles cover both disks. Re U0>0 pays the exact quotient throughout.",
        actual_negative_chart_enlargement_proved=False,full_return_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_subprincipal_root_parameter_transfer.py",
            "fourfold_subprincipal_root_regularized_fft_v2.py",
            "fourfold_phase_beta_bulk_box.py","fourfold_phase_root_fourier_fit.py",
            "fourfold_negative_collar_root_fourier_budget.py")},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),
        moduli=out["complete_complex_moduli"],U0_lower=out["complete_U0_real_lower"],seconds=out["seconds"]),flush=True)


if __name__=="__main__":main()

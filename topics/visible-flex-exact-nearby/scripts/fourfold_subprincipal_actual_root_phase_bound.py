#!/usr/bin/env python3
"""Complete actual root finite-part modulus via the nonsingular true root ODE.

Consumes the completed seven-field and regularized-source reports. It retains
all mean/cut/root terms, pays every true error, and transports along the actual
root-emitted characteristic. It does not use missing large reference shards.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_subprincipal_root_reference_v2 import CompleteRootReference
from fourfold_subprincipal_root_regularized_transport import source_error_bound


def fee_on_wider_strip(field,name,radius,strip):
    width=exact_arb(strip)
    old=exact_arb(field.Sout)
    if not width>=old:
        raise ValueError("widening helper requires a wider or equal strip")
    z=radius/field.scale
    # Every row's full finite arithmetic l1 fee was paid at old. Multiplying by
    # exp(max physical frequency * widening) bounds all its exact output modes.
    return sum((z**n*fee*(4*((len(row)-1)//2)*(width-old)).exp()
        for n,(row,fee) in enumerate(zip(field.rows[name],field.fees[name]))),
        arb(0)).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("root_source",type=Path)
    p.add_argument("--root-label-strip",type=Fraction,default=Fraction(1,900))
    p.add_argument("--flow-strip",type=Fraction,default=Fraction(17,10000))
    p.add_argument("--source-strip",type=Fraction,default=Fraction(1,550))
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new report required")
    ctx.prec=a.bits;start=time.monotonic()
    field=CompleteRootReference(a.root_source);d=field.doc
    eta,Sflow,Ssource=map(exact_arb,(a.root_label_strip,a.flow_strip,a.source_strip))
    Sin=exact_arb(field.Sin);R=exact_arb(field.R)
    if not 0<eta<Sflow<Ssource<Sin:
        raise ValueError("actual root label/flow/source/error strips not nested")
    cmin,cmax=stored(d["s_cut_lower"]).lower(),stored(d["s_cut_upper"]).upper()
    r=(cmax*cmax).upper()
    if not r<R:raise ValueError("true physical root cut leaves error disk")
    errors={k:stored(v).upper() for k,v in d["complete_input_errors"].items()}
    true={k:stored(v).upper() for k,v in d["true_input_moduli_on_error_bidisk"].items()}
    finite={k:stored(v).upper() for k,v in d["finite_input_norms_on_error_bidisk"].items()}
    motion=(r*true["q"]+arb(2)*cmax*r*true["kstar"]/3).upper()
    if not eta+motion<Sflow:
        raise ValueError("actual complete root characteristic leaves paid flow strip")
    exponent=motion/(Sin-Sflow)
    J=exponent.exp().upper()
    paid=source_error_bound(outer_radius=R,working_radius=r,s_radius=cmax,
        first_angle_loss=(Sin-Ssource)/2,second_angle_loss=(Sin-Ssource)/2,
        G_bound=true["G"],q_bound=true["q"],k_bound=true["kstar"],
        G_error=errors["G"],q_error=errors["q"],k_error=errors["kstar"],
        finite_q_bound=finite["q"],finite_k_bound=finite["kstar"])
    source_true_error=(paid["regularized_source_sup_error"]+
                       errors["Sreg"]/(Sin-Ssource)).upper()
    cut_true_error=(errors["G"]/(3*cmin**3)+paid["B1_sup_error"]/cmin+
                    errors["U0"]/(4*cmin**3)+errors["U1"]/(4*cmin)+
                    errors["Ltheta"]/4).upper()
    root_true_error=(errors["Ltheta"]/4).upper()
    mods={name:field.modulus(name,r,Ssource) for name in field.rows}
    fees={name:fee_on_wider_strip(field,name,r,a.source_strip) for name in field.rows}
    H=(mods["source_even"]+cmax*mods["source_odd"]+
       fees["source_even"]+cmax*fees["source_odd"]+source_true_error).upper()
    C=(mods["cut_m3"]/cmin**3+mods["cut_m1"]/cmin+mods["cut_regular"]+
       fees["cut_m3"]/cmin**3+fees["cut_m1"]/cmin+fees["cut_regular"]+
       cut_true_error).upper()
    Z=(mods["root_field"]+fees["root_field"]+root_true_error).upper()
    phase=(J*(C+cmax*H)+Z).upper()
    report={"kind":"R106_actual_complete_root_phase_finite_part_modulus",
      "complete":True,"proved":True,"source_sha256":sha(__file__),
      "input_path":str(a.root_source),"input_sha256":sha(a.root_source),
      "identity":d["identity"],"original_fixed_physical_cut":str(field.cut),
      "root":d["root"],"s_cut_lower":ball_record(cmin),"s_cut_upper":ball_record(cmax),
      "root_label_physical_strip":str(a.root_label_strip),
      "true_flow_physical_strip":str(a.flow_strip),
      "true_source_physical_strip":str(a.source_strip),
      "input_error_physical_strip":str(field.Sin),
      "actual_root_motion_bound":ball_record(motion),
      "label_plus_motion":ball_record((eta+motion).upper()),
      "true_root_J_exponent":ball_record(exponent.upper()),
      "true_root_J_modulus":ball_record(J),
      "complete_regularized_source_modulus":ball_record(H),
      "complete_cut_field_modulus":ball_record(C),
      "complete_root_field_modulus":ball_record(Z),
      "complete_root_finite_part_modulus":ball_record(phase),
      "true_source_error_on_enlarged_strip":ball_record(source_true_error),
      "true_cut_error_on_enlarged_strip":ball_record(cut_true_error),
      "finite_moduli":{k:ball_record(v) for k,v in mods.items()},
      "finite_arithmetic_fees_on_enlarged_strip":{k:ball_record(v) for k,v in fees.items()},
      "both_inward_branches":True,"both_physical_roots":True,"mean_retained":True,
      "physical_root_label_J0":1,
      "root_to_cut_formula":"h_sigma=Jc*C_sigma(Theta_c)+int_0^c H_sigma(s,Theta_s)*J_s ds+Z_sigma(eta)",
      "true_ODE":"Theta_s=2*s*q(s^2,Theta)-2*sigma*s^2*kstar(s^2,Theta); Theta(0,eta)=eta",
      "scope":"Complete finite part on the real root-to-cut interval, holomorphic in the full stated root-label strip, uniform in the real parameter family. This is before pulling back by a global root label, with no whole-return-frame or strong PDE remainder claim.",
      "dependencies":{n:sha(Path(__file__).with_name(n)) for n in (
        "fourfold_subprincipal_root_reference_v2.py",
        "fourfold_subprincipal_root_regularized_fft_v2.py",
        "fourfold_subprincipal_root_regularized_transport.py",
        "fourfold_subprincipal_root_fourier_v2.py","fourfold_phase_root_fourier_fit.py")},
      "wall_seconds":time.monotonic()-start}
    save(a.out,report)
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
           "phase_bound":report["complete_root_finite_part_modulus"],
           "J_bound":report["true_root_J_modulus"]},flush=True)


if __name__=="__main__":main()

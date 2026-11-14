#!/usr/bin/env python3
"""Complete full-parameter errors of the center regularized root expressions."""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_subprincipal_root_parameter_transfer import load_transferred
from fourfold_subprincipal_root_regularized_transport import (
    source_error_bound,full_polynomial_norm)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("transfer",type=Path)
    p.add_argument("--working-strip",type=Fraction,default=Fraction(1,800))
    p.add_argument("--cut",type=Fraction,default=Fraction(268136140016943,1125899906842624))
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new output required")
    ctx.prec=a.bits;start=time.monotonic()
    d,rows,scale=load_transferred(a.transfer)
    R=exact_arb(Fraction(d["working_rho_radius"]))
    Sin=exact_arb(Fraction(d["working_physical_angle_strip"]))
    Sout=exact_arb(a.working_strip)
    if not 0<Sout<Sin:raise ValueError("actual angular loss absent")
    root=stored(d["root"])
    rho=root-exact_arb(a.cut)
    if not rho>0:raise ValueError("fixed cut lies past actual root")
    cmin,cmax=rho.sqrt().lower(),rho.sqrt().upper()
    r=(cmax*cmax).upper()
    if not r<R:raise ValueError("actual cut leaves transferred error disk")
    errors={k:stored(v["complete_sup_error"]).upper()
            for k,v in d["complete_approximant_errors"].items()}
    finite={k:full_polynomial_norm(v,R/scale,Sin) for k,v in rows.items()}
    true={k:min(stored(d["complete_true_moduli_on_working_bidisk"][k]).upper(),
                (finite[k]+errors[k]).upper()) for k in rows}
    paid=source_error_bound(outer_radius=R,working_radius=r,s_radius=cmax,
        first_angle_loss=(Sin-Sout)/2,second_angle_loss=(Sin-Sout)/2,
        G_bound=true["G"],q_bound=true["q"],k_bound=true["kstar"],
        G_error=errors["G"],q_error=errors["q"],k_error=errors["kstar"],
        finite_q_bound=finite["q"],finite_k_bound=finite["kstar"])
    EH=(paid["regularized_source_sup_error"]+errors["Sreg"]/(Sin-Sout)).upper()
    EB=(errors["G"]/(3*cmin**3)+paid["B1_sup_error"]/cmin).upper()
    EC=(EB+errors["U0"]/(4*cmin**3)+errors["U1"]/(4*cmin)
        +errors["Ltheta"]/4).upper()
    EZ=(errors["Ltheta"]/4).upper()
    # At a common true ray and true endpoints, this is the field-only error.
    Eroot=(EB+cmax*EH+EZ).upper()
    report={"kind":"R106_full_parameter_center_reference_regularized_source_errors",
        "complete":True,"proved":True,"source_sha256":sha(__file__),
        "transfer_path":str(a.transfer),"transfer_sha256":sha(a.transfer),
        "identity":d["identity"],"root":d["root"],"original_fixed_cut":str(a.cut),
        "rho_cut":ball_record(rho),"s_cut_lower":ball_record(cmin),
        "s_cut_upper":ball_record(cmax),"source_physical_strip":str(a.working_strip),
        "input_error_rho_radius":d["working_rho_radius"],
        "input_error_physical_strip":d["working_physical_angle_strip"],
        "true_input_moduli":{k:ball_record(v) for k,v in true.items()},
        "finite_input_moduli":{k:ball_record(v) for k,v in finite.items()},
        "complete_regularized_source_sup_error":ball_record(EH),
        "complete_transport_boundary_sup_error":ball_record(EB),
        "complete_full_cut_field_sup_error":ball_record(EC),
        "complete_root_field_sup_error":ball_record(EZ),
        "field_only_root_error_before_global_J":ball_record(Eroot),
        "source_error_terms":{k:ball_record(v) for k,v in paid.items()},
        "scope":"Exact finite expressions formed from every center coefficient, compared with the actual full parameter family on the whole stated domain. A later rounded output coefficient choice, true-reference flow error and continuous quadrature still require their own complete fees.",
        "all_means_and_product_frequencies_retained":True,
        "true_reference_composition_error_paid":False,
        "continuous_phase_quadrature_paid":False,
        "dependencies":{n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_subprincipal_root_parameter_transfer.py",
            "fourfold_subprincipal_root_regularized_transport.py",
            "fourfold_phase_root_fourier_fit.py")},
        "wall_seconds":time.monotonic()-start}
    save(a.out,report)
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
        "H_error":report["complete_regularized_source_sup_error"],
        "transport_error":report["complete_transport_boundary_sup_error"],
        "root_field_error":report["field_only_root_error_before_global_J"]},flush=True)


if __name__=="__main__":main()

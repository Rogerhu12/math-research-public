#!/usr/bin/env python3
"""Tight actual q,kstar on a whole complex root disk, not just at the root.
Uses the unchanged infinite primitive/Cauchy machinery. No source theorem is
declared passed until every continuous angular box and full radial disk passes.
Run from the topic directory; outputs checkpoints and a gzip report.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb, acb_series, arb, ctx
from fourfold_phase_beta_interval import (
    analytic_tail_derivative, ball_record, pad_complex, vector_cross, vector_dot)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_beta_derivative_collar import ParameterDerivativeCollar
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_subprincipal_root_fields import RootPhaseModel

def root_curvature_disk(target,radius,Efinite,budget,scale,R):
    """Enclose K_r on the full disk. Its convex range encloses -K(t-rho)/rho."""
    R0,RE=budget["radial_radius"],budget["E_radius"]
    if not 0<R<RE<R0:
        raise ValueError("invalid nested true curvature disks")
    finite_E_bound=3*(budget["finite_field_bounds"][0]/(R0-RE))**2
    Ej=[]
    for j in range(3):
        tail=analytic_tail_derivative(finite_E_bound,RE,R,Efinite.prec,j)
        infinite=math.factorial(j)*budget["E_error"]/(RE-R)**j
        Ej.append((-1)**j*pad_complex(
            target.disk_series(Efinite,scale,R,j),tail+infinite))
    aj=[(-1)**j*target.disk_series(radius,scale,R,j) for j in range(4)]
    a=acb_series([aj[j]/math.factorial(j) for j in range(4)],prec=4)
    E=acb_series([Ej[j]/math.factorial(j) for j in range(3)],prec=3)
    if not a[0].real>0 or not E[0].real>0:
        raise ValueError("true target radius or E has unresolved complex denominator")
    K=(a.derivative()*E.derivative()-2*a.derivative().derivative()*E)/(2*a*E*E)
    value=K[1]
    if not value.real>0:
        raise ValueError("true root curvature quotient has unresolved positive branch")
    return value,{"true_Kr_disk":complex_record(value),
                  "radius_real_lower":ball_record(a[0].real.lower()),
                  "E_real_lower":ball_record(E[0].real.lower()),
                  "interpretation":"Convex average of true K_r(t-z rho), 0<=z<=1, with exact K(t)=0."}

def complex_record(v):
    return {"real":ball_record(v.real),"imag":ball_record(v.imag)}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--radial-radius",type=Fraction,default=Fraction(1,2500))
    p.add_argument("--physical-strip",type=Fraction,default=Fraction(1,320))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--angles",type=int,default=1024)
    p.add_argument("--precision",type=int,default=40)
    p.add_argument("--bits",type=int,default=192)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    if args.angles<args.nodes or args.precision<12:
        raise ValueError("insufficient complete angular/radial grid")
    if args.out.suffix!=".gz":
        raise ValueError("use gzip for complete continuous angular cells")
    ctx.prec,ctx.cap=args.bits,10
    wall,cpu=time.monotonic(),time.process_time()
    model=RootPhaseModel(args.object,args.half_width,args.root_certificate,
                         args.physical_strip,nodes=args.nodes,refine_steps=3)
    target=model.target
    target.angles=args.angles
    ctx.cap=args.precision
    R=exact_arb(args.radial_radius)
    sigma=4*exact_arb(args.physical_strip)
    # All base primitive rows are recomputed at the requested true series order.
    # None of the low-order root jets is silently reused as a whole-disk field.
    coefficient,radius,Efinite,_,_=target.target(model.root,model.scale,None)
    width=sigma+arb.pi()/args.angles
    fields=ParameterDerivativeCollar._disk_fields(
        target,coefficient,model.budget,model.root,model.scale,R,width)
    kappa,kreport=root_curvature_disk(
        target,radius,Efinite,model.budget,model.scale,R)
    root_factor=kappa.sqrt(analytic=True)
    report={
      "kind":"R106_actual_complete_complex_root_characteristic_disk",
      "complete":False,"proved":False,"source_sha256":sha(__file__),
      "identity":provenance(target,args.object),
      "root_certificate_path":str(args.root_certificate),
      "root_certificate_sha256":sha(args.root_certificate),
      "certified_root":ball_record(model.root),
      "common_scalar_span":model.spans,
      "radial_radius":str(args.radial_radius),
      "physical_theta_strip":str(args.physical_strip),
      "normalized_theta_strip":str(4*args.physical_strip),
      "closed_angular_cover_width":ball_record(width),
      "primitive_nodes":args.nodes,"angles":args.angles,
      "series_precision":args.precision,"bits":args.bits,
      "curvature":kreport,"cells":[],"failed":[],"rows_done":0,
      "full_root_finite_part_proved":False,
      "full_phase_proved":False,
      "dependencies":{name:sha(Path(__file__).with_name(name)) for name in (
         "fourfold_phase_beta_interval.py","fourfold_phase_beta_bulk_interval.py",
         "fourfold_phase_beta_derivative_collar.py",
         "fourfold_phase_beta_parameter_germ.py",
         "fourfold_subprincipal_root_fields.py",
         "fourfold_phase_root_cauchy_frame_ci_v1.py",
         "fourfold_phase_root_potential_complex_strip.py",
         "fourfold_native_series_fft.py")}
    }
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-wall
        report["cpu_seconds"]=time.process_time()-cpu
        save(args.out,report)
    checkpoint()
    F,X,Frr,Y,Frt,Ftt=fields
    maxima_q=[];maxima_k=[];minima_a=[];minima_G=[]
    for j in range(args.angles):
        C=vector_cross(Y[j],X[j])
        G=vector_dot(C,C)
        if not G.real>0:
            report["failed"].append({"index":j,"factor":"G","ball":complex_record(G)})
            checkpoint();raise ValueError("whole complex area factor unresolved")
        m=vector_dot(C,Frt[j]);n=vector_dot(C,Ftt[j])
        a0,b0=-n/G,m/G
        if not a0.real>0:
            report["failed"].append({"index":j,"factor":"a0","ball":complex_record(a0)})
            checkpoint();raise ValueError("whole complex a0 factor unresolved")
        q=b0/a0;k=root_factor/a0
        qm,km=abs(q).upper(),abs(k).upper()
        if not qm.is_finite() or not km.is_finite():
            report["failed"].append({"index":j,"factor":"nonfinite q/k"})
            checkpoint();raise ValueError("nonfinite actual characteristic modulus")
        maxima_q.append(qm);maxima_k.append(km)
        minima_a.append(a0.real.lower());minima_G.append(G.real.lower())
        report["cells"].append({
            "index":j,"exact_center_theta_over_pi":str(Fraction(j,2*args.angles)),
            "exact_real_half_width_theta_over_pi":str(Fraction(1,4*args.angles)),
            "full_complex_rho_disk":True,
            "q_modulus":ball_record(qm),"kstar_modulus":ball_record(km),
            "a0_real_lower":ball_record(a0.real.lower()),
            "area2_real_lower":ball_record(G.real.lower())})
        report["rows_done"]=j+1
        if (j+1)%64==0:
            checkpoint()
            print({"done":j+1,"total":args.angles,"wall":report["wall_seconds"]},flush=True)
    if len(report["cells"])!=args.angles:
        raise ValueError("incomplete full periodic angular cover")
    # max/min act on exact outward endpoints, never on overlapping interval balls.
    report.update(complete=True,proved=True,
        q_modulus=ball_record(max(maxima_q)),
        kstar_modulus=ball_record(max(maxima_k)),
        a0_real_lower=ball_record(min(minima_a)),
        area2_real_lower=ball_record(min(minima_G)),
        coverage="All equal closed cells fill the physical pi/2 circle. Full complex angle/rho errors were paid before every algebraic division.",
        inward_orientation="At the positive root q changes sign on reversing r; all modulus bounds remain valid.")
    checkpoint()
    print({"complete":True,"q":report["q_modulus"],"kstar":report["kstar_modulus"],
           "sha256":sha(args.out),"out":str(args.out)},flush=True)

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Actual grounded log-density on the complete negative-root analytic bidisk.

This is an input to the exact characteristic canonical chart. It is not the
positive-side finite coordinate approximation, and does not itself assert V.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record,vector_dot,vector_cross
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import save,sha
from fourfold_subprincipal_root_fields import RootPhaseModel
from fourfold_subprincipal_root_bidisk_domain import true_target_root_disk_jet
from fourfold_subprincipal_root_bidisk_boundary_v2 import complex_boundary_fields,seven_geometry


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--radial-radius",type=Fraction,default=Fraction(7,25000))
    p.add_argument("--physical-strip",type=Fraction,default=Fraction(1,400))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--angles",type=int,default=1024)
    p.add_argument("--precision",type=int,default=48)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.out.suffix!=".gz":raise ValueError("new gzip report required")
    if not 0<a.half_width<=Fraction(1,10**9):raise ValueError("outside paid actual family")
    if sha(a.object)!="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848":
        raise ValueError("actual object changed")
    ctx.prec,ctx.cap=a.bits,10;start=time.monotonic()
    model=RootPhaseModel(a.object,a.half_width,a.root_certificate,a.physical_strip,
                        nodes=a.nodes,refine_steps=3)
    target=model.target;target.angles=a.angles;ctx.cap=a.precision
    R,S=exact_arb(a.radial_radius),exact_arb(a.physical_strip)
    if not 0<R<model.budget["E_radius"]<model.budget["radial_radius"]:
        raise ValueError("actual radial analytic domains are not nested")
    cf,radius,Efinite,_,_=target.target(model.root,model.scale,None)
    Q,Qrho,kreport=true_target_root_disk_jet(target,radius,Efinite,model.budget,model.scale,R)
    geom,fees=complex_boundary_fields(target,cf,model.budget,model.scale,R,S)
    report={"kind":"actual_negative_root_grounded_log_density_bidisk",
        "complete":False,"proved":False,"source_sha256":sha(__file__),
        "identity":provenance(target,a.object),"object_path":str(a.object),
        "object_sha256":sha(a.object),"root_certificate_path":str(a.root_certificate),
        "root_certificate_sha256":sha(a.root_certificate),"root":ball_record(model.root),
        "rho_radius":str(a.radial_radius),"physical_angle_strip":str(a.physical_strip),
        "nodes":a.nodes,"angles":a.angles,"precision":a.precision,"bits":a.bits,
        "curvature_disk":kreport,"complete_geometry_fees":fees,"cells":[],
        "grounded_density_identity":"U=Q*Fz^4*area2^2/support^4",
        "log_density_identity":"log U=log Q+4 log Fz+2 log area2-4 log support",
        "root_angle_identity":"Y0_prime=1/kstar(0,theta)=2 U0(0,theta)",
        "exact_negative_canonical_potential_proved":False,
        "dependencies":{n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_subprincipal_root_fields.py","fourfold_subprincipal_root_bidisk_domain.py",
            "fourfold_subprincipal_root_bidisk_boundary_v2.py","fourfold_phase_beta_interval.py",
            "fourfold_phase_beta_bulk_interval.py","fourfold_phase_beta_parameter_germ.py",
            "fourfold_phase_root_cauchy_frame_ci_v1.py","fourfold_phase_root_potential_complex_strip.py",
            "fourfold_native_series_fft.py")}}
    mods={k:[] for k in ("logU","q","kstar","Yprime_extension")};mins=[]
    for j in range(a.angles):
        F,X,Frr,Y,Frt,Ftt=[g[j] for g in geom]
        C=vector_cross(Y,X)
        area,support=vector_dot(C,C),vector_dot(C,F)
        if any(not z.real>0 for z in (Q,F[2],area,support)):
            raise ValueError("true log branch not in the right half-plane")
        L=Q.log()+4*F[2].log()+2*area.log()-4*support.log()
        aa=-vector_dot(C,Ftt)/area
        yp=aa/Q.sqrt(analytic=True)
        values,_=seven_geometry(F,X,Frr,Y,Frt,Ftt,Q,Qrho,R)
        if not yp.real>0:raise ValueError("true root-angle derivative extension not positive")
        rowmods={"logU":abs(L).upper(),"q":values["q"],"kstar":values["kstar"],
                 "Yprime_extension":abs(yp).upper()}
        for k,v in rowmods.items():mods[k].append(v)
        mins.append(yp.real.lower())
        report["cells"].append({"index":j,"true_moduli":{k:ball_record(v) for k,v in rowmods.items()},
                               "Yprime_extension_real_lower":ball_record(yp.real.lower())})
        if (j+1)%128==0:
            report["wall_seconds"]=time.monotonic()-start;save(a.out,report)
    report.update(complete=True,proved=True,
        complete_true_moduli={k:ball_record(max(v)) for k,v in mods.items()},
        root_angle_derivative_real_lower=ball_record(min(mins)),
        coverage="Closed upper angular boundary cells, Schwarz lower boundary, full rho disk, and the full angular strip by successive positive-real/max-modulus extension.",
        scope="True grounded log-density and characteristic inputs only. The exact negative canonical chart and V,V_xi are separate downstream conclusions.",
        wall_seconds=time.monotonic()-start)
    save(a.out,report)
    print({"out":str(a.out),"sha256":sha(a.out),"bounds":report["complete_true_moduli"],
           "root_angle_derivative_real_lower":report["root_angle_derivative_real_lower"],
           "seconds":report["wall_seconds"]},flush=True)


if __name__=="__main__":main()

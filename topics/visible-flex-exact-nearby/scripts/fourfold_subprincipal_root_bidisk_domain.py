#!/usr/bin/env python3
"""Actual common wide root bidisk for all nonmean phase inputs G,q,kstar.

This is a new native computation, not a transfer of the old small angular strip.
It uses the same exact affine target, root and infinite primitive. All three
moduli refer to one common complex radial disk and physical angular strip.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
from flint import acb, acb_series, arb, ctx
from fourfold_phase_beta_interval import (ball_record, vector_cross, vector_dot,
    analytic_tail_derivative,pad_complex)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_derivative_collar import ParameterDerivativeCollar
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import save,sha
from fourfold_subprincipal_root_fields import RootPhaseModel




def true_target_root_disk_jet(target,radius,Efinite,budget,scale,R):
    """Q=-K(t-rho)/rho and Q_rho by convex averages of K_r and -K_rr/2."""
    R0,RE=budget["radial_radius"],budget["E_radius"]
    if not 0<R<RE<R0:raise ValueError("root target disks not nested")
    EF=3*(budget["finite_field_bounds"][0]/(R0-RE))**2
    ev=[]
    for j in range(4):
        fee=(analytic_tail_derivative(EF,RE,R,Efinite.prec,j)
             +math.factorial(j)*budget["E_error"]/(RE-R)**j)
        ev.append((-1)**j*pad_complex(target.disk_series(Efinite,scale,R,j),fee))
    av=[(-1)**j*target.disk_series(radius,scale,R,j) for j in range(5)]
    a=acb_series([av[j]/math.factorial(j) for j in range(5)],prec=5)
    E=acb_series([ev[j]/math.factorial(j) for j in range(4)],prec=4)
    if not a[0].real>0 or not E[0].real>0:
        raise ValueError("true target denominators not separated")
    K=(a.derivative()*E.derivative()-2*a.derivative().derivative()*E)/(2*a*E*E)
    Q,Qrho=K[1],-K[2]
    if not Q.real>0:raise ValueError("true deflated curvature branch unresolved")
    record=lambda z:{"real":ball_record(z.real),"imag":ball_record(z.imag)}
    return Q,Qrho,{"true_Q_disk":record(Q),"true_Qrho_disk":record(Qrho),
                  "identity":"Q=int_0^1 K_r(t-z rho) dz; Qrho=-int_0^1 z K_rr(t-z rho) dz",
                  "radius_real_lower":ball_record(a[0].real.lower()),
                  "E_real_lower":ball_record(E[0].real.lower())}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--radial-radius",type=Fraction,default=Fraction(1,2500))
    p.add_argument("--physical-strip",type=Fraction,default=Fraction(1,64))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--angles",type=int,default=2048)
    p.add_argument("--precision",type=int,default=40)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if not 0<a.half_width<=Fraction(1,10**9):
        raise ValueError("requested parameter box is outside the paid real family")
    if a.angles<a.nodes or a.angles&(a.angles-1) or a.precision<12:
        raise ValueError("invalid actual angular/series layout")
    if a.out.exists():
        raise ValueError("new output path required; preserve partial or prior certificate")
    if a.out.suffix!=".gz":
        raise ValueError("complete angular report must be gzip")
    if sha(a.object)!="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848":
        raise ValueError("exact delta5 object bytes changed")
    ctx.prec,ctx.cap=a.bits,10
    wall,cpu=time.monotonic(),time.process_time()
    model=RootPhaseModel(a.object,a.half_width,a.root_certificate,a.physical_strip,
                         nodes=a.nodes,refine_steps=3)
    target=model.target;target.angles=a.angles
    ctx.cap=a.precision
    R,S=exact_arb(a.radial_radius),exact_arb(a.physical_strip)
    if not 0<R<model.budget["E_radius"]<model.budget["radial_radius"]:
        raise ValueError("true analytic root disks are not nested")
    width=4*S+arb.pi()/a.angles
    if not width<model.budget["sigma_normalized_x"]:
        raise ValueError("true angular input strip exhausted")
    report={"kind":"R106_actual_common_root_Gqk_bidisk","complete":False,"proved":False,
        "source_sha256":sha(__file__),"identity":provenance(target,a.object),
        "object_path":str(a.object),"object_sha256":sha(a.object),
        "root_certificate_path":str(a.root_certificate),"root_certificate_sha256":sha(a.root_certificate),
        "certified_root":ball_record(model.root),"common_scalar_spans":model.spans,
        "outer_rho_radius":str(a.radial_radius),"outer_physical_angle_strip":str(a.physical_strip),
        "closed_normalized_angular_width":ball_record(width),
        "nodes":a.nodes,"angles":a.angles,"precision":a.precision,"bits":a.bits,
        "qk_cells":[],"rows_done":0,"phase_integral_proved":False,
        "dependencies":{name:sha(Path(__file__).with_name(name)) for name in (
          "fourfold_subprincipal_root_fields.py",
          "fourfold_phase_beta_interval.py","fourfold_phase_beta_derivative_collar.py",
          "fourfold_phase_beta_parameter_germ.py","fourfold_phase_root_cauchy_frame_ci_v1.py",
          "fourfold_phase_root_potential_complex_strip.py","fourfold_native_series_fft.py")}}
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-wall
        report["cpu_seconds"]=time.process_time()-cpu
        save(a.out,report)
        if a.out.stat().st_size>=5_000_000:raise ValueError("report exceeds repository single-file limit")
    checkpoint()
    # This frozen method encloses the same original-height nonmean G before
    # angular mean; every cell includes full radial and infinite angular fees.
    MG,Gdomain=target.collar_domain_bound(model.root,model.scale,R,4*S,model.budget)
    report["G_domain"]=Gdomain;report["uniform_G_bound"]=ball_record(MG)
    report["stage"]="complete G bidisk";checkpoint()
    print({"stage":"complete G bidisk","G":report["uniform_G_bound"]},flush=True)
    cf,radius,Efinite,_,_=target.target(model.root,model.scale,None)
    geometry=ParameterDerivativeCollar._disk_fields(
        target,cf,model.budget,model.root,model.scale,R,width)
    kappa,kappa_rho,kreport=true_target_root_disk_jet(target,radius,Efinite,model.budget,model.scale,R)
    rootfactor=kappa.sqrt(analytic=True)
    rho=pad_complex(0,R)
    report["kappa_domain"]=kreport
    F,X,Frr,Y,Frt,Ftt=geometry
    qmax=[];kmax=[]
    auxiliary={name:[] for name in ("Sreg","Ltheta","U0","U1")}
    for j in range(a.angles):
        C=vector_cross(Y[j],X[j]);G=vector_dot(C,C)
        if not G.real>0:raise ValueError("actual complex G denominator unresolved")
        m=vector_dot(C,Frt[j]);n=vector_dot(C,Ftt[j])
        aa,bb=-n/G,m/G
        if not aa.real>0:raise ValueError("actual complex a0 denominator unresolved")
        # Inward positive-root convention. Moduli would also be valid with -q.
        q=-bb/aa;k=rootfactor/aa
        if not q.is_finite() or not k.is_finite():raise ValueError("nonfinite true characteristic field")
        qmax.append(abs(q).upper());kmax.append(abs(k).upper())
        H=vector_dot(C,F[j]);R2=vector_dot(F[j],F[j])
        if not H.real>0 or not R2.real>0 or not F[j,2].real>0:
            raise ValueError("true original-height auxiliary denominator unresolved")
        Cr1,Cr2=vector_cross(Frt[j],X[j]),vector_cross(Y[j],Frr[j])
        Ct1,Ct2=vector_cross(Ftt[j],X[j]),vector_cross(Y[j],Frt[j])
        Cr=[Cr1[c]+Cr2[c] for c in range(3)]
        Ct=[Ct1[c]+Ct2[c] for c in range(3)]
        FX,FY=vector_dot(F[j],X[j]),vector_dot(F[j],Y[j])
        zr=vector_dot(Cr,F[j])/H-vector_dot(C,Cr)/G-FX/R2
        ztheta=vector_dot(Ct,F[j])/H-vector_dot(C,Ct)/G-FY/R2
        ell=Y[j,2]/F[j,2]-FY/R2
        l=vector_dot(C,Frr[j])
        actualK=(l*n-m*m)/(G*G)
        omega=(actualK+rho*kappa)/aa
        Ltheta=-2*ztheta
        Lrho_regular=kappa_rho/(2*kappa)+2*zr
        aux={"Sreg":omega*ell/rootfactor,"Ltheta":Ltheta,
             "U0":aa/(2*rootfactor),
             "U1":(aa*Lrho_regular-bb*Ltheta)/rootfactor}
        for name,z in aux.items():
            if not z.is_finite():raise ValueError("nonfinite true auxiliary field "+name)
            auxiliary[name].append(abs(z).upper())
        report["qk_cells"].append({"index":j,"q_modulus":ball_record(qmax[-1]),
            "kstar_modulus":ball_record(kmax[-1]),"area2_real_lower":ball_record(G.real.lower()),
            "a0_real_lower":ball_record(aa.real.lower()),
            "auxiliary_moduli":{name:ball_record(auxiliary[name][-1]) for name in aux}})
        report["rows_done"]=j+1
        if (j+1)%64==0:checkpoint()
    report.update(complete=True,proved=True,stage="complete common bidisk",
       uniform_q_bound=ball_record(max(qmax)),uniform_kstar_bound=ball_record(max(kmax)),
       uniform_root_auxiliary_bounds={name:ball_record(max(values)) for name,values in auxiliary.items()},
       root_auxiliary_convention="Sreg=s*S; V_rho=s^-3*U0+s^-1*U1; Ltheta is the original-height angular log-density derivative; all mixed signs are inward.",
       coverage="All closed equal angular cells fill the pi/2 period; full complex rho disk and angular strip paid before divisions.",
       root_identity="For actual original-height reduced G, kstar(0)*G(0)=-1/16 exactly; finite interval multiplication is not used to redefine geometry.")
    checkpoint()
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
       "G":report["uniform_G_bound"],"q":report["uniform_q_bound"],"kstar":report["uniform_kstar_bound"]},flush=True)


if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""True seven-field root bidisk through complete complex-angle boundaries.

New native calculation: no numerical output is implied by saving this source.
The finite primitive is evaluated at theta_j+i*S without real projection.
Real closed-cell motion, infinite angular error and radial Taylor tails are
paid separately. Positive-real geometry on both boundary circles implies the
same denominator gates throughout the periodic angular strip, in the stated
order. All radial disks refer to the exact real affine root t(p).
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb, acb_series, arb, ctx
from fourfold_phase_beta_interval import (analytic_tail_derivative,
    array_derivative, ball_record, pad_complex, polynomial_disk_bound,
    primitive_fourier_budget, series_array, vector_cross, vector_dot)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import save, sha
from fourfold_subprincipal_root_bidisk_domain import true_target_root_disk_jet
from fourfold_subprincipal_root_fields import RootPhaseModel

FIELD_KEYS=((0,0),(1,0),(2,0),(0,1),(1,1),(0,2))
NAMES=("G","q","kstar","Sreg","Ltheta","U0","U1")


def complex_boundary_fields(target,cf,budget,scale,R,S):
    """Six true physical jets on every closed cell of Im(theta)=+S.

    Finite coefficients use normalized mode k, physical angular frequency 4k.
    The cell half-width in normalized angle is pi/N. No imaginary cell padding
    is needed because exp(-4kS) is evaluated before the actual inverse DFT.
    """
    R0=budget["radial_radius"]
    sigma=4*S
    errors,finite=primitive_fourier_budget(
        target.nodes,budget["sigma_normalized_x"],sigma,R0,
        budget["radius_bound"],budget["height_bound"],budget["tangent_bound"])
    N=target.angles
    theta_gap=arb.pi()/N
    sources=[cf,target.angular(cf),target.angular(cf,2)]
    result={}
    fees={}
    for ar,at in FIELD_KEYS:
        source=array_derivative(sources[at],-scale,ar)
        # Radial differentiation lowers each finite polynomial's declared
        # precision. NativeSeriesFFT rejects padding zeros with ctx.cap instead.
        # These modes are exactly zero finite polynomials; declaring zero at the
        # common differentiated precision changes no coefficient or true tail.
        precision={v.prec for v in source.flat}
        if len(precision)!=1:
            raise ValueError("differentiated finite inputs have unequal precision")
        degree=precision.pop()
        padded=np.empty((N,3),dtype=object)
        for key in np.ndindex(padded.shape):
            padded[key]=acb_series([0],prec=degree)
        angular=[arb(0) for _ in range(3)]
        for k in range(target.nodes):
            signed=k if k<target.nodes//2 else k-target.nodes
            multiplier=(-signed*sigma).exp()
            for c in range(3):
                padded[signed%N,c]=source[k,c]*multiplier
                angular[c]+=polynomial_disk_bound(source[k,c],R/scale)*(
                    abs(signed)*theta_gap)*(abs(signed)*sigma).exp()
        # NativeSeriesFFT/NativeFFT carries all complex coefficients and balls.
        # Calling target.evaluate would erase the genuine imaginary boundary.
        rows=target.fourier.fft(padded,inverse=True)*N
        tail=analytic_tail_derivative(finite[at],R0,R,cf[0,0].prec,ar)
        infinite=math.factorial(ar)*errors[at]/(R0-R)**ar
        out=np.empty(rows.shape,object)
        for key in np.ndindex(rows.shape):
            out[key]=pad_complex(target.disk_series(rows[key],scale,R),
                                 angular[key[1]]+tail+infinite)
        result[(ar,at)]=out
        fees[f"r{ar}_theta{at}"]={
            "finite_closed_angle_cell":[ball_record(x.upper()) for x in angular],
            "finite_radial_Taylor_tail":ball_record(tail),
            "true_infinite_primitive":ball_record(infinite.upper())}
    return [result[key] for key in FIELD_KEYS],fees


def seven_geometry(F,X,Frr,Y,Frt,Ftt,Q,Qrho,R):
    """The original-height seven functions before any angular mean.

    a0=-n/area2 and b0=m/area2 are the zeta^2-scaled principal fields.
    The returned modulus bounds cover the whole complex rho disk.
    """
    C=vector_cross(Y,X)
    nr1,nr2=vector_cross(Frt,X),vector_cross(Y,Frr)
    nt1,nt2=vector_cross(Ftt,X),vector_cross(Y,Frt)
    nr=[nr1[c]+nr2[c] for c in range(3)]
    nt=[nt1[c]+nt2[c] for c in range(3)]
    area2,radius2,support=vector_dot(C,C),vector_dot(F,F),vector_dot(C,F)
    first={"area2":area2,"radius2":radius2,"support":support,"Fz":F[2]}
    if any(not z.real>0 for z in first.values()):
        raise ValueError("true geometric boundary denominator unresolved")
    l,m,n=[vector_dot(C,w) for w in (Frr,Frt,Ftt)]
    aa,bb,cc=-n/area2,m/area2,-l/area2
    if not aa.real>0:
        raise ValueError("true a0 boundary denominator unresolved")
    kap=Q.sqrt(analytic=True)
    if not kap.real>0:
        raise ValueError("true root-factor branch unresolved")
    rho=pad_complex(0,R)
    K=-rho*Q
    actualK=(l*n-m*m)/(area2*area2)
    omega,chat=(actualK-K)/aa,(bb*bb+K)/aa
    FX,FY=vector_dot(F,X),vector_dot(F,Y)
    d=(aa*(vector_dot(X,X)-FX*FX/radius2)
       +2*bb*(vector_dot(X,Y)-FX*FY/radius2)
       +cc*(vector_dot(Y,Y)-FY*FY/radius2))/radius2
    zr=vector_dot(nr,F)/support-vector_dot(C,nr)/area2-FX/radius2
    ztheta=vector_dot(nt,F)/support-vector_dot(C,nt)/area2-FY/radius2
    Lrho=Qrho/(2*Q)+2*zr
    Ltheta=-2*ztheta
    ell=Y[2]/F[2]-FY/radius2
    A=-aa/(16*kap)
    B=-(aa*Lrho-bb*Ltheta)/(4*kap)
    C2=(d+omega*(ell*ell+ell*Ltheta)
        -(aa*Lrho*Lrho-2*bb*Lrho*Ltheta+chat*Ltheta*Ltheta)/4)/kap
    values={"q":-bb/aa,"kstar":kap/aa,"Sreg":omega*ell/kap,
            "Ltheta":Ltheta,"U0":aa/(2*kap),
            "U1":(aa*Lrho-bb*Ltheta)/kap}
    if any(not z.is_finite() for z in values.values()):
        raise ValueError("nonfinite actual root auxiliary")
    # Avoid injecting a square enclosure for rho into the dominant constant.
    moduli={"G":(abs(A)+R*abs(B)+R*R*abs(C2)).upper()}
    moduli.update({name:abs(value).upper() for name,value in values.items()})
    minima={name:value.real.lower() for name,value in first.items()}
    minima["a0"]=aa.real.lower()
    return moduli,minima


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
    p.add_argument("--angles",type=int,default=4096)
    p.add_argument("--precision",type=int,default=40)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if not 0<a.half_width<=Fraction(1,10**9):
        raise ValueError("parameter family outside the paid actual root family")
    if a.angles<a.nodes or a.angles&(a.angles-1) or a.precision<12:
        raise ValueError("invalid angular/Taylor layout")
    if a.out.exists() or a.out.suffix!=".gz":
        raise ValueError("a new gzip report path is required")
    if sha(a.object)!="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848":
        raise ValueError("exact delta5 object bytes changed")
    ctx.prec,ctx.cap=a.bits,10
    wall,cpu=time.monotonic(),time.process_time()
    model=RootPhaseModel(a.object,a.half_width,a.root_certificate,a.physical_strip,
                         nodes=a.nodes,refine_steps=3)
    target=model.target
    target.angles=a.angles
    ctx.cap=a.precision
    R,S=exact_arb(a.radial_radius),exact_arb(a.physical_strip)
    if not 0<R<model.budget["E_radius"]<model.budget["radial_radius"]:
        raise ValueError("complex radial disks are not nested")
    if not 0<4*S<model.budget["sigma_normalized_x"]:
        raise ValueError("true angular input domain exhausted")
    names=("fourfold_subprincipal_root_bidisk_domain.py",
      "fourfold_subprincipal_root_fields.py","fourfold_phase_beta_interval.py",
      "fourfold_phase_beta_bulk_interval.py","fourfold_phase_beta_parameter_germ.py",
      "fourfold_phase_root_cauchy_frame_ci_v1.py",
      "fourfold_phase_root_potential_complex_strip.py","fourfold_native_series_fft.py")
    report={"kind":"R106_actual_common_root_Gqk_bidisk","complete":False,"proved":False,
      "source_file":Path(__file__).name,"source_sha256":sha(__file__),
      "identity":provenance(target,a.object),"object_path":str(a.object),
      "object_sha256":sha(a.object),"root_certificate_path":str(a.root_certificate),
      "root_certificate_sha256":sha(a.root_certificate),
      "certified_root":ball_record(model.root),"common_scalar_spans":model.spans,
      "outer_rho_radius":str(a.radial_radius),
      "outer_physical_angle_strip":str(a.physical_strip),
      "nodes":a.nodes,"angles":a.angles,"precision":a.precision,"bits":a.bits,
      "rows_done":0,"qk_cells":[],"phase_integral_proved":False,
      "dependencies":{name:sha(Path(__file__).with_name(name)) for name in names}}
    def checkpoint():
        report["cpu_seconds"]=time.process_time()-cpu
        report["wall_seconds"]=time.monotonic()-wall
        save(a.out,report)
        if a.out.stat().st_size>=5_000_000:
            raise ValueError("complete report exceeds the repository file limit")
    checkpoint()
    cf,radius,Efinite,_,_=target.target(model.root,model.scale,None)
    Q,Qrho,kreport=true_target_root_disk_jet(target,radius,Efinite,model.budget,model.scale,R)
    report["kappa_domain"]=kreport
    geometry,fees=complex_boundary_fields(target,cf,model.budget,model.scale,R,S)
    report["complete_geometry_fees"]=fees
    report["stage"]="true complex-boundary six jets"
    checkpoint()
    print({"stage":report["stage"],"angles":a.angles},flush=True)
    bounds={name:[] for name in NAMES}
    lowers={name:[] for name in ("area2","radius2","support","Fz","a0")}
    for j in range(a.angles):
        moduli,minima=seven_geometry(*(item[j] for item in geometry),Q,Qrho,R)
        for name,value in moduli.items():bounds[name].append(value)
        for name,value in minima.items():lowers[name].append(value)
        report["qk_cells"].append({"index":j,
            "full_true_moduli":{name:ball_record(value) for name,value in moduli.items()},
            "positive_real_lower":{name:ball_record(value) for name,value in minima.items()}})
        report["rows_done"]=j+1
        if (j+1)%64==0:checkpoint()
    report.update(complete=True,proved=True,stage="whole seven-field complex bidisk",
      uniform_G_bound=ball_record(max(bounds["G"])),
      uniform_q_bound=ball_record(max(bounds["q"])),
      uniform_kstar_bound=ball_record(max(bounds["kstar"])),
      uniform_root_auxiliary_bounds={name:ball_record(max(bounds[name]))
                                    for name in ("Sreg","Ltheta","U0","U1")},
      positive_real_minima={name:ball_record(min(values)) for name,values in lowers.items()},
      coverage="All closed real angular cells on Im(theta)=+S; -S follows by Schwarz and conjugation of the entire rho disk. Sequential harmonic minimum and maximum modulus extend the complete gates and moduli to the whole strip.",
      mean_retained=True,
      root_identity="kstar(0)*G(0)=-1/16 follows from the same actual original-height formulas; no nodal redefinition or mean substitution.",
      extension_order=["area2/radius2/support/Fz are entire in theta",
        "their positive real part implies reciprocal analyticity",
        "a0=-n/area2 is analytic with positive real boundary and hence interior",
        "Q is theta-independent and has positive real part on the full rho disk",
        "all seven actual fields are analytic; apply maximum modulus"])
    checkpoint()
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
           "uniform_G_bound":report["uniform_G_bound"]},flush=True)


if __name__=="__main__":
    main()

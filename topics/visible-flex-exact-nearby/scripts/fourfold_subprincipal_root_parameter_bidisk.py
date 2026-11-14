#!/usr/bin/env python3
"""True moving-root parameter derivatives of all seven R106 analytic fields.

All derivatives hold at fixed rho=t(p)-r and fixed physical theta, uniformly
through the real parameter interval and a complete complex rho/angle bidisk.
The shared parameter is differentiated before the finite Fourier evaluation.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb,acb_series,arb,ctx
from fourfold_phase_beta_interval import (
    analytic_tail_derivative,array_derivative,ball_record,pad_complex,
    polynomial_disk_bound,primitive_fourier_budget,vector_cross,vector_dot)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_derivative import ParameterDerivativeTarget,record_budget
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_beta_derivative_bulk import Dual
from fourfold_phase_root_fourier_fit import save,sha
from fourfold_subprincipal_root_fields import RootPhaseModel
from fourfold_native_series_fft import NativeSeriesFFT

KEYS=((0,0),(1,0),(2,0),(0,1),(1,1),(0,2))
NAMES=("G","q","kstar","Sreg","Ltheta","U0","U1")


def boundary_jets(target,cf,budget,scale,R,S,keys):
    R0=budget["radial_radius"]
    errors,finite=primitive_fourier_budget(target.nodes,
        budget["sigma_normalized_x"],4*S,R0,budget["radius_bound"],
        budget["height_bound"],budget["tangent_bound"])
    N=target.angles;gap=arb.pi()/N
    sources=[cf,target.angular(cf),target.angular(cf,2)]
    output={};fees={}
    for ar,at in keys:
        source=array_derivative(sources[at],-scale,ar)
        precision={z.prec for z in source.flat}
        if len(precision)!=1:raise ValueError("unequal finite jet precision")
        degree=precision.pop()
        padded=np.empty((N,3),object)
        for key in np.ndindex(padded.shape):padded[key]=acb_series([0],prec=degree)
        angle=[arb(0) for _ in range(3)]
        for k in range(target.nodes):
            signed=k if k<target.nodes//2 else k-target.nodes
            for c in range(3):
                padded[signed%N,c]=source[k,c]*(-4*signed*S).exp()
                angle[c]+=polynomial_disk_bound(source[k,c],R/scale)*(
                    abs(signed)*gap)*(4*abs(signed)*S).exp()
        rows=target.fourier.fft(padded,inverse=True)*N
        tail=analytic_tail_derivative(finite[at],R0,R,cf[0,0].prec,ar)
        infinite=math.factorial(ar)*errors[at]/(R0-R)**ar
        out=np.empty(rows.shape,object)
        for key in np.ndindex(rows.shape):
            out[key]=pad_complex(target.disk_series(rows[key],scale,R),
                                 angle[key[1]]+tail+infinite)
        output[(ar,at)]=out
        fees[f"r{ar}_theta{at}"]={
            "finite_closed_angle_cell":[ball_record(x.upper()) for x in angle],
            "finite_radial_Taylor_tail":ball_record(tail),
            "true_infinite_primitive":ball_record(infinite.upper())}
    return output,fees


def curvature_jets(target,data,budgets,scale,R,tp):
    base,change=budgets
    R0,RE=base["radial_radius"],base["E_radius"]
    if not 0<R<RE<R0:raise ValueError("curvature disks not nested")
    M=base["finite_field_bounds"][0]/(R0-RE)
    Md=change["finite_field_bounds"][0]/(R0-RE)
    bounds=(3*M*M,6*M*Md)
    ee=[]
    for source,fee,bound in zip((data["Efinite"],data["Edfinite"]),budgets,bounds):
        jets=[]
        for j in range(5):
            error=(analytic_tail_derivative(bound,RE,R,source.prec,j)
                   +math.factorial(j)*fee["E_error"]/(RE-R)**j)
            jets.append((-1)**j*pad_complex(target.disk_series(source,scale,R,j),error))
        ee.append(acb_series([v/math.factorial(j) for j,v in enumerate(jets)],prec=5))
    aa=[]
    for source in (data["a"],data["ad"]):
        aa.append(acb_series([(-1)**j*target.disk_series(source,scale,R,j)/
                             math.factorial(j) for j in range(6)],prec=6))
    a,ad=aa;E,Ed=ee
    if not a[0].real>0 or not E[0].real>0:
        raise ValueError("true scalar curvature denominators unresolved")
    C=a.derivative()*E.derivative()-2*a.derivative().derivative()*E
    Cd=(ad.derivative()*E.derivative()+a.derivative()*Ed.derivative()
        -2*ad.derivative().derivative()*E-2*a.derivative().derivative()*Ed)
    K=C/(2*a*E*E)
    Kd=Cd/(2*a*E*E)-K*(ad/a+2*Ed/E)
    if K.prec<4 or Kd.prec<3:raise ValueError("insufficient true curvature jets")
    # Exact root identity and its parameter derivative give these segment
    # averages; all physical r derivative ranges above cover their segments.
    Q=Dual(K[1],Kd[1]+2*tp*K[2])
    Qrho=Dual(-K[2],-Kd[2]-3*tp*K[3])
    if not Q.v.real>0:raise ValueError("true deflated curvature branch unresolved")
    rec=lambda z:{"real":ball_record(z.real),"imag":ball_record(z.imag)}
    return Q,Qrho,{"Q":rec(Q.v),"Qrho":rec(Qrho.v),
        "moving_parameter_Q":rec(Q.d),"moving_parameter_Qrho":rec(Qrho.d),
        "identities":[
            "Q=int_0^1 K_r(t-u*rho,p) du",
            "Q_p=int_0^1 (K_rp+t_p*K_rr)(t-u*rho,p) du",
            "Qrho=-int_0^1 u*K_rr(t-u*rho,p) du",
            "Qrho_p=-int_0^1 u*(K_rrp+t_p*K_rrr)(t-u*rho,p) du"]}


def seven_dual(fields,Q,Qrho,R):
    F,X,Frr,Y,Frt,Ftt=fields
    C=vector_cross(Y,X)
    cr1,cr2=vector_cross(Frt,X),vector_cross(Y,Frr)
    ct1,ct2=vector_cross(Ftt,X),vector_cross(Y,Frt)
    Cr=[cr1[j]+cr2[j] for j in range(3)]
    Ct=[ct1[j]+ct2[j] for j in range(3)]
    area,radius,support=vector_dot(C,C),vector_dot(F,F),vector_dot(C,F)
    first={"area2":area,"radius2":radius,"support":support,"Fz":F[2]}
    if any(not v.v.real>0 for v in first.values()):
        raise ValueError("true geometry boundary denominator unresolved")
    l,m,n=[vector_dot(C,z) for z in (Frr,Frt,Ftt)]
    a,b,c=-n/area,m/area,-l/area
    if not a.v.real>0:raise ValueError("true a0 boundary denominator unresolved")
    z=Q.v.sqrt(analytic=True);kap=Dual(z,Q.d/(2*z))
    rho=Dual(pad_complex(0,R),acb(0));K=-rho*Q
    omega,chat=((l*n-m*m)/(area*area)-K)/a,(b*b+K)/a
    FX,FY=vector_dot(F,X),vector_dot(F,Y)
    d=(a*(vector_dot(X,X)-FX*FX/radius)
       +2*b*(vector_dot(X,Y)-FX*FY/radius)
       +c*(vector_dot(Y,Y)-FY*FY/radius))/radius
    zr=vector_dot(Cr,F)/support-vector_dot(C,Cr)/area-FX/radius
    zt=vector_dot(Ct,F)/support-vector_dot(C,Ct)/area-FY/radius
    Lrho=Qrho/(2*Q)+2*zr;Ltheta=-2*zt
    ell=Y[2]/F[2]-FY/radius
    A=-a/(16*kap)
    B=-(a*Lrho-b*Ltheta)/(4*kap)
    C2=(d+omega*(ell*ell+ell*Ltheta)
        -(a*Lrho*Lrho-2*b*Lrho*Ltheta+chat*Ltheta*Ltheta)/4)/kap
    values={"q":-b/a,"kstar":kap/a,"Sreg":omega*ell/kap,
        "Ltheta":Ltheta,"U0":a/(2*kap),"U1":(a*Lrho-b*Ltheta)/kap}
    if any(not v.v.is_finite() or not v.d.is_finite() for v in values.values()):
        raise ValueError("nonfinite complete parameter jet")
    moduli={"G":(abs(A.v)+R*abs(B.v)+R*R*abs(C2.v)).upper()}
    derivatives={"G":(abs(A.d)+R*abs(B.d)+R*R*abs(C2.d)).upper()}
    moduli.update({k:abs(v.v).upper() for k,v in values.items()})
    derivatives.update({k:abs(v.d).upper() for k,v in values.items()})
    minima={k:v.v.real.lower() for k,v in first.items()}
    minima["a0"]=a.v.real.lower()
    return moduli,derivatives,minima


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
    if a.out.exists() or a.out.suffix!=".gz":raise ValueError("new gzip output required")
    if not 0<a.half_width<=Fraction(1,10**9) or a.precision<12:
        raise ValueError("outside actual family or insufficient precision")
    if a.angles<a.nodes or a.angles&(a.angles-1):raise ValueError("invalid angle layout")
    if sha(a.object)!="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848":
        raise ValueError("actual affine object differs")
    ctx.prec,ctx.cap=a.bits,10;start=time.monotonic()
    model=RootPhaseModel(a.object,a.half_width,a.root_certificate,a.physical_strip,
                         nodes=a.nodes,refine_steps=3)
    target=ParameterDerivativeTarget(a.object,a.half_width,a.nodes,a.angles,
                                    arb(".003"),arb(".0025"),arb(".32"))
    target.fourier=NativeSeriesFFT()
    knots={Fraction.from_float(float(v)) for k,vs in target.frozen.items()
           if k.endswith("_knots") for v in vs}
    knots|={-v for v in knots}
    cells=[(x,y) for x,y in zip(sorted(knots),sorted(knots)[1:])
           if exact_arb(x)<model.root.lower() and model.root.upper()<exact_arb(y)]
    if len(cells)!=1:raise ValueError("root leaves a common exact scalar span")
    target.set_cell(*cells[0]);ctx.cap=a.precision
    R,S=exact_arb(a.radial_radius),exact_arb(a.physical_strip)
    budgets=target.parameter_input_budget(model.root,arb(".003"),arb(".32"),arb(".0025"))
    if not 0<R<budgets[0]["E_radius"] or not 0<4*S<budgets[0]["sigma_normalized_x"]:
        raise ValueError("actual analytic domain exhausted")
    data=target.parameter_target(model.root,model.scale,budgets)
    Cr=-data["C"][1]/model.scale;Kr=-data["K"][1]/model.scale
    if not Cr.real>0 or not Kr.real>0:raise ValueError("root transversality unresolved")
    tp1=(-data["Cd"][0]/Cr).real;tp2=(-data["Kd"][0]/Kr).real
    if not tp1.overlaps(tp2):raise ValueError("implicit root formulas differ")
    tp=tp1.intersection(tp2)
    Q,Qrho,kreport=curvature_jets(target,data,budgets,model.scale,R,tp)
    basekeys=tuple(sorted(set(KEYS)|{(ar+1,at) for ar,at in KEYS}))
    base,bfees=boundary_jets(target,data["F"],budgets[0],model.scale,R,S,basekeys)
    change,dfees=boundary_jets(target,data["Fd"],budgets[1],model.scale,R,S,KEYS)
    report={"kind":"R106_actual_moving_root_parameter_seven_field_bidisk",
        "complete":False,"proved":False,"source_sha256":sha(__file__),
        "identity":provenance(target,a.object),"object_path":str(a.object),
        "object_sha256":sha(a.object),"root_certificate_path":str(a.root_certificate),
        "root_certificate_sha256":sha(a.root_certificate),"root":ball_record(model.root),
        "exact_common_scalar_span":[str(x) for x in cells[0]],
        "moving_root_parameter_derivative":ball_record(tp),
        "rho_radius":str(a.radial_radius),"physical_angle_strip":str(a.physical_strip),
        "nodes":a.nodes,"angles":a.angles,"precision":a.precision,"bits":a.bits,
        "base_infinite_budget":record_budget(budgets[0]),
        "parameter_infinite_budget":record_budget(budgets[1]),
        "base_geometry_fees":bfees,"parameter_geometry_fees":dfees,
        "curvature_parameter_jet":kreport,"rows_done":0,"cells":[],
        "dependencies":{n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_phase_beta_interval.py","fourfold_phase_beta_parameter_derivative.py",
            "fourfold_phase_beta_parameter_germ.py","fourfold_phase_beta_derivative_bulk.py",
            "fourfold_subprincipal_root_fields.py","fourfold_native_series_fft.py",
            "fourfold_phase_root_fourier_fit.py")}}
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-start
        save(a.out,report)
    checkpoint()
    print({"stage":"whole moving-root parameter jets","angles":a.angles},flush=True)
    mods={k:[] for k in NAMES};ders={k:[] for k in NAMES}
    lows={k:[] for k in ("area2","radius2","support","Fz","a0")}
    for j in range(a.angles):
        fields=[[Dual(base[(ar,at)][j,c],
                      change[(ar,at)][j,c]+tp*base[(ar+1,at)][j,c])
                 for c in range(3)] for ar,at in KEYS]
        values,derivatives,minima=seven_dual(fields,Q,Qrho,R)
        for k,v in values.items():mods[k].append(v)
        for k,v in derivatives.items():ders[k].append(v)
        for k,v in minima.items():lows[k].append(v)
        report["cells"].append({"index":j,
            "true_moduli":{k:ball_record(v) for k,v in values.items()},
            "true_moving_parameter_derivative_moduli":{
                k:ball_record(v) for k,v in derivatives.items()},
            "positive_real_minima":{k:ball_record(v) for k,v in minima.items()}})
        report["rows_done"]=j+1
        if (j+1)%128==0:checkpoint()
    report.update(complete=True,proved=True,
        uniform_true_moduli={k:ball_record(max(v)) for k,v in mods.items()})
    report["uniform_true_moving_parameter_derivative_moduli"]={
        k:ball_record(max(v)) for k,v in ders.items()}
    report["positive_real_minima"]={k:ball_record(min(v)) for k,v in lows.items()}
    report["coverage"]="All closed boundary angle cells, their Schwarz-reflected boundary, and the full rho disk. Positive-real denominator extension and maximum modulus give the entire strip."
    report["parameter_derivative_convention"]="Fixed rho=t(p)-r and physical theta; every physical field uses F_p+t_p*F_r before the seven-field algebra."
    checkpoint()
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
           "derivatives":report["uniform_true_moving_parameter_derivative_moduli"]},flush=True)


if __name__=="__main__":main()

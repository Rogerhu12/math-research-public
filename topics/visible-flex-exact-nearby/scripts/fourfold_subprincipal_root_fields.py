#!/usr/bin/env python3
"""True grounded root phase fields using the frozen R99 root geometry.

This preserves the exact affine family and true infinite primitive. It outputs
the nonmean R106 counterterms and root endpoint field. It does not certify the
continuous root integral or the complete returned phase.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction
from pathlib import Path
import time
from flint import acb, arb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import save, sha, stored
from fourfold_phase_root_cauchy_frame_ci_v1 import ComplexFrame
from fourfold_phase_root_potential_complex_strip import sin_cos
from fourfold_phase_canonical_root_jets import (
    along_shear, derivative, dot, cross, jet_function, trim)
from fourfold_subprincipal_grounded_fields import grounded_root_counterterms


def complex_record(value):
    return {"real": ball_record(value.real), "imag": ball_record(value.imag)}


class RootPhaseFormula:
    def phase_fields(self, angle):
        old, ctx.cap = ctx.cap, max(8, self.m+3, self.n+3)
        try:
            B,G = self.complex_phases(angle)
            sb,cb = sin_cos(trim(B,self.m,self.n))
            sg,cg = sin_cos(trim(G,self.m,self.n))
            tangent = [-sb*cg,cb*cg,sg]
            position = self.complex_position(angle,tangent)
            m,n = self.m-1,self.n
            keep = lambda value: trim(value,m,n)
            bt,gt = keep(derivative(B,"angle")),keep(derivative(G,"angle"))
            br = -trim(derivative(B,"radial"),m,n)/self.scale
            gr = -trim(derivative(G,"radial"),m,n)/self.scale
            sb,cb,sg,cg = map(keep,(sb,cb,sg,cg))
            tangent = list(map(keep,tangent))
            X = [-derivative(value,"radial")/self.scale for value in position]
            F = list(map(keep,position))
            hv = -sb*X[0]+cb*X[1]
            vv = -cb*X[0]-sb*X[1]
            Q = cg*X[2]-sg*hv
            W = Q*Q+vv*vv
            D = (1+bt)*cg*Q-gt*vv
            M = br*cg*Q-gr*vv
            H = dot(cross(tangent,X),F)
            R2 = dot(F,F)
            curvature_root = self.lift(self.kappa,m=m,n=n)
            factors = {"Fz":F[2],"W":W,"D":D,"H":H,
                       "target_curvature_root":curvature_root,"R2":R2}
            zero = lambda value: value.coefficient(0,0)
            for name,value in factors.items():
                if not zero(value).real > 0:
                    raise ValueError("unresolved actual root phase branch: "+name)
            q = M*jet_function(D,"inverse")
            lk,lz,lw,lh,ld = [jet_function(value,"log")
                              for value in (curvature_root,F[2],W,H,D)]
            logU = lk+4*lz+2*lw-4*lh
            logV = lk+2*lw-2*ld
            s1 = zero(along_shear(logU,q,self.scale))
            DV = zero(along_shear(logV,q,self.scale))
            qt = zero(derivative(q,"angle"))
            h1 = DV/2-qt
            logU_theta = zero(derivative(logU,"angle"))
            Yprime = zero(jet_function(-logV/2,"exp"))
            t0 = zero(jet_function(-logU/4,"exp"))
            result = grounded_root_counterterms(Yprime,s1,h1,logU_theta)
            result.update({"Y_prime":Yprime,"t0":t0,"s1":s1,"h1":h1,
                "logU_theta":logU_theta,"inward_shear_q":zero(q),
                "inward_shear_q_theta":qt})
            if any(not value.is_finite() for value in result.values()):
                raise ValueError("nonfinite actual R106 root field")
            return result,{name:zero(value) for name,value in factors.items()}
        finally:
            ctx.cap = old


class RootPhaseModel(RootPhaseFormula,ComplexFrame):
    pass


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    p.add_argument("--mode",choices=("point","strip"),default="point")
    p.add_argument("--point",type=Fraction,default=Fraction(1,16),
                   help="exact physical angle as rational multiple of pi")
    p.add_argument("--strip",type=Fraction,default=Fraction(1,256))
    p.add_argument("--nodes",type=int,default=512)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--refine-steps",type=int,default=3)
    p.add_argument("--angle-cells",type=int,default=128)
    p.add_argument("--max-depth",type=int,default=10)
    p.add_argument("--out",type=Path,required=True)
    a = p.parse_args()
    ctx.prec,ctx.cap = a.bits,10
    started,cpu = time.monotonic(),time.process_time()
    model = RootPhaseModel(a.object,a.half_width,a.root_certificate,a.strip,
                          nodes=a.nodes,refine_steps=a.refine_steps)
    here = Path(__file__).parent
    dependencies = ["fourfold_phase_root_cauchy_frame_ci_v1.py",
        "fourfold_phase_root_potential_complex_strip.py",
        "fourfold_phase_root_finite_grid_v2.py","fourfold_native_series_fft.py",
        "fourfold_phase_canonical_root_jets.py","fourfold_time_angle_jets.py",
        "fourfold_phase_beta_parameter_germ.py","fourfold_phase_beta_bulk_interval.py",
        "fourfold_phase_beta_interval.py","fourfold_phase_beta_affine.py",
        "fourfold_phase_root_fourier_fit.py","fourfold_subprincipal_grounded_fields.py",
        "fourfold_subprincipal_ray_fields.py"]
    report = {
        "kind":"R106_actual_grounded_root_phase_fields_"+a.mode,
        "complete":False,"proved":False,"source_sha256":sha(__file__),
        "identity":provenance(model.target,a.object),
        "root_certificate_path":str(a.root_certificate),
        "root_certificate_sha256":sha(a.root_certificate),
        "initial_family_root":ball_record(model.initial_root),
        "refined_family_root":ball_record(model.root),
        "root_refinement":model.root_refinement,"common_scalar_spans":model.spans,
        "physical_angle_strip":str(a.strip),"bits":a.bits,"primitive_nodes":a.nodes,
        "primitive_full_error":ball_record(model.budget["field_errors"][0]),
        "complex_primitive_full_error":ball_record(model.complex_errors[0]),
        "retained_radial_precision":model.m,"retained_angular_precision":model.n,
        "dependencies":{name:sha(here/name) for name in dependencies},
        "full_nonmean_return_phase_proved":False,
        "continuous_root_regularized_integral_proved":False}
    def checkpoint():
        report["wall_seconds"] = time.monotonic()-started
        report["cpu_seconds"] = time.process_time()-cpu
        save(a.out,report)
    checkpoint()
    if a.mode == "point":
        values,factors = model.phase_fields(acb(exact_arb(a.point)*arb.pi()))
        if any(not value.imag.contains(0) for value in values.values()):
            raise ValueError("actual point fields lost their real axis")
        report.update(exact_point_pi_multiple=str(a.point),
            point_values={name:ball_record(value.real) for name,value in values.items()},
            positive_factor_real_lower={name:ball_record(value.real.lower())
                                        for name,value in factors.items()},
            complete=True,proved=True)
    else:
        if a.angle_cells < 2 or a.angle_cells%2:
            raise ValueError("even positive quarter partition required")
        queue=deque((Fraction(j,a.angle_cells),Fraction(j+1,a.angle_cells),0)
                    for j in range(a.angle_cells//2))
        report.update(cells=[],failed=[],pending=[],attempts=0)
        while queue:
            left,right,depth=queue.popleft()
            report["attempts"] += 1
            angle=acb(
                exact_arb((left+right)/4)*arb.pi()
                +arb(0,(exact_arb((right-left)/4)*arb.pi()).upper()),
                exact_arb(a.strip/2)+arb(0,exact_arb(a.strip/2).upper()))
            try:
                values,factors=model.phase_fields(angle)
                report["cells"].append({
                    "exact_quarter_interval":[str(left),str(right)],
                    "exact_imaginary_interval":["0",str(a.strip)],"depth":depth,
                    "moduli":{name:ball_record(abs(value).upper()) for name,value in values.items()},
                    "positive_factor_real_lower":{name:ball_record(value.real.lower())
                                                   for name,value in factors.items()}})
            except (ValueError,ZeroDivisionError) as exc:
                if depth>=a.max_depth:
                    report["failed"].append({"interval":[str(left),str(right)],
                                              "depth":depth,"reason":str(exc)})
                    report["pending"]=[[str(l),str(r),d] for l,r,d in queue]
                    checkpoint()
                    raise
                mid=(left+right)/2
                queue.appendleft((mid,right,depth+1))
                queue.appendleft((left,mid,depth+1))
            if report["attempts"]%16==0:
                report["pending"]=[[str(l),str(r),d] for l,r,d in queue]
                checkpoint()
                print({"accepted":len(report["cells"]),"pending":len(queue),
                       "wall":report["wall_seconds"]},flush=True)
        cursor=Fraction(0)
        for row in sorted(report["cells"],key=lambda row:Fraction(row["exact_quarter_interval"][0])):
            left,right=map(Fraction,row["exact_quarter_interval"])
            if left!=cursor:
                raise ValueError("actual half-quarter strip has gap or overlap")
            cursor=right
        if cursor!=Fraction(1,2):
            raise ValueError("actual half-quarter strip incomplete")
        report.update(complete=True,proved=True,pending=[],
            full_strip_extension="exact even/odd D4 reflection and Schwarz conjugation; moduli unchanged",
            odd_fields=["logU_theta","inward_shear_q",
                        "grounded_root_endpoint_per_sigma","grounded_log_density_theta"],
            uniform_moduli={name:ball_record(max(stored(row["moduli"][name]).upper()
                                 for row in report["cells"]))
                            for name in report["cells"][0]["moduli"]})
    checkpoint()
    print({"complete":report["complete"],"proved":report["proved"],"out":str(a.out),
           "sha256":sha(a.out),"wall_seconds":report["wall_seconds"]},flush=True)


if __name__=="__main__":
    main()

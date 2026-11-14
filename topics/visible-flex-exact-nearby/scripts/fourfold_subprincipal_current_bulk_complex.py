#!/usr/bin/env python3
"""Current delta5 whole-parameter, continuous-r, full-complex-angle phase fields.

This computes the actual D, S, Vr and Ltheta of R106, before any mean.
The frozen directed Fourier/primitive machinery and affine scalar germs are
unchanged. Closed radial cells are subdivided only when an actual denominator
gate fails; every accepted cell carries the full angular strip and all tails.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction
from pathlib import Path
import time
import numpy as np
from flint import acb,arb,ctx
from fourfold_phase_beta_parameter_germ import ParameterGermFastBulkTarget,provenance
from fourfold_phase_beta_bulk_box import CBox,ccross,cdot
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import save,sha


class CurrentPhase(ParameterGermFastBulkTarget):
    def phase_fields(self,left,right,sigma,waist=False):
        radial=acb(real_interval(left,right))
        cf,K,Kp,err,real=self.complete_fast_data(radial)
        if not np.all(K.real.hi<0):
            raise ValueError("negative current target curvature unresolved")
        k=CBox.from_acb((-K).to_acb().sqrt(analytic=True))
        fields=self.fast_fields(radial,cf,err,real,sigma)
        F,X,Frr,Y,Frt,Ftt=[fields[z] for z in
            ((0,0),(1,0),(2,0),(0,1),(1,1),(0,2))]
        C=ccross(Y,X)
        Cr=ccross(Frt,X)+ccross(Y,Frr)
        Ct=ccross(Ftt,X)+ccross(Y,Frt)
        G,T,H=cdot(C,C),cdot(F,F),cdot(C,F)
        if any(not np.all(v.real.lo>0) for v in (G,T,H)):
            raise ValueError("current complex area/radius/support unresolved")
        l,m,n=[cdot(C,v) for v in (Frr,Frt,Ftt)]
        a,b,c=-n/G,m/G,-l/G
        if not np.all(a.real.lo>0):
            raise ValueError("current complex a0 unresolved")
        omega,chat=((l*n-m*m)/(G*G)-K)/a,(b*b+K)/a
        FX,FY=cdot(F,X),cdot(F,Y)
        d=(a*(cdot(X,X)-FX*FX/T)
          +2*b*(cdot(X,Y)-FX*FY/T)
          +c*(cdot(Y,Y)-FY*FY/T))/T
        zr=cdot(Cr,F)/H-cdot(C,Cr)/G-FX/T
        zt=cdot(Ct,F)/H-cdot(C,Ct)/G-FY/T
        Lr,Ltheta=Kp/(2*K)-2*zr,-2*zt
        if waist:
            if not np.all(X[:,2].real.lo>0):
                raise ValueError("smooth full waist quotient unresolved")
            # On this cell 0<=r<=right, the exact odd Fz and Ftheta,z
            # vanish at zero. Their ratios by r are convex averages of
            # the enclosed Fr,z and Frtheta,z on the SAME full interval.
            ell=Frt[:,2]/X[:,2]-FY/T
        else:
            if not np.all(F[:,2].real.lo>0):
                raise ValueError("current Fz denominator unresolved")
            ell=Y[:,2]/F[:,2]-FY/T
        D=(d+omega*(ell*ell+ell*Ltheta)
          -(a*Lr*Lr+2*b*Lr*Ltheta+chat*Ltheta*Ltheta)/4)/k
        values={"D":D,"S":omega*ell/k,
                "Vr":(a*Lr+b*Ltheta)/k,"Ltheta":Ltheta}
        if any(not np.all(np.isfinite(v.magnitude_upper())) for v in values.values()):
            raise ValueError("nonfinite true phase field")
        bounds={name:arb(float(np.max(v.magnitude_upper())))
                for name,v in values.items()}
        minima={name:arb(float(np.min(v.real.lo))) for name,v in
                (("area2",G),("radius2",T),("support",H),("a0",a))}
        return bounds,minima


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--half-width",type=Fraction,default=Fraction(1,10**9))
    ap.add_argument("--cut",type=Fraction,default=Fraction(268136140016943,1125899906842624))
    ap.add_argument("--physical-strip",type=Fraction,default=Fraction(1,640))
    ap.add_argument("--waist-width",type=Fraction,default=Fraction(1,1048576))
    ap.add_argument("--nodes",type=int,default=512)
    ap.add_argument("--angles",type=int,default=1024)
    ap.add_argument("--bits",type=int,default=192)
    ap.add_argument("--max-depth",type=int,default=20)
    ap.add_argument("--start-cell",type=int,default=0)
    ap.add_argument("--stop-cell",type=int)
    ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.out.suffix!=".gz":
        raise ValueError("a new gzip report is required")
    if not 0<a.half_width<=Fraction(1,10**9) or not a.physical_strip>0:
        raise ValueError("outside actual parameter family or invalid strip")
    if sha(a.object)!="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848":
        raise ValueError("actual delta5 object bytes differ")
    ctx.prec,ctx.cap=a.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    target=CurrentPhase(a.object,a.half_width,a.nodes,a.angles,
                       arb(".002"),arb(".0015"),arb(".32"))
    knots={Fraction(0),a.waist_width,a.cut}
    for key,vals in target.frozen.items():
        if key.endswith("_knots"):
            for v in vals:
                q=abs(Fraction.from_float(float(v)))
                if 0<q<a.cut:knots.add(q)
    points=sorted(knots)
    if points[1]!=a.waist_width:
        raise ValueError("waist does not stay in first common scalar span")
    pairs=list(zip(points,points[1:]))
    stop=len(pairs) if a.stop_cell is None else min(a.stop_cell,len(pairs))
    if not 0<=a.start_cell<stop:
        raise ValueError("invalid common-cell selection")
    names=("fourfold_phase_beta_parameter_germ.py","fourfold_phase_beta_bulk_box.py",
           "fourfold_phase_beta_bulk_interval.py","fourfold_phase_beta_interval.py",
           "fourfold_phase_root_interval.py","fourfold_phase_uniform_tail.py",
           "fourfold_phase_root_fourier_fit.py")
    report={"kind":"R106_current_delta5_complete_complex_bulk_fields",
      "complete":False,"proved":False,"source_sha256":sha(__file__),
      "identity":provenance(target,a.object),
      "object_path":str(a.object),"object_sha256":sha(a.object),
      "physical_angle_strip":str(a.physical_strip),
      "exact_cut":str(a.cut),"waist_width":str(a.waist_width),
      "nodes":a.nodes,"angles":a.angles,"bits":a.bits,
      "start_cell":a.start_cell,"stop_cell":stop,
      "common_cell_count":len(pairs),"cells":[],"failures":[],
      "mean_retained":True,"current_parameter_complex_fields":True,
      "full_return_phase_proved":False,
      "dependencies":{name:sha(Path(__file__).with_name(name)) for name in names}}
    totals={name:arb(0) for name in ("D","S")}
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-wall
        report["cpu_seconds"]=time.process_time()-cpu
        report["positive_radial_integrated_moduli"]={
            name:ball_record(x.upper()) for name,x in totals.items()}
        save(a.out,report)
    checkpoint()
    for index in range(a.start_cell,stop):
        left,right=pairs[index]
        target.set_cell(left,right)
        pending=deque([(left,right,0)])
        accepted=[]
        while pending:
            lo,hi,depth=pending.popleft()
            try:
                bounds,minima=target.phase_fields(lo,hi,4*exact_arb(a.physical_strip),
                                                  waist=(lo==0))
            except (ValueError,ZeroDivisionError,OverflowError) as exc:
                if depth>=a.max_depth or (lo==0 and hi<a.waist_width):
                    report["failures"].append({"common_cell":index,"left":str(lo),
                        "right":str(hi),"depth":depth,"reason":str(exc)})
                    checkpoint()
                    raise
                mid=(lo+hi)/2
                pending.appendleft((mid,hi,depth+1))
                pending.appendleft((lo,mid,depth+1))
                continue
            row={"common_cell":index,"left":str(lo),"right":str(hi),"depth":depth,
                 "whole_physical_angle_strip":True,
                 "moduli":{name:ball_record(v) for name,v in bounds.items()},
                 "positive_real_minima":{name:ball_record(v) for name,v in minima.items()}}
            report["cells"].append(row);accepted.append((lo,hi))
            for name in totals:totals[name]+=exact_arb(hi-lo)*bounds[name]
        cursor=left
        for lo,hi in sorted(accepted):
            if lo!=cursor:raise ValueError("radial subdivision gap")
            cursor=hi
        if cursor!=right:raise ValueError("common radial cell incomplete")
        report["completed_common_cell"]=index
        checkpoint()
        if index%8==0:
            print({"completed":index+1,"total":stop,"subcells":len(report["cells"]),
                   "D_int":float(totals["D"].upper()),
                   "wall":report["wall_seconds"]},flush=True)
    cursor=pairs[a.start_cell][0]
    for row in report["cells"]:
        if Fraction(row["left"])!=cursor:raise ValueError("final radial coverage gap")
        cursor=Fraction(row["right"])
    if cursor!=pairs[stop-1][1]:raise ValueError("final radial coverage endpoint differs")
    target.set_cell(*pairs[-1])
    endpoint,emin=target.phase_fields(a.cut,a.cut,4*exact_arb(a.physical_strip))
    report.update(complete=True,proved=True,
        exact_covered_interval=[str(pairs[a.start_cell][0]),str(cursor)],
        whole_positive_bulk=(a.start_cell==0 and stop==len(pairs)),
        fixed_cut_fields={name:ball_record(v) for name,v in endpoint.items()},
        fixed_cut_positive_minima={name:ball_record(v) for name,v in emin.items()},
        negative_radial_side="Exact radial reflection preserves all four field moduli; signed phase orientation is not discarded.",
        angular_coverage="Frozen exact D4 reflection and Schwarz conjugation fill the entire pi/2-periodic complex strip.",
        scope="Full current-parameter field moduli and radial integrals of moduli; no true-ray Jacobian, phase cancellation, strong propagator remainder or inverse inferred.")
    checkpoint()
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
           "whole_positive_bulk":report["whole_positive_bulk"],
           "subcells":len(report["cells"])},flush=True)


if __name__=="__main__":
    main()

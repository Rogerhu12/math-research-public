#!/usr/bin/env python3
"""Refine actual continuous complex bulk cells, preserving the complete cover."""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_subprincipal_current_bulk_complex import CurrentPhase
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--D-quota",type=Fraction,default=Fraction(75))
    p.add_argument("--S-quota",type=Fraction,default=Fraction(1,100))
    p.add_argument("--max-depth",type=int,default=20)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.out.suffix!=".gz":
        raise ValueError("new gzip output required")
    old=read(a.input)
    if (not old.get("complete") or not old.get("proved") or
        not old.get("whole_positive_bulk") or
        old["source_sha256"]!=sha(Path(__file__).with_name(
            "fourfold_subprincipal_current_bulk_complex.py"))):
        raise ValueError("completed current full complex bulk required")
    for name,digest in old["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("base bulk dependency changed "+name)
    ctx.prec,ctx.cap=old["bits"],4
    half=Fraction(old["identity"]["exact_parameter_half_width"])
    target=CurrentPhase(Path(old["object_path"]),half,old["nodes"],old["angles"],
                       arb(".002"),arb(".0015"),arb(".32"))
    if provenance(target,Path(old["object_path"]))!=old["identity"]:
        raise ValueError("actual affine family differs")
    start=time.monotonic()
    S=4*exact_arb(Fraction(old["physical_angle_strip"]))
    Dquota,Squota=exact_arb(a.D_quota),exact_arb(a.S_quota)
    if not Dquota>0 or not Squota>0:raise ValueError("positive quotas required")
    report={key:old[key] for key in (
        "identity","object_path","object_sha256","physical_angle_strip",
        "exact_cut","waist_width","nodes","angles","bits","common_cell_count",
        "mean_retained","current_parameter_complex_fields","fixed_cut_fields",
        "fixed_cut_positive_minima","negative_radial_side","angular_coverage")}
    report.update(kind="R106_current_delta5_complete_complex_bulk_refined",
        complete=False,proved=False,source_sha256=sha(__file__),
        input_path=str(a.input),input_sha256=sha(a.input),
        inherited_source_sha256=old["source_sha256"],
        inherited_dependencies=old["dependencies"],D_quota=str(a.D_quota),
        S_quota=str(a.S_quota),cells=[],failures=[],full_return_phase_proved=False)
    totals={"D":arb(0),"S":arb(0)}
    def checkpoint():
        report["wall_seconds"]=time.monotonic()-start
        report["positive_radial_integrated_moduli"]={
            k:ball_record(v.upper()) for k,v in totals.items()}
        save(a.out,report)
    checkpoint()
    for oldindex,parent in enumerate(old["cells"]):
        left,right=Fraction(parent["left"]),Fraction(parent["right"])
        oldbounds={k:stored(v).upper() for k,v in parent["moduli"].items()}
        oldmin={k:stored(v).lower() for k,v in parent["positive_real_minima"].items()}
        pending=deque([(left,right,0,oldbounds,oldmin)])
        accepted=[]
        while pending:
            lo,hi,depth,bounds,minima=pending.popleft()
            if bounds is None:
                target.set_cell(lo,hi)
                try:
                    bounds,minima=target.phase_fields(lo,hi,S,waist=(lo==0))
                except (ValueError,ZeroDivisionError,OverflowError) as exc:
                    if depth>=a.max_depth:
                        report["failures"].append({"old_cell":oldindex,
                            "left":str(lo),"right":str(hi),"reason":str(exc)})
                        checkpoint();raise
                    bounds=None
            width=exact_arb(hi-lo)
            sufficient=(bounds is not None and width*bounds["D"]<=Dquota
                        and width*bounds["S"]<=Squota)
            if not sufficient:
                if depth>=a.max_depth or lo==0:
                    raise ValueError("actual refinement quota unresolved")
                mid=(lo+hi)/2
                pending.appendleft((mid,hi,depth+1,None,None))
                pending.appendleft((lo,mid,depth+1,None,None))
                continue
            row={"common_cell":parent["common_cell"],"old_cell":oldindex,
                 "left":str(lo),"right":str(hi),"depth":parent["depth"]+depth,
                 "additional_depth":depth,"inherited_without_reevaluation":depth==0,
                 "whole_physical_angle_strip":True,
                 "moduli":{k:ball_record(v) for k,v in bounds.items()},
                 "positive_real_minima":{k:ball_record(v) for k,v in minima.items()}}
            report["cells"].append(row);accepted.append((lo,hi))
            for k in totals:totals[k]+=width*bounds[k]
        cursor=left
        for lo,hi in accepted:
            if lo!=cursor:raise ValueError("refinement gap")
            cursor=hi
        if cursor!=right:raise ValueError("refinement misses parent endpoint")
        report["completed_old_cell"]=oldindex
        checkpoint()
        if oldindex%16==0 or len(accepted)>8:
            print({"old_cells":oldindex+1,"total":len(old["cells"]),
                "new_cells":len(report["cells"]),"D_int":float(totals["D"].upper()),
                "S_int":float(totals["S"].upper()),"wall":report["wall_seconds"]},flush=True)
    cursor=Fraction(0)
    for row in report["cells"]:
        if Fraction(row["left"])!=cursor:raise ValueError("full refined coverage gap")
        cursor=Fraction(row["right"])
    if cursor!=Fraction(old["exact_cut"]):raise ValueError("wrong final physical cut")
    report.update(complete=True,proved=True,whole_positive_bulk=True,
        exact_covered_interval=["0",str(cursor)],
        scope="Actual whole-parameter continuous-r full-complex D,S,Vr,Ltheta field moduli; all accepted cells form an exact cover. No true-ray or return-frame completion is inferred.")
    checkpoint()
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
        "cells":len(report["cells"]),"D":report["positive_radial_integrated_moduli"]["D"],
        "S":report["positive_radial_integrated_moduli"]["S"]},flush=True)


if __name__=="__main__":main()

#!/usr/bin/env python3
"""Replay the SAME physical-r candidate on complete R85 source-position boxes.

The new true integrals narrow the original integral-defined quartic, without
choosing their midpoints.  Every actual derivative is in physical r; the
source x partition only specifies rigorously covered positions.  Original
R64 mean/root/inverse gates, full finite J modes through m80, and R77 remain.
No new source evaluation, quadrature, ODE, BVP, Node or candidate is used.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_split_joint_io import read,digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q,ball_record
from tail_outer_weighted_compatible import normalized_endpoint_jet,make_weighted_candidate,MOMENT_KEYS
from tail_outer_centered_quartic_fields_v2 import weighted_panel_fields,intersection,rational_identity_checks,finite
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_substage_span_refinement import finite_complete_J,MINIMUM_FIELDS,compact_ball,rounded_dyadic
from tail_outer_original_piece_finite_j import r77


EXPECTED={
    "tail_outer_physical_r_true_moments.py":"67ac79f49c47b4fc0cdef9d145decc955b6b6428c18e56150f3d299d1956c670",
    "tail_outer_original_piece_finite_j.py":"b5196622ed649c6e3a3d6ad3227f30b0c54651d402c5866cfa2102d5e6def2d4",
    "tail_outer_general_mean_bounds.py":"4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c",
    "tail_outer_substage_span_refinement.py":"85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8",
    "tail_outer_weighted_compatible.py":"03c88b010447c78e4fb6bb26f0d3704fafd23510d16cc00084f315daa07f3d1b",
    "tail_outer_centered_quartic_fields_v2.py":"671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("candidate","nodes","moment-summary","moment-resource","out-prefix"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    a=p.parse_args()
    summary=Path(str(a.out_prefix)+"-summary.json")
    output=Path(str(a.out_prefix)+"-fields.jsonl.gz")
    recovery=Path(str(a.out_prefix)+"-recovery.json")
    if any(path.exists() for path in (summary,output,recovery)):
        raise FileExistsError("Use a fresh complete physical-r replay prefix")
    ctx.prec,ctx.threads=192,1
    start=time.monotonic()
    paths=(a.candidate,a.nodes,a.moment_summary,a.moment_resource)
    inputs={str(path):digest(path) for path in paths}
    old,nodes,meta,usage=map(read,paths)
    if (old["cell"]!=0 or old["segment"]!=8 or meta["cell"]!=0 or meta["segment"]!=8
            or not all(old["gates"].values()) or not all(meta["gates"].values())
            or usage["exitcode"]!=0 or usage["termination_signal"] is not None
            or old["modes"]!=meta["modes"] or old["tau"]!=meta["tau"]
            or old["input_hashes"].get(str(a.nodes))!=inputs[str(a.nodes)]):
        raise ValueError("The completed original candidate and same-true-moment certificate are required")
    cmd=usage["command"];prefix=cmd[cmd.index("--out-prefix")+1]
    if (Path(prefix+"-summary.json")!=a.moment_summary
            or Path(prefix+"-resource.json")!=a.moment_resource):
        raise ValueError("The moment formal exit belongs to a different run")
    sources={name:digest(Path(__file__).with_name(name)) for name in EXPECTED}
    if sources!=EXPECTED:raise ValueError("An executed mathematical dependency changed")
    for data in (old,meta):
        for path,checksum in data["input_hashes"].items():
            if digest(Path(path))!=checksum:raise ValueError("An original input changed: "+path)
        for name,checksum in data["source_hashes"].items():
            if digest(Path(__file__).with_name(name))!=checksum:
                raise ValueError("An executed source changed: "+name)
            sources[name]=checksum
    for path in (a.candidate,a.nodes):
        if meta["input_hashes"].get(str(path))!=inputs[str(path)]:
            raise ValueError("The refined moments are not those of this exact original candidate")
    sources[Path(__file__).name]=digest(__file__)
    source=Path(meta["output"])
    if digest(source)!=meta["output_sha256"]:raise ValueError("The true position/moment primary changed")
    inputs[str(source)]=meta["output_sha256"]
    bg={key:ball(value) for key,value in old["background"].items()}
    width=intersection(bg["width"],ball(meta["true_width"]))
    if not width>0:raise ArithmeticError("Physical width is not positive")
    def endpoint(node):
        jets={key:{int(m):ball(v) for m,v in node["shared_physical_jets"][key].items()}
              for key in ("H","Hr","Hrr")}
        wi,wri=ball(node["w"]),ball(node["wr"])
        return normalized_endpoint_jet(jets["H"],jets["Hr"],jets["Hrr"],
            w=wi,radius_u=width,log_w_u=width*wri/wi)
    left,right=endpoint(nodes["rows"][8]),endpoint(nodes["rows"][9])
    total={key:intersection(ball(meta["total_true_positive_moments"][key]),
        ball(old["total_true_positive_moments"][key])) for key in MOMENT_KEYS}
    candidate=make_weighted_candidate(left,right,total)
    for m,value in candidate["bubble_coefficient"].items():
        candidate["bubble_coefficient"][m]=intersection(value,ball(old["bubble_coefficients"][str(m)]))
    modes,tau=old["modes"],F(old["tau"])
    cutoff=max(modes)
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in range(0,2*cutoff+1,2)}
    maxima,minima={},{}
    count,covered=0,F(0)
    checks=rational_identity_checks()
    def memory():
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak>a.rss_limit_mib*1024:raise MemoryError("Physical-r replay exceeded its RSS observation gate")
        return peak
    def checkpoint(error=None):
        recovery.write_text(json.dumps(dict(status="Only recorded complete leaves; no final full-segment claim",
            completed=count,covered_source_right=str(covered),input_hashes=inputs,source_hashes=sources,
            error=error,elapsed_seconds=time.monotonic()-start),indent=2)+"\n")
    header=trailer=False
    try:
        with gzip.open(source,"rt") as inp,gzip.open(output,"xt",compresslevel=6) as out:
            out.write(json.dumps(dict(kind="header",cell=0,segment=8,
                source_coordinate="original x for coverage; physical r for derivatives, r_r=1",
                complete_J_cosine_modes=list(range(0,2*cutoff+1,2)),
                same_true_candidate=True,input_hashes=inputs,source_hashes=sources),separators=(",",":"))+"\n")
            for line in inp:
                row=json.loads(line)
                if row["kind"]=="header":
                    if (header or count or row["input_hashes"]!=meta["input_hashes"]
                            or row["source_hashes"]!=meta["source_hashes"]):
                        raise ValueError("The true-moment header is inconsistent")
                    header=True;continue
                if row["kind"]=="trailer":
                    if trailer or not row["complete"] or row["panels"]!=count:
                        raise ValueError("The true-moment trailer is inconsistent")
                    trailer=True;continue
                if (not header or trailer or row["kind"]!="complete_physical_r_true_moment_leaf"
                        or row["panel"]!=count or row["branch"]!="raw" or row["sign"]!=-1):
                    raise ValueError("Unexpected true source-position row")
                aa,bb=F(row["x_left"]),F(row["x_right"])
                if aa!=covered or not aa<bb<=1:
                    raise ValueError("The complete actual source cover has a gap or overlap")
                if not ball(row["source_radius_x"])>0:
                    raise ArithmeticError("The source-to-physical monotonicity gate failed")
                u=intersection(ball(row["u"]),arb(0).union(arb(1)))
                radius=ball(row["radius"])
                w,ell=ball(row["w"]),ball(row["log_w_r"])
                before={key:ball(row["prefix_moments"][key]) for key in MOMENT_KEYS}
                after={key:ball(row["suffix_moments"][key]) for key in MOMENT_KEYS}
                H,K,Kr=weighted_panel_fields(candidate,u=u,u_x=1/width,
                    prefix_moments=before,suffix_moments=after)
                answer=general_mean_and_defect(H,K,Kr,modes=modes,weights=weights,
                    radius=radius,radius_x=arb(1),w=w,log_w_x=ell)
                if not answer["gate"]:
                    raise ArithmeticError("The complete same-candidate mean gate failed: "+str((count,answer.get("failure"))))
                geometry=dict(w=w,radius_x=arb(1),log_w_x=ell)
                full=finite_complete_J(H,K,Kr,radius=radius,g=geometry,
                    r64=answer,cutoff=cutoff,weights=weights)
                values=dict(answer["bounds"],**full["bounds"],**r77(full,answer,w))
                witness=dict(segment=8,panel=count,source_left=str(aa),source_right=str(bb),
                    physical_u=ball_record(u),source_coordinate="physical r; r_r=1")
                for key,value in values.items():
                    value=finite(value).upper()
                    if key not in maxima or value>maxima[key]["value"]:
                        maxima[key]=dict(value=value,witness=witness)
                for key in MINIMUM_FIELDS:
                    value=finite(answer[key]).lower()
                    if not value>0:raise ArithmeticError("A complete real/analytic mean margin failed")
                    if key not in minima or value<minima[key]["value"]:
                        minima[key]=dict(value=value,witness=witness)
                record=dict(kind="complete_physical_r_R64_J_R77_leaf",**witness,
                    same_candidate_complete_mean=True,
                    source={key:compact_ball(value) for key,value in (
                        ("radius",radius),("radius_x",arb(1)),("w",w),("log_w_x",ell),
                        ("physical_conversion_factor",full["physical_conversion_factor"]))},
                    bounds_upper={key:rounded_dyadic(value,upper=True) for key,value in values.items()},
                    gates_lower={key:rounded_dyadic(answer[key],upper=False) for key in MINIMUM_FIELDS},
                    full_J_cosine_intervals=[compact_ball(full["coefficients"][m])
                        for m in range(0,2*cutoff+1,2)],
                    actual_nonmean_jet_cosine_intervals={key:[compact_ball(2*v[m].real) for m in modes]
                        for key,v in (("H",H),("Kbar",K),("Kbar_r",Kr))})
                out.write(json.dumps(record,separators=(",",":"))+"\n")
                count+=1;covered=bb
                if count%32==0:
                    checkpoint()
                    print(json.dumps(dict(event="physical_r_replay_progress",completed=count,
                        total=meta["counts"]["final_panels"],seconds=time.monotonic()-start,
                        peak_RSS_KiB=memory())),flush=True)
            if not (header and trailer and covered==1 and count==meta["counts"]["final_panels"]):
                raise ValueError("The complete source/physical-r cover was not replayed")
            out.write(json.dumps(dict(kind="trailer",complete=True,panels=count,
                complete_source_cover=True,complete_physical_radius_cover=True),separators=(",",":"))+"\n")
    except BaseException as error:
        checkpoint(dict(type=type(error).__name__,message=str(error)))
        raise
    if output.stat().st_size>=5_000_000:raise ArithmeticError("Primary exceeds single-file limit")
    result=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete same physical-r candidate R64/J/R77 replay with true moments",
        cell=0,segment=8,modes=modes,tau=str(tau),panels=count,
        bounds={key:dict(value=ball_record(v["value"]),witness=v["witness"]) for key,v in maxima.items()},
        minima={key:dict(value=ball_record(v["value"]),witness=v["witness"]) for key,v in minima.items()},
        bubble_coefficients={str(m):ball_record(v) for m,v in candidate["bubble_coefficient"].items()},
        same_true_moment_refinement=dict(certificate=str(a.moment_summary),
            certificate_sha256=inputs[str(a.moment_summary)],
            identical_true_integrals_not_midpoints=True,identical_physical_endpoint_two_jets=True,
            original_physical_r_coordinate_retained=True,
            original_coefficient_enclosures_intersected=True),
        gates=dict(formal_true_moment_exit0_and_full_primary_identity=True,
            same_original_physical_r_candidate_and_true_metric=True,
            complete_exact_source_partition_and_monotone_physical_cover=True,
            complete_R64_mean_and_inverse_domain=True,
            actual_physical_radial_derivatives_not_PDE_substitutes=True,
            all_finite_J_modes_through_twice_height_cutoff=True,
            R77_full_mean_constraint_paid_every_leaf=True),
        input_hashes=inputs,source_hashes=sources,original_candidate_input_hashes=old["input_hashes"],
        finite_horner_checks=checks,output=str(output),output_sha256=digest(output),bytes=output.stat().st_size,
        new_source_evaluation_or_quadrature=False,new_radial_ODE_or_Node=False,
        exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=memory())
    with summary.open("x") as stream:json.dump(result,stream,indent=2);stream.write("\n")
    print(json.dumps(dict(event="complete_physical_r_replay",output=str(summary),panels=count,
        gates=result["gates"],Darboux=result["bounds"]["R77_full_physical_Darboux_upper"],
        seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

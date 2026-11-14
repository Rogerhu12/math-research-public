#!/usr/bin/env python3
"""Use physical r for the last R48 piece, joining the paid eight-piece prefix.

The same true metric and shared physical endpoint two-jets are retained.
Only the last candidate's radial parametrization changes. Its five exact
positive integrals are enclosed by the true whole-piece w range times
exact polynomial primitives in u=(r-r_left)/width. No source quadrature.
R64 is evaluated with x=r, r_x=1 and ell=w_r/w, without a spurious small
original-source speed in the physical derivative bounds.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_split_joint_io import read,digest,iter_array
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q,ball_record
from tail_outer_weighted_compatible import intersection,normalized_endpoint_jet,make_weighted_candidate,weighted_panel_fields
from tail_outer_positive_moment_panels import MOMENT_KEYS,positive_hull
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_segment_candidate_domain import primitive
from tail_outer_general_mean_bounds import general_mean_and_defect


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("cell-manifest","nodes","prefix-r64","background-ledger","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--parts",type=int,default=16)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError("Use a fresh physical-r last-piece result")
    if args.parts<=0:raise ValueError("Use a positive complete physical-r partition")
    ctx.prec=192;began=time.monotonic()
    paths=(args.cell_manifest,args.nodes,args.prefix_r64,args.background_ledger)
    hashes={str(path):digest(path) for path in paths}
    material,nodes,prior,background=map(read,paths)
    if (material["cell"]!=0 or nodes["cell"]!=0 or prior["cell"]!=0
            or not all(material["checks"].values())
            or not nodes["complete_original_segment_node_cover"]
            or not nodes["saved_cut_height_exactly_preserved"]
            or [r["segment"] for r in prior["segments"]]!=list(range(9))
            or not all(r["all_general_mean_gates"] for r in prior["segments"][:8])
            or prior["segments"][8]["all_general_mean_gates"]):
        raise ValueError("This application needs the stated actual eight-piece prefix")
    for key in (str(args.cell_manifest),str(args.nodes)):
        if prior["input_hashes"].get(key)!=hashes[key]:
            raise ValueError("The actual prefix/candidate input changed")
    ready_hashes=set(material["original_metadata"]["input_hashes"].values())
    if (not background["real_background_curvature_paid"]
            or background["all_cells_background_curvature_bound"]!=8
            or not ready_hashes.intersection(background["input_hashes"].values())
            or background["outer_formula_sha256"]!=digest(Path(__file__).with_name("closure_real_outer_radius.py"))):
        raise ValueError("The real R31 curvature cap belongs to another background")
    groups=[g for g in material["groups"] if g["source_segment"]==8]
    if len(groups)!=1 or groups[0]["panels"]!=1:
        raise ValueError("The original complete last real source panel is required")
    group=groups[0];path=Path(group["path"])
    if digest(path)!=group["sha256"]:raise ValueError("The true last source panel changed")
    hashes[str(path)]=group["sha256"]
    records=list(iter_array(path,"panels"))
    if len(records)!=1 or records[0]["x_left"]!="0" or records[0]["x_right"]!="1":
        raise ValueError("The last real source range must cover the whole segment")
    g=records[0];left,right=nodes["rows"][8],nodes["rows"][9]
    rl,rr=ball(left["radius"]),ball(right["radius"])
    width=intersection(ball(g["width"]),rr-rl)
    w=ball(g["w"])
    if not width>0 or not w>0:raise ArithmeticError("The true positive physical measure is missing")
    wr_source=w*ball(g["log_w_x"])/ball(g["radius_x"])
    cap=(8*(1+w*w)**(arb(3)/2)).upper()
    wr=intersection(wr_source,(-cap).union(cap))
    ell=wr/w
    def endpoint(node):
        jets={name:{int(m):ball(v) for m,v in node["shared_physical_jets"][name].items()}
              for name in ("H","Hr","Hrr")}
        wi,wri=ball(node["w"]),ball(node["wr"])
        return normalized_endpoint_jet(jets["H"],jets["Hr"],jets["Hrr"],
            w=wi,radius_u=width,log_w_u=width*wri/wi)
    def integral_boxes(lower,upper):
        return {key:nonnegative_integral(ball_record(positive_hull(
            (width.lower()*w.lower()*exact_q(lower[key])).lower(),
            (width.upper()*w.upper()*exact_q(upper[key])).upper())))
            for key in MOMENT_KEYS}
    whole=primitive(F(1));zero=primitive(F(0))
    total=integral_boxes(whole,whole)
    candidate=make_weighted_candidate(endpoint(left),endpoint(right),total)
    modes=nodes["modes"];tau=F(nodes["tau"])
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    bounds,minima,rows={}, {}, []
    for index in range(args.parts):
        a,b=F(index,args.parts),F(index+1,args.parts)
        pa,pb=primitive(a),primitive(b)
        before=integral_boxes(pa,pb)
        after=integral_boxes({key:whole[key]-pb[key] for key in MOMENT_KEYS},
                             {key:whole[key]-pa[key] for key in MOMENT_KEYS})
        u=exact_q(a).union(exact_q(b))
        radius=intersection(rl+width*u,rr-width*(1-u))
        H,K,Kr=weighted_panel_fields(candidate,u=u,u_x=1/width,
                                    prefix_moments=before,suffix_moments=after)
        result=general_mean_and_defect(H,K,Kr,modes=modes,weights=weights,
            radius=radius,radius_x=arb(1),w=w,log_w_x=ell)
        witness=dict(segment=8,physical_u_left=str(a),physical_u_right=str(b),
                     radius=ball_record(radius),source_coordinate="physical r")
        R=(result["norms"][1]["P"]+result["norms"][1]["K"]).upper()
        if "R_tau" not in bounds or R>bounds["R_tau"]["value"]:
            bounds["R_tau"]=dict(value=R,witness=witness)
        row=dict(panel=index,u_left=str(a),u_right=str(b),gate=result["gate"],R_tau=ball_record(R))
        if result["gate"]:
            for key,value in result["bounds"].items():
                if key not in bounds or value>bounds[key]["value"]:
                    bounds[key]=dict(value=value,witness=witness)
            for key in ("mean_sign_margin","mean_derivative_lower","real_y_lower","real_N_lower",
                        "real_D_lower","real_S_lower","real_L_lower","Wiener_L_lower"):
                value=result[key]
                if key not in minima or value<minima[key]["value"]:
                    minima[key]=dict(value=value,witness=witness)
            row["complete_mean_abs"]=ball_record(result["bounds"]["complete_mean_abs"])
        else:row["failure"]=result["failure"]
        rows.append(row)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>1024*args.rss_limit_mib:
            raise MemoryError("The owned physical-r last piece exceeded its RSS cap")
    good=all(row["gate"] for row in rows)
    aggregate={}
    for key,value in bounds.items():
        if key=="R_tau":
            previous=max((ball(row["R_tau"]).upper() for row in prior["segments"][:8]))
            old=dict(value=previous,witness={"scope":"maximum of the eight individually paid original pieces"})
        else:
            oldrow=prior["worst"][key]
            old=dict(value=ball(oldrow["value"]).upper(),witness=oldrow["witness"])
        selected=value if value["value"]>old["value"] else old
        aggregate[key]=dict(value=ball_record(selected["value"]),witness=selected["witness"])
    overall_min={}
    for key,value in minima.items():
        old=prior["minima_over_passed_panels"][key]
        oldvalue=ball(old["value"]).lower()
        selected=value if value["value"]<oldvalue else dict(value=oldvalue,witness=old["witness"])
        overall_min[key]=dict(value=ball_record(selected["value"]),witness=selected["witness"])
    packet=dict(status="Physical-r last-piece certification joined to the actual paid eight-piece prefix",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",cell=0,segment=8,modes=modes,tau=str(tau),
        coordinate="u=(r-r_left)/(r_right-r_left); the R64 source coordinate is x=r",
        new_last_piece_representation=True,other_eight_representations_unchanged=True,
        source_background_unchanged=True,shared_physical_endpoint_two_jets=True,
        exact_saved_cut_height_preserved=True,rows=rows,
        gates=dict(last_piece_complete_general_mean=good,whole_cell_complete_general_mean=good,
            whole_cell_complete_mean_derivative=good,whole_cell_complete_Darboux_defect=good),
        last_piece_bounds={key:dict(value=ball_record(v["value"]),witness=v["witness"]) for key,v in bounds.items()},
        whole_cell_bounds=aggregate,whole_cell_minima=overall_min,
        background=dict(radius_left=ball_record(rl),radius_right=ball_record(rr),width=ball_record(width),
            w_range=ball_record(w),wr_source_range=ball_record(wr_source),wr_intersected_R31=ball_record(wr)),
        total_true_positive_moments={key:ball_record(value) for key,value in total.items()},
        bubble_coefficients={str(m):ball_record(value) for m,value in candidate["bubble_coefficient"].items()},
        prefix_scope=dict(segments=list(range(8)),paid_panels=sum(row["panels"] for row in prior["segments"][:8]),
            original_whole_scan_had_one_failed_last_piece=True),
        actual_covered_panels=sum(row["panels"] for row in prior["segments"][:8])+args.parts,
        new_source_quadrature=0,new_Node_or_BVP=False,exact_radial_solution_claimed=False,
        input_hashes=hashes,source_hashes={name:digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name,"tail_outer_general_mean_bounds.py","tail_outer_weighted_compatible.py",
            "tail_outer_segment_candidate_domain.py","tail_outer_positive_moment_panels.py")},
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(packet,indent=2)+"\n")
    print(json.dumps(dict(output=str(args.out),gates=packet["gates"],last_R_tau=str(bounds["R_tau"]["value"]),
        seconds=packet["elapsed_seconds"],peak_RSS_KiB=packet["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

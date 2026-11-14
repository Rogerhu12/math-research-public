#!/usr/bin/env python3
"""Narrow true point functions of the already defined R66 source-x prefix.

Only the two stored worst witnesses are selected. All endpoint jets and
the five true total integrals define exactly the old candidate. Re-enclosing
one material leaf's partial integrals can narrow its constants, but does
not select new constants. A two-angle difference removes c_x exactly and
gives an optional rigorous lower bound for the actual physical defect.
No Node, radial ODE, BVP, or replacement by a PDE second derivative.
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
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import (
    source_range,positive_hull,add_moments,zero_moments,Subdivide,MOMENT_KEYS)
from tail_outer_segment_candidate_domain import local_moments,endpoint
from tail_outer_weighted_compatible import (
    intersection,make_weighted_candidate,weighted_panel_fields)
from tail_outer_general_mean_bounds import general_mean_and_defect


def endpoint_positive(value):
    return positive_hull(value.lower(),value.upper(),strict=True)


def local_refined_integrals(cell,segment,left,right,parts,memory_gate):
    """Range integrals of the same w dr moments on one subinterval."""
    total,width=zero_moments(),arb(0)
    stack=[(left+(right-left)*F(i,parts),left+(right-left)*F(i+1,parts),0)
           for i in range(parts-1,-1,-1)]
    leaves=0
    while stack:
        a,b,level=stack.pop()
        try:
            g=source_range(cell,segment,a,b,None,exact_q(F(1,16)))
            dw=endpoint_positive(g["radius_x"]*exact_q(b-a))
            row=dict(x_left=str(a),x_right=str(b),width=ball_record(dw),
                radius_x=ball_record(g["radius_x"]),w=ball_record(g["w"]))
            mm=local_moments(row)
        except Subdivide:
            if level>=24:raise ArithmeticError("The explicit local range budget was exhausted")
            c=(a+b)/2
            stack.extend([(c,b,level+1),(a,c,level+1)])
            continue
        total=add_moments(total,mm)
        width=positive_hull((width+dw).lower(),(width+dw).upper(),strict=True)
        leaves+=1
        if leaves%64==0:memory_gate("local-subinterval-range")
        if leaves+len(stack)>16384:
            raise ArithmeticError("Too many local material subintervals")
    return total,width,leaves


def two_angle_difference(H,K,Kx,*,modes,r,rx,w,ell,c_bound):
    """J/L at theta=0 minus theta=pi/2; its angle-constant part cancels."""
    c=(-c_bound).union(c_bound)
    E=1+w*w
    rows=[]
    for half_turn in (False,True):
        kb=tb=kxb=arb(0)
        for m in modes:
            sign=(-1 if (m//2)%2 else 1) if half_turn else 1
            h,k,kx=2*H[m].real,2*K[m].real,2*Kx[m].real
            kb+=sign*k
            tb+=sign*(-m*m*h/(r*w))
            kxb+=sign*kx
        fullk=c+kb
        L=1+fullk+E*tb
        if not L>0:
            return dict(gate=False,reason="The point L enclosure did not stay positive")
        # P and K_theta vanish at both stated angles for every even cosine mode.
        N=ell*((fullk+tb)**2+w*w*(2*fullk*tb+tb*tb))/L
        linear=kxb+ell*(2*kb+tb)
        rows.append(dict(L=L,N=N,linear=linear))
    delta=rows[0]["linear"]-rows[1]["linear"]-(rows[0]["N"]-rows[1]["N"])
    denominator=(1/rows[0]["L"]+1/rows[1]["L"]).upper()
    factor=w*w/(r*rx*(1+w*w)**2)
    lower=max(arb(0),(factor.lower()*abs(delta).lower()/denominator).lower())
    return dict(gate=True,
        statement="sup_theta |physical Darboux| >= the reported lower bound at this one true r",
        exact_mean_derivative_eliminated=True,
        full_mean_root_retained_in_N=True,
        first_angle="0",second_angle="pi/2",
        difference_J_over_L=ball_record(delta),
        inverse_L_sum_upper=ball_record(denominator),
        physical_factor=ball_record(factor),
        physical_Darboux_lower=ball_record(lower),
        proves_strictly_positive_actual_defect=bool(lower>0),
        angle_values=[{key:ball_record(value) for key,value in row.items()} for row in rows])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("cell-manifest","nodes","prefix-r64","ready","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--parts",type=int,default=16)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError("Keep each same-candidate probe under a fresh name")
    if args.parts<1:raise ValueError("Use a positive local range partition")
    ctx.prec=192;started=time.monotonic()
    def memory_gate(stage):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>1024*args.rss_limit_mib:
            raise MemoryError("The owned point probe exceeded its RSS limit at "+stage)
    paths=(args.cell_manifest,args.nodes,args.prefix_r64,args.ready)
    hashes={str(path):digest(path) for path in paths}
    material,nodes,prior,ready=map(read,paths)
    for path in (args.cell_manifest,args.nodes,args.ready):
        if prior["input_hashes"].get(str(path))!=hashes[str(path)]:
            raise ValueError("The original true prefix input changed")
    if not (material["cell"]==nodes["cell"]==prior["cell"]==0
            and all(row["all_general_mean_gates"] for row in prior["segments"][:8])
            and nodes["saved_cut_height_exactly_preserved"]):
        raise ValueError("The stated actual shared-jet prefix is required")
    for name,checksum in prior["source_hashes"].items():
        if digest(Path(__file__).with_name(name))!=checksum:
            raise ValueError("An executed source changed: "+name)
    head=SourceValues(ready);head.params=ready["rationalDeepModel"]["physicalParameters"]
    cell=OuterCell(head,0)
    modes,tau=nodes["modes"],F(nodes["tau"])
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    output=[]
    for name in ("actual_Darboux_defect_abs","full_finite_J_W1"):
        witness=prior["worst"][name]["witness"]
        j,target=int(witness["segment"]),int(witness["panel"])
        if not 0<=j<8:raise ValueError("This source-x probe only uses the unchanged first eight pieces")
        group=next(row for row in material["groups"] if row["source_segment"]==j)
        path=Path(group["path"])
        if digest(path)!=group["sha256"]:raise ValueError("The true source material changed")
        hashes[str(path)]=group["sha256"]
        before,after=zero_moments(),zero_moments()
        selected=None;count=0
        for i,row in enumerate(iter_array(path,"panels")):
            mm=local_moments(row)
            if i<target:before=add_moments(before,mm)
            elif i>target:after=add_moments(after,mm)
            else:selected=row
            count+=1
            if count%128==0:memory_gate("stream-old-material")
        if count!=group["panels"] or selected is None:
            raise ValueError("The complete selected material group is missing")
        if any(selected[key]!=witness[key] for key in ("x_left","x_right")):
            raise ValueError("Stored maximizing witness does not match its exact material row")
        a,b=F(selected["x_left"]),F(selected["x_right"])
        x=(a+b)/2
        left,dl,nl=local_refined_integrals(cell,cell.segments[j],a,x,args.parts,memory_gate)
        right,dr,nr=local_refined_integrals(cell,cell.segments[j],x,b,args.parts,memory_gate)
        original_width=ball(selected["width"])
        dl=intersection(dl,original_width-dr)
        dr=intersection(dr,original_width-dl)
        radius=intersection(ball(selected["radius_left"])+dl,
                            ball(selected["radius_right"])-dr)
        radius=intersection(radius,ball(selected["radius"]))
        current=source_range(cell,cell.segments[j],x,x,None,exact_q(F(1,16)))
        full_before,full_after=add_moments(before,left),add_moments(right,after)
        new_total=add_moments(full_before,full_after)
        stored=prior["segments"][j]
        total={key:intersection(new_total[key],ball(stored["total_local_positive_moments"][key]))
               for key in MOMENT_KEYS}
        candidate=make_weighted_candidate(endpoint(cell,j,0,nodes["rows"][j]),
            endpoint(cell,j,1,nodes["rows"][j+1]),total)
        # Both intervals enclose the same lambda determined by the same real integrals.
        candidate["bubble_coefficient"]={m:intersection(value,ball(stored["bubble_coefficients"][str(m)]))
            for m,value in candidate["bubble_coefficient"].items()}
        H,K,Kx=weighted_panel_fields(candidate,u=exact_q(x),u_x=arb(1),
            prefix_moments=full_before,suffix_moments=full_after)
        rkwargs=dict(modes=modes,weights=weights,radius=radius,
            radius_x=current["radius_x"],w=current["w"],log_w_x=current["log_w_x"])
        result=general_mean_and_defect(H,K,Kx,**rkwargs)
        if not result["gate"]:raise ArithmeticError("The same-candidate point lost its complete mean gate")
        physical_m2=(current["w"]/current["radius_x"])*(
            2*Kx[modes[0]].real+current["log_w_x"]*2*K[modes[0]].real)
        pair=two_angle_difference(H,K,Kx,modes=modes,r=radius,rx=current["radius_x"],
            w=current["w"],ell=current["log_w_x"],c_bound=result["bounds"]["complete_mean_abs"])
        record=dict(selected_worst_field=name,segment=j,original_panel=target,
            original_witness=witness,x_midpoint=str(x),
            actual_background_at_point={key:ball_record(value) for key,value in dict(
                radius=radius,radius_x=current["radius_x"],w=current["w"],log_w_x=current["log_w_x"]).items()},
            original_selected_upper=prior["worst"][name]["value"],
            same_candidate_definition=True,shared_endpoints_unchanged=True,
            true_total_integrals_reenclosed_not_reselected=True,
            original_total_positive_moments=stored["total_local_positive_moments"],
            point_total_positive_moments={key:ball_record(value) for key,value in total.items()},
            bubble_coefficient_m2=ball_record(candidate["bubble_coefficient"][modes[0]]),
            refined_local_material_leaves=nl+nr,
            complete_mean_gate=True,
            point_bounds={key:ball_record(value) for key,value in result["bounds"].items()},
            point_margins={key:ball_record(result[key]) for key in (
                "mean_sign_margin","mean_derivative_lower","real_y_lower","real_N_lower",
                "real_D_lower","real_S_lower","real_L_lower","Wiener_L_lower")},
            signed_nonmean_physical_hrr_m2=ball_record(physical_m2),
            two_angle_lower_function=pair)
        output.append(record)
        print(json.dumps(dict(event="same_candidate_true_point",target=name,segment=j,panel=target,
            physical_Darboux_upper=str(result["bounds"]["actual_Darboux_defect_abs"]),
            physical_Darboux_lower=pair.get("physical_Darboux_lower"),
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        memory_gate("point-record")
    packet=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete narrow point functions of the unchanged actual candidate",
        same_candidate_definition=True,source_background_unchanged=True,
        new_radial_ODE=False,new_Node_or_BVP=False,
        finite_points_not_continuous_radial_certificate=True,
        all_full_mean_gates=all(row["complete_mean_gate"] for row in output),rows=output,
        input_hashes=hashes,source_hashes={name:digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name,"tail_outer_segment_candidate_domain.py",
            "tail_outer_general_mean_bounds.py","tail_outer_weighted_compatible.py",
            "tail_outer_positive_moment_panels.py","closure_real_outer_radius.py")},
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    text=json.dumps(packet,indent=2)+"\n"
    if len(text.encode())>=1_000_000:raise ValueError("Use a compressed point report above 1 MB")
    args.out.write_text(text)
    memory_gate("terminal-record")
    print(json.dumps(dict(event="complete",output=str(args.out),seconds=packet["elapsed_seconds"],
        peak_RSS_KiB=packet["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

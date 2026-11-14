#!/usr/bin/env python3
"""Pay a genuine two-output whole-field ball using the complete R84 kernel.

Only exact Fraction arithmetic is used. All original source positions are
revisited. Uniform pointwise density quotients multiply the already executed
ordered positive Green norm, retaining both branches and same-panel terms.
The other Fourier height functions are fixed at their actual C_eta values.
This proves only the two projected equations with prescribed inner beta(a):
cut-parameter consistency and all other PDE outputs remain separate debts.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gc
import gzip
import json
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import read, read_field, iter_array, digest
from closure_outer_source_parameter_rows import point, bounds, record as rational_record
from closure_outer_whole_field_green_budget import pair
from root_moving_auxiliary_centre_family import upper, record, write_new
from root_anisotropic_true_cut_cauchy import uprecord


def up(x,bits=128):
    return upper(uprecord(x,bits))


def compact(x):
    return uprecord(x,128)["upper"]


def density(g,V,sigma,rho,M):
    """R84(84.13-17), including the complete mean and inverse derivative."""
    rlo,rhi=bounds(g["radius"])
    wlo,whi=bounds(g["w"])
    rxlo,rxhi=bounds(g["radius_x"])
    if min(rlo,wlo,rxlo)<=0 or whi>F(1,2):
        raise ArithmeticError("The same positive physical source domain is required")
    E=1+whi**2; s=rxhi/rlo; ell=max(map(abs,bounds(g["log_w_x"])))
    R=(sigma+rho)*V
    T=(40*sigma+M*rho)*V
    U=(41*sigma+(M+1)*rho)*V
    c=4*R**2; dc=16*R*V
    lead=c+R+E*T
    if not R<F(1,64) or not lead<1:
        raise ArithmeticError("The enlarged full mean/inverse domain is unpaid")
    dlead=dc+(1+M*E)*V
    q=E*s*U**2+E*ell*(R+T)**2
    dq=2*(M+1)*(E*s*U+E*ell*(R+T))*V
    mn=ell*(2*c*(R+E*T)+c**2)
    dmn=2*ell*(dc*(R+E*T+c)+c*(1+M*E)*V)
    Ncap=(q+mn)/(1-lead)
    Fcap=(dq+dmn)/(1-lead)+(q+mn)*dlead/(1-lead)**2
    return Fcap,Ncap,R,lead


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("profiles","green","family","rows","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--radius",default="16")
    ap.add_argument("--rss-kib",type=int,default=51200)
    a=ap.parse_args();began=time.monotonic()
    if a.rows.exists() or a.out.exists():
        raise FileExistsError("Use fresh immutable projected-field outputs")
    paths=(a.profiles,a.green,a.family)
    profiles,green,family=[read(p) for p in paths]
    hashes={str(p):digest(p) for p in paths}
    if not all(d["all_gates"] for d in (profiles,green,family)):
        raise ValueError("Complete actual geometry, ordered Green and family are required")
    if (green["input_hashes"].get(str(a.profiles))!=digest(a.profiles)
            or green["input_hashes"].get(str(a.family))!=digest(a.family)):
        raise ValueError("The positive kernel must belong to the same actual problem")
    if green["source_sha256"]!=digest(Path(__file__).with_name("closure_outer_whole_field_green_budget.py")):
        raise ValueError("The executed ordered consumer source changed")
    config=profiles["config"]
    if (config["modes"]!=[2,4] or config["input_cutoff"]!=92
            or config["field_radius"]!="1/16"
            or config["parameter_amplitude_sigma"]!="17/16"
            or green["subpanels"]!=10933
            or profiles["counts"]["original_material"]!=10793):
        raise ValueError("Keep the actual two-output, all-low46-input kernel")
    sigma=F(17,16);oldrho=F(1,16);rho=F(a.radius);M=92
    if not rho>oldrho:raise ValueError("Specify an actual enlarged field domain")
    axes={r["mode"]:r for r in family["parameter_axes"]}
    if sorted(axes)!=list(range(2,41,2)):
        raise ValueError("Retain every actual parameter coordinate")
    geometry_code=Path(__file__).with_name("closure_outer_whole_field_profiles.py")
    if digest(geometry_code)!=config["entrypoint_sha256"]:
        raise ValueError("The frozen true profile source changed")
    allgroups=[(n,j) for n in (11,10) for j in range(9)]
    if [(g["cell"],g["segment"]) for g in profiles["profile_groups"]]!=allgroups:
        raise ValueError("Retain all18 groups in the actual source order")
    max_K=max_B=max_R=max_lead=F(0)
    max_K_at=max_B_at=None
    total_original=total_subpanels=0;groups=[]
    with gzip.open(a.rows,"xt",encoding="utf-8",compresslevel=6) as out:
        for group in profiles["profile_groups"]:
            path=Path(group["path"])
            if digest(path)!=group["sha256"]:raise ValueError("A true profile changed")
            hashes[str(path)]=digest(path)
            source=Path(read_field(path,"source_group_path"))
            sh=read_field(path,"source_group_sha256")
            if digest(source)!=sh or profiles["input_hashes"].get(str(source))!=sh:
                raise ValueError("The original source geometry changed")
            hashes[str(source)]=sh
            geometry={}
            for g in iter_array(source,"panels"):
                if g["panel"]!=len(geometry) or g["segment"]!=group["segment"]:
                    raise ValueError("Original source indices are not complete")
                geometry[g["panel"]]={k:g[k] for k in
                    ("radius","radius_x","w","log_w_x","complete_mean_abs","x_left","x_right")}
            if len(geometry)!=group["original_panels"]:
                raise ValueError("An original material leaf is missing")
            calculated={};partitions={};subpanels=0
            for row in iter_array(path,"panels"):
                panel=row["panel"];g=geometry[panel]
                Vpair=pair(row["source_envelope"])
                if Vpair[0]!=Vpair[1] or Vpair[0]<=0:
                    raise ValueError("Use the exact fixed positive profile envelope")
                V=Vpair[0];oldF=point(row["whole_low46_source_derivative_density"])
                if oldF<=0 or V*V<bounds(g["complete_mean_abs"])[1]/4:
                    raise ArithmeticError("The actual candidate/old-density enclosure failed")
                key=(group["cell"],group["segment"],panel)
                if panel not in calculated:
                    check,_,_,_=density(g,V,sigma,oldrho,M)
                    if check>oldF:
                        raise ArithmeticError("Exact old density exceeds the preserved outward cap")
                    Fnew,_,R,lead=density(g,V,sigma,rho,M)
                    _,Neta,_,_=density(g,V,sigma,F(0),M)
                    Fnew,Neta=up(Fnew),up(Neta)
                    K,B=up(Fnew/oldF),up(Neta/oldF)
                    if not Fnew<=K*oldF or not Neta<=B*oldF:
                        raise ArithmeticError("A positive comparison rounded inward")
                    calculated[panel]=(V,oldF,K,B)
                    max_R=max(max_R,R);max_lead=max(max_lead,lead)
                    if K>max_K:max_K,max_K_at=K,key
                    if B>max_B:max_B,max_B_at=B,key
                    out.write(json.dumps(dict(cell=group["cell"],segment=group["segment"],panel=panel,
                        V=compact(V),original_density=compact(oldF),enlarged_density=compact(Fnew),
                        full_parameter_source_cap=compact(Neta),derivative_multiplier=compact(K),
                        parameter_source_multiplier=compact(B),mean_input=compact(R),
                        complete_inverse_leading_norm=compact(lead)),separators=(",",":"))+"\n")
                    total_original+=1
                elif calculated[panel][:2]!=(V,oldF):
                    raise ValueError("Subpanels of one original leaf changed its norm or density")
                left,right=F(row["x_left"]),F(row["x_right"])
                if not F(g["x_left"])<=left<right<=F(g["x_right"]):
                    raise ValueError("A true subpanel escaped its original source leaf")
                partitions.setdefault(panel,[]).append((left,right))
                subpanels+=1
            if set(calculated)!=set(geometry) or subpanels!=group["subpanels"]:
                raise ValueError("The complete old source partition was not revisited")
            for panel,parts in partitions.items():
                ordered=sorted(parts);g=geometry[panel]
                if (ordered[0][0]!=F(g["x_left"]) or ordered[-1][1]!=F(g["x_right"])
                        or any(x[1]!=y[0] for x,y in zip(ordered,ordered[1:]))):
                    raise ValueError("An original source leaf has a gap or overlap")
            total_subpanels+=subpanels
            groups.append(dict(cell=group["cell"],segment=group["segment"],
                original_leaves=len(geometry),subpanels=subpanels,all_exact_old_density_checks=True))
            del geometry,calculated,partitions
            gc.collect()
            peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if peak>a.rss_kib:raise MemoryError("The owned Fraction RSS observer was exceeded")
            print(json.dumps(dict(event="group_complete",cell=group["cell"],segment=group["segment"],
                derivative_multiplier=record(max_K)["display"],peak_RSS_KiB=peak)),flush=True)
    oldGamma=point(green["sums"]["derivative"])
    Gamma=up(max_K*oldGamma,192)
    Nresponse=up(max_B*oldGamma,192)
    Lnorm=F(0)
    for row in green["rows"]:
        m=row["mode"];eps=bounds(axes[m]["relative_radius"])[1]
        if eps!=(F(1,16) if m==4 else F(1,1024)):
            raise ValueError("The actual R74 outer-parameter axis changed")
        for data in row["physical_components"].values():
            Lnorm+=point(data["affine_outer_parameter_lift"])/eps
    candidate=4*sigma
    centre=Lnorm+candidate
    head=point(green["sums"]["true_head_value_lift"])
    value0=centre+Nresponse+head
    image=value0+rho*Gamma
    gates=dict(all18_true_source_groups=True,all10793_original_leaves=total_original==10793,
        all10933_original_subpanels=total_subpanels==10933,
        every_exact_old_density_below_its_persisted_cap=True,
        same_true_candidate_envelope_and_all20_parameters=True,
        enlarged_complete_mean_and_Wiener_inverse_domains=max_R<F(1,64) and max_lead<1,
        complete_mean_inverse_and_low46_direction_derivative_retained=True,
        ordered_two_branch_Green_compared_by_positive_pointwise_density=True,
        all_parameter_source_bound_not_only_Cstar=True,
        correct_linear_outer_lift_and_complete_inner_beta_kept=True,
        projected_full_ball_strict_self_map=image<rho,
        projected_full_ball_strict_contraction=Gamma<1)
    result=dict(status="Executed actual conditional two-mode outer field ball with prescribed complete beta(a)",
        author="/root (GPT-6 Astra Pro, AI-assisted)",all_gates=all(gates.values()),gates=gates,
        radius=record(rho),parameter_sigma=record(sigma),old_derivative_radius=record(oldrho),
        unknown_outputs=[2,4],derivative_input_cutoff=92,parameter_axes=family["parameter_axes"],
        other_height_functions="Fixed at the same C_eta; low6..40 retained, remaining low and high zero in this projected subproblem",
        actual_cut_parameter_consistency_paid=False,remaining_frequency_PDE_paid=False,
        full_outer_or_closed_surface_claimed=False,
        physical_norm=green["physical_norm"],
        complete_mean_input_max=uprecord(max_R),complete_inverse_leading_norm_max=uprecord(max_lead),
        derivative_density_multiplier=record(max_K),derivative_density_maximizer=max_K_at,
        complete_parameter_source_multiplier=record(max_B),source_multiplier_maximizer=max_B_at,
        original_ordered_Green_derivative=record(oldGamma),
        enlarged_complete_source_derivative_Green_upper=record(Gamma),
        complete_parameter_source_Green_upper=record(Nresponse),
        original_fixed_outer_linear_lift_upper=uprecord(Lnorm),
        whole_selected_candidate_norm_upper=record(candidate),
        linear_lift_minus_candidate_triangle_upper=uprecord(centre),
        complete_inner_head_beta_lift_upper=uprecord(head),
        projected_map_at_zero_upper=uprecord(value0),projected_map_full_ball_upper=uprecord(image),
        strict_ball_margin_lower=rational_record(rho-image) if image<rho else None,
        fixed_point_norm_upper=uprecord(value0/(1-Gamma)) if Gamma<1 else None,
        complete_groups=groups,source_rows=dict(path=str(a.rows),rows=total_original,
            bytes=a.rows.stat().st_size,sha256=digest(a.rows)),input_hashes=hashes,
        source_sha256=digest(__file__),helper_hashes={n:digest(Path(__file__).with_name(n)) for n in
            ("closure_split_joint_io_v2.py","closure_outer_source_parameter_rows.py",
             "closure_outer_whole_field_green_budget.py","root_moving_auxiliary_centre_family.py",
             "root_anisotropic_true_cut_cauchy.py")},
        no_new_Arb=True,no_new_ODE=True,no_new_source_integral=True,no_Node=True,
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result["peak_RSS_KiB"]>a.rss_kib:raise MemoryError("The owned Fraction RSS observer was exceeded")
    output=write_new(a.out,result)
    print(json.dumps(dict(event="done",all_gates=result["all_gates"],output=output,
        Gamma=record(Gamma)["display"],Nresponse=record(Nresponse)["display"],
        image=uprecord(image)["display"],seconds=result["elapsed_seconds"],RSS_KiB=result["peak_RSS_KiB"])),flush=True)
    if not result["all_gates"]:raise SystemExit(2)


if __name__=="__main__":main()

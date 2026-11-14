#!/usr/bin/env python3
"""Replan parameter-only layouts from already certified 0/419 domains.

No fresh field values are sampled.  The analytic alias/tail costs are actual
directed evaluations of the full budgets.  Each proposed grid has an explicit
remaining nodal RMS/rounding acceptance condition.  Saved finite-P proxy
domains certify density replanning for that SAME saved P, not a new unknown P.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx
from fourfold_forward_density_pipeline_Q1024_v3 import adaptive_layout, upper, lower, save
from fourfold_phase_time_circle_field_package import combined_budget
from fourfold_actual_reference_density import density_budget
from fourfold_joint_dft_l2_noise import joint_retained_rectangle_error
from fourfold_phase_domain_cover_verify import Time
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read


def records(d):
    return {key:ball_record(upper(v) if isinstance(v,dict) else v) for key,v in d.items()}


def layout_record(layout):
    N,K,Nt,m=layout
    return dict(nodes=N,degree=K,time_nodes=Nt,terms=m,
                independent_complex_time_nodes=Nt//2+1,
                sampled_time_angle_pairs=N*(Nt//2+1))


def study(path,targets):
    old=read(path)
    if not (old.get("complete") and old.get("complete_continuous_parameter_densities_proved",old.get("complete_continuous_signed_parameter_densities_proved"))):
        raise ValueError("a completed actual source report is required")
    source=old["identity"]["actual_parameter_source"]
    uniform=bool(old["identity"].get("whole_real_parameter_tube",False))
    if not uniform and not source.get("actual_center_parameter_only"):
        raise ValueError("unknown parameter scope")
    radii=source["base_identity"]
    a,b=map(Time.parse,radii["exact_time_endpoints"])
    h=abs((b-a).scale(Fraction(1,2)).value())
    q=lower(old["real_reference_gate"]["q"]["full_real_time_q_real_lower"])
    ps=exact_arb(Fraction(old["real_reference_gate"]["physical_approximation_strip"]))
    S=exact_arb(Fraction(old["label_strip"]))
    R=arb(source["source_time_radius"]);theta=arb(source["source_physical_theta_strip"])
    M=[upper(source["complete_source_moduli"][key]) for key in ("fp","fpp")]
    domains=[[(upper(d["time_radius"]),upper(d["label_strip"]),upper(d["modulus"]))
             for d in rows] for rows in old["finite_proxy_domains"]]
    common=[(a[0],a[1],max(a[2],b[2]).upper()) for a,b in zip(*domains)]
    previous_field=layout_record(tuple(old["field_layout"][k] for k in ("nodes","degree","time_nodes","terms")))
    previous_density=layout_record(tuple(old["density_layout"][k] for k in ("nodes","degree","time_nodes","terms")))
    answers=[]
    for target_string in targets:
        target=arb(target_string);field_target=(target*q/(8*h)).lower()
        def fb(N,K,Nt,m,errors):
            return combined_budget(N,K,theta,ps,1,errors,[(R,max(M))],Fraction(1),Nt,0)
        fl,_=adaptive_layout(fb,N=512,K=64,Nt=16,m=12,target=field_target,max_degree=4095,max_terms=128)
        N,K,Nt,m=fl
        field=[]
        for modulus in M:
            budget=combined_budget(N,K,theta,ps,1,[arb(0)]*m,[(R,modulus)],Fraction(1),Nt,0)
            factor=joint_retained_rectangle_error(arb(1),m,K,arb(1),ps,frequency_scale=4)
            allowed=((field_target/2-budget["total"])/factor).lower()
            if not allowed>0:raise ValueError("no positive field nodal RMS allowance")
            field.append(dict(analytic_budget=records(budget),
                normalized_nodal_RMS_allowed=ball_record(allowed),
                separate_coefficient_rounding_allowed=ball_record(field_target/4),
                finite_compression_allowed=ball_record(field_target/4)))
        def db(N,K,Nt,m,errors):
            return density_budget(common,errors,N,K,arb(1),Nt,S)
        dl,_=adaptive_layout(db,N=512,K=128,Nt=16,m=12,target=target/2,max_degree=4095,max_terms=128)
        N,K,Nt,m=dl;density=[]
        for domain in domains:
            budget=density_budget(domain,[arb(0)]*m,N,K,arb(1),Nt,S)
            factor=joint_retained_rectangle_error(arb(1),m,K,arb(1),S,frequency_scale=1)
            allowed=((target/4-upper(budget["total"]))/factor).lower()
            if not allowed>0:raise ValueError("no positive density nodal RMS allowance")
            density.append(dict(analytic_budget=budget,normalized_nodal_RMS_allowed=ball_record(allowed),
                separate_coefficient_rounding_allowed=ball_record(target/8),
                finite_compression_allowed=ball_record(target/8)))
        frec,drec=layout_record(fl),layout_record(dl)
        def db2(N,K,Nt,m,errors):
            return density_budget(domains[1],errors,N,K,arb(1),Nt,S)
        dl2,_=adaptive_layout(db2,N=512,K=128,Nt=16,m=12,target=target/2,max_degree=4095,max_terms=128)
        N2,K2,Nt2,m2=dl2
        order2_budget=db2(N2,K2,Nt2,m2,[arb(0)]*m2)
        order2_factor=joint_retained_rectangle_error(arb(1),m2,K2,arb(1),S,frequency_scale=1)
        order2_rms=((target/4-upper(order2_budget["total"]))/order2_factor).lower()
        if not order2_rms>0:raise ValueError("no positive second-source-only RMS allowance")
        if all("actual_cap_integrated_error" in row for row in old["density"]):
            caps=[upper(row["actual_cap_integrated_error"]) for row in old["density"]]
        elif (not uniform
              and radii["whole_real_interval_in_selected_germ"]):
            caps=[arb(0),arb(0)]
        else:
            raise ValueError("no complete crossing-cap witness")
        answers.append(dict(target=target_string,field_target=ball_record(field_target),field_layout=frec,
            field_orders=field,finite_density_layout=drec,finite_density_orders=density,
            field_sample_pair_ratio=float(Fraction(frec["sampled_time_angle_pairs"],previous_field["sampled_time_angle_pairs"])),
            finite_density_sample_pair_ratio=float(Fraction(drec["sampled_time_angle_pairs"],previous_density["sampled_time_angle_pairs"])),
            only_second_parameter_density_layout=layout_record(dl2),
            only_second_parameter_density_budget=order2_budget,
            only_second_parameter_density_RMS_allowed=ball_record(order2_rms),
            total_integrated_error_if_all_new_acceptance_conditions_pass=[ball_record((5*target/4+cap).upper()) for cap in caps],
            density_replanning_uses_same_saved_finite_P=True,
            future_new_field_needs_new_finite_proxy_domain_budget=True,
            new_sampling_not_performed=True))
    return dict(path=str(path),sha256=sha(path),segment=old["identity"]["reference"]["segment"],
        whole_real_parameter_tube=uniform,
        exact_parameter_interval=old["identity"].get("exact_parameter_interval",[radii["exact_delta_fraction"]]*2),
        previous_target=old["target_uniform_density_error"],previous_field_layout=previous_field,
        previous_density_layout=previous_density,actual_previous_nodal_RMS=old.get("field_joint_nodal_RMS"),
        actual_previous_integrated_source_errors=[v["true_integrated_error"] for v in old["density"]],
        alternatives=answers)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out",type=Path,required=True);p.add_argument("--bits",type=int,default=256)
    args=p.parse_args();ctx.prec=args.bits;tic=time.monotonic()
    base=Path("data/phase_ring_continuation")
    cases=[
        ("step5_parameter_density_forward/forward_0000_center.json.gz",["1e-11","1e-9","1e-8"]),
        ("type_fixed_step02_d5_step5_parameter_density419.json.gz",["1e-11","1e-9","1e-8"]),
        ("step5_uniform_parameter_density_forward_h1e9/forward_0000_ef134f2a18_uniform.json.gz",["1e-8","1e-7","1e-6","1e-5"]),
        ("type_fixed_step02_d5_step5_uniform_parameter_density419_h1e9_l2_degree.json.gz",["1e-8","1e-7","1e-6","1e-5"])]
    report=dict(kind="actual_domain_parameter_layout_budget_comparison",complete=True,
        source_sha256=sha(__file__),cases=[study(base/name,targets) for name,targets in cases],
        source_or_field_resampling_performed=False,
        meaning="Complete analytic budget evaluations and explicit remaining node/rounding gates; future smaller grids are not certified as sampled.",
        wall_seconds=time.monotonic()-tic)
    save(args.out,report)
    for case in report["cases"]:
        print(dict(segment=case["segment"],uniform=case["whole_real_parameter_tube"],
            alternatives=[dict(target=row["target"],field=row["field_layout"],density=row["finite_density_layout"],
                field_ratio=row["field_sample_pair_ratio"],density_ratio=row["finite_density_sample_pair_ratio"])
                for row in case["alternatives"]]),flush=True)
    print(dict(path=str(args.out),sha256=sha(args.out)),flush=True)


if __name__=="__main__":main()

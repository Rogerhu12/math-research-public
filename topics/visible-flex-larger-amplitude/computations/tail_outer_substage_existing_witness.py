#!/usr/bin/env python3
"""Locate the paid worst leaf from existing R48 data, without new quadrature.

Rebuild identical H,Kbar,Kbar_x from stored true bins and shared jets.
Evaluate only the same real source ranges on the leaf, its two halves,
and midpoint. Record r_x span, actual signed physical Hrr, and every
finite-J frequency through twice the saved angular cutoff. Complete
mean/c_x enclosures come from the unchanged R64 root. In particular
J above the saved cutoff is exactly independent of the scalar mean.
No radial flow, Node, BVP or new source integral is performed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb,acb,ctx
from closure_split_joint_io import read,digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q,ball_record
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import source_range,MOMENT_KEYS
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_weighted_compatible import intersection,normalized_endpoint_jet,make_weighted_candidate,weighted_panel_fields
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_r41_connection_polynomial import add,scale,product,derivative,norm


def rec(values):return {str(key):ball_record(value) for key,value in values.items()}
def l1(poly):return sum((abs(value) for value in poly.values()),arb(0)).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("candidate","ready","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--field",default="actual_Darboux_defect_abs")
    p.add_argument("--rss-limit-mib",type=int,default=40)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError("Use a fresh fixed-candidate witness diagnostic")
    ctx.prec=192;began=time.monotonic()
    hashes={str(q):digest(q) for q in (args.candidate,args.ready)}
    data,ready=map(read,(args.candidate,args.ready))
    if (data["cell"]!=0 or not all(data["gates"].values())
            or data["input_hashes"].get(str(args.ready))!=hashes[str(args.ready)]
            or not data["actual_polynomial_derivative_used_for_all_residuals"]):
        raise ValueError("A complete same-background actual candidate is required")
    for name,checksum in data["source_hashes"].items():
        if digest(Path(__file__).with_name(name))!=checksum:
            raise ValueError("An executed candidate dependency changed: "+name)
    witness=data["bounds"][args.field]["witness"]
    j,k,v=(witness[q] for q in ("segment","part","bin"))
    a,b=F(k,8),F(k+1,8);h=b-a
    lo,hi=F(witness["source_left"]),F(witness["source_right"]);mid=(lo+hi)/2
    if j!=data["segment"] or not a<=lo<hi<=b:raise ValueError("The actual witness has another domain")
    part=data["parts"][k];nodes=[data["nodes"][k],data["nodes"][k+1]]
    bins=[row for row in data["bins"] if row["part"]==k]
    if len(bins)!=8 or bins[v]["bin"]!=v:raise ValueError("The complete original eight true bins are required")
    modes,tau=data["modes"],F(data["tau"]);cutoff=max(modes)
    original_bound=data["bounds"][args.field]
    del data
    head=SourceValues(ready);head.params=ready["rationalDeepModel"]["physicalParameters"]
    cell=OuterCell(head,0);segment=cell.segments[j]
    def endpoint(node):
        x=F(node["source_x"]);g=source_range(cell,segment,x,x,None,exact_q(F(1,8)))
        w=intersection(g["w"],ball(node["w"]))
        ell=intersection(g["log_w_x"],ball(node["wr"])*g["radius_x"]/w)
        jets={key:{int(m):ball(val) for m,val in node["shared_physical_jets"][key].items()}
              for key in ("H","Hr","Hrr")}
        return normalized_endpoint_jet(jets["H"],jets["Hr"],jets["Hrr"],w=w,
            radius_u=exact_q(h)*g["radius_x"],log_w_u=exact_q(h)*ell)
    total={key:ball(part["total_true_positive_moments"][key]) for key in MOMENT_KEYS}
    candidate=make_weighted_candidate(endpoint(nodes[0]),endpoint(nodes[1]),total)
    for m,value in candidate["bubble_coefficient"].items():
        candidate["bubble_coefficient"][m]=intersection(value,ball(part["bubble_coefficients"][str(m)]))
    def sums(indices):return {key:sum((ball(bins[i]["values"][key]) for i in indices),arb(0))
                             for key in ("width",*MOMENT_KEYS)}
    pl,ph=sums(range(v)),sums(range(v+1))
    sl,sh=sums(range(v+1,8)),sums(range(v,8))
    def moments(low,high):return {key:nonnegative_integral(ball_record(
        max(arb(0),low[key].lower()).union(min(high[key].upper(),total[key].upper()))))
        for key in MOMENT_KEYS}
    prefix,suffix=moments(pl,ph),moments(sl,sh)
    rl,rr=ball(nodes[0]["radius"]),ball(nodes[1]["radius"])
    rleft=intersection(rl+pl["width"],rr-sh["width"])
    rright=intersection(rl+ph["width"],rr-sl["width"])
    radius=rleft.union(rright)
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    reports=[]
    for label,left,right in (("whole_original_leaf",lo,hi),("left_half",lo,mid),
                              ("right_half",mid,hi),("source_midpoint",mid,mid)):
        g=source_range(cell,segment,left,right,None,exact_q(F(1,8)))
        u=exact_q((left-a)/h).union(exact_q((right-a)/h))
        H,K,Kx=weighted_panel_fields(candidate,u=u,u_x=1/exact_q(h),prefix_moments=prefix,suffix_moments=suffix)
        r64=general_mean_and_defect(H,K,Kx,modes=modes,weights=weights,radius=radius,
            radius_x=g["radius_x"],w=g["w"],log_w_x=g["log_w_x"])
        if not r64["gate"]:raise ArithmeticError("The existing complete mean gate was lost on a subset")
        rx,w,ell=g["radius_x"],g["w"],g["log_w_x"]
        z=w*w;E=1+z;s=rx/radius
        P=scale(derivative(H),1/(radius*w));T=derivative(P);U=add(derivative(K),scale(P,-1))
        Lnon=add(K,scale(T,E))
        linear=add(Kx,scale(add(scale(K,2),T),ell))
        quadratic=add(product(Lnon,Kx),scale(product(U,U),-E*s),
            scale(add(product(K,K),scale(product(P,P),z),product(K,T)),ell))
        Jbase=add(linear,quadratic)
        cmax=r64["bounds"]["complete_mean_abs"].upper()
        cxmax=r64["bounds"]["complete_mean_source_derivative_abs"].upper()
        c=(-cmax).union(cmax);cx=(-cxmax).union(cxmax)
        J=add(Jbase,scale(linear,c),scale(Lnon,cx),
            {0:acb(cx*(1+c)+ell*(2*c+c*c))})
        if max(map(abs,J),default=0)>2*cutoff:raise AssertionError("The finite complete J support changed")
        bands={"mean":{m:q for m,q in J.items() if m==0},
               "retained_nonmean":{m:q for m,q in J.items() if 0<abs(m)<=cutoff},
               # This formula removes every mean term algebraically, without
               # subtracting two separately rounded interval polynomials.
               "outside_saved_height":{m:q for m,q in quadratic.items() if cutoff<abs(m)<=2*cutoff}}
        factor=z/(radius*rx*E*E)
        Hrr=scale(add(Kx,scale(K,ell)),w/rx)
        bdata={name:dict(modes=sorted(poly),zero_strip_l1=ball_record(l1(poly)),
            W1_tau=ball_record(norm(poly,exact_q(tau))),
            physical_Darboux_contribution_upper=ball_record((factor*l1(poly)).upper()))
            for name,poly in bands.items()}
        m2=abs(J.get(2,acb(0)))
        row=dict(scope=label,source_left=str(left),source_right=str(right),
            height_primitive_enclosure="Unchanged complete saved bin prefix/suffix hull; no partial integrals recomputed",
            radius=ball_record(radius),radius_x=ball_record(rx),
            radius_x_upper_lower_ratio=ball_record((rx.upper()/rx.lower()).upper()),
            w=ball_record(w),log_w_x=ball_record(ell),physical_conversion_factor=ball_record(factor),
            complete_R64_gate=True,R64_bounds=rec(r64["bounds"]),
            signed_actual_nonmean_Hrr_W1=ball_record(norm(Hrr,exact_q(tau))),
            signed_actual_nonmean_Hrr_l1=ball_record(l1(Hrr)),
            signed_actual_nonmean_Hrr_m2=ball_record(2*Hrr[2].real),
            full_mean_bounds_used=dict(c=ball_record(c),cx=ball_record(cx)),
            finite_J_bands=bdata,outside_J_exactly_independent_of_c_and_cx=True,
            finite_J_l1_Darboux_upper=ball_record((factor*l1(J)).upper()),
            finite_J_m2_coefficient_Darboux_lower=ball_record(max(arb(0),(factor.lower()*m2.lower()).lower())),
            finite_J_coefficients={str(m):dict(real=ball_record(q.real),imaginary=ball_record(q.imag)) for m,q in sorted(J.items())},
            complete_cosine_fields={name:rec({m:2*poly[m].real for m in modes}) for name,poly in (("H",H),("Kbar",K),("Kbar_x",Kx))})
        reports.append(row)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>1024*args.rss_limit_mib:
            raise MemoryError("The existing-data witness locator exceeded its RSS cap")
    out=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete same-candidate worst-leaf source/span/frequency location",cell=0,segment=j,part=k,bin=v,
        original_witness=witness,original_bound=original_bound,reports=reports,
        saved_height_cutoff=cutoff,complete_J_cutoff=2*cutoff,
        exact_high_band_identity="Pi_{|m|>cutoff} J = Pi_{|m|>cutoff} [(Kbar+E Ptheta)Kbar_x-E s(Kbar_theta-P)^2+ell(Kbar^2+zP^2+Kbar Ptheta)]",
        same_candidate_g_total_moments_and_endpoint_jets=True,new_source_integrals=0,
        new_radial_ODE_or_Node=False,entire_substage_maximum_recomputed=False,
        exact_solution_or_global_spectral_error_claimed=False,input_hashes=hashes,
        source_hashes={name:digest(Path(__file__).with_name(name)) for name in (
            Path(__file__).name,"tail_outer_weighted_compatible.py","tail_outer_general_mean_bounds.py",
            "tail_outer_positive_moment_panels.py","tail_outer_candidate_domain.py",
            "tail_r41_connection_polynomial.py","closure_real_outer_radius.py")},
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    text=json.dumps(out,indent=2)+"\n"
    if args.out.suffix!=".gz":raise ValueError("Use gzip for the complete finite Fourier records")
    with gzip.open(args.out,"wt") as stream:stream.write(text)
    if args.out.stat().st_size>=5_000_000:raise ValueError("The witness package exceeds the file limit")
    print(json.dumps(dict(event="complete",output=str(args.out),cases=len(reports),
        seconds=out["elapsed_seconds"],peak_RSS_KiB=out["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

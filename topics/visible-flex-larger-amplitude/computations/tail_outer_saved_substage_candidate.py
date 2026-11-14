#!/usr/bin/env python3
"""One original outer segment rebuilt from all eight saved shooting substages.

The true background, original outer endpoints and all twenty Fourier modes
are fixed. Six positive integrals (physical width and five R48 moments)
are rigorously integrated over the original R26 branch/sign partition.
Shared internal physical two-jets define a new eight-piece C2 candidate.
R64 uses its actual polynomial derivatives and restores the complete mean.
No Node, radial ODE, BVP, or claim of an accepted exact outer solution.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

from flint import arb,acb,ctx
from closure_split_joint_io import read,digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q,ball_record,power2
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import (
    source_range,positive_hull,add_moments,zero_moments,MOMENT_KEYS,Subdivide)
from tail_outer_weighted_compatible import (
    intersection,normalized_endpoint_jet,make_weighted_candidate,weighted_panel_fields)
from tail_outer_weighted_endpoint import finite_saved_endpoint
from tail_outer_finite_momentum_root import PureFiniteMomentumRoot
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_same_candidate_point_probe import two_angle_difference


def polynomials(u):
    return {"00":(1-u)**2*(1+2*u),"10":u*(1-u)**2,
            "01":u*u*(3-2*u),"11":u*u*(1-u),"b":u*u*(1-u)**2}


class RealSixIntegrals:
    """Same real R26 formulas, six positive integrands and explicit branch cuts."""
    def __init__(self,cell,segment,parents,memory_gate):
        self.cell,self.segment,self.parents=cell,segment,parents
        self.memory_gate=memory_gate
        self.analytic_calls=0
        self.range_strips=0

    def piece(self,left,right,part_left,part_right):
        totals={key:arb(0) for key in ("width",*MOMENT_KEYS)}
        records=[]
        h=part_right-part_left
        if not part_left<=left<right<=part_right:
            raise ValueError("The integrals must lie in one fixed positive substage")
        for parent_index,parent in enumerate(self.parents):
            a,b=max(left,F(parent["left"])),min(right,F(parent["right"]))
            if not a<b:continue
            kind=parent["branch_sign"]
            if kind is None:
                ranges=source_range(self.cell,self.segment,a,b,None,exact_q(F(1,8)))
                u=exact_q((a-part_left)/h).union(exact_q((b-part_left)/h))
                base=polynomials(u)
                rx,w=ranges["radius_x"],ranges["w"]
                values={"width":rx*exact_q(b-a)}
                values.update({key:rx*w*base[key]*exact_q(b-a) for key in MOMENT_KEYS})
                # Every true basis and the true physical measure are nonnegative.
                values={key:positive_hull(value.lower(),value.upper())
                        for key,value in values.items()}
                self.range_strips+=1
                method="Original complete possible-branch range on a certified tiny boundary strip"
            else:
                branch,sign=kind
                def integrand(x,key,analytic=False):
                    rx=self.cell.integrand(self.segment,x,branch,sign,analytic)
                    if key=="width":return rx
                    w=self.cell.profile(self.segment,x,branch)[0].exp()
                    u=(x-exact_q(part_left))/exact_q(h)
                    return rx*w*polynomials(u)[key]
                midpoint=exact_q((a+b)/2)
                values={}
                for key in totals:
                    scale=abs(integrand(midpoint,key)).upper()
                    if not scale>0:raise ArithmeticError("A positive true integrand scale was lost")
                    def f(z,analytic):
                        return integrand(z,key,analytic)/scale
                    value=acb.integral(f,acb(exact_q(a)),acb(exact_q(b)),
                        rel_tol=power2(-96),abs_tol=power2(-116),
                        deg_limit=64,eval_limit=100000,depth_limit=40)
                    self.analytic_calls+=1
                    if not value.is_finite() or not value.imag.contains(0):
                        raise ArithmeticError("A true six-integral component failed")
                    raw=scale*value.real
                    values[key]=positive_hull(raw.lower(),raw.upper())
                    self.memory_gate("true-six-integral")
                method="Rigorous same-source analytic Arb/Acb positive integral"
            for key in totals:
                raw=totals[key]+values[key]
                totals[key]=positive_hull(raw.lower(),raw.upper())
            records.append(dict(parent=parent_index,left=str(a),right=str(b),branch_sign=kind,
                method=method,values={key:ball_record(value) for key,value in values.items()}))
        if not records or records[0]["left"]!=str(left) or records[-1]["right"]!=str(right):
            raise ValueError("The stored real source partition did not cover the substage")
        if any(a["right"]!=b["left"] for a,b in zip(records,records[1:])):
            raise ValueError("A true branch interval was omitted")
        if not all(value>0 for value in totals.values()):
            raise ArithmeticError("A complete positive subinterval integral lost its lower bound")
        return totals,records


def record_values(values):
    return {key:ball_record(value) for key,value in values.items()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("nodes","radius-ledger","response","ready","prior-r64","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--subdivision-source",type=Path,required=True)
    p.add_argument("--segment",type=int,default=3)
    p.add_argument("--validation-parts",type=int,default=8)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError("Use a fresh complete substage candidate output")
    if not 0<=args.segment<8 or args.validation_parts<1:
        raise ValueError("This first application replaces one of the original source-x pieces")
    ctx.prec=192;began=time.monotonic()
    def memory_gate(stage):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>1024*args.rss_limit_mib:
            raise MemoryError("The owned substage candidate exceeded its RSS cap at "+stage)
    paths=(args.nodes,args.radius_ledger,args.response,args.ready,args.prior_r64,args.subdivision_source)
    hashes={str(path):digest(path) for path in paths}
    nodes,ledger,packet,ready,prior=map(read,paths[:5])
    for path in (args.radius_ledger,args.response,args.ready):
        if nodes["input_hashes"].get(str(path))!=hashes[str(path)]:
            raise ValueError("The saved original node/source identity changed")
    if prior["input_hashes"].get(str(args.nodes))!=hashes[str(args.nodes)]:
        raise ValueError("The original continuous candidate uses other shared endpoints")
    if (not nodes["complete_original_segment_node_cover"] or not ledger["complete_outer_radius"]
            or not packet["response"]["converged"] or not all(
                row["all_general_mean_gates"] for row in prior["segments"][:8])):
        raise ValueError("The actual original fixed-source packets are incomplete")
    subdivision=args.subdivision_source.read_text()
    for anchor in (
        "for(let j=old.profiles.length-1;j>=0;j--)for(let k=parts-1;k>=0;k--)",
        "const base=old.profiles[j],a=k/parts,b=(k+1)/parts,h=b-a;",
        "rawNode[rawDepth]=cells.length;"):
        if subdivision.count(anchor)!=1:
            raise ValueError("The actual saved source-x substage ordering changed")
    cp=packet["response"]["checkpoint"];cfg=cp["parameters"]
    M,parts,spacing=cfg["modes"],cfg["shootingParts"],cfg["spacing"]
    if (M!=20 or parts!=8 or spacing!=2 or cfg["physicalDepth"]!=12
            or cfg["orientation"]!=1 or len(cp["states"])!=865
            or cp["rawNode"]!=[72*n for n in range(13)]
            or cp["rawStates"]!=[cp["states"][i] for i in cp["rawNode"]]):
        raise ValueError("The complete original eight-substage shooting field changed")
    n,j=nodes["cell"],args.segment
    if n!=0:raise ValueError("This application is explicitly actual outer cell0")
    head=SourceValues(ready);head.params=ready["rationalDeepModel"]["physicalParameters"]
    cell=OuterCell(head,0);segment=cell.segments[j]
    original_segment=next(row for row in ledger["cells"] if row["cell"]==0)["segments"][j]
    if original_segment["segment"]!=j:raise ValueError("Original R26 segment order differs")
    engine=RealSixIntegrals(cell,segment,original_segment["panels"],memory_gate)
    recovery=args.out.with_name(args.out.stem+"-recovery.json")
    if recovery.exists():raise FileExistsError("The substage recovery prefix is already used")
    numeric_source_hashes={name:digest(Path(__file__).with_name(name)) for name in (
        Path(__file__).name,"tail_outer_weighted_endpoint.py","tail_outer_weighted_compatible.py",
        "tail_outer_finite_momentum_root.py","tail_outer_general_mean_bounds.py",
        "tail_outer_positive_moment_panels.py","closure_real_outer_radius.py",
        "tail_r33_middle_ordered_physical.py","tail_outer_same_candidate_point_probe.py")}
    bins=[];part_totals=[];node_rows=[];stage_rows=[];point_rows=[]
    def save_recovery(stage):
        partial=dict(status="Recovery-only partial true substage construction",phase=stage,
            author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
            cell=0,segment=j,accepted_exact_radial_solution=False,
            complete_bins=len(bins),complete_nodes=len(node_rows),complete_stages=len(stage_rows),
            bins=bins,nodes=node_rows,stages=stage_rows,input_hashes=hashes,
            source_hashes=numeric_source_hashes,analytic_integrals=engine.analytic_calls,
            range_strips=engine.range_strips,elapsed_seconds=time.monotonic()-began)
        text=json.dumps(partial,indent=2)+"\n"
        if len(text.encode())>=1_000_000:
            raise ValueError("Use compact source records before recovery exceeds 1 MB")
        temporary=recovery.with_name(recovery.name+".tmp")
        temporary.write_text(text);temporary.replace(recovery)
    for k in range(parts):
        a,b=F(k,parts),F(k+1,parts)
        totals={key:arb(0) for key in ("width",*MOMENT_KEYS)}
        for v in range(args.validation_parts):
            l=a+(b-a)*F(v,args.validation_parts);r=a+(b-a)*F(v+1,args.validation_parts)
            values,records=engine.piece(l,r,a,b)
            for key in totals:totals[key]+=values[key]
            bins.append(dict(part=k,bin=v,left=str(l),right=str(r),
                values=record_values(values),source_parts=records))
        part_totals.append(totals)
        save_recovery("true-integrals")
        print(json.dumps(dict(event="actual_substage_positive_integrals",segment=j,part=k,
            analytic_integrals=engine.analytic_calls,seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    width=sum((row["width"] for row in part_totals),arb(0))
    intersection(width,ball(original_segment["width"]))
    rleft,rright=ball(nodes["rows"][j]["radius"]),ball(nodes["rows"][j+1]["radius"])
    intersection(width,rright-rleft)
    pre=[arb(0)]
    for row in part_totals:pre.append(pre[-1]+row["width"])
    post=[arb(0)]*(parts+1)
    for k in range(parts-1,-1,-1):post[k]=post[k+1]+part_totals[k]["width"]
    radii=[intersection(rleft+pre[k],rright-post[k]) for k in range(parts+1)]
    radii[0],radii[-1]=rleft,rright
    root=PureFiniteMomentumRoot(M,spacing,cfg["quadrature"],cfg["projectionFloor"])
    modes,tau=nodes["modes"],F(nodes["tau"])
    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}
    mu=head.eps_phys*(head.a*head.d0.log()).exp()
    for k in range(parts+1):
        x=F(k,parts);idx=(9-j)*parts-k
        if k in (0,parts):
            old=nodes["rows"][j+(1 if k else 0)]
            if old["state_index"]!=idx:raise ValueError("Original endpoint state index changed")
            row=dict(point=k,source_x=str(x),state_index=idx,
                radius=old["radius"],w=old["w"],wr=old["wr"],
                shared_physical_jets=old["shared_physical_jets"],
                candidate_L_orthonormal_cosine=old["candidate_L_orthonormal_cosine"],
                finite_endpoint_definition=old["finite_endpoint_definition"],
                original_outer_endpoint_reused_exactly=True)
        else:
            g=source_range(cell,segment,x,x,None,exact_q(F(1,8)))
            state=cp["states"][idx];Q=[exact_q(value) for value in state[:M]]
            Pi=[exact_q(value) for value in state[M:]]
            L,diagnostic=root.solve([float(value.mid()) for value in Q+Pi],
                radius=float(radii[k].mid()),w=float(g["w"].mid()),mu=float(mu.mid()))
            jet=finite_saved_endpoint(Q,L,radius=radii[k],radius_x=g["radius_x"],
                w=g["w"],log_w_x=g["log_w_x"],spacing=spacing,tau=tau,
                inverse_degree=nodes["inverse_degree"])
            row=dict(point=k,source_x=str(x),state_index=idx,
                radius=ball_record(radii[k]),w=ball_record(g["w"]),
                wr=ball_record(g["w"]*g["log_w_x"]/g["radius_x"]),
                radius_x=ball_record(g["radius_x"]),log_w_x=ball_record(g["log_w_x"]),
                full_saved_Q=state[:M],full_saved_momentum=state[M:],
                local_momentum_multiplier=1,
                candidate_L_orthonormal_cosine=L,finite_root_diagnostic=diagnostic,
                shared_physical_jets={key:record_values(jet[key]) for key in ("H","Hr","Hrr")},
                finite_endpoint_definition=jet["report"],
                original_outer_endpoint_reused_exactly=False)
        node_rows.append(row)
        save_recovery("shared-inner-nodes")
        memory_gate("shared-finite-node")
    def endpoint_for(row,h):
        x=F(row["source_x"]);g=source_range(cell,segment,x,x,None,exact_q(F(1,8)))
        w=intersection(g["w"],ball(row["w"]))
        ell=intersection(g["log_w_x"],ball(row["wr"])*g["radius_x"]/w)
        jets={key:{int(m):ball(value) for m,value in row["shared_physical_jets"][key].items()}
              for key in ("H","Hr","Hrr")}
        return normalized_endpoint_jet(jets["H"],jets["Hr"],jets["Hrr"],w=w,
            radius_u=exact_q(h)*g["radius_x"],log_w_u=exact_q(h)*ell)
    candidates=[]
    global_bounds,global_min={},{}
    leaves=0
    def update(table,key,value,witness,minimum=False):
        edge=value.lower() if minimum else value.upper()
        if key not in table or (edge<table[key]["value"] if minimum else edge>table[key]["value"]):
            table[key]=dict(value=edge,witness=witness)
    for k in range(parts):
        a,b=F(k,parts),F(k+1,parts);h=b-a
        totals={key:part_totals[k][key] for key in MOMENT_KEYS}
        candidate=make_weighted_candidate(endpoint_for(node_rows[k],h),endpoint_for(node_rows[k+1],h),totals)
        candidates.append(candidate)
        stage_bins=bins[k*args.validation_parts:(k+1)*args.validation_parts]
        prefix=zero_moments()
        suffix=[zero_moments() for unused in range(len(stage_bins)+1)]
        for v in range(len(stage_bins)-1,-1,-1):
            mm={key:ball(stage_bins[v]["values"][key]) for key in MOMENT_KEYS}
            suffix[v]=add_moments(mm,suffix[v+1])
        rp=[arb(0)]
        for row in stage_bins:rp.append(rp[-1]+ball(row["values"]["width"]))
        rs=[arb(0)]*(len(stage_bins)+1)
        for v in range(len(stage_bins)-1,-1,-1):rs[v]=rs[v+1]+ball(stage_bins[v]["values"]["width"])
        count=good=0;local_bounds={};failures=[]
        for v,binrow in enumerate(stage_bins):
            l,r=F(binrow["left"]),F(binrow["right"])
            mm={key:ball(binrow["values"][key]) for key in MOMENT_KEYS}
            full=add_moments(prefix,mm)
            before={key:positive_hull(prefix[key].lower(),full[key].upper()) for key in MOMENT_KEYS}
            after={key:positive_hull(suffix[v+1][key].lower(),suffix[v][key].upper()) for key in MOMENT_KEYS}
            r0=intersection(radii[k]+rp[v],radii[k+1]-rs[v])
            r1=intersection(radii[k]+rp[v+1],radii[k+1]-rs[v+1])
            radius=positive_hull(r0.lower(),r1.upper(),strict=True)
            pending=[(l,r,0)]
            while pending:
                c,d,level=pending.pop()
                try:
                    g=source_range(cell,segment,c,d,None,exact_q(F(1,32)))
                    if d-c>h/F(32):raise Subdivide("Refine the actual polynomial substage coordinate")
                except Subdivide:
                    if level>=28:raise ArithmeticError("Actual validation panel budget exhausted")
                    mid=(c+d)/2;pending.extend([(mid,d,level+1),(c,mid,level+1)])
                    continue
                u=exact_q((c-a)/h).union(exact_q((d-a)/h))
                H,K,Kx=weighted_panel_fields(candidate,u=u,u_x=1/exact_q(h),
                    prefix_moments=before,suffix_moments=after)
                result=general_mean_and_defect(H,K,Kx,modes=modes,weights=weights,
                    radius=radius,radius_x=g["radius_x"],w=g["w"],log_w_x=g["log_w_x"])
                witness=dict(segment=j,part=k,bin=v,source_left=str(c),source_right=str(d))
                count+=1;leaves+=1
                R=(result["norms"][1]["P"]+result["norms"][1]["K"]).upper()
                update(local_bounds,"R_tau",R,witness);update(global_bounds,"R_tau",R,witness)
                if result["gate"]:
                    good+=1
                    for key,value in result["bounds"].items():
                        update(local_bounds,key,value,witness);update(global_bounds,key,value,witness)
                    for key in ("mean_sign_margin","mean_derivative_lower","real_y_lower","real_N_lower",
                                "real_D_lower","real_S_lower","real_L_lower","Wiener_L_lower"):
                        update(global_min,key,result[key],witness,True)
                elif len(failures)<12:
                    failures.append(dict(witness=witness,failure=result["failure"]))
                if leaves%64==0:memory_gate("complete-continuous-R64")
            prefix=full
        row=dict(part=k,left=str(a),right=str(b),panels=count,passed=good,
            complete_mean_and_defect=good==count,first_failures=failures,
            total_true_positive_moments=record_values(totals),
            bubble_coefficients=record_values(candidate["bubble_coefficient"]),
            bounds={key:dict(value=ball_record(value["value"]),witness=value["witness"])
                    for key,value in local_bounds.items()})
        stage_rows.append(row);save_recovery("continuous-complete-mean")
        print(json.dumps(dict(event="substage_continuous_R64",segment=j,part=k,panels=count,passed=good,
            R_tau=str(local_bounds["R_tau"]["value"]),
            Darboux=str(local_bounds.get("actual_Darboux_defect_abs",{}).get("value")),
            seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    for old_name in ("actual_Darboux_defect_abs","full_finite_J_W1"):
        witness=prior["worst"][old_name]["witness"]
        if witness["segment"]!=j:continue
        x=(F(witness["x_left"])+F(witness["x_right"]))/2;k=min(parts-1,int(x*parts))
        a,b=F(k,parts),F(k+1,parts);h=b-a
        left,_=engine.piece(a,x,a,b);right,_=engine.piece(x,b,a,b)
        radius=intersection(radii[k]+left["width"],radii[k+1]-right["width"])
        g=source_range(cell,segment,x,x,None,exact_q(F(1,8)))
        H,K,Kx=weighted_panel_fields(candidates[k],u=exact_q((x-a)/h),u_x=1/exact_q(h),
            prefix_moments={key:left[key] for key in MOMENT_KEYS},
            suffix_moments={key:right[key] for key in MOMENT_KEYS})
        result=general_mean_and_defect(H,K,Kx,modes=modes,weights=weights,radius=radius,
            radius_x=g["radius_x"],w=g["w"],log_w_x=g["log_w_x"])
        if not result["gate"]:raise ArithmeticError("A complete true substage comparison point failed")
        pair=two_angle_difference(H,K,Kx,modes=modes,r=radius,rx=g["radius_x"],w=g["w"],
            ell=g["log_w_x"],c_bound=result["bounds"]["complete_mean_abs"])
        point_rows.append(dict(old_worst_field=old_name,old_witness=witness,
            source_x=str(x),new_part=k,
            actual_background=record_values(dict(radius=radius,radius_x=g["radius_x"],
                w=g["w"],log_w_x=g["log_w_x"])),
            complete_cosine_fields={name:record_values({m:2*field[m].real for m in modes})
                for name,field in (("H",H),("Kbar",K),("Kbar_x",Kx))},
            exact_positive_prefix_moments={key:ball_record(left[key]) for key in MOMENT_KEYS},
            exact_positive_suffix_moments={key:ball_record(right[key]) for key in MOMENT_KEYS},
            bounds=record_values(result["bounds"]),
            two_angle_lower_function=pair,new_candidate_definition=True))
    all_good=all(row["complete_mean_and_defect"] for row in stage_rows)
    packet_out=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete eight-substage actual candidate with original segment outer jets",
        cell=0,segment=j,modes=modes,tau=str(tau),shooting_parts=parts,
        original_865_state_input_retained=True,raw_state_index_rule="(9-segment)*8-k for outward x=k/8 in cell0",
        only_original_segment_candidate_replaced=True,source_background_unchanged=True,
        original_outer_endpoint_two_jets_reused_exactly=True,all_internal_shared_two_jets=True,
        finite_endpoint_derivative_is_only_candidate_definition=True,
        actual_polynomial_derivative_used_for_all_residuals=True,
        gates=dict(complete_source_cover=True,complete_shared_node_cover=len(node_rows)==parts+1,
            full_mean_all_continuous_panels=all_good,full_physical_defect_all_continuous_panels=all_good),
        total_validation_panels=leaves,analytic_integrals=engine.analytic_calls,range_strips=engine.range_strips,
        bins=bins,nodes=node_rows,parts=stage_rows,old_worst_comparison_points=point_rows,
        bounds={key:dict(value=ball_record(value["value"]),witness=value["witness"])
                for key,value in global_bounds.items()},
        minima_over_passed_panels={key:dict(value=ball_record(value["value"]),witness=value["witness"])
                for key,value in global_min.items()},
        new_radial_ODE=False,new_Node_or_BVP=False,accepted_exact_radial_solution=False,
        continuous_defect_scope="Bounds cover all panels only if both complete-mean/defect gates are true",
        input_hashes=hashes,source_hashes=numeric_source_hashes,
        recovery_path=str(recovery),elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    text=json.dumps(packet_out,indent=2)+"\n"
    if len(text.encode())>=1_000_000:
        import gzip
        if args.out.suffix!=".gz":raise ValueError("Complete substage package above 1 MB needs a .gz output")
        with gzip.open(args.out,"wt") as stream:stream.write(text)
    else:
        if args.out.suffix==".gz":
            import gzip
            with gzip.open(args.out,"wt") as stream:stream.write(text)
        else:args.out.write_text(text)
    if args.out.stat().st_size>=5_000_000:raise ValueError("Substage package exceeds the file limit")
    print(json.dumps(dict(event="complete",output=str(args.out),gates=packet_out["gates"],
        panels=leaves,seconds=packet_out["elapsed_seconds"],peak_RSS_KiB=packet_out["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

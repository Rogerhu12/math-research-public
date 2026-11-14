#!/usr/bin/env python3
"""Ordered physical scalar source bounds on cells12..23, true positive deeper cells.

This uses only source values and monotone variations; it performs no
radial quadrature, BVP, Node run, or new fundamental-matrix integration.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_real_head_source_enclosure import RealHead,exact_q,ball_record
from closure_real_head_green_enclosure import load_json,ball
from closure_real_linear_head_enclosure import PositiveKernels


class SourceValues(RealHead):
    """The explicit source-only part of RealHead, without its constructor integrals."""
    def __init__(self,ready):
        p=ready["rationalDeepModel"]["physicalParameters"]
        c=ready["rationalDeepModel"]["exactSourceConstants"]
        self.data={r["n"]:r for r in ready["shallowSourceParameters"]["cells"]}
        self.rc=exact_q(p["rCuff"])
        self.eps_phys=exact_q(p["epsilonScale"])
        self.alpha=exact_q(ready["rationalDeepModel"]["frozenWarpAlpha"])
        self.d0=exact_q(F(c["delta0"]))
        self.c0=exact_q(F(c["etaRatioAtN0"]))
        self.a=arb(11)/4
        self.sqrt12=arb(12).sqrt()
        self.log2=arb(2).log()
        self.cells={}


def matvec(A,v):
    return [(A[i][0]*v[0]+A[i][1]*v[1]).upper() for i in range(2)]


def source_interval(head,segment,left,right):
    lo,hi=exact_q(left),exact_q(right)
    points=[lo]
    for z in segment["critical_points"]:
        if z>lo and z<hi:
            points.append(z)
        elif not (z<lo or z>hi):
            raise ArithmeticError("A dyadic endpoint overlaps a critical-root enclosure")
    points.append(hi)
    values=[head.source_point(segment,z) for z in points]
    logs=[v["log_w"] for v in values]
    w=[v["w"] for v in values]
    log_box=logs[0]
    for z in logs[1:]:
        log_box=log_box.union(z)
    TVlog=sum((abs(b-a) for a,b in zip(logs,logs[1:])),arb(0))
    TVw=sum((abs(b-a) for a,b in zip(w,w[1:])),arb(0))
    down=sum((max(arb(0),(a-b).upper()) for a,b in zip(logs,logs[1:])),arb(0))
    dro=values[0]["ro"]*(segment["length"]*(hi-lo)/head.sqrt12).expm1()
    return dict(log_box=log_box,w_lower=log_box.exp().lower(),
        w_upper=log_box.exp().upper(),TVlog=TVlog,TVw=TVw,down=down,dro=dro)


def panels(head,segment,span):
    stack=[(F(0),F(1),0)]
    while stack:
        left,right,level=stack.pop()
        values=source_interval(head,segment,left,right)
        width=values["log_box"].upper()-values["log_box"].lower()
        if width>span:
            if level>=30:
                raise ArithmeticError("Source-only subdivision limit")
            mid=(left+right)/2
            stack.append((mid,right,level+1));stack.append((left,mid,level+1))
        else:
            yield values


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--density",type=Path,required=True)
    p.add_argument("--positive",type=Path,required=True)
    p.add_argument("--ready",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--physical-through",type=int,default=23)
    p.add_argument("--log-span",default="1/8")
    args=p.parse_args();ctx.prec=192;began=time.monotonic()
    docs,hashes={},{}
    for name in ("density","positive","ready"):
        path=getattr(args,name);docs[name],raw=load_json(path)
        hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,positive,ready=(docs[n] for n in ("density","positive","ready"))
    if not all(density["gates"].values()):
        raise ValueError("The actual physical envelope must be certified")
    if any(hashes[str(args.ready)] not in d["input_hashes"].values() for d in (density,positive)):
        raise ValueError("The source identity differs")
    if not 12<=args.physical_through<=23:
        raise ValueError("This first hybrid calculation covers at most the twelve shallow deep-head cells")
    head=SourceValues(ready)
    kernels=PositiveKernels(head,225,2048)
    rc,R=head.rc,head.rc*257/256
    sqrt12,ln2=head.sqrt12,head.log2
    rho=(arb(11)/4*ln2).exp()
    M=density["cutoff"];k=ball(density["k"])
    rr={r["cell"]:r for r in density["rows"]}
    cc={r["cell"]:r for r in positive["cell_rows"]}
    bands=positive["bands"];count=len(bands)
    nu_lo=[arb(b["first_mode"]**2*(b["first_mode"]**2-1))/12 for b in bands]
    nu_hi=[arb(b["last_mode"]**2*(b["last_mode"]**2-1))/12 for b in bands]
    raw_out=[[[arb(0),arb(0)] for unused in bands] for kind in range(2)]
    worst=[[dict(value=arb(0),cell=None) for unused in bands] for kind in range(2)]

    def register(kind,index,value,n):
        if value>worst[kind][index]["value"]:
            worst[kind][index]=dict(value=value.upper(),cell=n)

    for n in range(224,args.physical_through,-1):
        r=rr[n];X=ball(r["canonical_total_envelope"]);B=ball(r["B"]);a=ball(r["Q_coefficient"])
        ml,mu,wl=(ball(r[key]) for key in ("mu_lower","mu_upper","w_lower"))
        C=ball(r["TV_log_w_upper"])+ball(r["normalized_width_upper"])
        vmax=X*(a*R**3+sqrt12*mu/(rc**4*wl))
        I=(R**4/(sqrt12*ml)*vmax*vmax*C).upper()
        drop=ball(r["tau_inner"])-ball(r["tau_outer"])
        gap=ball(r["reference_tau"])-ball(r["tau_inner"])
        for index,b in enumerate(bands):
            lo,hi=b["first_mode"],b["last_mode"]
            A=[[ball(z) for z in row] for row in cc[n]["positive_cell_matrices"][index]]
            for kind in range(2):
                intensity=I/nu_lo[index]
                if kind:
                    intensity*=16*(-lo*gap).exp()
                old=raw_out[kind][index]
                propagated=matvec(A,[old[0],old[1]/rho])
                emitted=[(A[i][1]*intensity).upper() for i in range(2)]
                inside=[propagated[i]+emitted[i] for i in range(2)]
                value=((1+hi)*(B*hi+hi*hi)/(a*X)*inside[0]+(1+hi)*nu_hi[index]/X*inside[1]).upper()
                register(kind,index,value,n)
                decay=(-lo*drop).exp()
                raw_out[kind][index]=[(decay*propagated[i]+emitted[i]).upper() for i in range(2)]
    # Convert actual canonical comparison state at node through+1 to physical |Bp|+|kappa|.
    boundary=args.physical_through+1
    previous=rr[boundary]
    B=ball(rr[args.physical_through]["B"])
    old_mu=ball(previous["mu_upper"])
    wport=(rho*ball(previous["mu_lower"])/R**7).lower()
    physical=[[arb(0) for unused in bands] for kind in range(2)]
    for kind in range(2):
        for index,b in enumerate(bands):
            hi=b["last_mode"];z=raw_out[kind][index]
            physical[kind][index]=(R**3*(B*hi+hi*hi)*z[0]+sqrt12*old_mu*nu_hi[index]/(rc**4*wport)*z[1]).upper()
    panel_count=0;cell_stats=[]
    for n in range(args.physical_through,11,-1):
        r=rr[n];X=ball(r["canonical_total_envelope"]);B=ball(r["B"]);a=ball(r["Q_coefficient"])
        mu=ball(r["mu_upper"]);gap=ball(r["reference_tau"])-ball(r["tau_inner"])
        bs=sqrt12*mu
        q=[max(arb(0),(1-arb(b["first_mode"])/B).upper()) for b in bands]
        residual_factor=[16*(-b["first_mode"]*gap).exp() for b in bands]
        start_count=panel_count;cell_max=[arb(0) for unused in bands]
        Jupper=arb(0);Jlower=arb(0)
        for segment in kernels.source_cell(n)["segments"]:
            for g in panels(head,segment,exact_q(F(args.log_span))):
                panel_count+=1
                wl,wu=g["w_lower"],g["w_upper"]
                vmax=X*(a*R**3+bs/(rc**4*wl))
                vmin=X*(a*rc**3+bs/(R**4*wu))
                amin=X*(a*rc**3/wu+bs/(R**4*wu**2))
                amax=X*(a*R**3/wl+bs/(rc**4*wl**2))
                cup=(g["TVlog"].upper()+(g["TVw"].upper()/8+head.alpha*g["dro"].upper())/rc).upper()
                clo=max(arb(0),g["TVlog"].lower())+g["dro"].lower()/(2*R)
                jlo=(clo*amin/k).lower()
                jhi=(cup*amax/k).upper()
                if not 0<=jlo<=jhi:
                    raise ArithmeticError("The positive chi integral was not enclosed")
                Jupper+=jhi;Jlower+=jlo
                for index,b in enumerate(bands):
                    lo,hi=b["first_mode"],b["last_mode"]
                    growth=(q[index]*g["down"]).exp().upper()
                    propagator=(q[index]*g["down"]-lo*jlo).exp().upper()
                    emission=(k*vmax*growth*(-(-lo*jhi).expm1())/lo).upper()
                    for kind in range(2):
                        source=emission*(residual_factor[index] if kind else 1)
                        inside=(growth*physical[kind][index]+source).upper()
                        value=((1+hi)*inside/vmin).upper()
                        register(kind,index,value,n)
                        if not kind and value>cell_max[index]:
                            cell_max[index]=value
                        physical[kind][index]=(propagator*physical[kind][index]+source).upper()
        cell_stats.append(dict(cell=n,panels=panel_count-start_count,
            chi_integral_lower=ball_record(Jlower),chi_integral_upper=ball_record(Jupper),
            density_log2_bounds=[ball_record(v.log()/ln2) for v in cell_max]))
        print(json.dumps(dict(event="physical_cell",cell=n,panels=panel_count,
            log2_first_band=cell_stats[-1]["density_log2_bounds"][0]["display"],
            seconds=time.monotonic()-began)),flush=True)
    result=dict(
        status="Ordered physical scalar majorants on the stated shallow cells; true positive canonical matrices on all deeper cells",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        physical_cells=[12,args.physical_through],log_panel_span=args.log_span,
        bands=[dict(first_mode=b["first_mode"],last_mode=b["last_mode"],
            gamma=ball_record(2*worst[0][i]["value"]),
            log2_gamma=ball_record((2*worst[0][i]["value"]).log()/ln2),
            gamma_worst_cell=worst[0][i]["cell"],
            low_source=ball_record(2*worst[1][i]["value"]),
            log2_low_source=ball_record((2*worst[1][i]["value"]).log()/ln2),
            source_worst_cell=worst[1][i]["cell"]) for i,b in enumerate(bands)],
        proof="The constructed tau rate contains B/r+abs(lambda)/B+chi. Its physical l1 logarithmic norm is <=max(0,1-m/B)*(-lambda)_+-m*chi. Since d=k*V*chi, the positive scalar panel source integral is <=k*Vmax*exp(q*down)*(1-exp(-m*chi_total))/m. Endpoint chi and monotone source variations are enclosed directly.",
        source_mean="The density is that of the complete R33 source and complete holonomy root.",
        omitted_extra_negative_term="The nonnegative m*eta/8192 damping is omitted, making the result an upper bound.",
        cell_stats=cell_stats,panel_count=panel_count,
        input_hashes=hashes,
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            [Path(__file__).name,"closure_real_head_source_enclosure.py","closure_real_linear_head_enclosure.py"]},
        radial_quadratures=0,new_fundamental_matrix_integrations=0,
        actual_complete_middle_closure_paid=False,
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    encoded=gzip.compress((json.dumps(result,indent=2)+"\n").encode(),mtime=0)
    if args.out.suffix!=".gz" or len(encoded)>=5_000_000:
        raise ValueError("Use a compressed output below the repository cap")
    args.out.write_bytes(encoded)
    print(json.dumps(dict(output=str(args.out),bands=[dict(first=b["first_mode"],last=b["last_mode"],
        log2_gamma=b["log2_gamma"]["display"],log2_source=b["log2_low_source"]["display"]) for b in result["bands"]],
        seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":
    main()

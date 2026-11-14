#!/usr/bin/env python3
"""Source-only ordered physical kernels, with zero incoming state per cell.

Companion to tail_r33_middle_ordered_physical: it retains the genuine
positive canonical matrices for subsequent whole-cell propagation by
exporting only local physical source responses and canonical end vectors.
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
from closure_real_head_source_enclosure import exact_q,ball_record
from closure_real_head_green_enclosure import load_json,ball
from closure_real_linear_head_enclosure import PositiveKernels
from tail_r33_middle_ordered_physical import SourceValues,panels


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--density",type=Path,required=True)
    p.add_argument("--positive",type=Path,required=True)
    p.add_argument("--ready",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--first-cell",type=int,default=12)
    p.add_argument("--last-cell",type=int,default=23)
    p.add_argument("--log-span",default="1/16")
    args=p.parse_args();ctx.prec=192;began=time.monotonic()
    docs,hashes={},{}
    for name in ("density","positive","ready"):
        path=getattr(args,name);docs[name],raw=load_json(path)
        hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,positive,ready=(docs[n] for n in ("density","positive","ready"))
    if not all(density["gates"].values()):
        raise ValueError("The physical envelope must be paid")
    if any(hashes[str(args.ready)] not in d["input_hashes"].values() for d in (density,positive)):
        raise ValueError("Source identity differs")
    if not 12<=args.first_cell<=args.last_cell<=23:
        raise ValueError("Use the shallow twelve real-source cells")
    head=SourceValues(ready);kernels=PositiveKernels(head,225,2048)
    rc,R=head.rc,head.rc*257/256
    root12,ln2=head.sqrt12,head.log2
    k=ball(density["k"])
    rr={r["cell"]:r for r in density["rows"]}
    bands=[(r["first_mode"],r["last_mode"]) for r in positive["bands"]]
    bands.extend([(2050,4096),(4098,8190)])
    rows=[];total_panels=0
    for n in range(args.first_cell,args.last_cell+1):
        r=rr[n];X=ball(r["canonical_total_envelope"]);B=ball(r["B"]);a=ball(r["Q_coefficient"])
        mu=ball(r["mu_upper"]);ml=ball(r["mu_lower"]);bs=root12*mu
        gap=ball(r["reference_tau"])-ball(r["tau_inner"])
        q=[max(arb(0),(1-arb(lo)/B).upper()) for lo,hi in bands]
        states=[arb(0) for unused in bands];maximum=[arb(0) for unused in bands]
        count=0
        for segment in kernels.source_cell(n)["segments"]:
            for g in panels(head,segment,exact_q(F(args.log_span))):
                count+=1
                wl,wu=g["w_lower"],g["w_upper"]
                vmax=X*(a*R**3+bs/(rc**4*wl))
                vmin=X*(a*rc**3+bs/(R**4*wu))
                amin=X*(a*rc**3/wu+bs/(R**4*wu**2))
                amax=X*(a*R**3/wl+bs/(rc**4*wl**2))
                cup=(g["TVlog"].upper()+(g["TVw"].upper()/8+head.alpha*g["dro"].upper())/rc).upper()
                clo=max(arb(0),g["TVlog"].lower())+g["dro"].lower()/(2*R)
                jlo=(clo*amin/k).lower();jhi=(cup*amax/k).upper()
                if not 0<=jlo<=jhi:
                    raise ArithmeticError("The chi integral lost its enclosure")
                for i,(lo,hi) in enumerate(bands):
                    growth=(q[i]*g["down"]).exp().upper()
                    propagator=(q[i]*g["down"]-lo*jlo).exp().upper()
                    emitted=(k*vmax*growth*(-(-lo*jhi).expm1())/lo).upper()
                    within=((growth*states[i]+emitted)/vmin).upper()
                    if within>maximum[i]:maximum[i]=within
                    states[i]=(propagator*states[i]+emitted).upper()
        endw=head.source_point(kernels.source_cell(n)["segments"][-1],arb(1))["w"]
        result=[]
        for i,(lo,hi) in enumerate(bands):
            nulo=arb(lo*lo*(lo*lo-1))/12
            endQ=(states[i]/(B*lo*rc**3)).upper()
            endZ=(R**4*endw.upper()/(root12*ml*nulo)*max(arb(1),arb(hi)/B)*states[i]).upper()
            gamma=(2*(1+hi)*maximum[i]).upper()
            result.append(dict(first_mode=lo,last_mode=hi,
                local_gamma=ball_record(gamma),log2_local_gamma=ball_record(gamma.log()/ln2),
                physical_norm_end=ball_record(states[i]),
                canonical_Q_end=ball_record(endQ),canonical_Xi_over_nu_end=ball_record(endZ),
                low_source_factor=ball_record(16*(-lo*gap).exp()),
                low_source_log2_peak=ball_record((gamma*16*(-lo*gap).exp()).log()/ln2)))
        rows.append(dict(cell=n,panels=count,bands=result))
        total_panels+=count
        print(json.dumps(dict(event="local_source",cell=n,panels=count,
            log2_gamma_first=result[0]["log2_local_gamma"]["display"],
            log2_gamma_last=result[-1]["log2_local_gamma"]["display"],
            seconds=time.monotonic()-began)),flush=True)
        kernels.release_cell(n)
    result=dict(status="Validated local ordered scalar source kernels; no incoming-state or full middle-window closure is asserted",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        bands=[dict(first_mode=a,last_mode=b) for a,b in bands],cell_rows=rows,
        physical_logarithmic_norm="max(0,1-m/B_n)*(-lambda)_+-m*chi after the constructed continuous strip cancels the two off-diagonal column sums",
        source_identity="d=k*V*chi; every physical source step uses its own interval, with zero initial state at the cell inner endpoint",
        end_coordinate_conversion="Q=p/(i*m*r^3); Xi/nu=r^4*w*(kappa+i*m*p)/(sqrt(12)*mu*nu)",
        extra_bands="The two bands above2048 have local physical kernels only; no unavailable deeper positive matrix is inferred.",
        input_hashes=hashes,
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            [Path(__file__).name,"tail_r33_middle_ordered_physical.py","closure_real_head_source_enclosure.py","closure_real_linear_head_enclosure.py"]},
        panel_count=total_panels,radial_quadratures=0,new_fundamental_integrations=0,
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        complete_middle_closure_paid=False)
    encoded=gzip.compress((json.dumps(result,indent=2)+"\n").encode(),mtime=0)
    if args.out.suffix!=".gz" or len(encoded)>=5_000_000:raise ValueError("Use a gzip output below5MB")
    args.out.write_bytes(encoded)
    print(json.dumps(dict(output=str(args.out),panels=total_panels,
        seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":
    main()

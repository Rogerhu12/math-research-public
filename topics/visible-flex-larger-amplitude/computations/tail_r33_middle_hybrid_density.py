#!/usr/bin/env python3
"""Combine actual canonical cell matrices and ordered physical local kernels.

Every minimum combines independent upper bounds on the same component.
The two upper middle bands use only their saved matrices on cells24..224;
their shallow propagation uses the separately saved physical kernels.
No new ODE, radial quadrature, or nonlinear solve is performed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import load_json, ball


def matvec(A, v):
    return [(A[i][0]*v[0]+A[i][1]*v[1]).upper() for i in range(2)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("density", "positive", "subhead", "local", "ready", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    docs, hashes={}, {}
    for name in ("density", "positive", "subhead", "local", "ready"):
        path=getattr(args,name);docs[name],raw=load_json(path)
        hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,positive,subhead,local,ready=(docs[n] for n in
        ("density", "positive", "subhead", "local", "ready"))
    ready_hash=hashes[str(args.ready)]
    for d in (density,positive,subhead,local):
        if ready_hash not in d["input_hashes"].values():
            raise ValueError("Real source identities differ")
    if hashes[str(args.density)] not in local["input_hashes"].values():
        raise ValueError("Local kernels use a different physical envelope")
    if not all(density["gates"].values()):
        raise ValueError("The physical envelope has unpaid gates")
    rc=exact_q(ready["rationalDeepModel"]["physicalParameters"]["rCuff"])
    R=rc*257/256;sqrt12=arb(12).sqrt();ln2=arb(2).log()
    rho=(arb(11)/4*ln2).exp()
    rr={r["cell"]:r for r in density["rows"]}
    cc={r["cell"]:r for r in positive["cell_rows"]}
    ss={r["cell"]:r for r in subhead["cell_rows"]}
    ll={r["cell"]:r for r in local["cell_rows"]}
    if sorted(rr)!=list(range(12,225)) or sorted(cc)!=sorted(rr):
        raise ValueError("The full-cell data must cover all213 cells")
    if sorted(ss)!=list(range(24,225)) or sorted(ll)!=list(range(12,24)):
        raise ValueError("The shallow and deep high-band ranges must meet exactly")
    subbands=[dict(first_mode=b[0],last_mode=b[1]) if isinstance(b,list) else b
        for b in subhead["bands"]]
    bands=positive["bands"]+subbands
    pairs=lambda x:[(b["first_mode"],b["last_mode"]) for b in x]
    if pairs(bands)!=pairs(local["bands"]):
        raise ValueError("Band endpoints differ")
    source_integrals={}
    for n,r in rr.items():
        X=ball(r["canonical_total_envelope"]);a=ball(r["Q_coefficient"])
        ml,mu,wl=(ball(r[k]) for k in ("mu_lower","mu_upper","w_lower"))
        C=ball(r["TV_log_w_upper"])+ball(r["normalized_width_upper"])
        vmax=X*(a*R**3+sqrt12*mu/(rc**4*wl))
        source_integrals[n]=(R**4*vmax*vmax*C/(sqrt12*ml)).upper()
    results=[]
    for index,band in enumerate(bands):
        lo,hi=band["first_mode"],band["last_mode"]
        nulo=arb(lo*lo*(lo*lo-1))/12
        nuhi=arb(hi*hi*(hi*hi-1))/12
        kinds={}
        for kind in ("density_operator","low_source_residual"):
            out=[arb(0),arb(0)];outR=arb(0);outB=None
            worst=arb(0);worst_cell=None;rows=[]
            for n in range(224,11,-1):
                r=rr[n];X=ball(r["canonical_total_envelope"])
                B=ball(r["B"]);a=ball(r["Q_coefficient"])
                ml,mu=(ball(r[k]) for k in ("mu_lower","mu_upper"))
                qweight=(1+hi)*(B*hi+hi*hi)/(a*X)
                zweight=(1+hi)*nuhi/X
                inner_w=(ml/R**7).lower()
                outer_w=(rho*mu/rc**7).upper()

                def physical(z, wlower):
                    return (R**3*(B*hi+hi*hi)*z[0]
                        +sqrt12*mu*nuhi/(rc**4*wlower)*z[1]).upper()

                incoming=[out[0],out[1]/rho]
                Rin=physical(incoming,inner_w)
                if outB is not None:
                    Rin=min(Rin,(max(arb(1),B/outB)*outR).upper())
                gap=ball(r["reference_tau"])-ball(r["tau_inner"])
                fac=arb(1) if kind=="density_operator" else 16*(-lo*gap).exp()
                drop=ball(r["tau_inner"])-ball(r["tau_outer"])
                decay=(-lo*drop).exp()
                A=None
                if index<len(positive["bands"]):
                    A=[[ball(z) for z in row] for row in cc[n]["positive_cell_matrices"][index]]
                elif n>=24:
                    j=index-len(positive["bands"])
                    A=[[ball(z) for z in row] for row in ss[n]["positive_cell_matrices"][j]]
                if A is not None:
                    prop=matvec(A,incoming)
                    own=[(A[i][1]*source_integrals[n]/nulo).upper() for i in range(2)]
                    incoming_peak=(qweight*prop[0]+zweight*prop[1]).upper()
                    source_peak=(qweight*own[0]+zweight*own[1]).upper()
                    hom_end=[(decay*z).upper() for z in prop]
                if n in ll:
                    loc=ll[n]["bands"][index]
                    local_peak=ball(loc["local_gamma"])/2
                    local_end=[ball(loc["canonical_Q_end"]),ball(loc["canonical_Xi_over_nu_end"])]
                    hom_peak=((1+hi)*Rin*ball(loc["homogeneous_peak_over_V"])).upper()
                    hom_R=(Rin*ball(loc["homogeneous_physical_end"])).upper()
                    physical_hom_end=[(hom_R/(B*lo*rc**3)).upper(),
                        (R**4*outer_w/(sqrt12*ml*nulo)*max(arb(1),arb(hi)/B)*hom_R).upper()]
                    if A is not None:
                        incoming_peak=min(incoming_peak,hom_peak)
                        source_peak=min(source_peak,local_peak)
                        own=[min(own[i],local_end[i]) for i in range(2)]
                        hom_end=[min(hom_end[i],physical_hom_end[i]) for i in range(2)]
                    else:
                        incoming_peak=hom_peak;source_peak=local_peak
                        own=local_end;hom_end=physical_hom_end
                    physical_end_R=(hom_R+fac*ball(loc["physical_norm_end"])).upper()
                elif A is None:
                    raise ValueError("A true cell bound is missing")
                combined=(incoming_peak+fac*source_peak).upper()
                if combined>worst:worst,worst_cell=combined,n
                out=[(hom_end[i]+fac*own[i]).upper() for i in range(2)]
                outer_wlower=(rho*ml/R**7).lower()
                outR=physical(out,outer_wlower)
                if n in ll:outR=min(outR,physical_end_R)
                outB=B
                rows.append(dict(cell=n,combined_bound=ball_record(combined),
                    log2_bound=ball_record(combined.log()/ln2),
                    own_source_bound=ball_record(fac*source_peak),
                    incoming_bound=ball_record(incoming_peak),
                    end_Q=ball_record(out[0]),end_Xi_over_nu=ball_record(out[1]),
                    end_physical_norm=ball_record(outR)))
            kinds[kind]=dict(bound=ball_record(2*worst),
                log2_bound=ball_record((2*worst).log()/ln2),worst_cell=worst_cell,rows=rows)
        results.append(dict(first_mode=lo,last_mode=hi,**kinds))
    result=dict(status="Rigorous middle-window linear density majorants; joint nonlinear block closure remains unpaid",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",bands=results,
        method="Independent canonical and ordered physical upper bounds are intersected componentwise, separately for homogeneous incoming states and local inhomogeneous sources. A third physical l1 endpoint bound is retained across interfaces.",
        physical_interface="Physical p,kappa are continuous; changing B multiplies the l1 bound by at most max(1,B_new/B_old). Canonical Xi/nu changes by1/rho.",
        frequency_scope="All even94..8190; high-subhead positive matrices are used only on cells24..224, physical local kernels only on cells12..23.",
        density_to_strong_norm="Twice the largest combined per-cell bound controls both separately maximized whole-head physical components.",
        input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        radial_integrations=0,new_fundamental_integrations=0,
        complete_middle_nonlinear_closure_paid=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=gzip.compress((json.dumps(result,indent=2)+"\n").encode(),mtime=0)
    if args.out.suffix!=".gz" or len(payload)>=5_000_000:raise ValueError("Use gzip below5MB")
    args.out.write_bytes(payload)
    print(json.dumps(dict(output=str(args.out),bands=[dict(first=b["first_mode"],last=b["last_mode"],
        log2_gamma=b["density_operator"]["log2_bound"]["display"],
        log2_source=b["low_source_residual"]["log2_bound"]["display"],
        worst_cell=b["density_operator"]["worst_cell"]) for b in results],
        elapsed_seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":
    main()

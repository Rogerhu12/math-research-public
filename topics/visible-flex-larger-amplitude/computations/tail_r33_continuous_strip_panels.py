#!/usr/bin/env python3
"""Enclose the actual continuous strip and physical source material on panels.

The real R26 endpoint radii anchor the same source profile.  Every panel
uses monotone source variations and positive bounds on the free radial
integrand; no new ODE or radial numerical quadrature is used.  The defined
strip is the original normalized positive-integral strip, not a replacement.
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
from tail_r33_middle_ordered_physical import SourceValues,source_interval


def record(x):
    d=ball_record(x)
    return {"lower":d["lower"],"upper":d["upper"]}


def intersect(x,y):
    lo=max(x.lower(),y.lower());hi=min(x.upper(),y.upper())
    if not lo<=hi:raise ArithmeticError("Certified real-radius enclosures do not intersect")
    return lo.union(hi)


def ratio_of_parts(p,q):
    lo=p.lower()/(p.lower()+q.upper())
    hi=p.upper()/(p.upper()+q.lower())
    return max(arb(0),lo.lower()).union(min(arb(1),hi.upper()))


def panels_with_positions(head,segment,span):
    stack=[(F(0),F(1),0)]
    while stack:
        a,b,level=stack.pop();g=source_interval(head,segment,a,b)
        if g["log_box"].upper()-g["log_box"].lower()>span:
            if level>=30:raise ArithmeticError("Source subdivision limit")
            mid=(a+b)/2;stack.append((mid,b,level+1));stack.append((a,mid,level+1));continue
        points=[exact_q(a)]+[x for x in segment["critical_points"] if x>exact_q(a) and x<exact_q(b)]+[exact_q(b)]
        slopes=[head.normal_slope(head.source_point(segment,x)["w"]) for x in points]
        curvature=sum((abs(y-x) for x,y in zip(slopes,slopes[1:])),arb(0))/8
        free_lo=(head.alpha*g["dro"].lower()/(1+g["w_upper"]**2)).lower()
        free_hi=(head.alpha*g["dro"].upper()/(1+g["w_lower"]**2)).upper()
        width=curvature+free_lo.union(free_hi)
        if not width>0:raise ArithmeticError("A physical panel width lost positivity")
        yield dict(segment=segment["j"],left=a,right=b,width=width,**g)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("density","columns","ready","out-prefix"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--first-cell",type=int,default=12)
    p.add_argument("--last-cell",type=int,default=23)
    p.add_argument("--log-span",default="1/16")
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    if not 12<=args.first_cell<=args.last_cell<=23:raise ValueError("Use the certified shallow deep-head cells")
    docs,hashes={},{}
    for name in ("density","columns","ready"):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,columns,ready=(docs[n] for n in ("density","columns","ready"))
    if not all(density["gates"].values()):raise ValueError("Physical envelope gates are unpaid")
    if hashes[str(args.ready)] not in density["input_hashes"].values() or hashes[str(args.columns)] not in density["input_hashes"].values():
        raise ValueError("Real source or real port radii differ")
    # The split column files carry arrays only.  Their exact file hash and
    # the ready hash are both bound by the already-paid density manifest.
    # An unsplit column package may additionally carry its own identity.
    if "input_hashes" in columns and hashes[str(args.ready)] not in columns["input_hashes"].values():
        raise ValueError("Column ports belong to a different real source")
    head=SourceValues(ready);kernels=PositiveKernels(head,225,2048)
    rr={r["cell"]:r for r in density["rows"]};cc={r["cell"]:r for r in columns["cell_rows"]}
    k=ball(density["k"]);M=density["cutoff"];span=exact_q(F(args.log_span));entries=[]
    sourcehashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
        [Path(__file__).name,"tail_r33_middle_ordered_physical.py","closure_real_head_source_enclosure.py","closure_real_linear_head_enclosure.py"]}
    for n in range(args.first_cell,args.last_cell+1):
        r=rr[n];X=ball(r["canonical_total_envelope"]);B=ball(r["B"]);a=ball(r["Q_coefficient"])
        mu_hi=ball(r["mu_upper"]);mu_lo=ball(r["mu_lower"]);bs=head.sqrt12*mu_hi
        rawpanels=[]
        for segment in kernels.source_cell(n)["segments"]:
            rawpanels.extend(panels_with_positions(head,segment,span))
        before=[arb(0)]
        for g in rawpanels:before.append(before[-1]+g["width"])
        after=[arb(0)]*(len(rawpanels)+1)
        for i in range(len(rawpanels)-1,-1,-1):after[i]=after[i+1]+rawpanels[i]["width"]
        inner,outer=ball(cc[n]["r_inner"]),ball(cc[n]["r_outer"])
        intersect(inner+before[-1],outer)
        total_material=arb(0);basepieces=[]
        for i,g in enumerate(rawpanels):
            rl=intersect(inner+before[i],outer-after[i])
            ru=intersect(inner+before[i+1],outer-after[i+1])
            radius=rl.lower().union(ru.upper())
            logdr=(ru/rl).log()
            if not logdr>0:raise ArithmeticError("Physical radial log increment is not strictly positive")
            wl,wu=g["w_lower"],g["w_upper"]
            vlo=(X*(a*radius.lower()**3+bs/(radius.upper()**4*wu))).lower()
            vhi=(X*(a*radius.upper()**3+bs/(radius.lower()**4*wl))).upper()
            alo=(X*(a*radius.lower()**3/wu+bs/(radius.upper()**4*wu**2))).lower()
            ahi=(X*(a*radius.upper()**3/wl+bs/(radius.lower()**4*wl**2))).upper()
            cmeasure=logdr+g["TVlog"]
            material=(cmeasure.lower()*alo).lower().union((cmeasure.upper()*ahi).upper())
            btau=(B+arb(4)/M)*logdr+(1/B+arb(1)/M)*g["TVlog"]+material/k
            if not material>0 or not btau>0:raise ArithmeticError("Positive source/strip material lost positivity")
            jfactor_lo=(X*(a*radius.lower()**7*wl/(head.sqrt12*mu_hi)+mu_hi/mu_hi)).lower()
            jfactor_hi=(X*(a*radius.upper()**7*wu/(head.sqrt12*mu_lo)+mu_hi/mu_lo)).upper()
            Jcan=(jfactor_lo*material.lower()).lower().union((jfactor_hi*material.upper()).upper())
            g.update(radius_left=rl,radius_right=ru,radius=radius,radial_log=logdr,
                V=vlo.union(vhi),V_over_w=alo.union(ahi),material=material,btau=btau,Jcan=Jcan)
            basepieces.append(btau);total_material+=material
        bprefix=[arb(0)]
        for b in basepieces:bprefix.append(bprefix[-1]+b)
        bsuffix=[arb(0)]*(len(basepieces)+1)
        for i in range(len(basepieces)-1,-1,-1):bsuffix[i]=bsuffix[i+1]+basepieces[i]
        total=bprefix[-1];tau_i=ball(r["tau_inner"]);tau_o=ball(r["tau_outer"]);drop=tau_i-tau_o
        rows=[];max_tau_width=arb(0)
        for i,g in enumerate(rawpanels):
            tl=tau_i-drop*ratio_of_parts(bprefix[i],bsuffix[i])
            tr=tau_i-drop*ratio_of_parts(bprefix[i+1],bsuffix[i+1])
            max_tau_width=max(max_tau_width,tl.upper()-tl.lower(),tr.upper()-tr.lower())
            rows.append(dict(segment=g["segment"],x_left=[g["left"].numerator,g["left"].denominator],
                x_right=[g["right"].numerator,g["right"].denominator],
                radius_left=record(g["radius_left"]),radius_right=record(g["radius_right"]),radius=record(g["radius"]),
                w=record(g["w_lower"].union(g["w_upper"])),V=record(g["V"]),V_over_w=record(g["V_over_w"]),
                log_w_variation=record(g["TVlog"]),log_w_down_variation=record(g["down"]),
                radial_log_increment=record(g["radial_log"]),material_cV_over_w=record(g["material"]),
                canonical_source_integral=record(g["Jcan"]),btau_integral=record(g["btau"]),
                btau_prefix_before=record(bprefix[i]),btau_prefix_after=record(bprefix[i+1]),
                tau_left=record(tl),tau_right=record(tr),tau_range=record(tr.lower().union(tl.upper()))))
        result=dict(status="True continuous-strip and pointwise source-material enclosures on the same real cell",
            author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",cell=n,log_span=args.log_span,panels=rows,
            btau_total=record(total),material_total=record(total_material),
            tau_inner=record(tau_i),tau_outer=record(tau_o),k=record(k),B=record(B),
            mu=record(mu_lo.union(mu_hi)),maximum_tau_endpoint_width=record(max_tau_width),
            strip_definition="tau(r)=tau_inner-(tau_inner-tau_outer)*integral_inner^r btau/integral_cell btau",
            btau_definition="(B+4/M)*dr/r+(1/B+1/M)*abs(d log w)+(cV/w)*dr/k, M=8192",
            material_definition="integral (1/r+abs(w_r/w))*V/w dr",
            canonical_definition="integral r^4*V*w/(sqrt(12)*mu) times the positive material (cV/w)dr; r^4*V*w/(sqrt(12)*mu)=Xbar*(a*r^7*w/(sqrt(12)*mu)+mu_upper/mu)",
            source_geometry="Physical widths use TV(w/sqrt(1+w^2))/8 + alpha*integral dr_o/(1+w^2); exact real port radius anchors intersect forward/backward width sums",
            no_new_ODE_or_radial_quadrature=True,input_hashes=hashes,source_hashes=sourcehashes,
            elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
        path=args.out_prefix.with_name(args.out_prefix.name+f'-cell{n:03d}.json.gz')
        if len(payload)>=5_000_000:raise ValueError("One source cell exceeded the repository cap")
        path.write_bytes(payload)
        entry=dict(cell=n,file=str(path),bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest(),panels=len(rows),
            maximum_tau_endpoint_width=ball_record(max_tau_width),elapsed_seconds=result["elapsed_seconds"])
        entries.append(entry);print(json.dumps(dict(event="cell",**entry)),flush=True)
        kernels.release_cell(n)
    summary=dict(status="Completed source-only panel export",author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        cells=entries,total_panels=sum(r["panels"] for r in entries),input_hashes=hashes,source_hashes=sourcehashes,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out=args.out_prefix.with_name(args.out_prefix.name+'-summary.json');out.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event="done",summary=str(out),panels=summary["total_panels"],seconds=summary["elapsed_seconds"],RSS_KiB=summary["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

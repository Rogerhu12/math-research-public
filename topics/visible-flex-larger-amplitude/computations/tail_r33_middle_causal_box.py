#!/usr/bin/env python3
"""Causal cell-by-cell middle-window source kernels and a nonlinear box probe.

Uses only saved rigorous source/matrix data, including the same minima as
the hybrid density tool.  Low46 is held fixed.  No low-feedback or infinite
window coupling is asserted by this probe.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,ball_record
from closure_real_head_green_enclosure import load_json,ball


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("density","positive","subhead","local","hybrid","ready","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--extra-positive",type=Path)
    p.add_argument("--z-log2",type=int,default=-2231)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    docs,hashes={},{}
    for name in ("density","positive","subhead","local","hybrid","ready","extra_positive"):
        path=getattr(args,name)
        if path is None:continue
        docs[name],raw=load_json(path);hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,positive,subhead,local,hybrid,ready=(docs[n] for n in
        ("density","positive","subhead","local","hybrid","ready"))
    readyhash=hashes[str(args.ready)];densityhash=hashes[str(args.density)]
    for name in ("density","positive","subhead","local"):
        if readyhash not in docs[name]["input_hashes"].values():
            raise ValueError("The certified real source differs")
    if densityhash not in local["input_hashes"].values() or densityhash not in hybrid["input_hashes"].values():
        raise ValueError("The physical density envelope differs")
    if not all(density["gates"].values()):raise ValueError("Unpaid density gates")
    pars=ready["rationalDeepModel"]["physicalParameters"]
    const=ready["rationalDeepModel"]["exactSourceConstants"]
    rc=exact_q(pars["rCuff"]);R=rc*257/256
    rt12=arb(12).sqrt();ln2=arb(2).log();rho=(arb(11)/4*ln2).exp()
    S=exact_q(pars["epsilonScale"])*(exact_q(Fraction(const["delta0"]))*arb(2)**-224)**(arb(11)/2)/rc**10
    rawcap=arb(2)**(1967+2*args.z_log2)
    normalize=lambda bs:[dict(first_mode=b[0],last_mode=b[1]) if isinstance(b,list) else b for b in bs]
    bands=normalize(positive["bands"])+normalize(subhead["bands"])
    pairs=lambda bs:[(b["first_mode"],b["last_mode"]) for b in bs]
    if pairs(bands)!=pairs(local["bands"]) or pairs(bands)!=pairs(hybrid["bands"]):
        raise ValueError("Frequency windows differ")
    rr={r["cell"]:r for r in density["rows"]};ll={r["cell"]:r for r in local["cell_rows"]}
    if sorted(rr)!=list(range(12,225)):raise ValueError("Need all213 cells")
    matrices={}
    for name in ("positive","subhead","extra_positive"):
        if name not in docs:continue
        d=docs[name]
        if readyhash not in d["input_hashes"].values():raise ValueError("Extra source identity differs")
        bp=pairs(normalize(d["bands"]))
        for row in d["cell_rows"]:
            for j,pair in enumerate(bp):
                key=(row["cell"],pair)
                A=[[ball(v) for v in a] for a in row["positive_cell_matrices"][j]]
                if key in matrices:raise ValueError("Overlapping saved positive matrix")
                matrices[key]=A
    cfg={}
    for bi,band in enumerate(bands):
        lo,hi=band["first_mode"],band["last_mode"]
        nulo=arb(lo*lo*(lo*lo-1))/12;nuhi=arb(hi*hi*(hi*hi-1))/12
        for n in range(12,225):
            r=rr[n];B=ball(r["B"]);X=ball(r["canonical_total_envelope"]);a=ball(r["Q_coefficient"])
            ml,mu,wl=(ball(r[k]) for k in ("mu_lower","mu_upper","w_lower"))
            qweight=(1+hi)*(B*hi+hi*hi)/(a*X);zweight=(1+hi)*nuhi/X
            yq=R**3*(B*hi+hi*hi)
            yin=rt12*mu*nuhi/(rc**4*(ml/R**7))
            yout=yin/rho
            I=(R**4/(rt12*ml)*(X*(a*R**3+rt12*mu/(rc**4*wl)))**2
                *(ball(r["TV_log_w_upper"])+ball(r["normalized_width_upper"]))).upper()
            A=matrices.get((n,(lo,hi)));localrow=ll[n]["bands"][bi] if n in ll else None
            decay=(-lo*(ball(r["tau_inner"])-ball(r["tau_outer"]))).exp()
            if A is not None:
                own=[(A[i][1]*I/nulo).upper() for i in range(2)]
                peak=(qweight*own[0]+zweight*own[1]).upper()
                ownR=(yq*own[0]+yout*own[1]).upper()
            if localrow is not None:
                localend=[ball(localrow["canonical_Q_end"]),ball(localrow["canonical_Xi_over_nu_end"])]
                localpeak=ball(localrow["local_gamma"])/2;localR=ball(localrow["physical_norm_end"])
                if A is None:own,peak,ownR=localend,localpeak,localR
                else:
                    own=[min(own[i],localend[i]) for i in range(2)]
                    peak=min(peak,localpeak);ownR=min(ownR,localR)
                hpeak=(1+hi)*ball(localrow["homogeneous_peak_over_V"])
                hend=ball(localrow["homogeneous_physical_end"])
                qconvert=1/(B*lo*rc**3)
                zconvert=R**4*(rho*mu/rc**7)/(rt12*ml*nulo)*max(arb(1),arb(hi)/B)
            else:
                if A is None:raise ValueError("Missing true cell kernel")
                hpeak=hend=qconvert=zconvert=None
            cfg[n,bi]=dict(B=B,A=A,decay=decay,qweight=qweight,zweight=zweight,
                yq=yq,yin=yin,yout=yout,own=own,ownR=ownR,peak=peak,
                hpeak=hpeak,hend=hend,qconvert=qconvert,zconvert=zconvert)

    def propagate(n,bi,state,oldB):
        c=cfg[n,bi];Q,Z,Y=state;inp=[Q,Z/rho]
        Rin=(c["yq"]*inp[0]+c["yin"]*inp[1]).upper()
        if oldB is not None:Rin=min(Rin,(max(arb(1),c["B"]/oldB)*Y).upper())
        A=c["A"]
        if A is not None:
            prop=[(A[i][0]*inp[0]+A[i][1]*inp[1]).upper() for i in range(2)]
            peak=(c["qweight"]*prop[0]+c["zweight"]*prop[1]).upper()
            end=[(c["decay"]*v).upper() for v in prop]
        if c["hpeak"] is not None:
            localpeak=(c["hpeak"]*Rin).upper();endR=(c["hend"]*Rin).upper()
            localend=[(c["qconvert"]*endR).upper(),(c["zconvert"]*endR).upper()]
            if A is None:peak,end=localpeak,localend
            else:peak=min(peak,localpeak);end=[min(end[i],localend[i]) for i in range(2)]
        Yout=(c["yq"]*end[0]+c["yout"]*end[1]).upper()
        if c["hpeak"] is not None:Yout=min(Yout,endR)
        return (end[0],end[1],Yout),peak

    gamma={(n,j):arb(0) for n in range(12,225) for j in range(n,225)}
    argmax={k:None for k in gamma};far={n:arb(0) for n in range(12,225)}
    for bi,b in enumerate(bands):
        for j in range(224,11,-1):
            c=cfg[j,bi];state=(c["own"][0],c["own"][1],c["ownR"])
            peak=2*c["peak"]
            if peak>gamma[j,j]:gamma[j,j]=peak.upper();argmax[j,j]=bi
            oldB=c["B"]
            for n in range(j-1,11,-1):
                state,peak=propagate(n,bi,state,oldB);oldB=cfg[n,bi]["B"]
                if 2*peak>gamma[n,j]:gamma[n,j]=(2*peak).upper();argmax[n,j]=bi
        lo=b["first_mode"];nulo=arb(lo*lo*(lo*lo-1))/12
        amp=(S*rawcap*(-lo*(38-ball(rr[224]["tau_inner"]))).exp()).upper()
        # propagate() inserts an outward Xi interface.  There is no such
        # interface at the initial far endpoint, so compensate exactly here.
        state=(amp,rho*amp/nulo,arb(0));oldB=None
        for n in range(224,11,-1):
            state,peak=propagate(n,bi,state,oldB);oldB=cfg[n,bi]["B"]
            far[n]=(far[n]+2*peak).upper()
        print(json.dumps(dict(event="band",first=lo,last=b["last_mode"],
            seconds=time.monotonic()-started)),flush=True)
    residual={n:far[n] for n in far}
    for b in hybrid["bands"]:
        for row in b["low_source_residual"]["rows"]:
            n=row["cell"];residual[n]=(residual[n]+2*ball(row["combined_bound"])).upper()
    radii={};fail=None;map_slack={}
    for n in range(224,11,-1):
        a=64*gamma[n,n]
        c=residual[n]+sum((64*gamma[n,j]*radii[j]*(1+radii[j]) for j in range(n+1,225)),arb(0))
        b=1-a;disc=b*b-4*a*c
        if not b>0 or not disc>0:
            fail=dict(cell=n,diagonal=ball_record(a),constant=ball_record(c),discriminant=ball_record(disc));break
        small=(2*c/(b+disc.sqrt())).upper()
        radius=(small*arb(101)/100+arb(2)**-10000).upper()
        phi=(c+a*radius*(1+radius)).upper()
        if not phi<radius:
            fail=dict(cell=n,reason="Rounded padded root did not give strict invariance",radius=ball_record(radius),image=ball_record(phi));break
        radii[n]=radius;map_slack[n]=(radius-phi).lower()
    domain={n:(ball(rr[n]["V_over_w_upper"])*(1+r)).upper() for n,r in radii.items()}
    mean_pass=all(v<arb(1)/64 for v in domain.values()) and fail is None
    weights={};lip=None
    if fail is None:
        target=arb(3)/4
        for n in range(224,11,-1):
            diag=64*gamma[n,n]*(1+2*radii[n])
            if not diag<target:fail=dict(cell=n,reason="Diagonal Lipschitz exceeds target");break
            rhs=sum((64*gamma[n,j]*(1+2*radii[j])*weights[j] for j in range(n+1,225)),arb(0))
            weights[n]=max(radii[n],(arb(101)/100*rhs/(target-diag)).upper(),arb(2)**-10000)
        if fail is None:
            lip=max((sum((64*gamma[n,j]*(1+2*radii[j])*weights[j] for j in range(n,225)),arb(0))/weights[n]).upper() for n in range(12,225))
    cells=[]
    for n in range(12,225):
        row=dict(cell=n,low_plus_far_residual=ball_record(residual[n]),far_boundary=ball_record(far[n]),
            diagonal_gamma=ball_record(gamma[n,n]))
        if n in radii:row.update(radius=ball_record(radii[n]),map_slack=ball_record(map_slack[n]),mean_domain=ball_record(domain[n]))
        if n in weights:row["metric_weight"]=ball_record(weights[n])
        cells.append(row)
    result=dict(status="Finite middle-window causal box with low46 held fixed; infinite-window and low feedback still unpaid",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",bands=[dict(first_mode=b["first_mode"],last_mode=b["last_mode"]) for b in bands],
        gamma_rows=[dict(output_cell=n,sources=[dict(source_cell=j,gamma=ball_record(gamma[n,j]),maximizing_band=argmax[n,j]) for j in range(n,225)]) for n in range(12,225)],
        cells=cells,z_log2=args.z_log2,far_normalized_raw_bound=ball_record(rawcap),
        box_formula="r_n >= low_source_n+far_n+64*sum_{j>=n}Gamma_nj*r_j*(1+r_j); Gamma_nj is the maximum of the eleven true mode-band operator bounds",
        gates=dict(causal_box=fail is None,complete_mean_domain=mean_pass,
            weighted_lipschitz=lip is not None and lip<arb(3)/4),
        weighted_lipschitz=ball_record(lip) if lip is not None else None,failure=fail,
        low46_held_fixed=True,infinite_window_unknown_included=False,complete_head_closed=False,
        input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if args.out.suffix!='.gz' or len(encoded)>=5_000_000:raise ValueError("Use gzip below5MB")
    args.out.write_bytes(encoded)
    summary=dict(output=str(args.out),bytes=len(encoded),gates=result["gates"],failure=fail,
        weighted_lipschitz=result["weighted_lipschitz"],
        maximum_radius_log2=ball_record(max(radii.values()).log()/ln2) if radii else None,
        elapsed_seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])
    print(json.dumps(summary),flush=True)


if __name__=="__main__":main()

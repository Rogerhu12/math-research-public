#!/usr/bin/env python3
"""Read-only positive-cell majorants for the R33 middle source window.

The source is integrated at its own cell. Whole positive cell matrices
bound ordered partial products; their excess can make these bounds fail.
No missing frequency band is extrapolated and no ODE is integrated here.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import load_json, ball


def matvec(A,v):
    return [(A[i][0]*v[0]+A[i][1]*v[1]).upper() for i in range(2)]


def rowmat(v,A):
    return [(v[0]*A[0][j]+v[1]*A[1][j]).upper() for j in range(2)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--density",type=Path,required=True)
    p.add_argument("--positive",type=Path,required=True)
    p.add_argument("--ready",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    ctx.prec=192
    started=time.monotonic()
    ds,hashes={},{}
    for name in ("density","positive","ready"):
        path=getattr(args,name);ds[name],raw=load_json(path)
        hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,positive,ready=(ds[k] for k in ("density","positive","ready"))
    if not all(density["gates"].values()):
        raise ValueError("The chosen physical envelope has not been paid")
    ready_hash=hashes[str(args.ready)]
    if any(ready_hash not in d["input_hashes"].values() for d in (density,positive)):
        raise ValueError("The source packages differ")
    rc=exact_q(ready["rationalDeepModel"]["physicalParameters"]["rCuff"])
    R=rc*257/256;sqrt12=arb(12).sqrt();ln2=arb(2).log()
    rho=(arb(11)/4*ln2).exp()
    rr={r["cell"]:r for r in density["rows"]}
    cc={r["cell"]:r for r in positive["cell_rows"]}
    if sorted(rr)!=list(range(12,225)) or sorted(cc)!=list(rr):
        raise ValueError("All 213 cells must agree")
    sources={}
    for n,r in rr.items():
        X=ball(r["canonical_total_envelope"]);a=ball(r["Q_coefficient"])
        ml=ball(r["mu_lower"]);mu=ball(r["mu_upper"]);wl=ball(r["w_lower"])
        C=ball(r["TV_log_w_upper"])+ball(r["normalized_width_upper"])
        vmax=X*(a*R**3+sqrt12*mu/(rc**4*wl))
        sources[n]=(R**4/(sqrt12*ml)*vmax*vmax*C).upper()
    results=[]
    for index,band in enumerate(positive["bands"]):
        lo,hi=band["first_mode"],band["last_mode"]
        nu_lo=arb(lo*lo*(lo*lo-1))/12
        nu_hi=arb(hi*hi*(hi*hi-1))/12
        matrices={n:[[ball(z) for z in row] for row in cc[n]["positive_cell_matrices"][index]] for n in rr}
        outputs={}
        for kind in ("density_operator","low_source_residual"):
            out=[arb(0),arb(0)];worst=(arb(0),None);rows=[]
            for n in range(224,11,-1):
                r=rr[n];X=ball(r["canonical_total_envelope"]);B=ball(r["B"]);a=ball(r["Q_coefficient"])
                incoming=[out[0],out[1]/rho]
                propagated=matvec(matrices[n],incoming)
                intensity=sources[n]/nu_lo
                gap=ball(r["reference_tau"])-ball(r["tau_inner"])
                if kind=="low_source_residual":
                    intensity*=16*(-lo*gap).exp()
                emitted=[(matrices[n][i][1]*intensity).upper() for i in range(2)]
                inside=[propagated[i]+emitted[i] for i in range(2)]
                Qweight=(1+hi)*(B*hi+hi*hi)/(a*X)
                Xiweight=(1+hi)*nu_hi/X
                combined=(Qweight*inside[0]+Xiweight*inside[1]).upper()
                if combined>worst[0]:
                    worst=(combined,n)
                drop=ball(r["tau_inner"])-ball(r["tau_outer"])
                decay=(-lo*drop).exp()
                out=[(decay*propagated[i]+emitted[i]).upper() for i in range(2)]
                rows.append(dict(cell=n,combined_component_bound=ball_record(combined),
                    log2_bound=ball_record(combined.log()/ln2)))
            outputs[kind]=dict(
                bound=ball_record(2*worst[0]),
                log2_bound=ball_record((2*worst[0]).log()/ln2),
                worst_cell=worst[1],
                bound_scope="Twice the maximum cell combined bound covers the two separate whole-head component suprema.",
                rows=rows)
        # Attribute the density majorant at its worst output cell to each source cell.
        target=outputs["density_operator"]["worst_cell"]
        r=rr[target];X=ball(r["canonical_total_envelope"]);B=ball(r["B"]);a=ball(r["Q_coefficient"])
        weights=[(1+hi)*(B*hi+hi*hi)/(a*X),(1+hi)*nu_hi/X]
        adj=rowmat(weights,matrices[target])
        contributions=[]
        for n in range(target,225):
            if n>target:
                adj=[adj[0],(adj[1]/rho).upper()]
                adj=rowmat(adj,matrices[n])
            contribution=(adj[1]*sources[n]/nu_lo).upper()
            contributions.append((contribution,n))
            if n>target:
                drop=ball(rr[n]["tau_inner"])-ball(rr[n]["tau_outer"])
                factor=(-lo*drop).exp()
                adj=[(z*factor).upper() for z in adj]
        contributions.sort(key=lambda z:float(z[0].log()/ln2),reverse=True)
        results.append(dict(first_mode=lo,last_mode=hi,**outputs,
            dominant_source_cells=[dict(cell=n,combined_bound=ball_record(v),
                log2_bound=ball_record(v.log()/ln2)) for v,n in contributions[:8]]))
    result=dict(
        status="Valid but insufficient whole-positive-cell density majorants; this is not an instability certificate",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        bands=results, last_available_frequency=positive["bands"][-1]["last_mode"],
        high_cutoff=density["cutoff"],
        source_formula="I_n >= integral r^4*w/(sqrt(12)*mu_n) * d(r) dr",
        source_bounds=[dict(cell=n,canonical_source_integral=ball_record(v)) for n,v in sources.items()],
        ordered_recursion="Inside_n=C_n*J*out_(n+1)+C_n*(0,I_n/nu_lo); out_n=exp(-lo*Delta_tau_n)*C_n*J*out_(n+1)+C_n*(0,I_n/nu_lo). The own-cell source receives no invented endpoint strip loss.",
        low_residual_formula="Own-cell input additionally multiplied by 16*exp(-lo*(tau_reference_n-tau_inner_n)); the complete mean and pointwise inverse are already included in R33.",
        reason_bound_valid="Positive comparison matrices have diagonal entries >=1 and nonnegative off-diagonal entries, so a whole-cell positive majorant bounds each ordered partial product. Real canonical Xi changes by 1/rho at an outward interface.",
        actual_middle_closure_paid=False,
        modes_above_available_data_inferred=False,
        input_hashes=hashes,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=[
            "The result encloses a calculated upper majorant, not a lower bound on the actual operator.",
            "Whole-cell majorants combine source and amplification locations too coarsely.",
            "The saved positive matrices stop at 2048; 2050..8190 are not covered by them.",
            "The independent rigorously paid m>=8192 window is unchanged."])
    import gzip
    encoded=gzip.compress((json.dumps(result,indent=2)+"\n").encode(),mtime=0)
    if args.out.suffix!=".gz" or len(encoded)>=5_000_000:
        raise ValueError("A gzip output below the single-file repository cap is required")
    args.out.write_bytes(encoded)
    print(json.dumps(dict(output=str(args.out),
        bands=[dict(first=r["first_mode"],last=r["last_mode"],
            log2_gamma=r["density_operator"]["log2_bound"]["display"],
            log2_source=r["low_source_residual"]["log2_bound"]["display"],
            worst_source=r["dominant_source_cells"][0]["cell"]) for r in results],
        elapsed_seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])))


if __name__=="__main__":
    main()

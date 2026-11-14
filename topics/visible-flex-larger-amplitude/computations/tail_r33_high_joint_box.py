#!/usr/bin/env python3
"""Join the finite middle causal box to the complete infinite high window.

Low46 remains fixed in its certified plateau box.  Both high blocks use
the same continuous strip and the complete pointwise source/mean root.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_real_head_source_enclosure import ball_record
from closure_real_head_green_enclosure import load_json,ball


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("density","middle","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--infinite-radius-log2",type=int,default=-90)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    density,draw=load_json(args.density);middle,mraw=load_json(args.middle)
    dhash=hashlib.sha256(draw).hexdigest()
    if dhash not in middle["input_hashes"].values():raise ValueError("Different physical envelope")
    if not all(density["gates"].values()) or not all(middle["gates"].values()):
        raise ValueError("Use only successfully paid constituent blocks")
    cells=list(range(12,225));N=len(cells);ln2=arb(2).log()
    rows={r["cell"]:r for r in middle["cells"]}
    dr={r["cell"]:r for r in density["rows"]}
    gamma={(r["output_cell"],s["source_cell"]):ball(s["gamma"])
        for r in middle["gamma_rows"] for s in r["sources"]}
    ghi=ball(density["gamma_high"]);h=arb(2)**args.infinite_radius_log2
    rawcap=ball(middle["far_normalized_raw_bound"])
    deep=(ball(density["far_high_lift_bound"])*rawcap).upper()
    base=(16*N*ghi*(-density["cutoff"]*ball(density["buffer"])).exp()).upper()
    radii={};slacks={};fail=None
    for n in reversed(cells):
        a=64*gamma[n,n]
        c=(ball(rows[n]["low_plus_far_residual"])+a*h*(1+h)
            +sum((64*gamma[n,j]*(radii[j]+h)*(1+radii[j]+h) for j in range(n+1,225)),arb(0)))
        b=1-a*(1+2*h);disc=b*b-4*a*c
        if not b>0 or not disc>0:
            fail=dict(cell=n,reason="No small positive quadratic majorant root",constant=ball_record(c),discriminant=ball_record(disc));break
        small=(2*c/(b+disc.sqrt())).upper()
        r=(arb(101)/100*small+arb(2)**-10000).upper()
        image=(c+a*(1+2*h)*r+a*r*r).upper()
        if not image<r:
            fail=dict(cell=n,reason="Padded radius did not give strict inclusion");break
        radii[n]=r;slacks[n]=(r-image).lower()
    infimage=None;weights={};row_sums={};inflip=None
    if fail is None:
        infimage=(deep+base+64*ghi*sum(((radii[n]+h)*(1+radii[n]+h) for n in cells),arb(0))).upper()
        target=arb(3)/4
        # Fix the infinite-block distance weight at1.  Solve a triangular
        # positive supersolution for all213 middle distance weights.
        for n in reversed(cells):
            d=64*gamma[n,n]*(1+2*(radii[n]+h))
            row_inf=sum((64*gamma[n,j]*(1+2*(radii[j]+h)) for j in range(n,225)),arb(0))
            rhs=row_inf+sum((64*gamma[n,j]*(1+2*(radii[j]+h))*weights[j] for j in range(n+1,225)),arb(0))
            if not d<target:
                fail=dict(cell=n,reason="Local derivative exceeds requested metric target");break
            weights[n]=max((arb(101)/100*rhs/(target-d)).upper(),arb(2)**-10000)
        if fail is None:
            for n in cells:
                row_sums[n]=(sum((64*gamma[n,j]*(1+2*(radii[j]+h))*(weights[j]+1)
                    for j in range(n,225)),arb(0))/weights[n]).upper()
            inflip=(64*ghi*sum(((1+2*(radii[n]+h))*(weights[n]+1) for n in cells),arb(0))).upper()
    mean={n:(ball(dr[n]["V_over_w_upper"])*(1+radii[n]+h)).upper() for n in radii}
    gates=dict(middle_invariance=fail is None,infinite_invariance=infimage is not None and infimage<h,
        complete_mean_domain=fail is None and all(v<arb(1)/64 for v in mean.values()),
        middle_metric=bool(row_sums) and max(row_sums.values())<arb(3)/4,
        infinite_metric=inflip is not None and inflip<arb(3)/4)
    outrows=[]
    for n in cells:
        r=dict(cell=n)
        if n in radii:r.update(middle_radius=ball_record(radii[n]),map_slack=ball_record(slacks[n]),mean_domain=ball_record(mean[n]))
        if n in weights:r["middle_metric_weight"]=ball_record(weights[n])
        if n in row_sums:r["weighted_derivative_row"]=ball_record(row_sums[n])
        outrows.append(r)
    result=dict(status="Joint complete high-mode box, conditional on a fixed low46 field in its paid plateau domain",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        high_modes="Every even Fourier mode >=94, including all >=8192 without truncation",
        low46_held_fixed=True,low_feedback_paid=False,whole_head_closed=False,
        infinite_radius=ball_record(h),infinite_image=ball_record(infimage) if infimage is not None else None,
        infinite_metric_weight=1,infinite_weighted_derivative_row=ball_record(inflip) if inflip is not None else None,
        deep_high_boundary=ball_record(deep),wide_low_infinite_residual=ball_record(base),
        z_log2=middle["z_log2"],gates=gates,failure=fail,rows=outrows,
        map_formula="Middle: b_n+64 sum_{j>=n}Gamma_nj(r_j+h)(1+r_j+h). Infinite: b_inf+16*N*gamma_inf*exp(-8192/8)+64*gamma_inf*sum_j(r_j+h)(1+r_j+h).",
        norm_justification="Each low cell has physical strong norm<=1 on tau+1/8. A whole-head source norm is at most the sum of its213 local source norms. No strip loss is charged to either unknown high block; only the fixed low residual uses the existing buffer.",
        derivative_formula="Middle derivative64 Gamma_nj(1+2(r_j+h)), infinite derivative64 gamma_inf(1+2(r_j+h)); the infinite-input column sums these coefficients over all source cells.",
        full_mean_and_pointwise_inverse=True,
        input_hashes={str(args.density):dhash,str(args.middle):hashlib.sha256(mraw).hexdigest()},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),gates=gates,failure=fail,
        max_middle_radius_log2=ball_record(max(radii.values()).log()/ln2) if radii else None,
        infinite_image_log2=ball_record(infimage.log()/ln2) if infimage is not None else None,
        infinite_derivative=result["infinite_weighted_derivative_row"],
        middle_derivative=ball_record(max(row_sums.values())) if row_sums else None,
        seconds=result["elapsed_seconds"],RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

#!/usr/bin/env python3
"""Pay the low46 variation to the complete high fixed-point-map column.

The wide pure-low derivative is separated from the high-dependent
derivative by a complex Cauchy circle.  This avoids assigning a second
analytic strip to the unknown high field.  The actual full far graph
derivative is included, with the low metric's saved far evaluation norm.
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
    for name in ("density","middle","joint","low-box","low-far","out"):
        p.add_argument("--"+name,type=Path,required=True)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    docs,hashes={},{}
    for name in ("density","middle","joint","low_box","low_far"):
        path=getattr(args,name);docs[name],raw=load_json(path)
        hashes[str(path)]=hashlib.sha256(raw).hexdigest()
    density,middle,joint,low,far=(docs[n] for n in ("density","middle","joint","low_box","low_far"))
    if not all(density["gates"].values()) or not all(joint["gates"].values()) or not all(low["gates"].values()) or not all(far["gates"].values()):
        raise ValueError("Use paid constituent domains")
    dh=hashes[str(args.density)]
    if dh not in joint["input_hashes"].values() or dh not in middle["input_hashes"].values():
        raise ValueError("High physical envelopes differ")
    if hashes[str(args.low_box)] not in density["input_hashes"].values():
        raise ValueError("The chosen low box did not define this V")
    if hashes[str(args.low_box)] not in far["input_hashes"].values():
        raise ValueError("The far low metric differs")
    if far["far_z_dyadic_bound"]!=f'2^{joint["z_log2"]}':
        raise ValueError("The far graph parameter domains differ")
    rr={r["cell"]:r for r in density["rows"]};lr={r["cell"]:r for r in low["rows"]}
    jr={r["cell"]:r for r in joint["rows"]};mr={r["cell"]:r for r in middle["cells"]}
    ns=list(range(12,225));ln2=arb(2).log()
    gamma={(r["output_cell"],s["source_cell"]):ball(s["gamma"])
        for r in middle["gamma_rows"] for s in r["sources"]}
    dn={n:(ball(lr[n]["metric_weight_multiple"])/ball(lr[n]["total_radius_multiple"])).upper() for n in ns}
    dmax=max(dn.values());h=ball(joint["infinite_radius"])
    t={n:(ball(jr[n]["middle_radius"])+h).upper() for n in ns}
    cauchy_gate=all(t[n]<=1 and ball(rr[n]["V_over_w_upper"])*(2+t[n])<arb(1)/64 for n in ns)
    if not cauchy_gate:raise ValueError("The complex Cauchy circles leave the complete-mean domain")
    z=arb(2)**joint["z_log2"];far_factor=(4*ball(far["eD"])/z).upper()
    records=[];worst=arb(0);worst_cell=None
    for n in ns:
        lowres=(ball(jr[n]["refined_low_residual"]) if "refined_low_residual" in jr[n]
            else ball(mr[n]["low_plus_far_residual"]))
        pure=(4*dmax*lowres).upper()
        mixed=(160*sum((gamma[n,j]*t[j]*dn[j] for j in range(n,225)),arb(0))).upper()
        boundary=(ball(mr[n]["far_boundary"])*far_factor).upper()
        value=(pure+mixed+boundary).upper()
        weighted=(value/ball(jr[n]["middle_metric_weight"])).upper()
        if weighted>worst:worst,worst_cell=weighted,n
        records.append(dict(cell=n,low_metric_to_local_physical=ball_record(dn[n]),
            pure_low_derivative=ball_record(pure),high_dependent_derivative=ball_record(mixed),
            true_far_derivative=ball_record(boundary),total=ball_record(value),
            high_weighted_column=ball_record(weighted)))
    ghi=ball(density["gamma_high"])
    pure_inf=(64*ghi*sum(dn.values(),arb(0))*(-density["cutoff"]*ball(density["buffer"])).exp()).upper()
    mixed_inf=(160*ghi*sum((t[n]*dn[n] for n in ns),arb(0))).upper()
    far_inf=(ball(joint["deep_high_boundary"])*far_factor).upper()
    inf=(pure_inf+mixed_inf+far_inf).upper()
    total=max(worst,inf)
    high_lip=max(max(ball(r["weighted_derivative_row"]) for r in joint["rows"]),
        ball(joint["infinite_weighted_derivative_row"]))
    solution_lip=(total/(1-high_lip)).upper()
    result=dict(status="Paid low46-to-complete-high map and implicit response Lipschitz columns; reverse low feedback remains independent",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        low_metric="max_n X_tau_ref_n(delta L)/(W_n*X_reference_n); W is dimensionless, hence local physical derivative <=W_n/U_n",
        high_metric="The213 middle weights and unit infinite weight in the stated successful joint high box",
        cauchy_proof="At a fixed cell, a complex low circle of radius1/d_n has norm<=2. Cauchy gives ||Df(L)delta L||_wide<=64d_n. For F(z)=f(L+H+z delta L)-f(L+z delta L), R33 Lipschitz gives ||F||<=32(4+t_n)t_n<=160t_n, hence ||F'(0)||<=160t_n*d_n in the original narrow strip.",
        far_derivative_proof="The saved high boundary lift already uses C_D*z_*^2. Multiply it by4*eD/z_* to get the complete D'(z)*delta z lift, using the SAME low metric eD.",
        complex_mean_domain_paid=cauchy_gate,rows=records,
        infinite_column=dict(pure_low=ball_record(pure_inf),high_dependent=ball_record(mixed_inf),far=ball_record(far_inf),total=ball_record(inf)),
        high_map_column=ball_record(total),log2_high_map_column=ball_record(total.log()/ln2),
        worst_middle_cell=worst_cell,high_response_column=ball_record(solution_lip),log2_high_response_column=ball_record(solution_lip.log()/ln2),
        high_self_contraction=ball_record(high_lip),low_to_high_paid=True,high_to_low_paid=False,full_head_closed=False,
        input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),log2_map=result["log2_high_map_column"],
        log2_response=result["log2_high_response_column"],worst_cell=worst_cell,
        seconds=result["elapsed_seconds"],RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()

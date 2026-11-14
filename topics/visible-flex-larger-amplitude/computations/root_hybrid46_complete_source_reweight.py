#!/usr/bin/env python3
"""Consume all46 original R83 positive source pieces using proved R100 bounds.

Prepared entry: this file has not been executed or AST checked yet. It reads
whole originals only on the local filesystem, writes one complete output, and
never changes the R97 successful original or its recovered entry.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

EXPECTED = {
 "r83":"4ec6d30adb9eb639e658bcaa86873cfed0675ab975d3a8f92778888339f966b2",
 "r100":"7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9",
 "far":"6ee19d3288cd6d8662eecbc7d72e83d59245383798c6a066d8c9160c432ea4dd",
 "trace":"44db92699bd9bf3d8ba613465b013033c82a7ed9f8fc8e5cc1f6a003539ad494",
 "r78":"9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930",
}
def p2(e):
    return F(1 << e) if e >= 0 else F(1, 1 << (-e))

def upper(x):
    if isinstance(x, bool):
        raise TypeError("Boolean is not a mathematical bound")
    if isinstance(x, (int, str)):
        return F(x)
    if not isinstance(x, dict):
        raise TypeError("Use exact fraction or dyadic records, never floats")
    if "upper" in x:
        return upper(x["upper"])
    if "numerator" in x and "denominator" in x:
        return F(int(x["numerator"]), int(x["denominator"]))
    if "mantissa" in x and "binary_exponent" in x:
        return F(int(x["mantissa"])) * p2(int(x["binary_exponent"]))
    raise ValueError("Unrecognized exact bound record")

def up(x, bits=192):
    x = F(x)
    if x < 0:
        raise ValueError("R97 positive arithmetic only")
    if not x:
        return F(0)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < p2(e):
        e -= 1
    quantum = p2(e - bits + 1)
    y = x / quantum
    return ((y.numerator + y.denominator - 1) // y.denominator) * quantum

def record(x):
    v = up(x)
    den = v.denominator
    if den & (den - 1):
        raise ArithmeticError("Directed result is not dyadic")
    with localcontext() as ctx:
        ctx.prec = 28
        ctx.rounding = ROUND_CEILING
        shown = str(Decimal(v.numerator) / Decimal(den))
    return {"upper": {"mantissa": str(v.numerator),
                      "binary_exponent": -(den.bit_length()-1)},
            "display_upward": shown}

def cauchy(x):
    return {"uniform_value_upper": record(x),
            "first_derivative_product_norm_upper": record(4*x),
            "second_derivative_product_norm_pair_upper": record(64*x)}

def digest_bytes(b):
    return hashlib.sha256(b).hexdigest()

def read_verified(path, wanted):
    b = path.read_bytes()
    sha = digest_bytes(b)
    if sha != wanted:
        raise ValueError("Pinned complete input changed: " + str(path))
    d = json.loads(b, parse_float=str)
    if d.get("all_gates") is not True:
        raise ValueError("Prerequisite did not pass all gates: " + str(path))
    return d, {"path": str(path), "sha256": sha, "bytes": len(b)}


def exp_upper(x, terms=64):
    x = F(x)
    if not 0 <= x < terms+2:
        raise ValueError("The complete positive exponential tail is not geometric")
    term = total = F(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    return up(total+term*x/(terms+1)/(1-x/(terms+2)))

def transfer(auxiliary, new_difference, old_difference, old_chosen, far):
    direct = auxiliary+new_difference+far
    bridge = new_difference+old_difference+2*far
    chosen = min(direct, old_chosen+bridge)
    return {
        "direct_complete_source":record(direct),
        "transverse_difference_from_zero":cauchy(bridge),
        "old_chosen_plus_complete_bridge":record(old_chosen+bridge),
        "chosen_complete_true_DN_minus_exact_linear":cauchy(chosen),
        "ratio_to_old_chosen":record(chosen/old_chosen),
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in EXPECTED:
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--rss-kib",type=int,default=98304)
    args=ap.parse_args()
    if args.out.exists():
        raise FileExistsError("Keep every output immutable")
    began=time.monotonic()
    data={};identities={}
    for k,sha in EXPECTED.items():
        data[k],identities[k]=read_verified(getattr(args,k),sha)
    old=data["r83"];budget=data["r100"]
    if budget["schema"]!="visible-flex-larger-R100-hybrid46-and-complete-source-v1":
        raise ValueError("The actual proved grouped-domain input changed")
    constants=budget["constants"]
    scale=upper(constants["S"]);q=upper(constants["q_complete"])
    emax=upper(constants["old_e_uniform"]);kt=upper(constants["KT"])
    factors={k:upper(v) for k,v in budget["complete_R83_piece_multipliers"].items()}
    if set(factors)!={"main","corr","quadratic","remainder"}:
        raise ValueError("Keep all four complete positive source terms")
    if (scale!=F(257,256) or q!=F(1074136831,395007)
            or factors["main"]!=q or factors["corr"]!=q or factors["quadratic"]!=q*q):
        raise ValueError("No display-derived comparison constants")
    t=emax/scale
    if factors["remainder"]!=q*(1+q*t+(q*t)**2/3):
        raise ValueError("The complete cubic majorant changed")
    domains=old["old_envelope_complete_correction_rows"]
    rows=old["selected_mode_rows"]
    if [r["cell"] for r in domains]!=list(range(12,225)):
        raise ValueError("All213 original complete correction rows are needed")
    if [r["mode"] for r in rows]!=list(range(2,93,2)):
        raise ValueError("All46 original complete source rows are needed")
    es=[upper(r["bound"]) for r in domains]
    if not all(0<e<emax for e in es):
        raise ValueError("An actual e exceeds the independently proved global bound")
    ci=upper(data["far"]["point_cut_inner_mu12_K_conversion"])
    tau=upper(data["trace"]["head_strip"]);sigma=F(1,64)
    if not ci>0 or not sigma<tau<2:
        raise ValueError("Retain the original positive true cut and two strips")
    for key in ("far","trace"):
        expected=EXPECTED[key]
        if expected not in old["input_hashes"].values():
            raise ValueError("R83 did not use this exact true cut input")
    far=upper(old["whole46_complete_true_far_upper"])
    if not far>0:
        raise ValueError("The complete true nonlinear far term is positive")
    new_sums={s:F(0) for s in ("Wsigma1","Wtau_b1")}
    mode_rows=[];comparisons=[]
    for row in rows:
        m=int(row["mode"])
        pieces={k:upper(v) for k,v in row["complete_difference_Xi_pieces"].items()}
        if set(pieces)!=set(factors) or not all(v>=0 for v in pieces.values()):
            raise ValueError("Missing or signed positive source piece")
        weighted={k:up(factors[k]*pieces[k]) for k in pieces}
        xi=up(sum(weighted.values()))
        values={}
        for name,strip in (("Wsigma1",sigma),("Wtau_b1",tau)):
            delta=up(ci*(1+m)*exp_upper(m*strip)*xi)
            new_sums[name]=up(new_sums[name]+delta)
            old_delta=upper(row["complete_difference_source_"+name+"_upper"])
            av=upper(row["uniform_R74_auxiliary_source_Wsigma1_upper"])
            ov=upper(row["chosen_complete_true_DN_minus_exact_linear_Wsigma1"]["uniform_value_upper"])
            if name=="Wtau_b1":
                multiplier=exp_upper(m*(tau-sigma))
                av=up(av*multiplier);ov=up(ov*multiplier)
            values[name]={
                "old_auxiliary":record(av),"old_complete_difference":record(old_delta),
                "new_complete_difference":record(delta),"old_chosen":record(ov),
                "complete":transfer(av,delta,old_delta,ov,far),
            }
            comparisons.append(delta<F(16916769)*old_delta)
        mode_rows.append({
            "mode":m,"source_cells":213,
            "old_complete_difference_Xi_pieces":{k:record(v) for k,v in pieces.items()},
            "new_complete_difference_Xi_pieces":{k:record(v) for k,v in weighted.items()},
            "new_complete_difference_Xi":record(xi),
            "both_strips":values,
        })
    whole={}
    for name in new_sums:
        av=upper(old["whole46_auxiliary_source_"+name+"_upper"])
        dv=upper(old["whole46_complete_difference_source_"+name+"_upper"])
        ov=upper(old["whole46_chosen_true_DN_minus_exact_linear_"+name]["uniform_value_upper"])
        whole[name]={
            "new_complete_difference":record(new_sums[name]),
            "complete":transfer(av,new_sums[name],dv,ov,far)}
    qhigh=upper(constants["q_pure_high"])
    high={}
    for strip,row in data["r78"]["complete_coarse_trace_rows"].items():
        if strip not in ("head","outer"):
            continue
        bands=row["high_bands_value_upper"]
        if len(bands)!=3:
            raise ValueError("Retain all near/rest/infinite high bands")
        high[strip]={
            "bands":[{"name":name,"uniform":cauchy(qhigh*upper(v)),
                      "transverse_global_lipschitz":record((kt/256)*upper(v))}
                     for name,v in zip(("near94to184","rest186to8190","infinite8192up"),bands)],
            "complete_balanced_P_K":cauchy(qhigh*upper(row["complete_high_balanced_P_K"]["uniform_value_upper"]))}
    beta=upper(whole["Wtau_b1"]["complete"]["chosen_complete_true_DN_minus_exact_linear"]["uniform_value_upper"])
    bridge=upper(whole["Wtau_b1"]["complete"]["transverse_difference_from_zero"]["uniform_value_upper"])
    gates={
        "all_five_pinned_whole_inputs":len(identities)==5,
        "all_actual_prerequisite_gates":all(v["all_gates"] is True for v in data.values()),
        "all213_error_rows_below_global_emax":len(es)==213 and max(es)<emax,
        "all46_four_complete_positive_pieces":len(mode_rows)==46,
        "same_original_true_cut_input_identity":True,
        "all92_strip_mode_differences_improve_R97_q_squared":len(comparisons)==92 and all(comparisons),
        "full_low_wide_beta_below_previous_coarse_envelope":beta<F("1.169846811e-48"),
        "full_transverse_bridge_below_previous_coarse_envelope":bridge<F("1.784042e-60"),
        "true_far_positive_and_once_per_whole_mass":far>0,
        "explicit_low_lift_cancels_in_nonlinear_DN":old["low_Q_and_P_nonlinear_remainder_identically_zero"] is True,
        "qhigh_excludes_low_lift":qhigh==1+kt/256,
        "both_high_strips_and_three_bands":set(high)=={"head","outer"},
    }
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss>args.rss_kib:
        raise MemoryError("Owned RSS guard exceeded")
    out={
        "schema":"visible-flex-larger-R100-complete-source-reweight-v1",
        "status":"Actual complete original46-by213 source totals reweighted by proved R100 comparison",
        "author":"/root (GPT-6 Astra Pro, AI-assisted)",
        "all_gates":all(gates.values()),"gates":gates,
        "input_identities":identities,"source_sha256":digest_bytes(Path(__file__).read_bytes()),
        "parameter_domain":"R100 six original R74 complex axes times40 original R59 weighted-l1 axes",
        "parameter_norm":"max(linf_S,weighted_l1_T)","cauchy_radius":"3/4",
        "actual_uniform_old_e":record(max(es)),"proved_global_emax":record(emax),
        "q":record(q),"q_high":record(qhigh),
        "four_piece_multipliers":{k:record(v) for k,v in factors.items()},
        "point_cut_inner_mu12_K_conversion":record(ci),"head_strip":record(tau),
        "true_far_added_once_per_whole_mass":record(far),
        "mode_rows":mode_rows,"whole_low46":whole,"complete_high":high,
        "complete_mean_inverse_and_far_retained":True,
        "mean_and_cuff_scope":"Same positive R94 proof re-established on R100 domain; no new mean translation",
        "all_cut_selfmap_or_joint_middle_high_or_closed_surface_claimed":False,
        "no_Arb":True,"no_ODE":True,"no_new_source_integral":True,"no_Node":True,
        "elapsed_seconds":time.monotonic()-began,"owned_peak_rss_kib":rss,
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open("x",encoding="utf8") as f:
        json.dump(out,f,ensure_ascii=False,separators=(",",":"));f.write("\n")
    raw=args.out.read_bytes()
    print(json.dumps({"event":"done","all_gates":out["all_gates"],"gates":len(gates),
        "output":str(args.out),"bytes":len(raw),"sha256":digest_bytes(raw),
        "seconds":out["elapsed_seconds"],"RSS_KiB":rss}),flush=True)
    if not out["all_gates"]:
        raise SystemExit(2)

if __name__=="__main__":
    main()

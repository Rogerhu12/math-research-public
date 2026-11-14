#!/usr/bin/env python3
"""Exact rational assembly of the actual common-root high-frequency budget.

No new geometry or Fourier sampling occurs. Both complete directed summaries
are hash-checked; their displayed balls are parsed as rational enclosures.
This gives only the root trial/frame comparison, retaining all finite columns.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

INPUTS = [
 ("notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json",
  "66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8"),
 ("notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json",
  "c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b"),
]


def interval(text):
    s=str(text).strip()
    if s.startswith("[") and s.endswith("]"):
        s=s[1:-1].strip()
        if s.startswith("+/-"):
            r=F(s[3:].strip())
            if r<0: raise ValueError("negative radius")
            return -r,r
        parts=s.split("+/-")
        if len(parts)!=2: raise ValueError("unrecognized directed ball")
        c,r=map(lambda x:F(x.strip()),parts)
        if r<0: raise ValueError("negative radius")
        return c-r,c+r
    a=F(s)
    return a,a


def upper(text):
    return interval(text)[1]


def lower(text):
    return interval(text)[0]


def rational_record(x,places=18):
    x=F(x)
    if x<0: raise ValueError("only nonnegative budgets")
    ten=10**places
    n=(x.numerator*ten+x.denominator-1)//x.denominator
    return {"numerator":str(x.numerator),"denominator":str(x.denominator),
            "decimal_upper":str(n//ten)+"."+str(n%ten).zfill(places)}


def choose(d,K,p,moment):
    r=[r for r in d["budgets"] if
       (r["high_cutoff"],r["weight_order"],r["moment"])==(K,p,moment)]
    if len(r)!=1: raise ValueError("missing or duplicated complete moment")
    return r[0]


def assemble(d0,d1):
    if not d0["proved"] or not d1["proved"]: raise ValueError("unproved input")
    if d0["identity"]!=d1["identity"]: raise ValueError("different actual objects")
    if d0["true_frequency"]!=d1["true_frequency"]:
        raise ValueError("different true frequency intervals")
    q=d0["true_frequency"]
    if not lower(q["lower"])>F("9.72") or not upper(q["upper"])<10:
        raise ValueError("frequency not inside the claimed rational interval")
    data=[
      dict(K=64,L=2527,r=F(1361,100),m=F(229,1000),m0=F(5419,50000),
           ai=F(1139,1000),t=F(329,250),C=366000000,Mv=5314,Lv=148981,
           Mb=694529,Lb=48192638,strong=77000000,small=F(22,25),
           amin=F(118,125),inv=F(16)),
      dict(K=128,L=5015,r=F(1711,100),m=F(3,100),ai=F(127,125),
           t=F(27,25),C=46000000,Mv=5218,Lv=22139,
           Mb=693436,Lb=6791922,strong=8700000,small=F(21,1000),
           amin=F(123,125),inv=F(26,25)),
      dict(K=256,L=9992,r=F(2153,100),m=F(7,1000),ai=F(251,250),
           t=F(103,100),C=7610000,Mv=5192,Lv=4520,
           Mb=692884,Lb=1136112,strong=2100000,small=F(1,1000),
           amin=F(249,250),inv=F(503,500)),
    ]
    out=[]
    for c in data:
        K=c["K"];L=F(c["L"]);r=c["r"];m=c["m"]
        checks={}
        for name,doc,p,moment in [
            ("Mv",d0,3,0),("Lv",d0,3,1),
            ("Mb",d1,1,0),("Lb",d1,3,1)]:
            row=choose(doc,K,p,moment)
            val=row["true_scaled_Wiener_upper"]
            if not upper(val)<c[name]: raise ValueError("moment bound: "+name)
            checks[name]={"actual_ball":val,"strict_upper":c[name]}
        actual_m=choose(d1,K,4,0)["D_Hs_operator_upper_for_abs_s_le_order"]
        if not upper(actual_m)<m: raise ValueError("actual Sobolev positivity")
        m0=c.get("m0",m)
        actual_m0=choose(d1,K,0,0)["D_Hs_operator_upper_for_abs_s_le_order"]
        if not upper(actual_m0)<m0: raise ValueError("actual L2 positivity")
        if not L<4*F("9.72")*(K+1): raise ValueError("frequency cutoff lower")
        if not r**3<L: raise ValueError("cube-root lower")
        if not c["ai"]**2*(1-m)>1: raise ValueError("inverse square root")
        if not c["ai"]*(1+F(c["Mv"])/(L*r))<c["t"]:
            raise ValueError("balanced inverse-frame norm")
        if not (F(20*c["Lb"],3*c["C"]))**2 < 1-m:
            raise ValueError("Airy fractional-power commutator")
        if not c["amin"]**2 < 1-m0:
            raise ValueError("positive root-amplitude lower")
        pieces={
            "sorting_v0":F(40*c["Lv"]),
            "fourth_order_PD_after_embedding":F(c["Mv"]*c["Mb"])/L,
            "sorting_v1_after_embedding":F(40*c["Lb"])/r**2,
            "common_amplitude_Airy_commutator":F(3*c["C"])/r**2,
        }
        strong=3*c["t"]*sum((pieces[k] for k in
              ("sorting_v0","fourth_order_PD_after_embedding","sorting_v1_after_embedding")),F(0))
        strong+=pieces["common_amplitude_Airy_commutator"]
        small=strong/(L**2*r)
        if not strong<c["strong"] or not small<c["small"]:
            raise ValueError("requested final clean bound not established")
        if not (c["amin"]-c["small"])*c["inv"]>1:
            raise ValueError("root high-block inverse")
        out.append({
          "canonical_high_cutoff":K,"actual_inputs":checks,
          "actual_m4_ball":actual_m,
          "rational_m4_strict_upper":str(m),
          "actual_m0_ball":actual_m0,"rational_m0_strict_upper":str(m0),
          "strict_Lambda_lower":str(L),
          "strict_cuberoot_Lambda_lower":str(r),
          "inverse_square_root_upper":str(c["ai"]),
          "balanced_inverse_frame_H7over3_upper":str(c["t"]),
          "Airy_power_commutator_H0_to_H3_upper":c["C"],
          "positive_A_lower":str(c["amin"]),
          "pieces_before_frame_multiplication":
              {k:rational_record(v) for k,v in pieces.items()},
          "root_remainder_H0_to_H7over3":rational_record(strong),
          "root_remainder_L2":rational_record(small),
          "clean_H0_to_H7over3_upper":c["strong"],
          "clean_L2_upper":str(c["small"]),
          "root_identity_plus_high_remainder_inverse_upper":str(c["inv"]),
          "low_dimension_per_scalar_slot":2*K+1,
          "finite_comparison_rank_upper_before_optional_mean_correction":4*(2*K+1),
          "full_high_output_tails_of_finite_columns_retained":True,
        })
    return {
      "kind":"actual-common-root-frame-comparison-exact-rational-budget-v1",
      "proved":True,"identity":d0["identity"],
      "input_reports":[{"path":p,"sha256":s} for p,s in INPUTS],
      "norm":"canonical L2(dphi) direct sum; Gamma_k=4q|k|, Gamma_0=1",
      "q_rational_lower":"243/25","q_rational_upper":"10",
      "b_is_actual_v1_divided_by_3":True,
      "mean_and_regular_slots_retained":True,
      "budgets":out,
      "scope":"Root trial/frame comparison only. No cap or core propagation source is omitted or certified by this budget.",
      "full_feedback_inverse_proved":False,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    docs=[]
    for path,expected in INPUTS:
        raw=Path(path).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=expected:
            raise ValueError("changed directed summary: "+path)
        docs.append(json.loads(raw))
    report=assemble(*docs)
    report["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"proved":True,"output":str(a.out),
        "sha256":hashlib.sha256(a.out.read_bytes()).hexdigest(),
        "budgets":[{"K":r["canonical_high_cutoff"],
                    "H7over3":r["root_remainder_H0_to_H7over3"]["decimal_upper"],
                    "L2":r["root_remainder_L2"]["decimal_upper"]}
                   for r in report["budgets"]]}))


if __name__=="__main__":
    main()

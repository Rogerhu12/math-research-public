#!/usr/bin/env python3
"""Exact loss-width comparison under the saved preconjugacy proxy inputs.

Only the algebraic change of widths is proved here. P,Q,T,B and the twist
are old floating proxy hypotheses, not certified norms of a return map.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


def exact_arb(x):
    x=F(x)
    return arb(x.numerator)/x.denominator


def dyadic(x):
    a,b=x.man_exp()
    return str(F(int(a))*F(2)**int(b))


def record(x):
    if isinstance(x,F):
        return dict(exact=str(x),display=float(x))
    return dict(lower_exact=dyadic(x.lower()),upper_exact=dyadic(x.upper()),display=float(x))


def gate(parameters,loss):
    # All saved binary64 assumptions are treated as exact rationals; no
    # claim is made that they bound the mathematical P/Q/T/B/sigma.
    m0,r0,p,q,t,b,sigma=[F.from_float(float(parameters[k])) for k in
                         ("M0","R0","P","Q","T","B","sigma")]
    M,R=m0+1,2*r0
    La=2*R/sigma
    A=R*(1+p*La)
    LH=M*F(3,2)*A
    C=F(3,2)*A+b*LH**2/2+q*LH*La+t*La**2/2
    Z=r0*q*LH+r0*t*La+p*r0*r0*LH
    terms=[1/(32*C),1/(4*r0*LH),sigma/(8*Z)]
    epsilon=loss*loss*min(terms)
    return dict(epsilon=epsilon,limiting_index=terms.index(min(terms)),La=La,LH=LH,
                parameter_displacement=2*La*epsilon,
                conjugacy_displacement=2*LH*epsilon/loss,
                derivative_displacement=2*LH*epsilon/(loss*loss))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proxy-report",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args();ctx.prec=192
    raw=args.proxy_report.read_bytes();data=json.loads(raw)
    S,old_s,new_s=F(1,128),F(1,512),F(3,512)
    old_loss,new_loss=old_s/8,new_s/5
    ratio=(new_loss/old_loss)**2
    if ratio!=F(576,25) or not 0<new_loss<new_s/4:
        raise ValueError("loss arithmetic failed")
    rows=[]
    for scenario in data["prospective_gate_scenarios"]:
        proxy=scenario["preconjugated"]
        old,new=gate(proxy,old_loss),gate(proxy,new_loss)
        if new["epsilon"]!=ratio*old["epsilon"]:
            raise ValueError("exact gate ratio failed")
        rows.append(dict(T_multiplier=scenario["assumed_T_multiplier_of_selected_ray_maximum"],
            assumed_binary64_inputs={k:record(F.from_float(float(proxy[k]))) for k in
                                     ("M0","R0","P","Q","T","B","sigma")},
            old_epsilon=record(old["epsilon"]),new_epsilon=record(new["epsilon"]),
            exact_ratio=str(ratio),limiting_index=new["limiting_index"],
            conditional_parameter_displacement=record(new["parameter_displacement"]),
            conditional_conjugacy_displacement=record(new["conjugacy_displacement"]),
            conditional_derivative_displacement=record(new["derivative_displacement"]),
            remaining_map_domain_gap_if_these_inputs_hold=record(S-new_s-new["conjugacy_displacement"])))
    def hardy(gap):
        d=exact_arb(gap)
        return (2*d.cosh()/d.sinh()-1).sqrt()
    old_factor,new_factor=hardy(S-old_s),hardy(S-new_s)
    report=dict(kind="exact_width_algebra_under_unproved_preconjugacy_proxy_assumptions",
        width_scaling_proved=True,actual_KAM_gate_proved=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        proxy_report_sha256=hashlib.sha256(raw).hexdigest(),
        proxy_object_sha256=data["object_sha256"],proxy_exact_delta_fraction=data["exact_delta_fraction"],
        widths={k:str(v) for k,v in dict(outer_map_strip=S,old_initial=old_s,old_loss=old_loss,
            new_initial=new_s,new_loss=new_loss,new_final=new_s-4*new_loss,
            new_unused_domain_gap=S-new_s).items()},exact_epsilon_factor=str(ratio),
        scenarios=rows,old_Hardy_factor=record(old_factor),new_Hardy_factor=record(new_factor),
        Hardy_factor_ratio=record(new_factor/old_factor),
        conditional_boundary_error_allowance_ratio=record(exact_arb(ratio)*old_factor/new_factor),
        limitations=["The old floating P/Q/T/B/twist values remain hypotheses, not rigorous upper/lower bounds.",
            "Actual E, parameter-box uniformity, all intermediate map domains, and R31 inequalities still require certification.",
            "The proxy object is delta3; no numerical norm or twist is transferred to delta4 by this comparison.",
            "The calculation only chooses widths inside a prospective outer G strip 1/128."])
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(exact_factor=str(ratio),new_final_strip=str(new_s-4*new_loss),
        new_epsilon=[row["new_epsilon"]["display"] for row in rows],
        parameter_displacement=[row["conditional_parameter_displacement"]["display"] for row in rows],
        Hardy_factor_ratio=float(new_factor/old_factor),
        boundary_error_ratio=float(exact_arb(ratio)*old_factor/new_factor))))


if __name__=="__main__":main()

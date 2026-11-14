#!/usr/bin/env python3
"""Resume the actual saved eight-substage construction, preserving true integrals.

The executed source and its ordinary failure remain unchanged.  The complete
64 six-integral bins and nine shared physical two-jets are reused under their
full source/input hashes.  A true prefix/suffix moment belongs to [0,I_total]
because its original real integrand is nonnegative.  This independently proved
domain is intersected with the stored Arb enclosure; the result is represented
by the already published exact midpoint/radius nonnegative constructor.
No stored integral, endpoint, g, H, mean equation, or PDE test is replaced.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
from pathlib import Path
import sys
import types

from flint import arb
from closure_split_joint_io import read,digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import ball_record
from tail_outer_positive_moment_panels import MOMENT_KEYS
from tail_outer_candidate_domain import nonnegative_integral


ORIGINAL_SHA = "9c2903ea8e44191166bd5f00c929f596915669482a1d3709844cd6945a227ffc"


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--resume",type=Path,required=True)
    wrapper,remainder=parser.parse_known_args()
    sys.argv=[sys.argv[0]]+remainder
    path=Path(__file__).with_name("tail_outer_saved_substage_candidate.py")
    if digest(path)!=ORIGINAL_SHA:
        raise ValueError("The formally executed substage source changed")
    prior=read(wrapper.resume)
    if (prior["phase"]!="shared-inner-nodes" or prior["complete_bins"]!=64
            or prior["complete_nodes"]!=9 or prior["complete_stages"]!=0
            or prior["cell"]!=0 or prior["segment"]!=3 or prior["stages"]):
        raise ValueError("This adapter resumes the recorded pre-validation failure only")
    for name,checksum in prior["source_hashes"].items():
        if digest(path.with_name(name))!=checksum:
            raise ValueError("A paid substage dependency changed: "+name)
    saved_bins=prior.pop("bins");saved_nodes=prior.pop("nodes")
    identity=dict(path=str(wrapper.resume),sha256=digest(wrapper.resume),
        original_executed_source_sha256=ORIGINAL_SHA,
        original_analytic_integrals=prior["analytic_integrals"],
        original_range_strips=prior["range_strips"],
        reused_six_integral_bins=64,reused_shared_physical_nodes=9,
        recomputed_saved_integrals=False,recomputed_saved_physical_two_jets=False,
        positive_domain=("Each true prefix/suffix moment is the integral of the same "
            "nonnegative R48 basis against the same positive r_x*w measure; hence it "
            "belongs to [0,the same true total]. Intersect this proven domain before "
            "using an exact nonnegative midpoint/radius Arb representation."))
    repair=dict(prefix_or_suffix_entries=0,rounded_negative_entries=0,
        total_upper_intersections=0,examples=[])

    def recover_integrals(args,hashes,parts,engine):
        if parts!=8 or args.validation_parts!=8 or args.segment!=3:
            raise ValueError("The saved mathematical subdivision changed")
        if hashes!=prior["input_hashes"]:
            raise ValueError("A complete fixed-source substage input changed")
        totals=[]
        for k in range(parts):
            total={key:arb(0) for key in ("width",*MOMENT_KEYS)}
            for v in range(8):
                row=saved_bins[8*k+v]
                l,r=F(8*k+v,64),F(8*k+v+1,64)
                if (row["part"]!=k or row["bin"]!=v
                        or F(row["left"])!=l or F(row["right"])!=r):
                    raise ValueError("A saved true integral bin has another domain")
                records=row["source_parts"]
                if (not records or F(records[0]["left"])!=l
                        or F(records[-1]["right"])!=r
                        or any(a["right"]!=b["left"] for a,b in zip(records,records[1:]))):
                    raise ValueError("The complete original real branch cover changed")
                for key in total:
                    value=ball(row["values"][key])
                    if not value>0:
                        raise ArithmeticError("A saved full subinterval integral is not strictly positive")
                    total[key]+=value
            totals.append(total)
        engine.analytic_calls=prior["analytic_integrals"]
        engine.range_strips=prior["range_strips"]
        hashes[str(wrapper.resume)]=identity["sha256"]
        return saved_bins,totals

    def recover_nodes(cp,original_nodes,j,parts):
        for k,row in enumerate(saved_nodes):
            index=(9-j)*parts-k
            if (row["point"]!=k or F(row["source_x"])!=F(k,parts)
                    or row["state_index"]!=index):
                raise ValueError("A saved shared node has another source coordinate")
            if k in (0,parts):
                old=original_nodes["rows"][j+(1 if k else 0)]
                if not row["original_outer_endpoint_reused_exactly"]:
                    raise ValueError("An outer physical endpoint was replaced")
                for key in ("radius","w","wr","shared_physical_jets",
                            "candidate_L_orthonormal_cosine","finite_endpoint_definition"):
                    if row[key]!=old[key]:
                        raise ValueError("The original shared two-jet differs: "+key)
            elif (row["full_saved_Q"]+row["full_saved_momentum"]!=cp["states"][index]
                    or row["local_momentum_multiplier"]!=1):
                raise ValueError("A full saved internal state or its momentum convention changed")
        return saved_nodes

    source=path.read_text()
    start=source.index("    for k in range(parts):\n        a,b=F(k,parts),F(k+1,parts)\n        totals=")
    stop=source.index("    width=sum((row[\"width\"] for row in part_totals),arb(0))",start)
    integral_block=source[start:stop]
    start=source.index("    root=PureFiniteMomentumRoot(")
    stop=source.index("    def endpoint_for(row,h):",start)
    node_block=source[start:stop]
    changes=[
        (integral_block,"    bins,part_totals=_recover_integrals(args,hashes,parts,engine)\n"),
        (node_block,
         "    modes,tau=nodes['modes'],F(nodes['tau'])\n"
         "    weights={m:((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}\n"
         "    node_rows=_recover_nodes(cp,nodes,j,parts)\n"
         "    del packet,cp\n"
         "    memory_gate('recovered-complete-moments-and-nodes')\n"),
        ("Path(__file__).name,\"tail_outer_weighted_endpoint.py\"",
         "Path(__file__).name,\"tail_outer_substage_nonnegative_resume.py\","
         "\"tail_outer_candidate_domain.py\",\"tail_outer_weighted_endpoint.py\""),
        ("source_hashes=numeric_source_hashes,analytic_integrals=engine.analytic_calls,",
         "source_hashes=numeric_source_hashes,recovered_construction=_resume_identity,"
         "positive_domain_representation=_repair_record,analytic_integrals=engine.analytic_calls,"),
        ("        recovery_path=str(recovery),elapsed_seconds=time.monotonic()-began,",
         "        recovered_construction=_resume_identity,positive_domain_representation=_repair_record,\n"
         "        recovery_path=str(recovery),elapsed_seconds=time.monotonic()-began,"),
    ]
    for before,after in changes:
        if source.count(before)!=1:
            raise ValueError("A frozen resume insertion is not unique")
        source=source.replace(before,after)
    restored=source
    for before,after in reversed(changes):
        if restored.count(after)!=1:
            raise ValueError("A narrow resume insertion is not reversibly unique")
        restored=restored.replace(after,before)
    if restored!=path.read_text():
        raise AssertionError("The executed original source is not exactly recovered")
    module=types.ModuleType("tail_outer_same_substage_positive_resume")
    module.__file__=str(path)
    module.__dict__.update(_recover_integrals=recover_integrals,_recover_nodes=recover_nodes,
        _resume_identity=identity,_repair_record=repair)
    exec(compile(source,str(path),"exec"),module.__dict__)
    original_fields=module.weighted_panel_fields

    def nonnegative_fields(candidate,**kwargs):
        for side in ("prefix_moments","suffix_moments"):
            bounded={}
            for key,value in kwargs[side].items():
                total=candidate["total_moments"][key]
                lo=max(arb(0),value.lower())
                hi=min(value.upper(),total.upper())
                if not lo<=hi or not hi>=0:
                    raise ArithmeticError("The true positive-integral intersection is empty")
                record=ball_record(lo.union(hi))
                fixed=nonnegative_integral(record)
                repair["prefix_or_suffix_entries"]+=1
                if not value>=0:
                    repair["rounded_negative_entries"]+=1
                    if len(repair["examples"])<3:
                        repair["examples"].append(dict(side=side,moment=key,
                            old=ball_record(value),proven_domain_upper=ball_record(total.upper()),
                            nonnegative_enclosure=ball_record(fixed)))
                if total.upper()<value.upper():repair["total_upper_intersections"]+=1
                bounded[key]=fixed
            kwargs[side]=bounded
        return original_fields(candidate,**kwargs)

    module.weighted_panel_fields=nonnegative_fields
    module.main()


if __name__=="__main__":main()

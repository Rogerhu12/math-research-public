#!/usr/bin/env python3
"""Apply the frozen eight-substage construction with exact positive domains.

The source, fixed g, saved full states, endpoint jets, six true integrals,
complete mean and actual derivative tests are the already executed R66
construction. Only the proved nonnegative partial-integral representation
from its successful resume is installed before evaluation. Unused copies
of saved arrays are released; no numerical values are replaced.
Any segment 0..7 accepted by the original source can be selected explicitly.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from pathlib import Path
import types

from flint import arb
from closure_split_joint_io import digest
from closure_real_head_source_enclosure import ball_record
from tail_outer_candidate_domain import nonnegative_integral


ORIGINAL_SHA="9c2903ea8e44191166bd5f00c929f596915669482a1d3709844cd6945a227ffc"


def main():
    path=Path(__file__).with_name("tail_outer_saved_substage_candidate.py")
    if digest(path)!=ORIGINAL_SHA:
        raise ValueError("The formally executed complete substage source changed")
    repair=dict(prefix_or_suffix_entries=0,rounded_negative_entries=0,
        total_upper_intersections=0,examples=[],
        theorem=("The same true prefix and suffix R48 integrals belong to "
            "[0,the same true total], because every exact basis and the measure "
            "r_x*w are nonnegative. Intersect that proved domain with the "
            "existing enclosure, then use the exact midpoint/radius constructor."))

    def trim_reference(prior):
        # Retain every item the original mathematical construction reads.
        # The complete source packet is still identified by its original SHA.
        keep={key:prior[key] for key in ("input_hashes","segments","worst")}
        keep["segments"]=[dict(segment=row["segment"],
            all_general_mean_gates=row["all_general_mean_gates"]) for row in keep["segments"]]
        keep["worst"]={key:keep["worst"][key] for key in
            ("actual_Darboux_defect_abs","full_finite_J_W1")}
        prior.clear();prior.update(keep)

    def trim_nodes(nodes,j):
        # The same two original endpoints are used, with all their fields.
        # The other eight rows are never read by this one-segment application.
        nodes["rows"]=[row if index in (j,j+1) else None
                       for index,row in enumerate(nodes["rows"])]

    source=path.read_text()
    changes=[
        ("    nodes,ledger,packet,ready,prior=map(read,paths[:5])",
         "    nodes,ledger,packet,ready,prior=map(read,paths[:5])\n"
         "    _trim_reference_memory(prior)"),
        ("    n,j=nodes[\"cell\"],args.segment",
         "    n,j=nodes[\"cell\"],args.segment\n    _trim_node_memory(nodes,j)"),
        ("    def endpoint_for(row,h):",
         "    del packet,cp,root\n    def endpoint_for(row,h):"),
        ("Path(__file__).name,\"tail_outer_weighted_endpoint.py\"",
         "Path(__file__).name,\"tail_outer_checked_substage_candidate.py\","
         "\"tail_outer_candidate_domain.py\",\"tail_outer_weighted_endpoint.py\""),
        ("source_hashes=numeric_source_hashes,analytic_integrals=engine.analytic_calls,",
         "source_hashes=numeric_source_hashes,positive_domain_representation=_repair_record,"
         "analytic_integrals=engine.analytic_calls,"),
        ("        recovery_path=str(recovery),elapsed_seconds=time.monotonic()-began,",
         "        positive_domain_representation=_repair_record,\n"
         "        same_original_physical_source_and_all_acceptance_tests=True,\n"
         "        released_unused_saved_arrays_only=True,\n"
         "        recovery_path=str(recovery),elapsed_seconds=time.monotonic()-began,"),
    ]
    for before,after in changes:
        if source.count(before)!=1:
            raise ValueError("A frozen same-candidate insertion anchor changed")
        source=source.replace(before,after)
    restored=source
    for before,after in reversed(changes):
        if restored.count(after)!=1:raise ValueError("A source insertion is not uniquely reversible")
        restored=restored.replace(after,before)
    if restored!=path.read_text():raise AssertionError("The original complete mathematical source is not recovered")
    module=types.ModuleType("tail_outer_positive_domain_substage_application")
    module.__file__=str(path)
    module.__dict__.update(_trim_reference_memory=trim_reference,
        _trim_node_memory=trim_nodes,_repair_record=repair)
    exec(compile(source,str(path),"exec"),module.__dict__)
    original_fields=module.weighted_panel_fields

    def checked_fields(candidate,**kwargs):
        for side in ("prefix_moments","suffix_moments"):
            bounded={}
            for key,value in kwargs[side].items():
                total=candidate["total_moments"][key]
                lo=max(arb(0),value.lower());hi=min(value.upper(),total.upper())
                if not lo<=hi or not hi>=0:
                    raise ArithmeticError("The true nonnegative partial-integral intersection is empty")
                fixed=nonnegative_integral(ball_record(lo.union(hi)))
                repair["prefix_or_suffix_entries"]+=1
                if not value>=0:
                    repair["rounded_negative_entries"]+=1
                    if len(repair["examples"])<3:
                        repair["examples"].append(dict(side=side,moment=key,old=ball_record(value),
                            total_upper=ball_record(total.upper()),nonnegative_enclosure=ball_record(fixed)))
                if total.upper()<value.upper():repair["total_upper_intersections"]+=1
                bounded[key]=fixed
            kwargs[side]=bounded
        return original_fields(candidate,**kwargs)

    module.weighted_panel_fields=checked_fields
    module.main()


if __name__=="__main__":main()

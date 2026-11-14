#!/usr/bin/env python3
"""Resume the paid R64 prefix using a full real endpoint branch union.

Single-branch endpoints use the original evaluator unchanged. At an
undecided exact cap/critical endpoint, the frozen source_range includes
every possible real branch. Intersect its w and w_r with the already
shared physical jet point; no midpoint or branch selection is substituted.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
from pathlib import Path
import sys
import types

from closure_split_joint_io import read, digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q
from tail_outer_positive_moment_panels import source_range
from tail_outer_weighted_compatible import intersection, normalized_endpoint_jet


ORIGINAL_SHA = "836074abfdc5758822633a591d5ed4eb0cdf1aae6d018f486308f20c2330f32f"


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--resume", type=Path, required=True)
    wrapper, remainder = parser.parse_known_args()
    sys.argv = [sys.argv[0]]+remainder
    path = Path(__file__).with_name("tail_outer_segment_candidate_domain.py")
    if digest(path) != ORIGINAL_SHA:
        raise ValueError("The actually executed R64 scan source changed")
    source = path.read_text()
    prior = read(wrapper.resume)
    if (prior["abort"] is None or prior["abort"]["message"] != "A local original endpoint branch is unresolved"
            or prior["failed_mean_panels"] != 0
            or [row["segment"] for row in prior["segments"]] != list(range(len(prior["segments"])))
            or not all(row["all_general_mean_gates"] for row in prior["segments"])
            or sum(row["panels"] for row in prior["segments"]) != prior["panels"]):
        raise ValueError("The exact recorded completed prefix is not the expected one")
    for name, checksum in prior["source_hashes"].items():
        if digest(path.with_name(name)) != checksum:
            raise ValueError("A paid prefix dependency changed: "+name)
    resume_info = dict(path=str(wrapper.resume),sha256=digest(wrapper.resume),
        completed_segments=len(prior["segments"]),paid_panels=prior["panels"],
        prior_scope="Completed R64 segment rows of a formally failed whole scan; unresolved endpoint only")

    def recover(material, nodes, hashes):
        if prior["cell"] != material["cell"] or prior["modes"] != nodes["modes"] or prior["tau"] != nodes["tau"]:
            raise ValueError("The recovered candidate and the new scan have different definitions")
        for key, checksum in hashes.items():
            if prior["input_hashes"].get(key) != checksum:
                raise ValueError("A paid prefix actual input changed")
        groups={g["source_segment"]:g for g in material["groups"]}
        for row in prior["segments"]:
            group=groups[row["segment"]]
            if row["panels"] != group["panels"] or prior["input_hashes"].get(group["path"]) != group["sha256"]:
                raise ValueError("A paid prefix real source group changed")
        hashes[str(wrapper.resume)] = resume_info["sha256"]
        maxima={key:dict(value=ball(row["value"]).upper(),witness=row["witness"])
                for key,row in prior["worst"].items()}
        minima={key:dict(value=ball(row["value"]).lower(),witness=row["witness"])
                for key,row in prior["minima_over_passed_panels"].items()}
        return list(prior["segments"]),maxima,minima,[]

    changes = [
        ("    segments, worst, minima, failed_panels = [], {}, {}, []\n    count, failures, abort = 0, 0, None",
         "    segments, worst, minima, failed_panels = _recover_prefix(material,nodes,hashes)\n"
         "    count, failures, abort = sum(row['panels'] for row in segments), 0, None"),
        ("            hashes[str(path)] = group[\"sha256\"]\n            moments, total = [], zero_moments()",
         "            hashes[str(path)] = group[\"sha256\"]\n"
         "            if j < _resume_info['completed_segments']:\n                continue\n"
         "            moments, total = [], zero_moments()"),
        ("        cell=n,modes=modes,tau=str(tau),panels=count,segments=segments,abort=abort,",
         "        cell=n,modes=modes,tau=str(tau),panels=count,segments=segments,abort=abort,\n"
         "        recovered_prefix=_resume_info,newly_evaluated_panels=count-_resume_info['paid_panels'],\n"
         "        endpoint_range_method='Original single branch where certified; otherwise full R26 possible-branch union intersected with the same shared physical point',"),
        ("Path(__file__).name,\"tail_outer_general_mean_bounds.py\"",
         "Path(__file__).name,\"tail_outer_segment_endpoint_union.py\",\"tail_outer_general_mean_bounds.py\""),
    ]
    for before,after in changes:
        if source.count(before)!=1:
            raise ValueError("A narrow frozen scan/resume anchor changed")
        source=source.replace(before,after)
    restored=source
    for before,after in reversed(changes):
        if restored.count(after)!=1:
            raise ValueError("A resume insertion is not uniquely reversible")
        restored=restored.replace(after,before)
    if restored!=path.read_text():
        raise AssertionError("The unchanged original scan could not be recovered")
    module=types.ModuleType("tail_outer_R64_same_prefix_endpoint_union")
    module.__file__=str(path)
    module.__dict__.update(_recover_prefix=recover,_resume_info=resume_info)
    exec(compile(source,str(path),"exec"),module.__dict__)
    old_endpoint=module.endpoint
    def union_endpoint(cell,segment_index,side,node):
        x=F(side)
        segment=cell.segments[segment_index]
        if cell.classify(segment,x,x) is not None:
            return old_endpoint(cell,segment_index,side,node)
        ranges=source_range(cell,segment,x,x,None,exact_q(F(1,8)))
        w=intersection(ranges["w"],ball(node["w"]))
        rx=ranges["radius_x"]
        ell=intersection(ranges["log_w_x"],ball(node["wr"])*rx/w)
        jets={key:{int(m):ball(value) for m,value in node["shared_physical_jets"][key].items()}
              for key in ("H","Hr","Hrr")}
        return normalized_endpoint_jet(jets["H"],jets["Hr"],jets["Hrr"],
                                       w=w,radius_u=rx,log_w_u=ell)
    module.endpoint=union_endpoint
    module.main()


if __name__=="__main__":
    main()

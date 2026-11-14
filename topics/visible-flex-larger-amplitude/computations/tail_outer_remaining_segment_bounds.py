#!/usr/bin/env python3
"""Extract remaining same-candidate segment maxima, then assemble physical units.

The old R64 scan did not save a maximum for each segment.  This adapter
replays only the unchanged seven pieces (0,1,2,4,5,6,7), with the same
true positive-moment construction and endpoint branch union.  The paid
eight-substage segment3 and physical-r segment8 are consumed unchanged.
No source quadrature, Node, radial ODE or new candidate is introduced.
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
from closure_real_head_source_enclosure import exact_q,ball_record
from tail_outer_positive_moment_panels import source_range
from tail_outer_weighted_compatible import intersection,normalized_endpoint_jet


ORIGINAL_SHA="836074abfdc5758822633a591d5ed4eb0cdf1aae6d018f486308f20c2330f32f"
SELECTED=(0,1,2,4,5,6,7)
PHYSICAL_KEYS=("R_tau","complete_mean_abs","actual_Darboux_defect_abs",
    "physical_nonmean_second_source_W1","nonmean_physical_hrr_W1",
    "mean_physical_hrr_minus_background_abs","full_D_nonconstant_W1",
    "full_weight_minus_one_W0","P_theta_W1","K_theta_minus_P_W1")


def main():
    parser=argparse.ArgumentParser(add_help=False)
    for name in ("prior-r64","substage","last-piece"):
        parser.add_argument("--"+name,type=Path,required=True)
    extra,remainder=parser.parse_known_args()
    sys.argv=[sys.argv[0]]+remainder
    path=Path(__file__).with_name("tail_outer_segment_candidate_domain.py")
    if digest(path)!=ORIGINAL_SHA:
        raise ValueError("The original actually executed R64 source changed")
    old,sub,last=map(read,(extra.prior_r64,extra.substage,extra.last_piece))
    if (old["cell"]!=0 or sub["cell"]!=0 or last["cell"]!=0
            or sub["segment"]!=3 or last["segment"]!=8
            or not all(sub["gates"].values()) or not all(last["gates"].values())
            or not sub["original_outer_endpoint_two_jets_reused_exactly"]
            or not last["shared_physical_endpoint_two_jets"]
            or not all(old["segments"][j]["all_general_mean_gates"] for j in SELECTED)):
        raise ValueError("The three complete same-source candidate components are required")
    for name,checksum in old["source_hashes"].items():
        if digest(path.with_name(name))!=checksum:
            raise ValueError("An unchanged candidate dependency changed: "+name)
    # These primary records remain on disk and are bound by their full SHA.
    # This short assembly needs their proved bounds/identities, not a second
    # resident copy of all integral bins, endpoint fields or point probes.
    for key in ("bins","nodes","old_worst_comparison_points","positive_domain_representation"):
        sub.pop(key,None)
    identity=dict(selected_original_segments=list(SELECTED),
        segment3=dict(path=str(extra.substage),sha256=digest(extra.substage)),
        segment8=dict(path=str(extra.last_piece),sha256=digest(extra.last_piece)),
        prior_complete_candidate=dict(path=str(extra.prior_r64),sha256=digest(extra.prior_r64)),
        same_candidate_replay_only=True,new_source_integrals=0,
        purpose="The previous aggregate did not retain the unchanged pieces' individual physical maxima")

    def validate_inputs(material,nodes,hashes):
        if material["cell"]!=0 or nodes["cell"]!=0:
            raise ValueError("This application concerns the actual fixed-source cell0")
        if nodes["modes"]!=sub["modes"] or nodes["tau"]!=sub["tau"]:
            raise ValueError("The physical trace mode/strip convention changed")
        for name,checksum in hashes.items():
            if old["input_hashes"].get(name)!=checksum:
                raise ValueError("An unchanged R64 component input differs: "+name)
        for proof in (sub,last):
            for name,checksum in hashes.items():
                if name in proof["input_hashes"] and proof["input_hashes"][name]!=checksum:
                    raise ValueError("A paid replacement component has another input")
        for proof in (sub,last):
            if not set(hashes.values()).intersection(proof["input_hashes"].values()):
                raise ValueError("A paid replacement lacks a common saved-jet/source identity")
        for p in (extra.prior_r64,extra.substage,extra.last_piece):
            hashes[str(p)]=digest(p)

    def candidate_guard(j,total,candidate):
        previous=old["segments"][j]
        if (previous["segment"]!=j
                or {key:ball_record(v) for key,v in total.items()}!=previous["total_local_positive_moments"]
                or {str(m):ball_record(v) for m,v in candidate["bubble_coefficient"].items()}
                    !=previous["bubble_coefficients"]):
            raise ValueError("An unchanged true candidate coefficient enclosure differs")

    def assemble(result):
        result["component_identity"]=identity
        result["selected_original_segments"]=list(SELECTED)
        result["original_scan_scope"]=result.pop("status")
        result["status"]="Remaining unchanged segment bounds and assembled same-g cell0 candidate"
        complete=all(result["gates"].values())
        result["all_remaining_candidate_coefficient_enclosures_bitwise_checked"]=complete
        coverage=[dict(segment=r["segment"],panels=r["panels"],source="this same-candidate replay")
                  for r in result["segments"]]
        coverage.extend([dict(segment=3,panels=sub["total_validation_panels"],source=str(extra.substage)),
                         dict(segment=8,panels=len(last["rows"]),source=str(extra.last_piece))])
        coverage.sort(key=lambda r:r["segment"])
        result["whole_cell_coverage"]=coverage
        result["whole_cell_panels"]=sum(r["panels"] for r in coverage)
        result["whole_cell_complete_mean_and_actual_defect"]=complete and [r["segment"] for r in coverage]==list(range(9))
        choices=[("remaining-original-source-pieces",result["worst"]),
                 ("eight-source-substage-segment3",sub["bounds"]),
                 ("physical-r-segment8",last["last_piece_bounds"])]
        maxima={}
        for key in PHYSICAL_KEYS:
            for origin,table in choices:
                if key not in table:continue
                row=table[key]
                if key not in maxima or ball(row["value"]).upper()>ball(maxima[key]["value"]).upper():
                    maxima[key]=dict(value=row["value"],witness=row["witness"],origin=origin)
        result["whole_cell_common_unit_maxima"]=maxima
        result["source_coordinate_dependent_fields_not_aggregated"]=[
            "complete_mean_source_derivative_abs","finite_actual_linear_residual_W1",
            "complete_nonlinear_source_W1","complete_nonmean_source_residual_W1",
            "complete_scalar_mean_residual_abs","full_finite_J_W1"]
        result["unit_rule"]="Only physical-r or dimensionless fields are aggregated across the source-x and physical-r charts; each local source residual retains its own chart."
        result["exact_outer_radial_solution_claimed"]=False
        result["outer_Green_Schur_gate_paid"]=False

    source=path.read_text()
    changes=[
        ("    n, tau, modes = material[\"cell\"], F(nodes[\"tau\"]), nodes[\"modes\"]",
         "    _validate_inputs(material,nodes,hashes)\n"
         "    n, tau, modes = material[\"cell\"], F(nodes[\"tau\"]), nodes[\"modes\"]"),
        ("            hashes[str(path)] = group[\"sha256\"]\n            moments, total = [], zero_moments()",
         "            hashes[str(path)] = group[\"sha256\"]\n"
         "            if j not in _selected:continue\n"
         "            moments, total = [], zero_moments()"),
        ("    def update_max(name, value, witness):\n        if name not in worst",
         "    def update_max(name, value, witness):\n"
         "        if name not in local_worst or value>local_worst[name]['value']:\n"
         "            local_worst[name]=dict(value=value.upper(),witness=witness)\n"
         "        if name not in worst"),
        ("            prefix, local_count, good, maxR, local_min = zero_moments(), 0, 0, arb(0), None",
         "            _candidate_guard(j,total,candidate)\n"
         "            local_worst={}\n"
         "            prefix, local_count, good, maxR, local_min = zero_moments(), 0, 0, arb(0), None"),
        ("                shared_endpoint_points=[j,j+1])",
         "                shared_endpoint_points=[j,j+1],\n"
         "                local_bounds={key:dict(value=ball_record(row['value']),witness=row['witness']) for key,row in local_worst.items()})"),
        ("    complete = abort is None and count==material[\"panels\"] and len(segments)==9",
         "    complete = abort is None and count==sum(g['panels'] for g in material['groups'] if g['source_segment'] in _selected) and [r['segment'] for r in segments]==list(_selected)"),
        ("Path(__file__).name,\"tail_outer_general_mean_bounds.py\"",
         "Path(__file__).name,\"tail_outer_remaining_segment_bounds.py\",\"tail_outer_general_mean_bounds.py\""),
        ("    payload=(json.dumps(result,indent=2)+\"\\n\").encode()",
         "    _assemble_result(result)\n    payload=(json.dumps(result,indent=2)+\"\\n\").encode()"),
    ]
    for before,after in changes:
        if source.count(before)!=1:raise ValueError("A narrow same-candidate replay anchor changed")
        source=source.replace(before,after)
    restored=source
    for before,after in reversed(changes):restored=restored.replace(after,before)
    if restored!=path.read_text():raise AssertionError("The original continuous source is not recovered exactly")
    module=types.ModuleType("tail_outer_unchanged_segment_maxima")
    module.__file__=str(path)
    module.__dict__.update(_selected=SELECTED,_validate_inputs=validate_inputs,
        _candidate_guard=candidate_guard,_assemble_result=assemble)
    exec(compile(source,str(path),"exec"),module.__dict__)
    old_endpoint=module.endpoint
    def endpoint(cell,j,side,node):
        x=F(side);segment=cell.segments[j]
        if cell.classify(segment,x,x) is not None:return old_endpoint(cell,j,side,node)
        g=source_range(cell,segment,x,x,None,exact_q(F(1,8)))
        w=intersection(g["w"],ball(node["w"]))
        ell=intersection(g["log_w_x"],ball(node["wr"])*g["radius_x"]/w)
        jets={key:{int(m):ball(v) for m,v in node["shared_physical_jets"][key].items()}
              for key in ("H","Hr","Hrr")}
        return normalized_endpoint_jet(jets["H"],jets["Hr"],jets["Hrr"],
            w=w,radius_u=g["radius_x"],log_w_u=ell)
    module.endpoint=endpoint
    module.main()


if __name__=="__main__":main()

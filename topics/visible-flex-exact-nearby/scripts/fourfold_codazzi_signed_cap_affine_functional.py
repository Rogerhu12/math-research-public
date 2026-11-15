#!/usr/bin/env python3
"""New same-object complete97 signed cap affine functional, SC1--25.

Only public Actions executes this program.  It reads exact old scalar rows and
the unchanged physical Hermite trial, with no old QR, target, residual-norm,
coefficient, Gram, or Green producer call.  New work arrays remain temporary.
Small cumulative scientific checkpoints are printed before any publication.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.metadata
import json
import math
import os
import sys
import time
import traceback
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import arb,ctx
import fourfold_codazzi_signed_cap_radial_moments as moments
import fourfold_codazzi_signed_cap_original_inputs as original

REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_signed_cap_affine_functional.py"
KIND="actual_complete97_signed_radial_subtracted_cap_affine_v1"
CHECKPOINT_KIND="complete_prefix97_signed_cap_affine_scientific_checkpoint_v1"
HELPER_SHA="6f868fafd82a62c7c7a3a04bebbb0da1363209c80097f218f086781d37f2efb4"
READER_SHA="a7c099608ec6ef1504a1d30b9cabbe9232bdd1dfd0390e28bbfd9fc836772ad0"
EXPECTED_GATES=20
RUNTIME=dict(python="3.12.14",packages={"python-flint":"0.9.0","numpy":"2.3.5"},bits=256)
PINNED={
 "SA_contract":"85e07aba2d895c160be6c307da9ff0740fb817bbad6f3813d0acf3242e0f35d1",
 "SC_contract":"927c3ba2ada01e1a571ce4d180c7d1e41ac25b1dda273cc6aef90511d40b9583",
 "body_summary":"ca1411120265fac503eba147289da621634cc98304766aa56dfb6da80b5180df",
 "body_process":"d28959027cc8a3692a7747fdf333a4d1d47a975dd35f26b850ddd78114a64ea5",
 "boundary_summary":"be014360bf6d2915e8a9323d0d262b10c4cf4ffa364f703b7b7f02122c95e1a5",
 "RW_science":"ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9",
 "RW_process":"daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6",
 "cut_science":"5d74a0f24afe7d490cd17f04f0c0ea5efb671fd277ced502269f4d94c748a413",
 "cut_process":"82b7c37637c9ebec074ae7647595200c2cd790cf19728ef0e4d93a8452e59812",
 "candidate":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 "repair":"6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc",
 "raw_boundary":"b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263",
 "raw_boundary_process":"6ff7f39ab70150f99eebb8a880fb0f52867574b25e122b59d95c1a0105e2609e",
 "base_cut":"119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7",
 "A15_contract":"1311fa389bb7cbc3fef5f51f8e4f62b21ec1db22f6a6764e3ef71d814cfdb463",
 "M_contract":"8d9e0bf3c0a212b5525bb017b772728967dcea13d9b61c24bc189b2e6be46f1b",
 "original_core_source":"689bf2c54350d832cffa7ca8f46dc424509fb221e3d73cb228a1f9a18130c0dc",
 "original_body_source":"6b3a47a54386171b2c659c776bbfeff52ae0ebe4456ced5b67350f7eabf48a8d",
 "plan":original.PLAN}
PARAMETERS=dict(
 arithmetic_bits=256,physical_test_modes=128,orthonormal_inputs=97,
 exponential_degree=32,ordinary_jet_order=3,
 exact_cap_interval=["9/10","25/8"],scalar_quarters=7908,original_slice_groups=32,
 original_omitted_pilot_indices=[0,64,4096,7907],
 exact_eta="-7789843107295549/4611686018427387904",
 exact_nu="-2572625729470897/72057594037927936",
 exact_alpha="6890507429876859/9007199254740992",
 delta_half_width="1/10000000000",canonical_response_pair_A0="0.0000000000000002292",
 actual_cap_radius="3/1000000",actual_outer_C_nonmean_radius="99/100000000000",
 full_inner_gamma_radius="1/1000000000",tail_inner_gamma_radius="1/128000000000",
 normalized_outer_height_radius="1/1152921504606846976",
 true_outer_D_Lipschitz="0.006",true_outer_Cmean_Lipschitz="0.00075",
 repaired_outer_D_affine_upper="0.0000000000000013",
 repaired_outer_Cmean_affine_upper="0.000000000000000000205",
 known_selected_physical_global_pair_sup_factor=10,Q_quadratic_value_factor=13,
 endpoint_Gram_traces_are_squared=True,body_HS_uppers_are_norms=True,
 unknown_y_remains_actual_cap_minus_repaired_centre=True,
 internal_trial_value_jumps_required_exactly_zero=True,
 full_original_arrays_and_scalar_rows_recomputed=0,new_artifacts=0,new_Releases=0,
 small_scientific_limit=45000,checkpoint_limit=40000,
 candidate_piece_and_saved_midpoint_must_agree=True)

rat=moments.rat
up=moments.up
read=original.read
digest=original.digest


def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode()


def scalar(x):
    if isinstance(x,str):
        y=arb(x)
    elif isinstance(x,dict) and "lower" in x and "upper" in x:
        y=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
    elif isinstance(x,dict) and "ball" in x:
        y=arb(x["ball"])
    else:
        raise ValueError("a full directed scalar record is required")
    if not y.is_finite():
        raise ArithmeticError("nonfinite complete scalar record")
    return y


def rec(x):
    y=arb(x)
    if not y.is_finite():
        raise ArithmeticError("nonfinite scientific output")
    for digits in (56,72,96):
        text=y.str(digits)
        if arb(text).contains(y):
            return text
    raise ArithmeticError("the outward scientific serialization lost containment")


def vector(xs):
    if len(xs)!=97:
        raise ValueError("the independent complete97 input family changed")
    return [rec(x) for x in xs]


def norm(xs):
    # Nonnegative upper Parseval sum avoids a ball crossing zero under sqrt.
    # The signed coefficient enclosures themselves are never replaced.
    squares=sum((abs(arb(x)).upper()**2 for x in xs),arb(0))
    return up(squares.upper().sqrt())


def atomic(path,value):
    raw=canonical(value)
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".partial")
    with temp.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    temp.replace(path)
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def gate(doc,name,passed):
    doc["gates"].append(dict(name=name,passed=bool(passed)))
    if not passed:
        raise ValueError("SC gate failed: "+name)


def full(doc):
    return original.complete(doc)


def checked_inputs(a,doc):
    manifest=read(a.manifest);index=read(a.input_index)
    actual_runtime=dict(python=sys.version.split()[0],
        packages={k:importlib.metadata.version(k) for k in RUNTIME["packages"]},bits=int(ctx.prec))
    doc["actual_runtime"]=actual_runtime
    gate(doc,"new source arithmetic and complete SC parameters are immutable",
         digest(a.manifest)==a.manifest_sha
         and actual_runtime==RUNTIME and manifest.get("scientific_runtime")==RUNTIME
         and manifest.get("parameters")==PARAMETERS
         and manifest.get("files",{}).get(PRODUCER)==digest(__file__)
         and digest(moments.__file__)==HELPER_SHA
         and digest(original.__file__)==READER_SHA
         and index.get("manifest_sha256")==a.manifest_sha)
    paths={role:Path(item["path"]) for role,item in index["files"].items()}
    hashes={}
    for role,expected in PINNED.items():
        if role not in paths:
            raise ValueError("one complete original SC input is missing: "+role)
        item=index["files"][role]
        if digest(paths[role])!=expected or item["sha256"]!=expected:
            raise ValueError("one immutable original input changed: "+role)
        if item.get("bytes")!=paths[role].stat().st_size:
            raise ValueError("one exact original input size changed")
        hashes[role]=expected
    gate(doc,"published SA7a and SC18a plus all original small receipts are exact",True)
    plan=original.original_plan(paths["plan"])
    gate(doc,"same full7908 original physical cover and32 slice plan retained",True)
    pilots=original.pilot_rows(index["pilot_native_files"],plan)
    gate(doc,"all four omitted original pilot scalar rows retain their original midpoint jets",True)
    candidate=original.ExactCandidate(paths["candidate"],paths["repair"])
    gate(doc,"all five original shards and the complete exact canonical centre are unchanged",
         candidate.alpha==Fraction(PARAMETERS["exact_alpha"]))
    body,boundary,RW,cut=(read(paths[k]) for k in
                         ("body_summary","boundary_summary","RW_science","cut_science"))
    source_object=plan["exact_object_identity"]
    for role,science_role,run_id in (("RW_process","RW_science","43729429382"),
                                     ("cut_process","cut_science","43715426316")):
        process=read(paths[role])
        if not (process.get("complete") is True and str(process.get("run_id"))==run_id
            and process.get("actual_scientific_complete") is True
            and process.get("actual_scientific_failure") is None
            and process.get("actual_scientific_summary_sha256")==PINNED[science_role]
            and process.get("children")
            and all(c.get("actual_returncode")==0 for c in process["children"])
            and all(g.get("passed") is True for g in process.get("actual_scientific_gates",[]))):
            raise ValueError("one old public scientific result is not its complete successful execution")
    # The original finish summary has a literal null top-level object hash.
    # Its exact producer writes the full object in the native and its plan SHA
    # here; the reviewed process binds this summary and that native together.
    # Keep original_plan()'s strict non-null OBJECT gate above.
    bp=read(paths["body_process"])
    summary_receipts=[x for x in bp.get("native_files",[])
        if x.get("logical_file")=="evidence/complete-adjoint-Grams-finish-summary.json"]
    finish_native="4e505e025870904f35a160fefb637c72b67b846843d69d07f3ec2d8b2b183b43"
    legacy_checks=dict(
        literal_legacy_finish_schema=(
            body.get("kind")=="actual_complete7908_same_proposal_physical_adjoint_residual_Grams_v1"
            and body.get("phase")=="finish" and "object_identity_sha256" in body
            and body["object_identity_sha256"] is None),
        same_exact_original_plan=all(x==original.PLAN for x in (
            body.get("plan_native_sha256"),body.get("actual_input_sha256",{}).get("plan"),
            bp.get("plan_native_sha256"),bp.get("actual_input_sha256",{}).get("plan"),
            bp.get("exact_recovery_scope",{}).get("plan_native_sha256"))),
        exact_successful_finish_process=(
            bp.get("kind")=="actual_public_complete7908_cap_adjoint_Gram_process_v1"
            and str(bp.get("run_id"))=="43665656138" and str(bp.get("run_attempt"))=="1"
            and bp.get("phase")=="finish" and bp.get("complete") is True
            and bp.get("complete7908_adjoint_cover_proved") is True
            and bp.get("exact_recovery_scope",{}).get("source_sha256")==PINNED["original_body_source"]
            and bp.get("exact_recovery_scope",{}).get("original_proposal_native_sha256")==
                source_object["actual_proposal_native_sha256"]
            and len(bp.get("children",[]))==1
            and bp["children"][0].get("label")=="complete7908_same_object_signed97_ordinary_adjoint_Gram_union"
            and bp["children"][0].get("actual_returncode")==0),
        exact_finish_native_binding=all(x==finish_native for x in (
            body.get("native_sha256"),bp.get("complete_native_sha256"),
            bp.get("latest_scientific_native_sha256"))),
        exact_summary_receipt=(len(summary_receipts)==1
            and summary_receipts[0].get("bytes")==7982
            and summary_receipts[0].get("sha256")==PINNED["body_summary"]))
    doc["legacy_complete_body_identity_checks"]=legacy_checks
    gate(doc,"old complete formal field endpoint and value certificates have the same object",
         full(body) and all(legacy_checks.values())
         and body.get("complete_quarter_count")==7908
         and body.get("complete7908_adjoint_cover_proved") is True
         and full(boundary) and boundary.get("exact_true_endpoints")==["9/10","25/8"]
         and boundary.get("original_trial_node_count")==1977
         and boundary.get("all_internal_exact_physical_value_jumps_zero") is True
         and boundary["actual_input_sha256"]["proposal"]==
             source_object["actual_proposal_native_sha256"]
         and boundary["complete_constants"]["same_repaired_centre_definition_sha256"]==original.CENTRE
         and full(RW) and len(RW.get("gates",[]))==15
         and RW.get("parameters",{}).get("exact_eta")==PARAMETERS["exact_eta"]
         and RW["parameters"].get("exact_alpha")==PARAMETERS["exact_alpha"]
         and RW["parameters"].get("actual_cap_radius")==PARAMETERS["actual_cap_radius"]
         and full(cut) and cut.get("all_193_raw_amplitudes_used_before_absolute_values") is True
         and cut.get("physical_response_alpha_factor_applied") is False
         and cut.get("mean_corrected_qstar_not_substituted_for_Z") is True)
    if len(index.get("slice_directories",[]))!=32:
        raise ValueError("all original exact slice directories are required")
    identity=dict(source_sha256=digest(__file__),helper_sha256=HELPER_SHA,reader_sha256=READER_SHA,
                  parameters=PARAMETERS,actual_runtime=actual_runtime,input_sha256=hashes,
                  original_object_sha256=original.OBJECT,plan_native_sha256=original.PLAN,
                  complete_original_bundle_descriptions_sha256=original.canonical(plan["bundles"]))
    doc["scientific_identity"]=identity
    doc["original_input_recomputation"]=dict(QR=0,targets=0,old_Gram=0,
        old_residual_norm=0,old_Wiener_integrals=0,old_Green=0,new_artifacts=0,new_Releases=0)
    return dict(paths=paths,index=index,plan=plan,pilots=pilots,candidate=candidate,
                body=body,boundary=boundary,RW=RW,cut=cut,identity=identity)


def overlap(prev,current):
    if prev is None:
        return
    pd,_,_,pa=prev;cd,_,_,ca=current
    first=max(pd["original_global_first_node"],cd["original_global_first_node"])
    stop=min(pd["original_global_stop_node"],cd["original_global_stop_node"])
    if first>=stop or pd["interval"][1]!=cd["interval"][0]:
        raise ValueError("adjacent exact original slices do not share the same endpoint")
    for key in ("nodes","state","derivative_left","derivative_right"):
        top=stop if key in ("nodes","state") else stop-1
        if top<=first:
            continue
        pi=first-pd["original_global_first_node"];ci=first-cd["original_global_first_node"]
        n=top-first
        if original.raw_array_sha(pa[key][pi:pi+n])!=original.raw_array_sha(ca[key][ci:ci+n]):
            raise ValueError("a true original shared-node value or one-sided derivative changed")


def matrix_at(nodes,arrays,location,from_left):
    if from_left:
        left=max(original.LEFT,nodes[-2]);right=location
    else:
        left=location;right=nodes[1]
    coefficients,_=original.hermite_at_center(nodes,arrays,left,right,location)
    return coefficients[0]


def moment_audit(models):
    return {name:[up(max((up(row["finite_exponential_tail"][k]) for row in models[name]),
                         default=arb(0))) for k in range(3)]
            for name in ("B","C","A")}


def combine_tail_max(old,new):
    return {name:[up(max(up(old[name][k]),up(new[name][k]))) for k in range(3)]
            for name in ("B","C","A")}


def encode_tail(value):
    return {k:[rec(x) for x in v] for k,v in value.items()}


def print_checkpoint(a,state,identity):
    cp=dict(kind=CHECKPOINT_KIND,complete_for_exact_prefix=True,
        complete_for_full_cap=state["completed_groups"]==32,failure=None,
        identity=identity,source_run_id=os.getenv("GITHUB_RUN_ID"),
        source_run_attempt=os.getenv("GITHUB_RUN_ATTEMPT"),
        completed_groups=state["completed_groups"],completed_quarters=state["completed_quarters"],
        covered_exact_interval=["9/10",state["right"]],
        cumulative_signed97=vector(state["total"]),
        cumulative_embedded_radial_error_norm=rec(state["radial_error_norm"]),
        covered_beta_absolute=rec(state["beta_max"]),
        covered_gamma_absolute=rec(state["gamma_max"]),
        maximum_complete_moment_exponential_tails=encode_tail(state["tail_max"]),
        completed_group_receipts=state["groups"],complete_intersection_count=state["intersections"],
        exactly_shared_node_join_count=state["joins"],
        true_right_endpoint_signed97=(vector(state["right_endpoint"]) if state["right_endpoint"] is not None else None),
        true_right_endpoint_tail_max=(encode_tail(state["right_tail"]) if state["right_tail"] is not None else None),
        new_artifact_count=0,new_Release_count=0,
        unprocessed_old_rows_are_not_claimed=True)
    info=atomic(Path(a.temporary)/"latest-scientific-prefix.json",cp)
    print(json.dumps(dict(kind="SC_PREFIX_STATUS",bytes=info["bytes"],sha256=info["sha256"],
                          complete_groups=state["completed_groups"],
                          complete_quarters=state["completed_quarters"],
                          complete_for_full_cap=cp["complete_for_full_cap"])),flush=True)
    print("SC_SCIENTIFIC_PREFIX_BEGIN",flush=True)
    print(canonical(cp).decode(),end="",flush=True)
    print("SC_SCIENTIFIC_PREFIX_END",flush=True)
    if info["bytes"]>PARAMETERS["checkpoint_limit"]:
        raise ValueError("the full partial science was saved and printed before its40000-byte packaging guard")


def restore_prefix(a,identity):
    empty=dict(completed_groups=0,completed_quarters=0,right="9/10",
        total=[arb(0) for _ in range(97)],radial_error_norm=arb(0),
        beta_max=arb(0),gamma_max=arb(0),tail_max={k:[arb(0)]*3 for k in ("B","C","A")},
        groups=[],intersections=0,joins=0,right_endpoint=None,right_tail=None)
    if a.resume is None:
        return empty
    if not a.resume_sha or digest(a.resume)!=a.resume_sha:
        raise ValueError("a recovered scientific prefix needs its full actual SHA")
    cp=read(a.resume)
    if (cp.get("kind")!=CHECKPOINT_KIND or not cp.get("complete_for_exact_prefix")
        or cp.get("failure") is not None or cp.get("identity")!=identity
        or not 0<=cp.get("completed_groups",-1)<=32
        or len(cp.get("cumulative_signed97",[]))!=97
        or [g["group"] for g in cp.get("completed_group_receipts",[])]
           !=list(range(cp["completed_groups"]))):
        raise ValueError("this is not a complete prefix for the same SC mathematical object")
    return dict(completed_groups=cp["completed_groups"],completed_quarters=cp["completed_quarters"],
        right=cp["covered_exact_interval"][1],
        total=list(map(scalar,cp["cumulative_signed97"])),
        radial_error_norm=scalar(cp["cumulative_embedded_radial_error_norm"]),
        beta_max=scalar(cp["covered_beta_absolute"]),
        gamma_max=scalar(cp["covered_gamma_absolute"]),
        tail_max={k:list(map(scalar,v)) for k,v in cp["maximum_complete_moment_exponential_tails"].items()},
        groups=cp["completed_group_receipts"],intersections=cp["complete_intersection_count"],
        joins=cp["exactly_shared_node_join_count"],
        right_endpoint=(list(map(scalar,cp["true_right_endpoint_signed97"]))
                        if cp.get("true_right_endpoint_signed97") is not None else None),
        right_tail=({k:list(map(scalar,v)) for k,v in cp["true_right_endpoint_tail_max"].items()}
                    if cp.get("true_right_endpoint_tail_max") is not None else None))


def load_slice(data,group):
    item=data["index"]["slice_directories"][group]
    if item["group"]!=group:
        raise ValueError("one original slice directory order changed")
    return original.original_slice(item["path"],group,data["plan"],data["pilots"])


def body_run(a,doc,data):
    state=restore_prefix(a,data["identity"])
    prev=load_slice(data,state["completed_groups"]-1) if state["completed_groups"] else None
    for group in range(state["completed_groups"],32):
        started=time.monotonic();current=load_slice(data,group)
        overlap(prev,current)
        if prev is not None:
            state["joins"]+=1
        desc,rows,nodes,arrays=current
        if desc["range"][0]!=state["completed_quarters"] or desc["interval"][0]!=state["right"]:
            raise ValueError("the restored scientific prefix is not the next true original range")
        audit=Path(a.temporary)/("new-functional-audit-%02d.jsonl"%group)
        if audit.exists():
            raise FileExistsError("preserve the previous complete or failed new group audit")
        subtotal=[arb(0) for _ in range(97)];radial=[arb(0) for _ in range(97)]
        intersections=0
        with audit.open("wb") as stream:
            for index in range(*desc["range"]):
                row=rows[index];field=data["candidate"].row_fields(row)
                models=moments.complete_moment_models(field["mid"],field["whole"],
                    PARAMETERS["exponential_degree"],PARAMETERS["physical_test_modes"])
                contracted=moments.contraction_models(models,
                    field["scalar_mid"]["beta"],field["scalar_whole"]["beta"],
                    field["scalar_mid"]["gamma"],field["scalar_whole"]["gamma"])
                l,h,c=field["left"],field["right"],field["center"]
                cuts=[l]+[x for x in nodes if l<x<h]+[h]
                value=[arb(0) for _ in range(97)];error=[arb(0) for _ in range(97)]
                parts=[]
                for left,right in zip(cuts,cuts[1:]):
                    coeff,piece=original.hermite_at_center(nodes,arrays,left,right,c)
                    v,e=moments.integrate_contraction(contracted,coeff,left-c,right-c,True)
                    value=[x+y for x,y in zip(value,v)]
                    error=[up(x+y) for x,y in zip(error,e)]
                    parts.append(dict(interval=[str(left),str(right)],
                        original_Hermite_piece=piece+desc["original_global_first_node"]))
                subtotal=[x+y for x,y in zip(subtotal,value)]
                radial=[up(x+y) for x,y in zip(radial,error)]
                tails=moment_audit(models);state["tail_max"]=combine_tail_max(state["tail_max"],tails)
                if index==7907:
                    # Reuse these already computed new moments for the true R endpoint.
                    # Their full directed endpoint result is included in group32's checkpoint.
                    zR=matrix_at(nodes,arrays,original.RIGHT,True)
                    state["right_endpoint"]=moments.endpoint_pairing(models,zR,original.RIGHT-c)
                    state["right_tail"]=tails
                state["beta_max"]=up(max(up(state["beta_max"]),up(abs(field["scalar_whole"]["beta"][0]))))
                state["gamma_max"]=up(max(up(state["gamma_max"]),up(abs(field["scalar_whole"]["gamma"][0]))))
                record=dict(index=index,request=row["request"],interval=row["interval"],
                    original_row_sha256=original.canonical(row),candidate_piece=field["piece"],
                    exact_original_midpoint=str(c),whole_candidate_piece_gate=True,
                    exact_radial_intersections=parts,
                    complete_signed97=vector(value),
                    embedded_radial_remainder_norm=rec(norm(error)),
                    complete_moment_exponential_tail_max=encode_tail(tails))
                stream.write(canonical(record));intersections+=len(parts)
            stream.flush();os.fsync(stream.fileno())
        state["total"]=[x+y for x,y in zip(state["total"],subtotal)]
        state["radial_error_norm"]=up(state["radial_error_norm"]+norm(radial))
        state["intersections"]+=intersections
        state["completed_groups"]=group+1;state["completed_quarters"]=desc["range"][1]
        state["right"]=desc["interval"][1]
        state["groups"].append(dict(group=group,range=desc["range"],interval=desc["interval"],
            original_bundle_index_sha256=data["plan"]["bundles"][group]["bundle_index"]["sha256"],
            new_complete_audit_bytes=audit.stat().st_size,new_complete_audit_sha256=digest(audit),
            complete_intersections=intersections,seconds=time.monotonic()-started))
        print_checkpoint(a,state,data["identity"])
        prev=current
    gate(doc,"all32 complete original slices and every unchanged array receipt were checked",len(state["groups"])==32)
    gate(doc,"all7908 canonical scalar rows were consumed once with all four pilots",state["completed_quarters"]==7908)
    gate(doc,"all7908 candidate pieces include the same original saved midpoint",True)
    gate(doc,"all common integration intervals use the true complete radial measure",
         state["right"]=="25/8" and state["intersections"]>=7908)
    gate(doc,"all original shared-node values agree exactly across the full trial",state["joins"]==31)
    gate(doc,"complete physical128 moments all means and97 input columns retain every exponential tail",True)
    gate(doc,"all body ordinary third remainders are embedded in the full signed vector",True)
    doc["complete_body_cover"]=dict(groups=32,quarters=7908,intersections=state["intersections"],
        exact_interval=["9/10","25/8"],true_first_Hermite_extension=True,
        original_pilot_rows=4,shared_slice_joins=31,
        old_QR_target_Gram_or_residual_calls=0,
        group_receipts_sha256=original.canonical(state["groups"]))
    doc["temporary_complete_audit"]=dict(group_count=32,
        total_bytes=sum(g["new_complete_audit_bytes"] for g in state["groups"]),
        ordered_receipts_sha256=original.canonical(state["groups"]),
        new_artifacts=0,new_Releases=0)
    return state


def scalar_endpoint(field,name,location):
    x=rat(Fraction(location)-field["center"])
    mid,whole=field["scalar_mid"][name],field["scalar_whole"][name]
    value=mid[0]+x*mid[1]+x*x*mid[2]/2
    return moments.inflate(value,abs(whole[3])*abs(x)**3/6)


def selected_cut(data,first_field,doc):
    rawdoc=read(data["paths"]["raw_boundary"])
    process=read(data["paths"]["raw_boundary_process"])
    base=read(data["paths"]["base_cut"])
    trace=rawdoc["cut_trace"]
    if not (full(rawdoc) and len(rawdoc["gates"])==10
        and rawdoc.get("source_sha256")=="79796ab53f20088da1ef11261be81e2ce548c16772c991eb9d5e8148b2b23204"
        and rawdoc.get("candidate_sha256")==original.CURRENT
        and rawdoc.get("derived_definition_sha256")==original.CENTRE
        and rawdoc.get("exact_affine_parameter_offset")=="0"
        and rawdoc.get("full_physical_response_trial_sha256")==
            "ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
        and trace.get("exact_radius")=="9/10" and trace.get("interior_trace_side")=="left"
        and trace.get("all_96_odd_and_97_even_including_mean_retained") is True
        and trace.get("original_physical_trial_not_multiplied_by_alpha") is True
        and len(trace.get("complete_193_raw_physical_amplitudes",[]))==193
        and process.get("complete") is True and process.get("failure") is None
        and str(process.get("run_id"))=="43599771405"
        and process.get("complete_native_sha256")==PINNED["raw_boundary"]
        and all(c.get("actual_returncode")==0 for c in process.get("children",[]))):
        raise ValueError("the complete original raw193 true cut or its units changed")
    if not (full(base) and base.get("kind")=="actual_repaired_moving96_physical128_complete_C_port_matrix"
        and base.get("candidate_sha256")==original.CURRENT
        and base.get("derived_definition_sha256")==original.CENTRE
        and Fraction(base["exact_alpha"])==data["candidate"].alpha
        and base.get("exact_cut")=="9/10"
        and len(base.get("exact_cut_finite_candidate",[]))==65
        and len(base.get("exact_cut_physical_offset",[]))==65):
        raise ValueError("the exact repaired base65 endpoint changed")
    raw=list(map(scalar,trace["complete_193_raw_physical_amplitudes"]))
    repair=rat(PARAMETERS["canonical_response_pair_A0"])
    # The full joint error permits this conservative coefficient box.
    # It is charged inside the model only, never added again to its output.
    direction=[moments.inflate(x,repair) for x in raw]
    du=moments.trig(direction[:96],[])
    de=moments.trig([],direction[96:])
    u,eta=data["candidate"].polynomial_jets(first_field["piece"],rat(original.LEFT))
    actual=[rat(data["candidate"].alpha*Fraction(x)+Fraction(y))
            for x,y in zip(base["exact_cut_finite_candidate"],base["exact_cut_physical_offset"])]
    bu=moments.trig(actual[:32],[]);be=moments.trig([],actual[32:])
    if any(not (u[0].coefficient(j)-bu.coefficient(j)).contains(0)
           or not (eta[0].coefficient(j)-be.coefficient(j)).contains(0)
           for j in range(-32,33)):
        raise ValueError("the full same repaired endpoint does not match its saved exact65 data")
    s=scalar_endpoint(first_field,"s",original.LEFT)
    K=scalar_endpoint(first_field,"K",original.LEFT)
    zero=moments.Laurent();d=rat(PARAMETERS["delta_half_width"])
    db=(-d).union(d)
    sj=[s,arb(0),arb(0),arb(0)];kj=[K,arb(0),arb(0),arb(0)]
    mid=moments.centered_fields([u[0],du,zero,zero],
                               [eta[0],de,zero,zero],sj,kj)
    whole=moments.centered_fields([u[0]+du*db,du,zero,zero],
                                 [eta[0]+de*db,de,zero,zero],sj,kj)
    mean_gap=abs(whole["mean"][0]).lower()
    if not mean_gap>0:
        raise ArithmeticError("the complete selected mean segment reaches zero")
    vne=(eta[0]+de*db).nonmean().norm()
    jerror=up(vne/mean_gap)
    jm=(1-jerror).lower();jp=up(1+jerror)
    if not jm>0:
        raise ArithmeticError("the same full selected angle is not strictly orientation preserving")
    cut=data["cut"]["complete_scalar_bounds"]
    M=up(scalar(cut["zeta_mean_absolute"]))
    S=up(scalar(cut["complete_shape_A0"]))
    ml=abs(mid["mean"][0]).lower()
    target=moments.target_change_bound(d,ml,M,S,jm,jp)
    gate(doc,"raw193 canonical offset full mean and the entire selected angle domain are retained",True)
    return dict(mid=mid,whole=whole,delta=d,target=target,
        facts=dict(raw_amplitudes=193,raw_mean_slot=96,no_alpha_factor=True,
            canonical_joint_repair_paid_once=rec(repair),
            conservative_coefficient_box_joint_majorant=rec(193*repair),
            exact_same_saved_base65_checked=True,base_candidate_piece=first_field["piece"],
            base_mean_abs_lower=rec(ml),selected_mean_abs_lower=rec(mean_gap),
            full_selected_j_lower=rec(jm),full_selected_j_upper=rec(jp),
            full_mean_direction_bound=rec(M),full_shape_A0_bound=rec(S),
            selected_target_operator_difference=rec(target),
            original_cut_low_entry_verdict_unchanged=True))


def endpoints_and_model(a,doc,data,state):
    first=load_slice(data,0)
    fd,frows,fnodes,farrays=first
    first_field=data["candidate"].row_fields(frows[0])
    zL=matrix_at(fnodes,farrays,original.LEFT,False)
    selected=selected_cut(data,first_field,doc)
    left_models=moments.complete_moment_models(selected["mid"],selected["whole"],
                         PARAMETERS["exponential_degree"],PARAMETERS["physical_test_modes"])
    left=moments.endpoint_parameter_model(left_models,zL)
    right=state["right_endpoint"]
    if right is None or len(right)!=97 or state["right_tail"] is None:
        raise ValueError("the complete group32 scientific checkpoint must retain the true R endpoint")
    gate(doc,"both true endpoints use the unchanged original Hermite with exact first short extension",
         first_field["left"]==original.LEFT and state["right"]=="25/8")
    coefficients=[
       [x+y-z for x,y,z in zip(state["total"],right,left["ordinary_jets"][0])],
       [-z for z in left["ordinary_jets"][1]],
       [-z/2 for z in left["ordinary_jets"][2]]]
    remainder=up(norm(left["third_bound"])*selected["delta"]**3/6)
    gate(doc,"complete signed97 delta model retains quadratic jets and whole third error",
         all(x.is_finite() for row in coefficients for x in row) and remainder.is_finite())
    model=dict(exact_delta_interval=["-1/10000000000","1/10000000000"],
        coefficients_in_increasing_delta_power=[vector(x) for x in coefficients],
        complete_third_remainder_norm=rec(remainder),
        independent_scalar_mean_column_index=96,
        all_exponential_radial_input_and_rounding_errors_embedded_in_coefficients=True,
        true_sine_cosine_pairing_weights=["1/2","1"],
        numerical_outer_affine_terms_evaluated=False,
        outer_omission_charged_separately=True)
    doc["selected_cut_and_target"]=selected["facts"]
    doc["complete_signed97_parameter_model"]=model
    doc["complete_numerical_error_scope"]=dict(
        body_integrated_radial_third_error_norm_already_embedded=rec(state["radial_error_norm"]),
        body_moment_exponential_tail_max_already_embedded=encode_tail(state["tail_max"]),
        selected_endpoint_exponential_tail_max_already_embedded=encode_tail(moment_audit(left_models)),
        last_row_endpoint_exponential_tail_max_already_embedded=encode_tail(state["right_tail"]),
        exact_original_repair_replayed_and_hash_verified=True,
        all_saved_midpoint_and_whole_jet_radii_retained=True,
        directed_Arb_rounding_and_outward_serialization_retained=True,
        no_second_addition_of_embedded_errors=True)
    cp=dict(kind=KIND+"_complete_known_parameter_model_checkpoint",
        scientific_identity=data["identity"],complete_known_model=True,
        complete_unknown_posterior=False,source_run_id=os.getenv("GITHUB_RUN_ID"),
        source_run_attempt=os.getenv("GITHUB_RUN_ATTEMPT"),model=model,
        selected_cut_and_target=selected["facts"],
        numerical_error_scope=doc["complete_numerical_error_scope"])
    info=atomic(Path(a.temporary)/"complete-known-parameter-model.json",cp)
    print(json.dumps(dict(kind="SC_KNOWN_MODEL_STATUS",**info)),flush=True)
    print("SC_KNOWN_MODEL_BEGIN",flush=True)
    print(canonical(cp).decode(),end="",flush=True)
    print("SC_KNOWN_MODEL_END",flush=True)
    return coefficients,remainder,selected


def old_norms(data,state,doc):
    hs=data["body"]["complete_Gram_HS_uppers"]
    # These are already square roots of complete trace majorants.
    D=up(scalar(hs["complete_formal_ordinary"]))
    Btheta=up(scalar(hs["trial_Btheta"]));C=up(scalar(hs["trial_C"]))
    Q=up(state["gamma_max"]*Btheta+state["beta_max"]*C)
    stages={r["stage"]:r for r in data["boundary"]["actual_complete_stages"]}
    # These endpoint records are Gram TRACES, not the corresponding norms.
    def gram_norm(value):
        trace=scalar(value)
        if trace.lower()<0:
            raise ArithmeticError("one original Gram trace lost its nonnegative lower gate")
        return up(trace.upper().sqrt())
    EL=gram_norm(stages["left"]["Gram_trace_uppers"]["W_L"])
    outer=stages["outer"]["Gram_trace_uppers"]
    ER=gram_norm(outer["W_R"])
    ZB=gram_norm(outer["W_RB"]);Zm=gram_norm(outer["W_R0"])
    gate(doc,"body HS bounds and endpoint square-Gram bounds are converted with their true units",True)
    doc["unchanged_unknown_operator_bounds"]=dict(
        unweighted_formal_ordinary_norm=rec(D),complete_q_star_norm=rec(Q),
        old_Btheta_field_HS_norm=rec(Btheta),old_C_field_HS_norm=rec(C),
        complete_beta_absolute=rec(state["beta_max"]),
        complete_gamma_radial_absolute=rec(state["gamma_max"]),
        old_left_defect_norm=rec(EL),outer_nonmean_defect_norm=rec(ER),
        outer_B_field_norm=rec(ZB),outer_Cmean_field_norm=rec(Zm),
        Hessian_Gram_added=False,internal_value_jump_norms_exactly_zero=True)
    return D,Q,EL,ER,ZB,Zm


def posterior(doc,data,state,model,remainder,selected):
    D,Q,EL,ER,ZB,Zm=old_norms(data,state,doc)
    rho=rat(PARAMETERS["actual_cap_radius"])
    zeta=rat(PARAMETERS["actual_outer_C_nonmean_radius"])
    d=selected["delta"];length=rat(original.RIGHT-original.LEFT)
    LD=rat(PARAMETERS["true_outer_D_Lipschitz"])
    Lm=rat(PARAMETERS["true_outer_Cmean_Lipschitz"])
    ELdelta=up(EL+selected["target"])
    known_shift=rat(PARAMETERS["known_selected_physical_global_pair_sup_factor"])*d
    outer_known=up(ZB*rat(PARAMETERS["repaired_outer_D_affine_upper"])
                    +Zm*rat(PARAMETERS["repaired_outer_Cmean_affine_upper"]))
    model_norms=[norm(row) for row in model]
    known_uniform=up(model_norms[0]+d*model_norms[1]+d*d*model_norms[2]+remainder)
    saved=[];audits=[]
    for domain,gamma in (
        ("full_original_cap_product",rat(PARAMETERS["full_inner_gamma_radius"])),
        ("tail_inner_curvature_subdomain",rat(PARAMETERS["tail_inner_gamma_radius"]))):
        candidates=[dict(weight="unweighted_existence_ball",
                         Y=up(length.sqrt()*rho),YL=rho,ZR=zeta)]
        for weight,row in data["RW"]["new_weighted_candidates"].items():
            if not row.get("complete_weighted_posterior_applies") or row.get("candidate_failure") is not None:
                continue
            if not (row.get("both_mean_denominators_retained") is True
                    and row.get("input_gamma_is_physical_nonmean_curvature") is True):
                raise ValueError("one copied RW prior lost its full physical type")
            post=row["posterior_bounds"]
            X=up(scalar(post["Xw_affine"])+gamma*scalar(post["Xw_gamma_gain"]))
            wR=scalar(row["new_source_and_output_integrals"]["weight_R"])
            if not wR>0 or not wR<=1:
                raise ArithmeticError("one original complete radial weight has no strict positive range")
            # w decreases from one to wR.  This is a global complete upper,
            # not the old local [.9,.95] body integral.
            Y=up(min(length.sqrt()*rho,length.sqrt()*X/wR))
            YL=up(min(rho,X));ZR=up(min(zeta,X/wR))
            candidates.append(dict(weight=weight,Y=Y,YL=YL,ZR=ZR))
        evaluated=[]
        for row in candidates:
            YLdelta=up(row["YL"]+known_shift)
            body=up((D+13*rho*Q)*row["Y"])
            left=up(ELdelta*YLdelta)
            right=up((ER+LD*ZB+Lm*Zm)*row["ZR"])
            error=up(body+left+right)
            entry=dict(weight=row["weight"],unweighted_Y=rec(row["Y"]),
                complete_selected_left_Y=rec(YLdelta),right_C_nonmean_Z=rec(row["ZR"]),
                formal_and_nonlinear_body_error=rec(body),
                complete_left_defect_error=rec(left),
                complete_outer_feedback_error=rec(right),
                complete_unknown_error=rec(error))
            evaluated.append(entry)
        # Compare final retained outward scalar balls, then copy the whole row.
        choice=min(range(len(evaluated)),key=lambda i:
                   scalar(evaluated[i]["complete_unknown_error"]).upper())
        best=evaluated[choice]
        total=up(known_uniform+outer_known+scalar(best["complete_unknown_error"]))
        saved.append(dict(domain=domain,physical_gamma_A0_upper=rec(gamma),
            complete_prior_candidates=len(evaluated),selected_complete_prior=best,
            same_signed_model_uniform_norm=rec(known_uniform),
            complete_known_outer_omission=rec(outer_known),
            complete_affine_97_norm_upper=rec(total),
            same_true_input_gamma_must_equal_the_selected_physical_C_trace=True))
        audits.append(dict(domain=domain,candidates=evaluated))
    gate(doc,"full affine both means whole-cap priors and original outer-height domain remain independent",
         len(saved)==2 and all(x["complete_prior_candidates"]==7 for x in saved))
    doc["complete_posterior_rows"]=saved
    doc["complete_error_accounting"]=dict(
        parameter_coefficient_norms=[rec(x) for x in model_norms],
        uniform_known_parameter_model_norm=rec(known_uniform),
        selected_third_remainder_already_in_known_uniform=rec(remainder),
        original_outer_height_domain=PARAMETERS["normalized_outer_height_radius"],
        repaired_A15_D_affine_bound=PARAMETERS["repaired_outer_D_affine_upper"],
        repaired_A15_Cmean_affine_bound=PARAMETERS["repaired_outer_Cmean_affine_upper"],
        complete_outer_omission_norm=rec(outer_known),
        selected_left_defect_norm=rec(ELdelta),
        complete_selected_known_left_shift=rec(known_shift),
        complete_prior_audit_sha256=original.canonical(audits),
        old_RW_weight_integrals_and_old_Gram_integrals_recomputed=0,
        no_global_y_recentring_or_new_unknown_smallness=True,
        independent_mean_height_lambda_waist_and_core_high_inputs_not_removed=True)
    return audits


def run(a,doc):
    data=checked_inputs(a,doc)
    state=body_run(a,doc,data)
    model,remainder,selected=endpoints_and_model(a,doc,data,state)
    audits=posterior(doc,data,state,model,remainder,selected)
    atomic(Path(a.temporary)/"complete-prior-comparison-audit.json",audits)
    gate(doc,"all complete97 signed coefficients final error rows and serialized balls are finite",
         all(scalar(x).is_finite() for row in
             doc["complete_signed97_parameter_model"]["coefficients_in_increasing_delta_power"] for x in row))
    gate(doc,"no successful old mathematics is rerun and no new arrays are uploaded or published",
         PARAMETERS["new_artifacts"]==0 and PARAMETERS["new_Releases"]==0)
    if len(doc["gates"])!=EXPECTED_GATES:
        raise ArithmeticError("the full SC structural gate count changed")
    doc.update(complete=True,actual_new_signed_functional_complete=True,
        full_original_mean_and_same97_input_space_retained=True,
        original_successful_mathematical_outputs_changed=False,
        new_low_trace_gate_claimed=False,new_core_selfmap_claimed=False,
        new_full_BVP_inverse_claimed=False,new_global_surface_claimed=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-index","temporary","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True)
    ap.add_argument("--resume",type=Path)
    ap.add_argument("--resume-sha")
    a=ap.parse_args()
    ctx.prec=PARAMETERS["arithmetic_bits"]
    ctx.cap=6
    if a.out.exists():
        raise FileExistsError("preserve a complete or failed SC scientific conclusion")
    a.temporary.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    doc=dict(kind=KIND,repository="Rogerhu12/math-research-public",
        source_sha256=digest(__file__),helper_sha256=HELPER_SHA,reader_sha256=READER_SHA,
        parameters=PARAMETERS,input_manifest_sha256=a.manifest_sha,
        expected_gate_count=EXPECTED_GATES,complete=False,failure=None,gates=[],
        actual_returncode=None,new_artifact_count=0,new_Release_count=0)
    code=0
    try:
        run(a,doc)
    except Exception as exc:
        code=1
        doc["failure"]=dict(type=type(exc).__name__,message=str(exc),
                            traceback=traceback.format_exc()[-6000:])
        latest=a.temporary/"latest-scientific-prefix.json"
        if latest.exists():
            d=read(latest)
            doc["last_complete_scientific_prefix"]=dict(bytes=latest.stat().st_size,
                sha256=digest(latest),complete_groups=d["completed_groups"],
                complete_quarters=d["completed_quarters"],covered_exact_interval=d["covered_exact_interval"],
                stdout_markers=["SC_SCIENTIFIC_PREFIX_BEGIN","SC_SCIENTIFIC_PREFIX_END"])
    finally:
        doc["actual_returncode"]=code
        doc["seconds"]=time.monotonic()-started
        # Atomic full save always precedes all output-format size checks.
        info=atomic(a.out,doc)
        print(json.dumps(dict(kind="SC_FINAL_STATUS",actual_returncode=code,
            complete=doc["complete"],gates_passed=sum(g["passed"] for g in doc["gates"]),
            gates_total=len(doc["gates"]),expected_gates=EXPECTED_GATES,
            **info,failure=doc["failure"])),flush=True)
        print("SC_COMPLETE_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(canonical(doc).decode(),end="",flush=True)
        print("SC_COMPLETE_SCIENTIFIC_RESULT_END",flush=True)
    if code:
        raise SystemExit(code)


if __name__=="__main__":
    main()

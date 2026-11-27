"""Explicit zero-child WRC continuation after the actual reviewed_rules lookup failure.

The same mathematical owner, four targets and all whole scientific inputs
are retained.  The only input-role repair restores the public engine's
unprefixed reviewed_rules receipt; both existing path aliases remain.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT=TOPIC+"/scripts/fourfold_codazzi_complete_reference_world_height_public_worker.py"
PARENT_SHA="057dfb6b54e1173bfff17a7e417e3d56c47f31ec2bbe0af74479a9d16957fd42"
PREVIOUS_MANIFEST=TOPIC+"/notes/2026-11-27-complete-reference-world-height-inputs.json"
PREVIOUS_MANIFEST_SHA="3cc5872a6fca337572a41c96974d80c2875b4b475375c97376da41ea03a41290"
FAILURE=TOPIC+"/notes/2026-11-27-complete-reference-world-height-rule-role-failure.json"
FAILURE_SHA="7968a56e570ba152c7f964dc24b15c99d2d0f7bc7248425cbfb48f4e6d4a11cf"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def read_whole(root,path,digest):
    raw=(root/path).read_bytes()
    require(0<len(raw)<100000 and hashlib.sha256(raw).hexdigest()==digest,
        "whole explicit metadata predecessor: "+path)
    return raw


def admit_zero_predecessor(root,manifest):
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
        "zero-prefix admission precedes numerical imports")
    previous=json.loads(read_whole(root,PREVIOUS_MANIFEST,PREVIOUS_MANIFEST_SHA))
    failure=json.loads(read_whole(root,FAILURE,FAILURE_SHA))
    require(failure["kind"]=="WRC_observed_prechild_rule_role_failure_v1"
        and failure["run_id"]=="45941738781" and failure["run_attempt"]=="1"
        and failure["job_id"]==140317367517 and failure["job_conclusion"]=="failure"
        and failure["actual_failure"]["type"]=="KeyError"
        and failure["actual_failure"]["missing_key"]=="reviewed_rules"
        and failure["scientific_children"]==failure["new_scientific_target_calls"]==failure["new_saved_records"]==0
        and failure["completed_targets"]==[]
        and failure["native_scientific_output_created"] is False
        and failure["native_execution_output_published"] is False
        and failure["zero_prefix_provenance"]["review_lookup_precedes_Popen"] is True,
        "the genuine terminal prechild failure, not an assumed partial result")
    continuation=manifest["explicit_zero_child_continuation"]
    require(continuation=={
        "kind":"WRC_zero_child_rule_role_continuation_v1",
        "previous_run_id":"45941738781","previous_run_attempt":"1",
        "previous_manifest_sha256":PREVIOUS_MANIFEST_SHA,
        "failure_receipt_path":FAILURE,"failure_receipt_sha256":FAILURE_SHA,
        "previous_completed_targets":[],
        "mathematical_target_and_input_changes":0,
        "primary_rules_role_repaired":"reviewed_rules"},
        "one explicitly named zero-prefix continuation")
    for key in ("repository","kind","scientific_kind","stage","parameters","runtime",
                "target_order","complete_record_counts","allowed_scientific_fields","historical_inputs"):
        require(manifest[key]==previous[key],"unchanged entire mathematical contract: "+key)
    old={item["role"]:item for item in previous["files"]}
    current={item["role"]:item for item in manifest["files"]}
    for role in ("science","kernel_math","relative_restore","RHI_actual","RHI_execution"):
        require(current[role]==old[role],"unchanged whole scientific input: "+role)
    original=old["RHI_reviewed_rules"];fixed=current["reviewed_rules"]
    require({key:fixed[key] for key in ("path","bytes","sha256","git_blob_sha")}
        =={key:original[key] for key in ("path","bytes","sha256","git_blob_sha")}
        and manifest["roles"]["reviewed_rules"]==manifest["roles"]["RHI_reviewed_rules"]==fixed["path"],
        "same whole rule file, corrected primary receipt, both original aliases")
    require(current["predecessor_manifest"]["sha256"]==PREVIOUS_MANIFEST_SHA
        and current["previous_failure"]["sha256"]==FAILURE_SHA,
        "actual predecessor evidence in the complete input inventory")
    return failure


def build_adapter(root):
    raw=read_whole(root,PARENT,PARENT_SHA)
    spec=importlib.util.spec_from_file_location("_WRC_rule_role_original_worker",root/PARENT)
    parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    return parent.build_adapter(root)


def main():
    parser=argparse.ArgumentParser(add_help=False)
    for name in ("repo","manifest","manifest-sha"):
        parser.add_argument("--"+name,required=True)
    args,unused=parser.parse_known_args()
    root=Path(args.repo).resolve();mpath=Path(args.manifest)
    if not mpath.is_absolute():
        mpath=root/mpath
    raw=mpath.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==args.manifest_sha,"whole concrete continuation manifest")
    manifest=json.loads(raw);admit_zero_predecessor(root,manifest)
    namespace={"__name__":"_WRC_explicit_zero_child_public_worker","__file__":__file__}
    exec(compile(build_adapter(root),"<WRC same four targets with corrected rule role>","exec"),namespace)
    namespace["main"]()


if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Generate the single explicit R497 sampler source view; never import it.

This standard-library metadata generator runs only in the named public Actions.
Its parent owns the original namespace, absolute clock and complete source graph.
Author: ChatGPT /root (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import hashlib
import json
import os
import time

SCHEMA="R497-completed-inverse-box-cache-source-generation-v1"
PLAN_SCHEMA="R497-completed-inverse-box-cache-source-plan-v1"
REPOSITORY="Rogerhu12/math-research-public"
PLAN_NAME="r497-completed-inverse-box-cache-source-plan.json"
SOURCE_NAME="geometry_20261116_current_C_cached_inverse_joint_radial_sampling.py"
HELPER_NAME="geometry_20261116_completed_inverse_box_cache.py"
BASE_NAME="geometry_20261115_current_C_pruefer_joint_radial_sampling.py"
BASE_SHA="32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4"
OUTPUT_SHA="ae9dde7a93cd0477d7d8669593459bedf75fdc58083625beee40dd047eab5594"


def identity(path,raw=None):
    if raw is None:raw=Path(path).read_bytes()
    return dict(file=Path(path).name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def same(receipt,expected):
    return all(receipt.get(k)==expected.get(k) for k in ("file","bytes","sha256"))


def write_new(path,raw):
    with Path(path).open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return identity(path,raw)


def main(argv=None):
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Source materialization belongs to public repository Actions")
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--computations",type=Path,required=True)
    p.add_argument("--plan",type=Path,required=True)
    p.add_argument("--plan-sha256",required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args(argv)
    comp=args.computations.resolve();out=args.out.resolve()
    temp=Path(os.environ["RUNNER_TEMP"]).resolve()
    if comp!=Path(__file__).resolve().parent:
        raise ValueError("Use the actual complete computations directory")
    if args.plan.resolve()!=comp/PLAN_NAME:
        raise ValueError("Use the actual separately pinned current source plan")
    if not out.is_relative_to(temp) or out==temp or out.exists():
        raise ValueError("Use a fresh caller-owned temporary receipt directory")
    if out==comp or comp.is_relative_to(out):
        raise ValueError("The receipt directory cannot own source files")
    if not out.parent.is_dir():
        raise ValueError("The caller must already own the parent receipt namespace")
    out.mkdir()
    started=time.monotonic()
    report=dict(schema=SCHEMA,repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],source=identity(__file__),
        completed=False,current_stage="read-plan",generated_source=None,error=None,
        source_text_generation_only=True,scientific_program_imported_or_run=False,
        no_clock_or_original_namespace_recreated=True,no_raw_deleted=True)
    code=2
    try:
        raw=args.plan.read_bytes();plan_receipt=identity(args.plan,raw)
        if plan_receipt["sha256"]!=args.plan_sha256:
            raise ValueError("The actual plan SHA differs")
        plan=json.loads(raw)
        if plan.get("schema")!=PLAN_SCHEMA or plan.get("repository")!=REPOSITORY:
            raise ValueError("Use the complete explicit R497 source plan")
        report["plan"]=plan_receipt
        if (plan["baseline"]["file"]!=BASE_NAME or plan["baseline"]["sha256"]!=BASE_SHA
                or plan["output"]["file"]!=SOURCE_NAME or plan["output"]["sha256"]!=OUTPUT_SHA):
            raise ValueError("The complete baseline/output source tuple differs")
        report["current_stage"]="bind-helper-and-baseline"
        if plan["helper"]["file"]!=HELPER_NAME:
            raise ValueError("Use the one explicitly registered cache helper")
        helper=identity(comp/plan["helper"]["file"])
        if not same(helper,plan["helper"]):
            raise ValueError("The actual explicit cache helper differs")
        baseline_raw=(comp/BASE_NAME).read_bytes();baseline=identity(BASE_NAME,baseline_raw)
        if not same(baseline,plan["baseline"]):
            raise ValueError("The full original sampler bytes differ")
        report.update(helper=helper,baseline=baseline)
        destination=comp/SOURCE_NAME
        if destination.exists():
            raise FileExistsError("Never overwrite an existing source or generated view")
        report["current_stage"]="prepare-complete-source"
        text=baseline_raw.decode("utf-8")
        changes=[]
        for i,change in enumerate(plan["changes"]):
            count=text.count(change["before"])
            if count!=change["occurrences"] or count!=1:
                raise ValueError("Source anchor occurrence differs at change "+str(i))
            text=text.replace(change["before"],change["after"])
            changes.append(dict(index=i,actual_occurrences=count))
        output=text.encode("utf-8");receipt=identity(destination,output)
        if not same(receipt,plan["output"]) or len(output)>=100000:
            raise ValueError("The complete actual generated source identity differs")
        report["changes"]=changes
        report["current_stage"]="write-exclusive-source"
        report["generated_source"]=write_new(destination,output)
        report["current_stage"]="completed-source-only";report["completed"]=True;code=0
    except Exception as error:
        report["error"]=dict(type=type(error).__name__,message=str(error))
        report["unconfirmed_output_not_relabelled_as_complete"]=True
    report["elapsed_seconds"]=time.monotonic()-started
    raw=(json.dumps(report,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()
    result=write_new(out/"result.json",raw)
    print(json.dumps(dict(event="R497_actual_source_generation",result=result,
        completed=report["completed"],current_stage=report["current_stage"],
        error=report["error"]),ensure_ascii=False),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())

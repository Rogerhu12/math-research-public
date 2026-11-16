#!/usr/bin/env python3
"""Materialize the three explicitly declared R503 source views in public Actions.

Only exact source text and byte metadata are handled here. No generated
scientific module is imported, parsed as an AST, compiled, exercised or gated.
An outer real entry still owns the original namespace clock and full source
registration. Old files remain unchanged and output names must be new.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re

REPO="Rogerhu12/math-research-public"
NAME="root_20261116_explicit_coast_base_source_views.py"
PLAN="r503-explicit-coast-base-source-plan.json"
PLAN_BYTES=18919
PLAN_SHA="2f6113ce7b1928d2954d8768d2117db4452abf89cbb7f2f8b1a57719228e9dd3"
SCHEMA="R503-explicit-coast-base-complete-candidate-and-original-two-phase-source-plan-v1"

def identity(raw):
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def require(value,message):
    if not value:raise ValueError(message)

def unique(pairs):
    answer={}
    for key,value in pairs:
        require(key not in answer,"Duplicate source-plan key: "+key)
        answer[key]=value
    return answer

def name(value):
    require(isinstance(value,str) and re.fullmatch(r"[A-Za-z0-9_.-]+",value)
        and value not in (".",".."),"Use one explicit source basename")
    return value

def checked_source(root,descriptor):
    path=root/name(descriptor["file"])
    require(path.is_file() and not path.is_symlink()
        and path.resolve().parent==root,"Keep actual source files in the same computations")
    raw=path.read_bytes()
    require(identity(raw)=={key:descriptor[key] for key in ("bytes","sha256")},
        "Actual original source bytes differ: "+path.name)
    return path,raw

def main(argv=None):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPO,
        "Source materialization belongs to this public repository Actions")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--source-sha256",required=True)
    parser.add_argument("--receipt",type=Path,required=True)
    args=parser.parse_args(argv)
    root=args.computations.resolve()
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve()
    require(root!=temporary and root.is_relative_to(temporary),
        "Use the real exclusive computations under RUNNER_TEMP")
    actual=Path(__file__).resolve()
    require(actual.parent==root and actual.name==NAME
        and not Path(__file__).is_symlink(),"Use this actual same-HERE generator")
    source_raw=actual.read_bytes()
    require(identity(source_raw)["sha256"]==args.source_sha256,
        "Actual source generator identity differs")
    receipt_path=args.receipt
    require(not receipt_path.exists() and not receipt_path.is_symlink()
        and receipt_path.resolve().is_relative_to(temporary)
        and receipt_path.resolve()!=temporary,
        "A new request-owned receipt is required")
    _,plan_raw=checked_source(root,dict(file=PLAN,bytes=PLAN_BYTES,sha256=PLAN_SHA))
    plan=json.loads(plan_raw,object_pairs_hook=unique,
        parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
    require(plan.get("schema")==SCHEMA and plan.get("repository")==REPO
        and plan.get("scientific_execution") is False,"The explicit source contract differs")
    require(isinstance(plan.get("views"),list) and len(plan["views"])==3,
        "Materialize exactly the three declared source views")
    targets=[name(row["output"]["file"]) for row in plan["views"]]
    require(len(set(targets))==len(targets),"Duplicate generated source name")
    rows=[]
    for row in plan["views"]:
        old_path,original=checked_source(root,row["base"])
        target=root/name(row["output"]["file"])
        require(not target.exists() and not target.is_symlink()
            and target.resolve().parent==root,
            "Never overwrite any original or generated source: "+target.name)
        text=original.decode("utf-8")
        applied=[]
        for ordinal,change in enumerate(row["replacements"]):
            before,after,count=change["before"],change["after"],change["count"]
            require(isinstance(before,str) and before and isinstance(after,str)
                and type(count) is int and count>0,
                "A complete literal before/after/count is required")
            actual_count=text.count(before)
            require(actual_count==count,
                "Declared original source literal count differs: "+str(ordinal))
            text=text.replace(before,after)
            applied.append(dict(index=ordinal,count=count,
                before=identity(before.encode("utf-8")),after=identity(after.encode("utf-8"))))
        result=text.encode("utf-8")
        require(identity(result)=={key:row["output"][key] for key in ("bytes","sha256")},
            "Complete generated source identity differs: "+target.name)
        with target.open("xb") as handle:
            handle.write(result);handle.flush();os.fsync(handle.fileno())
        require(old_path.read_bytes()==original,"The original source changed during generation")
        require(identity(target.read_bytes())==identity(result),
            "Actual generated file differs from its complete source bytes")
        rows.append(dict(original=row["base"],generated=row["output"],literal_applications=applied))
    report=dict(schema=SCHEMA+"-receipt",repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        generator=dict(file=NAME,**identity(source_raw)),
        plan=dict(file=PLAN,**identity(plan_raw)),sources=rows,
        original_files_unchanged=True,actual_same_computations=True,
        generated_science_imported_or_executed=False,
        old_entry_or_source_identity_relabelled=False,
        current_candidate_arithmetic_or_C_factory_or_BVP_executed=False,
        original_outer_clock_not_started_or_reset=True,
        outer_entry_and_complete_necessary_readers_still_require_explicit_registration=True)
    raw=(json.dumps(report,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
    with receipt_path.open("xb") as handle:
        handle.write(raw);handle.flush();os.fsync(handle.fileno())
    print(json.dumps(dict(event="R503_source_views_materialized",receipt=dict(
        file=str(receipt_path),**identity(raw)),outputs=[row["generated"] for row in rows],
        scientific_execution=False),sort_keys=True),flush=True)
    return 0

if __name__=="__main__":
    raise SystemExit(main())

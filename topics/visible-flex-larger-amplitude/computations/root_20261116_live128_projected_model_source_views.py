#!/usr/bin/env python3
"""R534 source-only composition of the current-owner projected64 full model.

The frozen225 generator produces its original14 temporary source views.
Two explicit R534 literal plans then produce13 new names in the same real
computations directory. No scientific module is imported or evaluated; no
compiler, numerical fixture or scientific deadline is started here.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

HERE=Path(__file__).resolve().parent
TOPIC=HERE.parent
SCHEMA="R534-current-owner-projected-model-source-preparation-v1"
PLAN_SCHEMA="R534-current-owner-projected-model-complete-source-plan-v1"
CORE_SCHEMA="R534-current-owner-projected-model-core-source-plan-v1"
META_NAME="request229-source-preparation"
FRAME="R534_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY"
RUN_KEYS=("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")
REPOSITORY="Rogerhu12/math-research-public"
LIMIT=90000


def require(ok,message):
    if not ok:raise ValueError(message)


def canonical(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,
        separators=(",",":"),allow_nan=False).encode("ascii")+b"\n"


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def identity(path):
    path=Path(path).resolve(strict=True)
    return dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path))


def write(path,value,replace=False):
    path=Path(path)
    temporary=path.with_name(path.name+".writing")
    require(not temporary.exists() and (replace or not path.exists()),
            "Exclusive actual source metadata")
    with temporary.open("xb") as f:f.write(canonical(value))
    os.replace(temporary,path)


def basename(name):
    require(isinstance(name,str) and name and Path(name).name==name
            and name not in (".","..") and "\x00" not in name,
            "One explicit ordinary source basename")
    return name


def checked(path,desc):
    path=Path(path)
    require(path.is_file() and not path.is_symlink()
            and path.stat().st_size==desc["bytes"] and sha(path)==desc["sha256"],
            "Actual full source/metadata identity: "+str(path))
    return path.resolve(strict=True)


def topic_file(desc):
    name=Path(desc["file"])
    require(not name.is_absolute() and ".." not in name.parts,
            "Ordinary contained topic metadata")
    path=TOPIC/name
    require(path.resolve(strict=True).is_relative_to(TOPIC),
            "Source-plan metadata stays in this topic")
    return checked(path,desc)


def context(args):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
            "Source preparation belongs to this public Actions repository")
    workspace=Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE==workspace/"topics/visible-flex-larger-amplitude/computations"
            and args.computations.resolve(strict=True)==HERE,
            "Every actual new view is written beside its true bound callers")
    path=args.plan.resolve(strict=True)
    require(not args.plan.is_symlink() and sha(path)==args.plan_sha256,
            "The complete caller-supplied R534 plan")
    plan=json.loads(path.read_bytes())
    require(plan["schema"]==PLAN_SCHEMA and plan["repository"]==REPOSITORY,
            "The complete R534 source plan")
    checked(__file__,plan["generator"])
    core_path=topic_file(plan["core_plan"])
    core=json.loads(core_path.read_bytes())
    require(core["schema"]==CORE_SCHEMA and core["repository"]==REPOSITORY,
            "The separately complete core source plan")
    views=core["views"]+plan["views"]
    require(len(views)==13 and len({x["role"] for x in views})==13
            and len({x["output"]["file"] for x in views})==13,
            "All13 distinct explicit current model/caller views")
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve()
    require(out.parent==runner and out.name==META_NAME
            and not args.out.is_symlink(),"The actual independent source-preparation directory")
    return workspace,plan,path,core,core_path,views,out


def literal(text,patches,label):
    changes=[]
    for patch in patches:
        before,after,count=patch["before"],patch["after"],patch["count"]
        require(isinstance(before,str) and before and isinstance(after,str)
                and type(count) is int and count>0,"Explicit literal text transformation")
        require(text.count(before)==count,label+"/"+patch["id"]+": complete original occurrence count")
        text=text.replace(before,after)
        changes.append(dict(id=patch["id"],count=count,
            before_sha256=hashlib.sha256(before.encode("utf-8")).hexdigest(),
            after_sha256=hashlib.sha256(after.encode("utf-8")).hexdigest()))
    return text,changes


def prepare(args):
    workspace,plan,path,core,core_path,views,out=context(args)
    require(not out.exists(),"A fresh actual source-preparation directory is required")
    out.mkdir(mode=0o700)
    record=dict(schema=SCHEMA,run={k:os.environ.get(k) for k in RUN_KEYS},
        source=identity(__file__),plan=identity(path),core_plan=identity(core_path),
        actual_computations=str(HERE),complete=False,phase="bind-complete-ancestry",
        original_published_files_modified=False,scientific_modules_imported=False,
        scientific_code_evaluated=False,compiler_started=False,scientific_clock_created=False,
        original225_internal_number_is_source_ancestry_only=True,
        generated=[],not_generated=[x["role"] for x in views],error=None)
    output=out/"source-views.json"
    write(output,record)
    code=2
    try:
        head=subprocess.check_output(["git","-C",str(workspace),"rev-parse","HEAD"],text=True).strip()
        require(head==os.environ["GITHUB_SHA"],"The actual unmodified science checkout head")
        ancestor=plan["ancestor"]
        req_path=checked(HERE/basename(ancestor["request"]["file"]),ancestor["request"])
        request=json.loads(req_path.read_bytes())
        require(request["schema"]=="public-live128-paired-cache-original-full112-FD-fullDN-request-v1"
                and request["request_number"]==225
                and len(request["source_sha256"])==356
                and len(request["generated_source_sha256"])==14,
                "The frozen complete225 contract supplies only source/input ancestry")
        generator=checked(HERE/basename(ancestor["generator"]["file"]),ancestor["generator"])
        ancestor_plan=topic_file(ancestor["plan"])
        require(request["source_generator"]==ancestor["generator"]
                and request["source_plan"]==ancestor["plan"],
                "The actual unchanged225 generator and plan are bound by its complete request")
        record["ancestor_request"]=identity(req_path)
        record["ancestor_generator"]=identity(generator)
        record["ancestor_plan"]=identity(ancestor_plan)
        for row in plan["additional_public_sources"]:
            checked(HERE/basename(row["file"]),row)
        for view in views:
            target=HERE/basename(view["output"]["file"])
            require(not target.exists() and not target.is_symlink(),
                    "No existing source may be overwritten: "+target.name)
        ancestor_out=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)/"request225-source-preparation"
        require(not ancestor_out.exists(),"The source-only225 ancestor is materialized once in this job")
        command=[sys.executable,"-u",str(generator),"prepare",
            "--request",str(req_path),"--request-sha256",ancestor["request"]["sha256"],
            "--out",str(ancestor_out)]
        child=dict(command=command,started=False,returned=False,returncode=None,
            scientific_child=False,creates_scientific_clock=False)
        record["ancestor_source_child"]=child
        write(output,record,True)
        with (out/"ancestor-source.stdout.log").open("xb") as stdout,(
                out/"ancestor-source.stderr.log").open("xb") as stderr:
            child["started"]=True
            write(output,record,True)
            completed=subprocess.run(command,stdout=stdout,stderr=stderr,
                                     check=False,start_new_session=False)
        child.update(returned=True,returncode=completed.returncode,
            stdout=identity(out/"ancestor-source.stdout.log"),
            stderr=identity(out/"ancestor-source.stderr.log"))
        original_path=ancestor_out/"source-views.json"
        if original_path.is_file():
            original=json.loads(original_path.read_bytes())
            child["actual_source_receipt"]=identity(original_path)
            child["original_record"]=original
        else:original=None
        write(output,record,True)
        require(completed.returncode==0 and isinstance(original,dict)
                and original.get("complete") is True and original.get("error") is None
                and original.get("run")==record["run"],
                "Actual complete same-job225 source ancestry has returned")
        complete=dict(request["source_sha256"])
        record["verified_ancestor_sources"]=[]
        for name,digest in complete.items():
            actual=HERE/basename(name)
            require(actual.is_file() and not actual.is_symlink() and sha(actual)==digest,
                    "Every actual225 public/generated source remains unchanged: "+name)
            record["verified_ancestor_sources"].append(identity(actual))
        for row in plan["additional_public_sources"]:
            require(row["file"] not in complete,"Each additional public source has a new name")
            actual=checked(HERE/row["file"],row)
            complete[row["file"]]=row["sha256"]
        current=identity(__file__)
        require(Path(__file__).name not in complete,"Distinct actual source generator")
        complete[Path(__file__).name]=current["sha256"]
        pending=[]
        for view in views:
            baseline=checked(HERE/basename(view["baseline"]["file"]),view["baseline"])
            require(complete.get(baseline.name)==view["baseline"]["sha256"],
                    "Every literal baseline belongs to the complete actual source closure")
            text,changes=literal(baseline.read_bytes().decode("utf-8"),
                                 view["patches"],view["role"])
            raw=text.encode("utf-8")
            require(len(raw)==view["output"]["bytes"]
                    and hashlib.sha256(raw).hexdigest()==view["output"]["sha256"],
                    "Complete actual new source: "+view["role"])
            name=basename(view["output"]["file"])
            require(name not in complete,"No old public or generated source is replaced")
            complete[name]=view["output"]["sha256"]
            pending.append((view,HERE/name,raw,changes))
        require(len(complete)==372 and plan["counts"]==dict(
            original225_public=342,original225_generated=14,
            additional_public_libraries=2,new_generator=1,new_views=13,complete=372),
            "The exact finite composed source set is declared, not an implicit import claim")
        record["phase"]="publish-new-distinct-views"
        record["source_counts"]=plan["counts"]
        write(output,record,True)
        for view,target,raw,changes in pending:
            with target.open("xb") as f:f.write(raw)
            checked(target,view["output"])
            record["generated"].append(dict(role=view["role"],
                actual=identity(target),baseline=view["baseline"],literal_changes=changes))
            record["not_generated"].remove(view["role"])
            write(output,record,True)
        mapping=out/"complete-source-map.json"
        write(mapping,dict(schema=SCHEMA+"-complete-source-map-v1",
            run=record["run"],plan=record["plan"],core_plan=record["core_plan"],
            sources=complete,generated_sources=dict(request["generated_source_sha256"],
                **{x["output"]["file"]:x["output"]["sha256"] for x in views}),
            counts=plan["counts"],roles=plan["roles"]))
        record.update(complete=True,phase="source-prepared",complete_source_map=identity(mapping),
            requested_scientific_run_not_started_here=True,
            registered_current_policy_schema=plan["schemas"]["policy"],
            future_science_namespace="visible-live128-projected-model229")
        code=0
    except Exception as exc:
        record["error"]=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
    record["actual_exit"]=code
    write(output,record,True)
    print(json.dumps(dict(event="R534_source_preparation_return",complete=record["complete"],
        actual_exit=code,actual_source_receipt=identity(output),
        science_success_inferred=False),ensure_ascii=True),flush=True)
    return code


def readback(args):
    workspace,plan,path,core,core_path,views,out=context(args)
    result=dict(schema=SCHEMA+"-necessary-v1",source=identity(__file__),
        run={k:os.environ.get(k) for k in RUN_KEYS},plan=identity(path),core_plan=identity(core_path),
        source_preparation_complete=False,necessary_readback_complete=False,error=None,
        numerical_acceptance_inferred=False,all_scientific_raw_outside_this_source_scope=True)
    code=2
    try:
        actual=out/"source-views.json"
        require(actual.is_file() and not actual.is_symlink(),"The actual source record is retained")
        record=json.loads(actual.read_bytes())
        require(record["schema"]==SCHEMA and record["run"]==result["run"]
                and record["plan"]==result["plan"] and record["core_plan"]==result["core_plan"],
                "This complete original same-job source scope")
        result["actual_source_record"]=identity(actual)
        for key in ("complete","phase","actual_computations","original_published_files_modified",
                    "scientific_modules_imported","scientific_code_evaluated","compiler_started",
                    "scientific_clock_created","original225_internal_number_is_source_ancestry_only",
                    "generated","not_generated","error","actual_exit","source_counts",
                    "complete_source_map","registered_current_policy_schema"):
            if key in record:result[key]=record[key]
        child=record.get("ancestor_source_child")
        if isinstance(child,dict):
            result["ancestor_source_child"]={k:v for k,v in child.items() if k!="original_record"}
            original=child.get("original_record")
            if isinstance(original,dict):
                result["ancestor_source_child"]["selected_original_scope"]={
                    k:v for k,v in original.items() if k not in ("verified_public_sources","R522_child")}
                inner=original.get("R522_child")
                if isinstance(inner,dict):
                    selected={k:v for k,v in inner.items() if k!="source_result"}
                    value=inner.get("source_result")
                    if isinstance(value,dict):
                        selected["original_result"]={k:v for k,v in value.items() if k!="public_inputs"}
                        selected["public_input_count"]=len(value.get("public_inputs",[]))
                    result["ancestor_source_child"]["R522_child"]=selected
        result["verified_ancestor_source_count"]=len(record.get("verified_ancestor_sources",[]))
        result["complete_original_source_stderr"]=[]
        roots=[out,Path(os.environ["RUNNER_TEMP"])/"request225-source-preparation"]
        for root in roots:
            if not root.is_dir():continue
            for log in sorted(root.rglob("*.stderr.log")):
                if log.is_file() and not log.is_symlink() and log.stat().st_size:
                    result["complete_original_source_stderr"].append(dict(actual=identity(log),
                        complete_text=log.read_bytes().decode("utf-8","surrogateescape"),
                        encoding="UTF-8-surrogateescape in ASCII JSON; original bytes preserved"))
        result["source_preparation_complete"]=record.get("complete") is True
        result["necessary_readback_complete"]=True
        code=0
    except Exception as exc:
        result["error"]=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
    raw=canonical(result)
    if len(raw)>LIMIT:
        if out.is_dir():
            full=out/"necessary-source-overflow.json"
            write(full,result)
            full_receipt=identity(full)
        else:full_receipt=None
        result=dict(schema=SCHEMA+"-necessary-v1",source=identity(__file__),run=result["run"],
            plan=result["plan"],core_plan=result["core_plan"],necessary_readback_complete=False,
            source_preparation_complete=False,transport_exit_code=70,
            attempted_bytes=len(raw),attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=full_receipt,cleanup_permitted=False,
            no_segments_or_encoded_raw=True,numerical_success_not_inferred=True)
        raw=canonical(result);code=70
    target=Path(os.environ["RUNNER_TEMP"])/(META_NAME+"-necessary.json")
    with target.open("xb") as f:f.write(raw)
    print("BEGIN_"+FRAME,flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_"+FRAME,flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as f:
            f.write("source_necessary_summary="+str(target)+"\n")
            f.write("source_necessary_bytes="+str(len(raw))+"\n")
            f.write("source_necessary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
            f.write("source_readback_complete="+str(result["necessary_readback_complete"]).lower()+"\n")
    return code


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode",choices=("prepare","readback"))
    p.add_argument("--plan",type=Path,required=True)
    p.add_argument("--plan-sha256",required=True)
    p.add_argument("--computations",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    try:return prepare(args) if args.mode=="prepare" else readback(args)
    except Exception as exc:
        print(json.dumps(dict(event="R534_source_preparation_unreturned",schema=SCHEMA,
            source=identity(__file__),complete=False,cleanup_permitted=False,
            error=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())),
            ensure_ascii=True),flush=True)
        return 2


if __name__=="__main__":
    raise SystemExit(main())

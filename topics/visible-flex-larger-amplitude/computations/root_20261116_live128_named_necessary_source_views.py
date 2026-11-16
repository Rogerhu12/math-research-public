#!/usr/bin/env python3
"""R589: complete R573 source ancestry and two named necessary readers.

The original R573 preparation and original readback each run once, in their
original same-job namespace. Only two new caller identities are generated.
All scientific modules, input objects, mathematical gates and clocks remain
the original R573 objects. R588 may represent only the complete source-only
necessary object; every original field, transport70 and unknown/error stays.
No scientific import, compilation or arithmetic is performed by this module.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

HERE=Path(__file__).resolve().parent
TOPIC=HERE.parent
SCHEMA="R589-complete-current-owner-named-necessary-source-preparation-v1"
PLAN_SCHEMA="R589-complete-current-owner-named-necessary-source-plan-v1"
ANCESTOR_SCHEMA="R573-root-synthesis-product-current-owner-projected-model-source-preparation-v1"
META_NAME="request246-source-preparation"
ANCESTOR_META_NAME="request240-source-preparation"
FRAME="R589_NAMED_NECESSARY_SOURCE_PREPARATION_NECESSARY"
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
            "This source preparation belongs to the public repository Actions")
    workspace=Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE==workspace/"topics/visible-flex-larger-amplitude/computations"
            and args.computations.resolve(strict=True)==HERE,
            "Generated views live beside their actual callers")
    path=args.plan.resolve(strict=True)
    require(not args.plan.is_symlink() and sha(path)==args.plan_sha256,
            "Whole complete current source plan")
    plan=json.loads(path.read_bytes())
    require(plan["schema"]==PLAN_SCHEMA and plan["repository"]==REPOSITORY,
            "Current plan schema and repository")
    checked(__file__,plan["generator"])
    helper=checked(HERE/basename(plan["relation_helper"]["file"]),plan["relation_helper"])
    views=plan["views"]
    require(len(views)==2 and {v["role"] for v in views}=={"runner","reader"}
            and len({v["output"]["file"] for v in views})==2,
            "Only two distinct new procedure/necessary caller views")
    ancestor=plan["ancestor"]
    request_path=checked(HERE/basename(ancestor["request"]["file"]),ancestor["request"])
    request=json.loads(request_path.read_bytes())
    require(request["schema"]=="public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request-v1"
            and request["request_number"]==240
            and len(request["source_sha256"])==447
            and len(request["generated_source_sha256"])==87,
            "Frozen complete original240 source ancestry")
    require(request["source_generator"]==ancestor["generator"]
            and request["source_plan"]==ancestor["plan"],
            "The unchanged original R573 generator and full source plan")
    generator=checked(HERE/basename(ancestor["generator"]["file"]),ancestor["generator"])
    ancestor_plan=topic_file(ancestor["plan"])
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve()
    require(out.parent==runner and out.name==META_NAME and not args.out.is_symlink(),
            "One exact independent current source metadata directory")
    expected=dict(request["source_sha256"])
    for row in [plan["relation_helper"],plan["generator"]]+[v["output"] for v in views]:
        require(row["file"] not in expected,"Distinct explicitly declared source addition")
        expected[basename(row["file"])]=row["sha256"]
    generated=dict(request["generated_source_sha256"])
    generated.update({v["output"]["file"]:v["output"]["sha256"] for v in views})
    require(len(expected)==451 and len(generated)==89
            and plan["counts"]==dict(original240_public=360,original240_generated=87,
                additional_relation_helper=1,new_generator=1,new_caller_views=2,
                public=362,generated=89,complete=451),
            "Complete451 sources; all original447 remain unchanged")
    require(plan["roles"]["fulldn"]==json.loads(ancestor_plan.read_bytes())["roles"]["fulldn"]
            and plan["unchanged_scientific_entry"]==plan["roles"]["fulldn"],
            "Original complete scientific entry is byte-identical")
    return workspace,plan,path,views,out,request,request_path,generator,ancestor_plan,helper,expected,generated

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



def source_child(command,out,label,record,record_path):
    child=dict(command=command,started=False,returned=False,actual_exit=None,
        scientific_child=False,creates_scientific_clock=False,starts_new_session=False)
    record[label]=child
    write(record_path,record,True)
    stdout_path=out/(label+".stdout.log")
    stderr_path=out/(label+".stderr.log")
    with stdout_path.open("xb") as stdout,stderr_path.open("xb") as stderr:
        child["started"]=True
        write(record_path,record,True)
        completed=subprocess.run(command,stdout=stdout,stderr=stderr,
            check=False,start_new_session=False)
    child.update(returned=True,actual_exit=completed.returncode,
        stdout=identity(stdout_path),stderr=identity(stderr_path))
    write(record_path,record,True)
    return child



def prepare(args):
    workspace,plan,path,views,out,request,request_path,generator,ancestor_plan,helper,expected,generated=context(args)
    require(not out.exists(),"Fresh actual current source preparation directory")
    out.mkdir(mode=0o700)
    record=dict(schema=SCHEMA,request_number=246,
        run={k:os.environ.get(k) for k in RUN_KEYS},
        source=identity(__file__),plan=identity(path),actual_computations=str(HERE),
        ancestor_request=identity(request_path),ancestor_plan=identity(ancestor_plan),
        relation_helper=identity(helper),
        complete=False,phase="bind-source-ancestry",error=None,
        original_published_files_modified=False,scientific_modules_imported=False,
        scientific_code_evaluated=False,compiler_started=False,
        scientific_clock_created=False,ancestor240_is_source_only=True,
        generated=[],not_generated=[v["role"] for v in views])
    record_path=out/"source-views.json"
    write(record_path,record)
    code=2
    try:
        head=subprocess.check_output(["git","-C",str(workspace),"rev-parse","HEAD"],
                                     text=True).strip()
        require(head==os.environ["GITHUB_SHA"],"Unmodified actual science checkout head")
        for view in views:
            target=HERE/basename(view["output"]["file"])
            require(not target.exists() and not target.is_symlink(),
                    "Never overwrite an existing caller: "+target.name)
        runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        ancestor_out=runner/ANCESTOR_META_NAME
        require(not ancestor_out.exists(),"Call unchanged R573 prepare exactly once")
        command=[sys.executable,"-u",str(generator),"prepare",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(ancestor_out)]
        record["phase"]="original-R573-source-preparation"
        child=source_child(command,out,"R573_child",record,record_path)
        original_path=ancestor_out/"source-views.json"
        original=None
        if original_path.is_file() and not original_path.is_symlink():
            original=json.loads(original_path.read_bytes())
            child["actual_source_receipt"]=identity(original_path)
        write(record_path,record,True)
        require(child["actual_exit"]==0 and isinstance(original,dict)
            and original.get("schema")==ANCESTOR_SCHEMA
            and original.get("complete") is True and original.get("error") is None
            and original.get("run")==record["run"]
            and original.get("actual_computations")==str(HERE),
            "Actual complete same-job original R573 source preparation returned")
        record["verified_ancestor_sources"]=[]
        for name,digest in request["source_sha256"].items():
            source=HERE/basename(name)
            require(source.is_file() and not source.is_symlink() and sha(source)==digest,
                    "Every original447 source stays byte-identical: "+name)
            record["verified_ancestor_sources"].append(identity(source))
        record["verified_public_sources"]=[identity(helper),identity(__file__)]
        record["source_counts"]=plan["counts"]
        record["phase"]="publish-two-distinct-callers"
        write(record_path,record,True)
        for view in views:
            baseline=checked(HERE/basename(view["baseline"]["file"]),view["baseline"])
            require(request["source_sha256"].get(baseline.name)==view["baseline"]["sha256"],
                    "Caller baseline belongs to original447 source closure")
            text,changes=literal(baseline.read_bytes().decode("utf-8"),
                                 view["patches"],view["role"])
            raw=text.encode("utf-8")
            require(len(raw)==view["output"]["bytes"]
                    and hashlib.sha256(raw).hexdigest()==view["output"]["sha256"],
                    "Whole newly generated caller identity: "+view["role"])
            target=HERE/basename(view["output"]["file"])
            with target.open("xb") as stream:stream.write(raw)
            checked(target,view["output"])
            record["generated"].append(dict(role=view["role"],actual=identity(target),
                baseline=view["baseline"],literal_changes=changes))
            record["not_generated"].remove(view["role"])
            write(record_path,record,True)
        for name,digest in expected.items():
            source=HERE/basename(name)
            require(source.is_file() and not source.is_symlink() and sha(source)==digest,
                    "Complete current451 source closure matches: "+name)
        mapping=out/"complete-source-map.json"
        write(mapping,dict(schema=SCHEMA+"-complete-source-map-v1",run=record["run"],
            plan=record["plan"],sources=expected,generated_sources=generated,
            counts=plan["counts"],roles=plan["roles"]))
        record.update(complete=True,phase="source-prepared",complete_source_map=identity(mapping),
            current_policy_schema=plan["schemas"]["policy"],
            future_science_namespace=plan["schemas"]["namespace"],
            source_preparation_is_not_compilation_or_scientific_acceptance=True)
        code=0
    except Exception as error:
        record["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    record["actual_exit"]=code
    write(record_path,record,True)
    print(json.dumps(dict(event="R589_source_preparation_return",complete=record["complete"],
        actual_exit=code,actual_source_receipt=identity(record_path),
        science_success_inferred=False),ensure_ascii=True),flush=True)
    return code


def readback(args):
    workspace,plan,path,views,out,request,request_path,generator,ancestor_plan,helper,expected,generated=context(args)
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    run={k:os.environ.get(k) for k in RUN_KEYS}
    result=dict(schema=SCHEMA+"-necessary-v1",request_number=246,run=run,
        source=identity(__file__),plan=identity(path),
        source_preparation_complete=False,necessary_readback_complete=False,
        current_source_record=None,original_R573_readback=None,
        original_R573_transport=None,original_R573_complete_necessary=None,
        complete_current_source_stderr=[],source_stdout_identities=[],
        metadata_read_errors=[],numerical_acceptance_inferred=False,
        all_scientific_raw_outside_this_source_scope=True,
        scope=dict(whole_original_R573_necessary_selection_consumed=True,
            original_source_preparation_called_once=True,
            original_readback_called_once=True,
            complete_current_caller_source_record_retained=True,
            actual_child70_and_original_false_transport_preserved=True,
            full_retained_overflow_body_bound_before_selection=True,
            all_actual_errors_and_ungenerated_suffixes_retained=True,
            original_scientific_necessary_selection_unchanged=True,
            no_scientific_arrays_or_generic_tree_codec=True))
    code=2
    try:
        require(out.is_dir() and not out.is_symlink(),"Actual current source directory")
        current_path=out/"source-views.json"
        require(current_path.is_file() and not current_path.is_symlink(),
                "Actual current source record returned")
        current=json.loads(current_path.read_bytes())
        require(current.get("schema")==SCHEMA and current.get("run")==run
                and current.get("source")==identity(__file__)
                and current.get("plan")==result["plan"],
                "This actual source preparation, source and plan")
        result["current_source_record"]=dict(actual=identity(current_path),record=current)
        result["source_preparation_complete"]=current.get("complete") is True
        result["actual_exit"]=current.get("actual_exit")
        result["error"]=current.get("error")
        result["not_generated"]=current.get("not_generated")
        result["source_counts"]=current.get("source_counts")
        original_out=runner/ANCESTOR_META_NAME
        source_path=original_out/"source-views.json"
        if isinstance(current.get("R573_child"),dict):
            desc=current["R573_child"].get("actual_source_receipt")
            if desc is not None:
                require(source_path.is_file() and not source_path.is_symlink()
                        and identity(source_path)==desc,
                        "Exact same-job original source receipt remains bound")
        command=[sys.executable,"-u",str(generator),"readback",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(original_out)]
        child=dict(command=command,reader_source=identity(generator),
            original_plan=identity(ancestor_plan),started=False,returned=False,
            actual_exit=None,scientific_child=False,starts_new_session=False)
        result["original_R573_readback"]=child
        stdout_path=out/"R573-readback.stdout.log"
        stderr_path=out/"R573-readback.stderr.log"
        child["started"]=True
        with stdout_path.open("xb") as stdout,stderr_path.open("xb") as stderr:
            completed=subprocess.run(command,stdout=stdout,stderr=stderr,
                check=False,start_new_session=False)
        child.update(returned=True,actual_exit=completed.returncode,
            stdout=identity(stdout_path),stderr=identity(stderr_path))
        transport_path=runner/(ANCESTOR_META_NAME+"-necessary.json")
        require(transport_path.is_file() and not transport_path.is_symlink(),
                "Original R573 necessary transport object returned")
        transport_raw=transport_path.read_bytes()
        transport=json.loads(transport_raw)
        require(transport.get("schema")==ANCESTOR_SCHEMA+"-necessary-v1"
                and transport.get("run")==run and transport.get("request_number")==240
                and transport.get("source")==identity(generator)
                and transport.get("plan")==identity(ancestor_plan),
                "Same actual original R573 reader/run/source/plan")
        result["original_R573_transport"]=dict(actual=identity(transport_path),
            original_reader_exit=completed.returncode,
            original_necessary_readback_complete=transport.get("necessary_readback_complete"),
            original_source_preparation_complete=transport.get("source_preparation_complete"),
            original_transport_exit_code=transport.get("transport_exit_code"),
            original_transport_body=None)
        if transport.get("transport_exit_code")==70:
            require(completed.returncode==70
                    and transport.get("necessary_readback_complete") is False,
                    "Preserve the actual original70 and false transport")
            desc=transport["complete_local_necessary_object"]
            complete_path=original_out/"necessary-source-overflow.json"
            require(Path(desc["file"])==complete_path and complete_path.is_file()
                    and not complete_path.is_symlink() and identity(complete_path)==desc,
                    "Read complete same-job original overflow file bytes, not its descriptor")
            complete_raw=complete_path.read_bytes()
            require(len(complete_raw)==transport["attempted_bytes"]
                    and hashlib.sha256(complete_raw).hexdigest()==transport["attempted_sha256"],
                    "Every original attempted byte is actually read and bound")
            complete=json.loads(complete_raw)
            result["original_R573_transport"]["original_transport_body"]=transport
            full_from_retained_overflow=True
        else:
            require(completed.returncode in (0,2) and "transport_exit_code" not in transport,
                    "Explicit ordinary original reader return")
            complete_path=transport_path;complete_raw=transport_raw;complete=transport
            full_from_retained_overflow=False
        require(complete.get("schema")==ANCESTOR_SCHEMA+"-necessary-v1"
                and complete.get("run")==run and complete.get("request_number")==240
                and complete.get("source")==identity(generator)
                and complete.get("plan")==identity(ancestor_plan),
                "Complete original necessary object has the real source and run")
        result["original_R573_complete_necessary"]=dict(actual=identity(complete_path),
            from_retained_overflow=full_from_retained_overflow,
            complete_original_necessary_readback_complete=complete.get("necessary_readback_complete"),
            original_record=complete)
        if not full_from_retained_overflow:
            result["original_R573_transport"]["original_transport_body"]=dict(
                same_actual_complete_original_necessary=True,actual=identity(complete_path),
                inverse="Use original_R573_complete_necessary.original_record, preserving its complete original selected object and its original readback result")
        for log in sorted(out.glob("*.stderr.log")):
            if log.is_file() and not log.is_symlink():
                result["complete_current_source_stderr"].append(dict(actual=identity(log),
                    complete_text=log.read_bytes().decode("utf-8","surrogateescape"),
                    encoding="UTF-8-surrogateescape in ASCII JSON; original bytes retained"))
        for log in sorted(out.glob("*.stdout.log")):
            if log.is_file() and not log.is_symlink():
                result["source_stdout_identities"].append(identity(log))
        result["necessary_readback_complete"]=(
            type(current.get("actual_exit")) is int
            and complete.get("necessary_readback_complete") is True)
        code=0 if result["necessary_readback_complete"] else 2
    except Exception as error:
        result["metadata_read_errors"].append(dict(type=type(error).__name__,
            message=str(error),traceback=traceback.format_exc()))
        result["necessary_readback_complete"]=False;code=2
    # The complete original scope above exists before representation is attempted.
    # All R588 tables travel in this same original source-only necessary body.
    # Representation failure is recorded with the complete original scope retained.
    complete_before_representation=result
    try:
        checked(helper,plan["relation_helper"])
        require(expected.get(helper.name)==plan["relation_helper"]["sha256"],
                "Actual relation helper belongs to complete current451 sources")
        spec=importlib.util.spec_from_file_location("_R589_complete_source_relation",helper)
        require(spec is not None and spec.loader is not None,"Metadata helper import spec")
        module=importlib.util.module_from_spec(spec)
        sys.modules[spec.name]=module
        spec.loader.exec_module(module)
        selected,relation=module.source_necessary_relation(result,expected,str(HERE))
        candidate=dict(selected)
        candidate["R588_complete_nested_relation"]=relation
        candidate["R588_inverse_order"]=[
            "Apply restore_relation to this source-only selected object with this same body's R588_complete_nested_relation; exclude the two added R588 wrapper members from the reconstructed original.",
            "Then apply each unchanged R573 and earlier named-source catalogue/reference inverse in its original nested scope.",
            "Retain original child exit70, original false transport, all complete selected values, unknown fields, errors and ungenerated suffixes."
        ]
        if len(canonical(candidate))<len(canonical(result)):
            result=candidate
    except Exception as error:
        result=dict(complete_before_representation)
        result["R588_relation_error"]=dict(type=type(error).__name__,
            message=str(error),traceback=traceback.format_exc(),
            complete_original_scope_retained=True,
            additional_scientific_acceptance_gate=False)
    raw=canonical(result)
    if len(raw)>LIMIT:
        full=out/"necessary-source-overflow.json" if out.is_dir() else None
        if full is not None:write(full,result)
        result=dict(schema=SCHEMA+"-necessary-v1",request_number=246,source=identity(__file__),
            run=run,plan=complete_before_representation["plan"],
            necessary_readback_complete=False,source_preparation_complete=False,
            transport_exit_code=70,attempted_bytes=len(raw),
            attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=identity(full) if full is not None else None,
            original_R573_readback_exit=(complete_before_representation.get("original_R573_readback") or {}).get("actual_exit"),
            original_R573_transport=(complete_before_representation.get("original_R573_transport") or {}).get("actual"),
            original_R573_complete_necessary=(complete_before_representation.get("original_R573_complete_necessary") or {}).get("actual"),
            cleanup_permitted=False,no_segments_or_encoded_raw=True,numerical_success_not_inferred=True)
        raw=canonical(result);code=70
    target=runner/(META_NAME+"-necessary.json")
    with target.open("xb") as stream:stream.write(raw)
    print("BEGIN_"+FRAME,flush=True);print(raw.decode("ascii"),end="",flush=True)
    print("END_"+FRAME,flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("source_necessary_summary="+str(target)+"\n")
            stream.write("source_necessary_bytes="+str(len(raw))+"\n")
            stream.write("source_necessary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
            stream.write("source_readback_complete="+str(complete_before_representation["necessary_readback_complete"] if code!=70 else False).lower()+"\n")
    return code


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("prepare","readback"))
    parser.add_argument("--plan",type=Path,required=True)
    parser.add_argument("--plan-sha256",required=True)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    try:return prepare(args) if args.mode=="prepare" else readback(args)
    except Exception as error:
        print(json.dumps(dict(event="R589_source_preparation_unreturned",schema=SCHEMA,
            source=identity(__file__),complete=False,cleanup_permitted=False,
            error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())),
            ensure_ascii=True),flush=True)
        return 2


if __name__=="__main__":
    raise SystemExit(main())

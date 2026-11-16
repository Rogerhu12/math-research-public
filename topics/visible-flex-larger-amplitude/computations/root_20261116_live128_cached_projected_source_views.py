#!/usr/bin/env python3
"""R547: actual R534 model sources plus the original R535 owner compiler.

Only source and necessary metadata are processed. The unchanged R534 source
generator returns first; the unchanged R535 adapter creates its two include
views; ten explicit new callers are then written under new basenames. No
scientific clock, import, compilation, fixture or numerical solve starts here.
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
SCHEMA="R547-root-cached-current-owner-projected-model-source-preparation-v1"
PLAN_SCHEMA="R547-root-cached-current-owner-projected-model-complete-source-plan-v1"
META_NAME="request231-source-preparation"
FRAME="R547_CACHED_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY"
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
            "Actual source views are beside their true callers")
    path=args.plan.resolve(strict=True)
    require(not args.plan.is_symlink() and sha(path)==args.plan_sha256,
            "Actual complete R547 source plan")
    plan=json.loads(path.read_bytes())
    require(plan["schema"]==PLAN_SCHEMA and plan["repository"]==REPOSITORY,
            "R547 plan schema and public repository")
    checked(__file__,plan["generator"])
    views=plan["views"]
    require(len(views)==10 and len({v["role"] for v in views})==10
            and len({v["output"]["file"] for v in views})==10,
            "Ten distinct new callers; unchanged R534 mathematical consumers retained")
    ancestor=plan["ancestor"]
    req_path=checked(HERE/basename(ancestor["request"]["file"]),ancestor["request"])
    request=json.loads(req_path.read_bytes())
    require(request["schema"]=="public-live128-projected-model-original-full112-FD-fullDN-request-v1"
            and request["request_number"]==229
            and len(request["source_sha256"])==372
            and len(request["generated_source_sha256"])==27,
            "Frozen complete229 source/input ancestry; not a new scientific call")
    require(request["source_generator"]==ancestor["generator"]
            and request["source_plan"]==ancestor["plan"]
            and request["core_source_plan"]==ancestor["core_plan"],
            "Exact actual R534 generator and both plans from the complete ancestor")
    generator=checked(HERE/basename(ancestor["generator"]["file"]),ancestor["generator"])
    ancestor_plan=topic_file(ancestor["plan"])
    topic_file(ancestor["core_plan"])
    root_plan=topic_file(plan["root_word_plan"])
    root_words=json.loads(root_plan.read_bytes())
    require(root_words["schema"]=="R535-native-root-finite-words-complete-source-plan-v1"
            and root_words["header"]==plan["root_word_header"]
            and [dict(role=v["role"],output=v["output"]) for v in root_words["views"]]
                ==plan["root_word_outputs"],
            "The complete unchanged R535 source plan and both real include views")
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve()
    require(out.parent==runner and out.name==META_NAME and not args.out.is_symlink(),
            "Exact independent source metadata directory")
    return workspace,plan,path,views,out,request,req_path,generator,ancestor_plan,root_plan

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
    workspace,plan,path,views,out,request,req_path,generator,ancestor_plan,root_plan=context(args)
    require(not out.exists(),"Fresh actual source preparation directory")
    out.mkdir(mode=0o700)
    record=dict(schema=SCHEMA,request_number=231,
        run={k:os.environ.get(k) for k in RUN_KEYS},
        source=identity(__file__),plan=identity(path),actual_computations=str(HERE),
        ancestor_request=identity(req_path),ancestor_plan=identity(ancestor_plan),
        root_word_plan=identity(root_plan),
        complete=False,phase="bind-source-ancestry",error=None,
        original_published_files_modified=False,scientific_modules_imported=False,
        scientific_code_evaluated=False,compiler_started=False,
        scientific_clock_created=False,ancestor229_is_source_only=True,
        generated=[],not_generated=["R535/"+r["role"] for r in plan["root_word_outputs"]]
            +[v["role"] for v in views])
    record_path=out/"source-views.json"
    write(record_path,record)
    code=2
    try:
        head=subprocess.check_output(["git","-C",str(workspace),"rev-parse","HEAD"],
                                     text=True).strip()
        require(head==os.environ["GITHUB_SHA"],"Actual unmodified science checkout head")
        for row in plan["additional_public_sources"]:
            checked(HERE/basename(row["file"]),row)
        for row in [r["output"] for r in plan["root_word_outputs"]]+[v["output"] for v in views]:
            target=HERE/basename(row["file"])
            require(not target.exists() and not target.is_symlink(),
                    "Do not overwrite an existing source: "+target.name)
        runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        ancestor_out=runner/"request229-source-preparation"
        require(not ancestor_out.exists(),"The unchanged R534 generator is called once")
        command=[sys.executable,"-u",str(generator),"prepare",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(ancestor_out)]
        record["phase"]="R534-source-preparation"
        child=source_child(command,out,"R534_child",record,record_path)
        original_path=ancestor_out/"source-views.json"
        if original_path.is_file() and not original_path.is_symlink():
            original=json.loads(original_path.read_bytes())
            child["actual_source_receipt"]=identity(original_path)
            child["source_result"]=original
        else:original=None
        write(record_path,record,True)
        require(child["actual_exit"]==0 and isinstance(original,dict)
            and original.get("schema")=="R534-current-owner-projected-model-source-preparation-v1"
            and original.get("complete") is True and original.get("error") is None
            and original.get("run")==record["run"]
            and original.get("actual_computations")==str(HERE),
            "Actual complete same-job R534 source preparation has returned")
        complete=dict(request["source_sha256"])
        record["verified_ancestor_sources"]=[]
        for name,digest in complete.items():
            source=HERE/basename(name)
            require(source.is_file() and not source.is_symlink() and sha(source)==digest,
                    "Every original372 source stays byte-identical: "+name)
            record["verified_ancestor_sources"].append(identity(source))
        for row in plan["additional_public_sources"]:
            require(row["file"] not in complete,"Distinct additional public source")
            checked(HERE/row["file"],row)
            complete[row["file"]]=row["sha256"]
        require(Path(__file__).name not in complete,"Distinct R547 generator")
        complete[Path(__file__).name]=sha(__file__)
        pending=[]
        for view in views:
            baseline=checked(HERE/basename(view["baseline"]["file"]),view["baseline"])
            require(complete.get(baseline.name)==view["baseline"]["sha256"],
                    "All literal bases belong to the unchanged complete R534 closure")
            text,changes=literal(baseline.read_bytes().decode("utf-8"),
                                 view["patches"],view["role"])
            raw=text.encode("utf-8")
            require(len(raw)==view["output"]["bytes"]
                    and hashlib.sha256(raw).hexdigest()==view["output"]["sha256"],
                    "Whole new caller output identity: "+view["role"])
            name=basename(view["output"]["file"])
            require(name not in complete,"Each new caller keeps its own source name")
            complete[name]=view["output"]["sha256"]
            pending.append((view,HERE/name,raw,changes))
        for row in plan["root_word_outputs"]:
            desc=row["output"]
            require(desc["file"] not in complete,"Independent real R535 include source")
            complete[desc["file"]]=desc["sha256"]
        require(len(complete)==387 and plan["counts"]==dict(
            original229_public=345,original229_generated=27,
            additional_R535_public=2,additional_R535_generated=2,
            new_generator=1,new_caller_views=10,public=348,generated=39,complete=387),
            "The exact full387 source set, without an implicit import-completeness claim")
        record["source_counts"]=plan["counts"]
        record["phase"]="R535-source-generation"
        root_adapter=checked(HERE/plan["root_word_adapter"]["file"],plan["root_word_adapter"])
        root_out=out/"R535"
        root_out.mkdir(mode=0o700)
        binding_file=root_out/"source-binding.json"
        command=[sys.executable,"-u",str(root_adapter),"--source-plan",str(root_plan),
                 "--binding-out",str(binding_file)]
        root_child=source_child(command,out,"R535_child",record,record_path)
        root_child["observed_generated_sources"]=[]
        for item in plan["root_word_outputs"]:
            desc=item["output"];actual=HERE/desc["file"]
            observed=dict(role=item["role"],expected=desc,present=actual.exists(),
                actual=None,full_declared_source_matches=False)
            if actual.is_file() and not actual.is_symlink():
                observed["actual"]=identity(actual)
                observed["full_declared_source_matches"]=(
                    observed["actual"]["bytes"]==desc["bytes"]
                    and observed["actual"]["sha256"]==desc["sha256"])
                if observed["full_declared_source_matches"]:
                    record["generated"].append(dict(role="R535/"+item["role"],
                        actual=observed["actual"],original_R535_output_bytes_unchanged=True))
                    record["not_generated"].remove("R535/"+item["role"])
            root_child["observed_generated_sources"].append(observed)
        if binding_file.is_file() and not binding_file.is_symlink():
            root_child["actual_source_receipt"]=identity(binding_file)
            root_child["source_result"]=json.loads(binding_file.read_bytes())
        write(record_path,record,True)
        bound=root_child.get("source_result")
        require(root_child["actual_exit"]==0 and isinstance(bound,dict)
            and bound.get("schema")=="R535-native-root-finite-words-source-binding-v1"
            and bound.get("source_preparation_complete") is True
            and bound.get("compiler_completed") is False
            and bound.get("scientific_evaluation_performed_by_preparation") is False
            and Path(bound["actual_source_root"]).resolve()==HERE
            and bound.get("actual_generated_sources")==[r["output"] for r in plan["root_word_outputs"]]
            and all(r["full_declared_source_matches"] for r in root_child["observed_generated_sources"]),
            "Actual complete R535 source binding; compilation has not yet occurred")
        record["phase"]="publish-new-distinct-callers"
        write(record_path,record,True)
        for view,target,raw,changes in pending:
            with target.open("xb") as stream:stream.write(raw)
            checked(target,view["output"])
            record["generated"].append(dict(role=view["role"],actual=identity(target),
                baseline=view["baseline"],literal_changes=changes))
            record["not_generated"].remove(view["role"])
            write(record_path,record,True)
        mapping=out/"complete-source-map.json"
        generated=dict(request["generated_source_sha256"])
        generated.update({r["output"]["file"]:r["output"]["sha256"] for r in plan["root_word_outputs"]})
        generated.update({v["output"]["file"]:v["output"]["sha256"] for v in views})
        write(mapping,dict(schema=SCHEMA+"-complete-source-map-v1",run=record["run"],
            plan=record["plan"],sources=complete,generated_sources=generated,
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
    print(json.dumps(dict(event="R547_source_preparation_return",complete=record["complete"],
        actual_exit=code,actual_source_receipt=identity(record_path),
        science_success_inferred=False),ensure_ascii=True),flush=True)
    return code


def readback(args):
    workspace,plan,path,views,out,request,req_path,generator,ancestor_plan,root_plan=context(args)
    result=dict(schema=SCHEMA+"-necessary-v1",request_number=231,
        run={k:os.environ.get(k) for k in RUN_KEYS},source=identity(__file__),
        plan=identity(path),source_preparation_complete=False,
        necessary_readback_complete=False,error=None,
        numerical_acceptance_inferred=False,all_scientific_raw_outside_this_source_scope=True)
    code=2
    try:
        record_path=out/"source-views.json"
        require(record_path.is_file() and not record_path.is_symlink(),"Actual source record retained")
        record=json.loads(record_path.read_bytes())
        require(record["schema"]==SCHEMA and record["run"]==result["run"]
                and record["plan"]==result["plan"],"Same actual R547 source scope")
        result["actual_source_record"]=identity(record_path)
        for key in ("complete","phase","actual_computations","ancestor_request","ancestor_plan",
            "root_word_plan","original_published_files_modified","scientific_modules_imported",
            "scientific_code_evaluated","compiler_started","scientific_clock_created",
            "ancestor229_is_source_only","generated","not_generated","error","actual_exit",
            "source_counts","complete_source_map","current_policy_schema",
            "source_preparation_is_not_compilation_or_scientific_acceptance"):
            if key in record:result[key]=record[key]
        result["verified_ancestor_source_count"]=len(record.get("verified_ancestor_sources",[]))
        for label in ("R534_child","R535_child"):
            child=record.get(label)
            if isinstance(child,dict):
                result[label]={k:v for k,v in child.items() if k!="source_result"}
                if label=="R535_child" and "source_result" in child:
                    result[label]["complete_original_source_binding"]=child["source_result"]
        runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        ancestor_out=runner/"request229-source-preparation"
        ancestor_summary=runner/"request229-source-preparation-necessary.json"
        command=[sys.executable,"-u",str(generator),"readback",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(ancestor_out)]
        stdout_path=out/"R534-readback.stdout.log"
        stderr_path=out/"R534-readback.stderr.log"
        with stdout_path.open("xb") as stdout,stderr_path.open("xb") as stderr:
            returned=subprocess.run(command,stdout=stdout,stderr=stderr,
                check=False,start_new_session=False)
        result["actual_ancestor_readback_process"]=dict(command=command,
            returned=True,actual_exit=returned.returncode,
            stdout=identity(stdout_path),stderr=identity(stderr_path))
        ancestor_complete=False
        if ancestor_summary.is_file() and not ancestor_summary.is_symlink():
            original=json.loads(ancestor_summary.read_bytes())
            result["actual_ancestor_necessary_file"]=identity(ancestor_summary)
            result["complete_original_ancestor_necessary"]=original
            ancestor_complete=(original.get("schema")==
                "R534-current-owner-projected-model-source-preparation-v1-necessary-v1"
                and original.get("run")==result["run"]
                and original.get("necessary_readback_complete") is True
                and returned.returncode==0)
        result["complete_original_source_stderr"]=[]
        # Ancestor necessary already retains all of its own original stderr.
        # These are only this layer's actual source children, read in full.
        for log in sorted(out.glob("*.stderr.log")):
            if log.is_file() and not log.is_symlink() and log.stat().st_size:
                result["complete_original_source_stderr"].append(dict(actual=identity(log),
                    complete_text=log.read_bytes().decode("utf-8","surrogateescape"),
                    encoding="UTF-8-surrogateescape in ASCII JSON; original bytes preserved"))
        result["source_preparation_complete"]=record.get("complete") is True
        result["necessary_readback_complete"]=ancestor_complete
        code=0 if ancestor_complete else 2
    except Exception as error:
        result["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    raw=canonical(result)
    if len(raw)>LIMIT:
        full=out/"necessary-source-overflow.json" if out.is_dir() else None
        if full is not None:write(full,result)
        result=dict(schema=SCHEMA+"-necessary-v1",request_number=231,source=identity(__file__),
            run=result["run"],plan=result["plan"],necessary_readback_complete=False,
            source_preparation_complete=False,transport_exit_code=70,
            attempted_bytes=len(raw),attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=identity(full) if full is not None else None,
            cleanup_permitted=False,no_segments_or_encoded_raw=True,
            numerical_success_not_inferred=True)
        raw=canonical(result);code=70
    target=Path(os.environ["RUNNER_TEMP"])/(META_NAME+"-necessary.json")
    with target.open("xb") as stream:stream.write(raw)
    print("BEGIN_"+FRAME,flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_"+FRAME,flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("source_necessary_summary="+str(target)+"\n")
            stream.write("source_necessary_bytes="+str(len(raw))+"\n")
            stream.write("source_necessary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
            stream.write("source_readback_complete="+str(result["necessary_readback_complete"]).lower()+"\n")
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
        print(json.dumps(dict(event="R547_source_preparation_unreturned",schema=SCHEMA,
            source=identity(__file__),complete=False,cleanup_permitted=False,
            error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())),
            ensure_ascii=True),flush=True)
        return 2


if __name__=="__main__":
    raise SystemExit(main())

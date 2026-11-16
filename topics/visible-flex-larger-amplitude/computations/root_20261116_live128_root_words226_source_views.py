#!/usr/bin/env python3
"""Request226: explicit R518/R527/R522/R535 source composition before original science.

Only literal source/JSON identities are processed here. The unchanged R522
generator prepares its actual three views and the published R535 adapter
prepares two include views. Eleven new callers are formed through the fully
identified R518 and R527 text intermediates. No scientific module, compiler,
solver, scientific clock, raw array or state is created by this program.
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
REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R536-live128-root-words-source-view-preparation-v1"
PLAN_SCHEMA="R536-live128-root-words-complete-source-plan-v1"
REQUEST_SCHEMA="public-live128-root-words-original-full112-FD-fullDN-request-v1"
META_NAME="request226-source-preparation"
SCIENCE_NAME="visible-live128-root-words226"
FRAME="REQUEST226_SOURCE_PREPARATION_NECESSARY"
RUN_KEYS=("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")
LIMIT=90000


def require(ok,message):
    if not ok:raise ValueError(message)


def canonical(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,
        separators=(",",":"),allow_nan=False).encode("ascii")+b"\n"


def sha(path):
    value=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):value.update(block)
    return value.hexdigest()


def identity(path):
    path=Path(path).resolve(strict=True)
    return dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path))


def checked(path,expected,label):
    path=Path(path)
    require(path.is_file() and not path.is_symlink(),label+": actual regular file")
    require(path.stat().st_size==expected["bytes"] and sha(path)==expected["sha256"],
            label+": complete bytes and SHA")
    return path.resolve(strict=True)


def basename(name):
    require(isinstance(name,str) and name and Path(name).name==name
        and name not in (".","..") and "\x00" not in name,"One explicit source basename")
    return name


def relative_file(name):
    path=Path(name)
    require(not path.is_absolute() and ".." not in path.parts,"Actual relative topic metadata")
    return TOPIC/path


def write(path,value,replace=False):
    path=Path(path)
    temporary=path.with_name(path.name+".writing")
    require(not temporary.exists() and (replace or not path.exists()),"Exclusive metadata write")
    with temporary.open("xb") as stream:stream.write(canonical(value))
    os.replace(temporary,path)


def run_identity():
    return {key:os.environ.get(key) for key in RUN_KEYS}


def metadata_directory(value,must_exist):
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    supplied=Path(value)
    require(supplied.is_absolute() and ".." not in supplied.parts
        and not supplied.is_symlink(),"Absolute source-metadata directory")
    out=supplied.resolve(strict=must_exist)
    require(out.parent==runner and out.name==META_NAME,
            "Only the explicitly named source-metadata directory")
    return out


def context(args,require_original_head=True):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"Only the actual public Actions job")
    workspace=Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE==workspace/"topics/visible-flex-larger-amplitude/computations",
            "The true checkout HERE for every current caller")
    actual=subprocess.check_output(["git","-C",str(workspace),"rev-parse","HEAD"],text=True).strip()
    if require_original_head:
        require(actual==os.environ["GITHUB_SHA"],"The current checkout source")
    path=args.request.resolve(strict=True)
    require(not args.request.is_symlink() and sha(path)==args.request_sha256,
            "The actual complete request226 bytes")
    request=json.loads(path.read_bytes())
    require(request["schema"]==REQUEST_SCHEMA and request["request_number"]==226
        and request["repository"]==REPOSITORY and request["namespace"]==SCIENCE_NAME,
        "The independent226 contract, not the frozen221 internal number")
    plan_path=checked(relative_file(request["source_plan"]["file"]),request["source_plan"],
                      "The complete R536 source plan")
    plan=json.loads(plan_path.read_bytes())
    require(plan["schema"]==PLAN_SCHEMA and plan["repository"]==REPOSITORY,
            "The explicit R536 source plan")
    checked(__file__,plan["generator"],"The actual source generator")
    require(request["source_sha256"].get(Path(__file__).name)==plan["generator"]["sha256"],
            "The generator belongs to the actual current source map")
    return workspace,request,path,plan,plan_path


def literal(text,patches,label):
    changes=[]
    for item in patches:
        before,after,count=item["before"],item["after"],item["count"]
        require(isinstance(before,str) and before and isinstance(after,str)
            and type(count) is int and count>0,"One explicit source replacement")
        require(text.count(before)==count,label+"/"+item["id"]+": original literal count")
        text=text.replace(before,after)
        changes.append(dict(id=item["id"],count=count,
            before_sha256=hashlib.sha256(before.encode("utf-8")).hexdigest(),
            after_sha256=hashlib.sha256(after.encode("utf-8")).hexdigest()))
    return text,changes


def expected_text(text,expected,label):
    raw=text.encode("utf-8")
    require(len(raw)==expected["bytes"] and hashlib.sha256(raw).hexdigest()==expected["sha256"],
            label+": whole generated source")
    return raw


def prepare(args):
    out=metadata_directory(args.out,False)
    require(not out.exists(),"Fresh source-preparation metadata, without reusing an old job")
    out.mkdir(mode=0o700)
    record=dict(schema=SCHEMA,request_number=226,run=run_identity(),source=identity(__file__),
        complete=False,phase="binding",actual_checkout=None,actual_computations=str(HERE),
        original_public_files_modified=False,scientific_module_imported=False,
        compiler_started=False,scientific_code_evaluated=False,scientific_clock_created=False,
        old_221_input_or_response_completion_not_inferred=True,
        verified_public_sources=[],published_metadata=[],R518_intermediates=[],
        R527_intermediates=[],R522_child=None,R535_child=None,
        generated=[],not_generated=[],request=None,plan=None,error=None)
    path=out/"source-views.json"
    write(path,record)
    code=2
    try:
        workspace,request,request_path,plan,plan_path=context(args)
        record.update(request=identity(request_path),plan=identity(plan_path),
                      actual_checkout=str(workspace))
        record["not_generated"]=[item["role"] for item in plan["views"]]+[
            "R535/"+item["role"] for item in plan["root_word_outputs"]]
        original_path=checked(HERE/plan["baseline_request"]["file"],plan["baseline_request"],
                              "The unchanged complete221 request ancestor")
        original=json.loads(original_path.read_bytes())
        require(original["schema"]=="public-live128-scoped-original-full112-FD-fullDN-request-v1"
            and original["request_number"]==221 and len(original["source_sha256"])==336,
            "The complete original221 ancestor contract")
        record["original_request"]=identity(original_path)
        for name in plan["unchanged_request_members"]:
            require(request[name]==original[name],"Original numerical/resource contract: "+name)
        correction=plan["descriptive_request_member_correction"]
        require(correction["member"]=="original_scientific_contract"
            and correction["field"]=="output_jets_order",
            "One explicit descriptive output-order correction")
        expected_contract=dict(original["original_scientific_contract"])
        require(expected_contract[correction["field"]]==correction["original"],
            "The complete original descriptive order is identified")
        expected_contract[correction["field"]]=correction["current"]
        require(request["original_scientific_contract"]==expected_contract,
            "All original mathematical policy fields are identical apart from the declared description")
        public=dict(original["source_sha256"])
        for row in plan["additional_public_sources"]:
            name=basename(row["file"])
            require(name not in public,"One explicit additional public file")
            public[name]=row["sha256"]
        declared_public={name:digest for name,digest in request["source_sha256"].items()
                         if name not in request["generated_source_sha256"]}
        require(public==declared_public
            and len(public)==plan["counts"]["public_files"],
            "All original336 plus the explicit current public inputs")
        for name,digest in public.items():
            actual=HERE/basename(name)
            require(actual.is_file() and not actual.is_symlink() and sha(actual)==digest,
                    "Actual public source: "+name)
            record["verified_public_sources"].append(identity(actual))
        for row in plan["published_metadata_dependencies"]:
            actual=checked(relative_file(row["file"]),row,"Published source-plan metadata")
            record["published_metadata"].append(identity(actual))
        source_plans={}
        for role,row in plan["upstream_plans"].items():
            actual=checked(relative_file(row["file"]),row,"Original source plan "+role)
            source_plans[role]=json.loads(actual.read_bytes())
        p518=source_plans["R518"]
        require(p518["schema"]=="R518-live128-radial-cache-complete-source-plan-v1"
            and p518["baseline_request"]==plan["baseline_request"],
            "The complete published R518 intermediate contract")
        intermediates={}
        for view in p518["views"]:
            baseline=checked(HERE/basename(view["baseline"]["file"]),view["baseline"],
                             "Actual public R518 source baseline")
            require(public.get(baseline.name)==view["baseline"]["sha256"],
                    "Every R518 baseline is a current public input")
            text,changes=literal(baseline.read_bytes().decode("utf-8"),view["patches"],
                                 "R518/"+view["role"])
            expected_text(text,view["output"],"R518/"+view["role"])
            intermediates[view["role"]]=(view,text)
            record["R518_intermediates"].append(dict(role=view["role"],
                original=identity(baseline),intermediate=view["output"],
                prepared_text_only=True,written_imported_or_executed=False))
        require(len(intermediates)==12,"All twelve published R518 source intermediates")
        p522=source_plans["R522"]
        require(p522["schema"]=="R522-native128-paired-digit-complete-component-source-plan-v1",
                "The complete original R522 three-view plan")
        require(p522["generator"]==plan["paired_generator"],"The actual R522 generator tuple")
        require([item["output"] for item in p522["views"]]==plan["paired_outputs"],
                "All three original R522 outputs retain their whole bytes")
        p527=source_plans["R527"]
        require(p527["schema"]=="R527-live128-paired-cache-complete-source-plan-v1"
            and p527["baseline_request"]==plan["baseline_request"],
            "The complete published225 paired-cache source intermediate contract")
        old225_path=checked(relative_file(plan["paired_cache_request"]["file"]),
                            plan["paired_cache_request"],"The unchanged complete225 request ancestor")
        old225=json.loads(old225_path.read_bytes())
        require(old225.get("schema")=="public-live128-paired-cache-original-full112-FD-fullDN-request-v1"
            and old225.get("request_number")==225
            and old225.get("source_plan")==plan["upstream_plans"]["R527"],
            "The complete actual225 request and declared original source plan")
        record["paired_cache_request"]=identity(old225_path)
        for name,digest in old225["source_sha256"].items():
            if name not in old225["generated_source_sha256"]:
                require(public.get(name)==digest,"All original225 public source words: "+name)
        paired_views={row["role"]:row for row in p527["views"]}
        require(len(paired_views)==11,"All eleven complete original225 caller intermediates")
        p535=source_plans["R535"]
        require(p535["schema"]=="R535-native-root-finite-words-complete-source-plan-v1"
            and [dict(role=row["role"],output=row["output"]) for row in p535["views"]]
                ==plan["root_word_outputs"],
            "Both complete R535 include source views")
        require(p535["header"]==plan["root_word_header"],
            "The unchanged complete R535 finite-word header")
        pending=[];names=set()
        for item in plan["views"]:
            ancestor,text=intermediates[item["published_prefix"]["plan_role"]]
            require(ancestor["output"]==item["published_prefix"]["intermediate"],
                    "The exact R518 source intermediate for "+item["role"])
            paired_view=paired_views[item["role"]]
            require(paired_view["published_prefix"]==item["published_prefix"]
                and paired_view["output"]==item["paired_cache_intermediate"],
                "The whole original225 intermediate for "+item["role"])
            text,paired_changes=literal(text,paired_view["patches"],"R527/"+item["role"])
            expected_text(text,paired_view["output"],"R527/"+item["role"])
            record["R527_intermediates"].append(dict(role=item["role"],
                intermediate=paired_view["output"],prepared_text_only=True,
                written_imported_or_executed=False))
            text,changes=literal(text,item["patches"],"R536/"+item["role"])
            raw=expected_text(text,item["output"],"R536/"+item["role"])
            name=basename(item["output"]["file"])
            require(name not in names and name not in public and not (HERE/name).exists(),
                    "One fresh actual caller name")
            names.add(name)
            pending.append((item,HERE/name,raw,changes))
        require(len(pending)==11 and len(names)==11,"The complete eleven new callers")
        paired_names={basename(row["file"]) for row in plan["paired_outputs"]}
        require(len(paired_names)==3 and not paired_names.intersection(names)
            and not paired_names.intersection(public),"The distinct caller and paired-stage outputs")
        root_names={basename(row["output"]["file"]) for row in plan["root_word_outputs"]}
        require(len(root_names)==2 and not root_names.intersection(names)
            and not root_names.intersection(public) and not root_names.intersection(paired_names),
            "The two independent R535 include source names")
        complete_map=dict(public)
        complete_map.update({item["output"]["file"]:item["output"]["sha256"] for item in plan["views"]})
        complete_map.update({row["file"]:row["sha256"] for row in plan["paired_outputs"]})
        complete_map.update({row["output"]["file"]:row["output"]["sha256"]
                             for row in plan["root_word_outputs"]})
        generated_map={name:digest for name,digest in complete_map.items() if name not in public}
        require(generated_map==request["generated_source_sha256"]
            and complete_map==request["source_sha256"]
            and len(complete_map)==plan["counts"]["complete_files"],
            "All current caller and paired-stage identities before source publication")
        record["phase"]="R522-source-generation"
        generator=checked(HERE/plan["paired_generator"]["file"],plan["paired_generator"],
                          "The unchanged actual R522 generator")
        paired_plan=checked(relative_file(plan["upstream_plans"]["R522"]["file"]),
                            plan["upstream_plans"]["R522"],"Original R522 plan")
        child_out=out/"R522"
        command=[sys.executable,"-u",str(generator),"--computations",str(HERE),
                 "--namespace",str(out),"--plan",str(paired_plan),
                 "--plan-sha256",plan["upstream_plans"]["R522"]["sha256"],
                 "--out",str(child_out)]
        child=dict(command=command,started=False,returned=False,actual_exit=None,
                   scientific_child=False,starts_new_session=False)
        record["R522_child"]=child
        write(path,record,True)
        with (out/"R522.stdout.log").open("xb") as stdout,(out/"R522.stderr.log").open("xb") as stderr:
            child["started"]=True
            write(path,record,True)
            returned=subprocess.run(command,stdout=stdout,stderr=stderr,
                                    check=False,start_new_session=False)
        child.update(returned=True,actual_exit=returned.returncode,
                     stdout=identity(out/"R522.stdout.log"),stderr=identity(out/"R522.stderr.log"))
        source_receipt=child_out/"source-views.json"
        if source_receipt.is_file():
            child["actual_source_receipt"]=identity(source_receipt)
            child["source_result"]=json.loads(source_receipt.read_bytes())
        write(path,record,True)
        require(returned.returncode==0,"The actual R522 source child returned nonzero")
        observed=child.get("source_result")
        require(isinstance(observed,dict) and observed.get("complete") is True
            and observed.get("transport_complete") is True
            and observed.get("run")==os.environ["GITHUB_RUN_ID"]
            and observed.get("attempt")==os.environ["GITHUB_RUN_ATTEMPT"]
            and observed.get("actual_checkout_source")==os.environ["GITHUB_SHA"],
            "The actual same-job complete R522 source return")
        for row in plan["paired_outputs"]:
            actual=checked(HERE/row["file"],row,"Actual R522 output")
            record["generated"].append(dict(role="R522/"+next(
                v["role"] for v in p522["views"] if v["output"]==row),
                actual=identity(actual),original_R522_output_bytes_unchanged=True))
        record["phase"]="R535-source-generation"
        root_adapter=checked(HERE/plan["root_word_adapter"]["file"],plan["root_word_adapter"],
                             "The unchanged actual R535 source adapter")
        root_plan=checked(relative_file(plan["upstream_plans"]["R535"]["file"]),
                          plan["upstream_plans"]["R535"],"Complete published R535 source plan")
        root_out=out/"R535"
        root_out.mkdir(mode=0o700)
        root_binding=root_out/"source-binding.json"
        command=[sys.executable,"-u",str(root_adapter),"--source-plan",str(root_plan),
                 "--binding-out",str(root_binding)]
        root_child=dict(command=command,started=False,returned=False,actual_exit=None,
                        scientific_child=False,starts_new_session=False,
                        observed_generated_sources=[])
        record["R535_child"]=root_child
        write(path,record,True)
        with (out/"R535.stdout.log").open("xb") as stdout,(out/"R535.stderr.log").open("xb") as stderr:
            root_child["started"]=True
            write(path,record,True)
            root_returned=subprocess.run(command,stdout=stdout,stderr=stderr,
                                         check=False,start_new_session=False)
        root_child.update(returned=True,actual_exit=root_returned.returncode,
            stdout=identity(out/"R535.stdout.log"),stderr=identity(out/"R535.stderr.log"))
        for item in plan["root_word_outputs"]:
            row=item["output"];actual=HERE/row["file"]
            observed=dict(role=item["role"],expected=row,present=actual.exists(),
                          actual=None,full_declared_source_matches=False)
            if actual.is_file() and not actual.is_symlink():
                observed["actual"]=identity(actual)
                observed["full_declared_source_matches"]=(
                    observed["actual"]["bytes"]==row["bytes"]
                    and observed["actual"]["sha256"]==row["sha256"])
                if observed["full_declared_source_matches"]:
                    record["generated"].append(dict(role="R535/"+item["role"],
                        actual=observed["actual"],original_R535_output_bytes_unchanged=True))
                    record["not_generated"].remove("R535/"+item["role"])
            root_child["observed_generated_sources"].append(observed)
        if root_binding.is_file() and not root_binding.is_symlink():
            root_child["actual_source_receipt"]=identity(root_binding)
            root_child["source_result"]=json.loads(root_binding.read_bytes())
        write(path,record,True)
        require(root_returned.returncode==0,"The actual R535 source-only child returned nonzero")
        root_observed=root_child.get("source_result")
        require(isinstance(root_observed,dict)
            and root_observed.get("schema")=="R535-native-root-finite-words-source-binding-v1"
            and root_observed.get("source_preparation_complete") is True
            and root_observed.get("compiler_completed") is False
            and root_observed.get("scientific_evaluation_performed_by_preparation") is False
            and Path(root_observed["actual_source_root"]).resolve()==HERE
            and root_observed.get("actual_generated_sources")
                ==[item["output"] for item in plan["root_word_outputs"]]
            and all(row["full_declared_source_matches"]
                    for row in root_child["observed_generated_sources"]),
            "Actual complete R535 source preparation, distinct from compilation and science")
        record["phase"]="new-caller-publication"
        write(path,record,True)
        for item,target,raw,changes in pending:
            with target.open("xb") as stream:stream.write(raw)
            record["generated"].append(dict(role=item["role"],actual=identity(target),
                R518_intermediate=item["published_prefix"]["intermediate"],
                R527_intermediate=item["paired_cache_intermediate"],
                literal_substitutions=changes))
            record["not_generated"].remove(item["role"])
            write(path,record,True)
        record.update(complete=True,phase="source-prepared",
            source_count=dict(public=len(public),paired_generated=3,
                root_word_generated=2,caller_generated=len(pending),complete=len(complete_map)),
            current_policy_schema="R536-current-H-live128-root-words-client-policy-v1",
            current_science_namespace=str(Path(os.environ["RUNNER_TEMP"])/SCIENCE_NAME))
        write(path,record,True)
        code=0
    except Exception as error:
        record["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        write(path,record,True)
    print(json.dumps(dict(event="request226_source_preparation_return",
        complete=record["complete"],actual_exit=code,actual_source_receipt=identity(path),
        original_science_not_started_by_source_preparation=True)),flush=True)
    return code


def readback(args):
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    summary_path=runner/"request226-source-necessary.json"
    result=dict(schema=SCHEMA+"-necessary",request_number=226,run=run_identity(),
        source=identity(__file__),source_preparation_complete=False,
        necessary_readback_complete=False,science_success_inferred=False,
        no_scientific_array_or_result_tree_read=True,actual_error=None)
    code=2
    out=None
    try:
        out=metadata_directory(args.out,False)
        workspace,request,request_path,plan,plan_path=context(args,False)
        result["request"]=identity(request_path)
        result["plan"]=identity(plan_path)
        path=out/"source-views.json"
        require(path.is_file() and not path.is_symlink(),"Actual source-preparation receipt returned")
        original=json.loads(path.read_bytes())
        require(original.get("schema")==SCHEMA and original.get("request_number")==226
            and original.get("run")==run_identity(),"The original same-run source-preparation scope")
        if original.get("request") is not None:
            require(original["request"]==identity(request_path),"The actual source request remains identical")
        result["complete_source_preparation_receipt"]=identity(path)
        for key in ("complete","phase","actual_checkout","actual_computations",
            "original_public_files_modified","scientific_module_imported","compiler_started",
            "scientific_code_evaluated","scientific_clock_created",
            "old_221_input_or_response_completion_not_inferred","original_request",
            "published_metadata","R518_intermediates","R527_intermediates","paired_cache_request",
            "generated","not_generated",
            "source_count","current_policy_schema","current_science_namespace","error"):
            if key in original:result[key]=original[key]
        result["verified_public_source_count"]=len(original.get("verified_public_sources",[]))
        result["complete_public_file_receipts_retained_in_bound_local_preparation"]=True
        child=original.get("R522_child")
        if isinstance(child,dict):
            result["R522_child"]={key:value for key,value in child.items() if key!="source_result"}
            actual=child.get("source_result")
            if isinstance(actual,dict):
                result["R522_child"]["selected_original_source_result"]={
                    key:actual[key] for key in ("schema","complete","transport_complete",
                    "transport_exit_code","run","attempt","actual_checkout_source","namespace",
                    "computations","plan","generator","views","not_generated","error",
                    "scientific_code_imported","scientific_code_compiled","scientific_code_executed",
                    "creates_scientific_clock","changes_original_clock_or_resource_caps",
                    "source_preparation_is_not_numerical_acceptance",
                    "existing_owner_and_full_source_closure_still_required") if key in actual}
                result["R522_child"]["original_public_inputs_count"]=len(actual.get("public_inputs",[]))
        if "R535_child" in original:
            result["R535_child"]=original["R535_child"]
        result["complete_original_source_stderr"]=[]
        for path in sorted(out.glob("*.stderr.log")):
            if path.is_file() and not path.is_symlink():
                raw=path.read_bytes()
                if raw:
                    result["complete_original_source_stderr"].append(dict(actual=identity(path),
                        text=raw.decode("utf-8","surrogateescape"),
                        encoding="UTF-8-surrogateescape then ASCII JSON; all original bytes preserved"))
        result["source_preparation_complete"]=original.get("complete") is True
        result["necessary_readback_complete"]=True
        code=0
    except Exception as error:
        result["actual_error"]=dict(type=type(error).__name__,message=str(error),
                                   traceback=traceback.format_exc())
    raw=canonical(result)
    if len(raw)>LIMIT:
        full=out/"source-necessary-overflow.json" if out is not None and out.is_dir() else None
        if full is not None:write(full,result)
        result=dict(schema=SCHEMA+"-necessary",request_number=226,run=run_identity(),
            source=identity(__file__),
            request=dict(file=str(args.request),sha256=args.request_sha256),
            necessary_readback_complete=False,source_preparation_complete=False,
            transport_exit_code=70,attempted_bytes=len(raw),
            attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=identity(full) if full is not None else None,
            original_preparation_success_not_inferred_from_transport_failure=True,
            full_selected_scope_not_returned=True,no_segments_or_encoded_tree_returned=True,
            cleanup_permitted=False)
        raw=canonical(result);code=70
    with summary_path.open("xb") as stream:stream.write(raw)
    print("BEGIN_"+FRAME,flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_"+FRAME,flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        delimiter="R536_SOURCE_NECESSARY_"+hashlib.sha256(raw).hexdigest()
        require(delimiter not in raw.decode("ascii"),"One literal output delimiter")
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("source_necessary_json<<"+delimiter+"\n"+
                         raw.decode("ascii").rstrip("\n")+"\n"+delimiter+"\n")
            stream.write("source_necessary_bytes="+str(len(raw))+"\n")
            stream.write("source_necessary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
            stream.write("source_readback_complete="+str(
                result.get("necessary_readback_complete") is True).lower()+"\n")
            stream.write("source_preparation_complete="+str(
                result.get("source_preparation_complete") is True).lower()+"\n")
    return code


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("prepare","readback"))
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if args.mode=="readback":return readback(args)
    try:return prepare(args)
    except Exception as error:
        print(json.dumps(dict(event="request226_source_preparation_not_returned",
            schema=SCHEMA,request_number=226,run=run_identity(),source=identity(__file__),
            complete=False,actual_error=dict(type=type(error).__name__,message=str(error),
            traceback=traceback.format_exc()),scientific_success_not_inferred=True,
            cleanup_permitted=False),ensure_ascii=True),flush=True)
        return 2


if __name__=="__main__":
    raise SystemExit(main())

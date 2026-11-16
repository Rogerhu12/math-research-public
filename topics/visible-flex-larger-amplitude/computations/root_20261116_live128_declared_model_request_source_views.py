#!/usr/bin/env python3
"""R554: bind the actual declared-model request, retaining the complete R548 chain.

This is source preparation and metadata readback only. The unchanged R547
generator forms its real R534/R535 ancestry first. Nine new callers then name
the corrected current request consumer. No scientific source is imported here.
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
SCHEMA="R554-declared-model-request-source-preparation-v1"
PLAN_SCHEMA="R554-declared-model-request-complete-source-plan-v1"
META_NAME="request233-source-preparation"
FRAME="R554_DECLARED_MODEL_REQUEST_SOURCE_PREPARATION_NECESSARY"
REPOSITORY="Rogerhu12/math-research-public"
RUN_KEYS=("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")
LIMIT=90000
LINEAGE=(
    ("R547","request231-source-preparation/source-views.json",
     "R547-root-cached-current-owner-projected-model-source-preparation-v1"),
    ("R534","request229-source-preparation/source-views.json",
     "R534-current-owner-projected-model-source-preparation-v1"),
    ("R527","request225-source-preparation/source-views.json",
     "R527-live128-paired-cache-source-view-preparation-v1"),
    ("R522","request225-source-preparation/R522/source-views.json",
     "R522-native128-paired-digit-source-preparation-v1"),
    ("R535","request231-source-preparation/R535/source-binding.json",
     "R535-native-root-finite-words-source-binding-v1"),
)
SOURCE_CHILDREN=("ancestor_source_child","R534_child","R535_child","R522_child","ancestor_child")
SUCCESS_CHANGE_KEYS={"id","count","before_sha256","after_sha256","before_bytes","after_bytes"}
INVENTORY_KEYS={"verified_ancestor_sources","verified_public_sources"}
SOURCE_DUPLICATE_KEYS={"source_result","original_result","selected_original_scope"}


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
    path=Path(path);temporary=path.with_name(path.name+".writing")
    require(not temporary.exists() and (replace or not path.exists()),
            "Exclusive source metadata, never an overwritten scientific result")
    with temporary.open("xb") as stream:stream.write(canonical(value))
    os.replace(temporary,path)


def basename(name):
    require(isinstance(name,str) and name and Path(name).name==name
            and name not in (".","..") and "\x00" not in name,
            "One ordinary explicit source basename")
    return name


def checked(path,desc):
    path=Path(path)
    require(path.is_file() and not path.is_symlink()
            and path.stat().st_size==desc["bytes"] and sha(path)==desc["sha256"],
            "Actual source/metadata bytes and SHA: "+str(path))
    return path.resolve(strict=True)


def topic_file(desc):
    rel=Path(desc["file"])
    require(not rel.is_absolute() and ".." not in rel.parts,
            "Ordinary topic metadata path")
    path=TOPIC/rel
    require(path.resolve(strict=True).is_relative_to(TOPIC),
            "Metadata remains in the actual topic")
    return checked(path,desc)


def context(args):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
            "Only this public repository Actions prepares the source views")
    workspace=Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE==workspace/"topics/visible-flex-larger-amplitude/computations"
            and args.computations.resolve(strict=True)==HERE,
            "Actual generated views are beside their true callers")
    path=args.plan.resolve(strict=True)
    require(not args.plan.is_symlink() and sha(path)==args.plan_sha256,
            "Actual complete R554 plan")
    plan=json.loads(path.read_bytes())
    require(plan["schema"]==PLAN_SCHEMA and plan["repository"]==REPOSITORY,
            "Explicit complete source plan and repository")
    checked(__file__,plan["generator"])
    views=plan["views"]
    require(len(views)==9 and len({v["role"] for v in views})==9
            and len({v["output"]["file"] for v in views})==9,
            "Nine explicit changed callers; original cached owner is unchanged")
    ancestor=plan["ancestor"]
    request_path=checked(HERE/basename(ancestor["request"]["file"]),ancestor["request"])
    request=json.loads(request_path.read_bytes())
    require(request["schema"]=="public-live128-root-cached-projected-model-original-full112-FD-fullDN-request-v1"
            and request["request_number"]==231 and len(request["source_sha256"])==387
            and len(request["generated_source_sha256"])==39,
            "The complete frozen R548 source/input ancestry")
    require(request["source_generator"]==ancestor["generator"]
            and request["source_plan"]==ancestor["plan"],
            "Actual unchanged ancestor generator and its plan")
    generator=checked(HERE/basename(ancestor["generator"]["file"]),ancestor["generator"])
    ancestor_plan=topic_file(ancestor["plan"])
    # The generated owner is bound only after its real ancestor generator returns.
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve()
    require(not args.out.is_symlink() and out==runner/META_NAME,
            "Only this exact temporary source-preparation directory")
    return workspace,runner,plan,path,views,out,request,request_path,generator,ancestor_plan


def literal(source,changes,role):
    text=source;record=[]
    for change in changes:
        before=change["before"];after=change["after"];count=change["count"]
        require(isinstance(before,str) and before and isinstance(after,str)
                and type(count) is int and count>0 and text.count(before)==count,
                "Exact declared literal source anchor: "+role+"/"+change["id"])
        text=text.replace(before,after)
        record.append(dict(id=change["id"],count=count,
            before_bytes=len(before.encode()),before_sha256=hashlib.sha256(before.encode()).hexdigest(),
            after_bytes=len(after.encode()),after_sha256=hashlib.sha256(after.encode()).hexdigest()))
    return text,record


def prepare(args):
    workspace,runner,plan,path,views,out,request,request_path,generator,ancestor_plan=context(args)
    require(not out.exists(),"Fresh source preparation; no cached scientific response")
    out.mkdir(mode=0o700)
    record=dict(schema=SCHEMA,request_number=233,run={k:os.environ.get(k) for k in RUN_KEYS},
        source=identity(__file__),plan=identity(path),actual_computations=str(HERE),
        ancestor_request=identity(request_path),ancestor_plan=identity(ancestor_plan),
        unchanged_owner=plan["unchanged_owner"],complete=False,phase="bind-source-ancestry",
        original_published_files_modified=False,scientific_modules_imported=False,
        scientific_code_evaluated=False,compiler_started=False,scientific_clock_created=False,
        ancestor231_is_source_only=True,generated=[],not_generated=[v["role"] for v in views],
        error=None)
    record_path=out/"source-views.json";write(record_path,record)
    code=2
    try:
        head=subprocess.check_output(["git","-C",str(workspace),"rev-parse","HEAD"],text=True).strip()
        require(head==os.environ["GITHUB_SHA"],"Actual checkout head, not a historical source label")
        for view in views:
            target=HERE/basename(view["output"]["file"])
            require(not target.exists() and not target.is_symlink(),
                    "Never overwrite an original or already generated source: "+target.name)
        ancestor_out=runner/"request231-source-preparation"
        require(not ancestor_out.exists(),"The actual frozen R547 source chain is called once")
        command=[sys.executable,"-u",str(generator),"prepare",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(ancestor_out)]
        record["phase"]="R547-source-preparation"
        child=dict(command=command,started=True,returned=False,scientific_child=False,
            starts_new_session=False,creates_scientific_clock=False)
        record["ancestor_child"]=child;write(record_path,record,True)
        stdout_path=out/"R547.stdout.log";stderr_path=out/"R547.stderr.log"
        with stdout_path.open("xb") as stdout,stderr_path.open("xb") as stderr:
            completed=subprocess.run(command,stdout=stdout,stderr=stderr,
                check=False,start_new_session=False)
        child.update(returned=True,actual_exit=completed.returncode,
            stdout=identity(stdout_path),stderr=identity(stderr_path))
        original_path=ancestor_out/"source-views.json"
        if original_path.is_file() and not original_path.is_symlink():
            original=json.loads(original_path.read_bytes())
            child["actual_source_receipt"]=identity(original_path)
        else:original=None
        write(record_path,record,True)
        require(completed.returncode==0 and isinstance(original,dict)
            and original.get("schema")==LINEAGE[0][2] and original.get("complete") is True
            and original.get("error") is None and original.get("run")==record["run"]
            and original.get("actual_computations")==str(HERE),
            "Actual same-job complete R547 source preparation")
        complete=dict(request["source_sha256"])
        record["verified_ancestor_sources"]=[]
        for name,digest in complete.items():
            source=HERE/basename(name)
            require(source.is_file() and not source.is_symlink() and sha(source)==digest,
                    "All original387 sources remain byte-identical: "+name)
            record["verified_ancestor_sources"].append(identity(source))
        checked(HERE/plan["unchanged_owner"]["file"],plan["unchanged_owner"])
        require(complete[plan["unchanged_owner"]["file"]]==plan["unchanged_owner"]["sha256"],
                "The original cached owner is retained as its real source")
        require(Path(__file__).name not in complete,"Distinct actual R554 generator")
        complete[Path(__file__).name]=sha(__file__)
        pending=[]
        for view in views:
            base=checked(HERE/basename(view["baseline"]["file"]),view["baseline"])
            require(complete.get(base.name)==view["baseline"]["sha256"],
                    "Each baseline belongs to the actual frozen ancestor")
            text,changes=literal(base.read_bytes().decode("utf-8"),view["replacements"],view["role"])
            raw=text.encode("utf-8");desc=view["output"]
            require(len(raw)==desc["bytes"] and hashlib.sha256(raw).hexdigest()==desc["sha256"],
                    "Complete declared output bytes: "+view["role"])
            name=basename(desc["file"]);require(name not in complete,"New source basename")
            complete[name]=desc["sha256"];pending.append((view,HERE/name,raw,changes))
        expected=dict(original231_public=348,original231_generated=39,
                      new_generator=1,new_caller_views=9,public=349,generated=48,complete=397)
        require(plan["counts"]==expected and len(complete)==397,
                "The actual complete397 set; no automatic transitive-import claim")
        record["source_counts"]=expected;record["phase"]="write-distinct-current-callers"
        write(record_path,record,True)
        for view,target,raw,changes in pending:
            with target.open("xb") as stream:stream.write(raw)
            checked(target,view["output"])
            record["generated"].append(dict(role=view["role"],actual=identity(target),
                baseline=view["baseline"],literal_changes=changes))
            record["not_generated"].remove(view["role"]);write(record_path,record,True)
        generated=dict(request["generated_source_sha256"])
        generated.update({v["output"]["file"]:v["output"]["sha256"] for v in views})
        mapping=out/"complete-source-map.json"
        write(mapping,dict(schema=SCHEMA+"-complete-source-map-v1",run=record["run"],
            plan=record["plan"],sources=complete,generated_sources=generated,
            counts=expected,roles=plan["roles"]))
        record.update(complete=True,phase="source-prepared",complete_source_map=identity(mapping),
            current_policy_schema=plan["schemas"]["policy"],
            future_science_namespace=plan["schemas"]["namespace"])
        code=0
    except Exception as error:
        record["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    record["actual_exit"]=code;write(record_path,record,True)
    print(json.dumps(dict(event="R554_source_preparation_return",complete=record["complete"],
        actual_exit=code,actual_source_receipt=identity(record_path),
        science_success_inferred=False),ensure_ascii=True),flush=True)
    return code


def ordered_metadata(value):
    return json.dumps(value,sort_keys=False,ensure_ascii=True,
        separators=(",",":"),allow_nan=False).encode("ascii")+b"\n"


class NamedSourceTables:
    """Only the two explicitly named source-record row schemas below."""
    CHANGE_COLUMNS=("id","count","before_bytes","before_sha256","after_bytes","after_sha256")

    def __init__(self,request,request_path,plan):
        self.mapping=dict(request["source_sha256"])
        additions=[plan["generator"]]+[v["output"] for v in plan["views"]]
        for item in additions:
            require(item["file"] not in self.mapping,"Distinct source catalogue addition")
            self.mapping[item["file"]]=item["sha256"]
        self.names=sorted(self.mapping)
        self.indices={name:i for i,name in enumerate(self.names)}
        self.actual_bytes={}
        self.literal_sha256_values=[]
        self.definition=dict(schema="R554-named-source-identity-catalogue-v1",
            actual_computations=str(HERE),ancestor_request=identity(request_path),
            ancestor_object_pointer="/source_sha256",
            complete_ancestor_source_map_retained=True,
            explicit_distinct_additions=additions,
            index_order="Python sorted ordinary source basenames from the exact combined map",
            source_count=len(self.names),
            reconstruction="file=actual_computations/name; sha256=the exact combined map[name]; bytes=the observed_bytes row for this index",
            no_unobserved_source_size_filled=True)

    @staticmethod
    def orders(rows):
        orders=[];indices=[]
        for row in rows:
            order=list(row)
            if order not in orders:orders.append(order)
            indices.append(orders.index(order))
        return orders,indices

    def inventory(self,rows):
        # No unknown keys, guessed path, absent/null conflation or invented byte count.
        sizes=dict(self.actual_bytes);indices=[]
        for row in rows:
            if not isinstance(row,dict) or set(row)!={"file","bytes","sha256"}:
                return None
            file=row["file"];size=row["bytes"];digest=row["sha256"]
            if not isinstance(file,str) or type(size) is not int or size<0:
                return None
            name=Path(file).name;index=self.indices.get(name)
            if index is None or file!=str(HERE/name) or digest!=self.mapping[name]:
                return None
            if index in sizes and sizes[index]!=size:return None
            sizes[index]=size;indices.append(index)
        orders,order_indices=self.orders(rows)
        self.actual_bytes=sizes
        raw=canonical(rows)
        return dict(schema="R554-ordered-source-inventory-rows-v1",
            ordered_source_indices=indices,original_key_orders=orders,
            row_key_order_indices=order_indices,original_row_count=len(rows),
            complete_canonical_metadata_bytes=len(raw),
            complete_canonical_metadata_sha256=hashlib.sha256(raw).hexdigest(),
            inverse="For each source index reconstruct file/bytes/sha256 from the named catalogue, inserting keys in that row's original key order")

    def changes(self,rows):
        if not all(isinstance(row,dict) and set(row)<=SUCCESS_CHANGE_KEYS
                and "id" in row and "count" in row for row in rows):
            return None
        digests=list(self.literal_sha256_values);values=[]
        for row in rows:
            values_row=[]
            for key in self.CHANGE_COLUMNS:
                value=row.get(key)
                if key in ("before_sha256","after_sha256") and key in row:
                    if not isinstance(value,str) or len(value)!=64 \
                            or any(c not in "0123456789abcdef" for c in value):
                        return None
                    if value not in digests:digests.append(value)
                    value=digests.index(value)
                values_row.append(value)
            values.append(values_row)
        self.literal_sha256_values=digests
        orders,indices=self.orders(rows);raw=canonical(rows)
        return dict(schema="R554-ordered-literal-change-identity-rows-v1",
            original_columns=list(self.CHANGE_COLUMNS),
            rows=values,sha256_index_columns=["before_sha256","after_sha256"],
            original_key_orders=orders,row_key_order_indices=indices,
            original_row_count=len(rows),complete_canonical_metadata_bytes=len(raw),
            complete_canonical_metadata_sha256=hashlib.sha256(raw).hexdigest(),
            inverse="For each original key in the recorded row order, retain its column value; only present before_sha256/after_sha256 columns resolve their exact original string through literal_sha256_values. Absent and explicit null are not identified.")

    def describe(self):
        return dict(**self.definition,
            observed_bytes=[[i,self.actual_bytes[i]] for i in sorted(self.actual_bytes)],
            literal_sha256_values=self.literal_sha256_values,
            literal_sha256_scope="Only before_sha256 and after_sha256 in the two named literal_changes/replacements source-record lists; every exact original string is retained once.")


def selected_source_record(value,references,tables,path=()):
    """Two named reversible source tables and exact whole-record references.

    Every error, unknown field, state, ungenerated suffix and actual output
    identity remains literal. Inventory rows are referenced only after all
    original file/SHA values exactly match the frozen complete source map.
    Their actual byte counts and every original row/key order remain explicit.
    All literal-change identity values remain in fixed named columns.
    """
    if isinstance(value,list):
        return [selected_source_record(v,references,tables,path+(str(i),)) for i,v in enumerate(value)]
    if not isinstance(value,dict):return value
    result={}
    for key,item in value.items():
        replacement=None
        if key in INVENTORY_KEYS and isinstance(item,list):
            replacement=tables.inventory(item)
        elif key in ("literal_changes","replacements") and isinstance(item,list):
            replacement=tables.changes(item)
        if replacement is not None:
            result[key]=replacement
        elif key in SOURCE_DUPLICATE_KEYS and isinstance(item,dict):
            raw=ordered_metadata(item)
            matches=[r for r in references if raw==r["ordered"]]
            if matches:
                result[key]=dict(schema=item.get("schema"),same_actual_source_record_role=matches[0]["role"],
                    actual_original_record=matches[0]["actual"],
                    complete_ordered_metadata_bytes=len(raw),
                    complete_ordered_metadata_sha256=hashlib.sha256(raw).hexdigest(),
                    inverse="Reuse the complete independently selected source record for this role, including original member order; no unknown field is omitted")
            else:
                result[key]=selected_source_record(item,references,tables,path+(key,))
        else:result[key]=selected_source_record(item,references,tables,path+(key,))
    return result


def match_run(value,run,label):
    if "run" not in value:return
    actual=value["run"]
    if isinstance(actual,dict):
        require(actual==run,"Same actual four-key source run: "+label)
    else:
        require(str(actual)==run["GITHUB_RUN_ID"],"Same actual source run: "+label)
        if "attempt" in value:
            require(str(value["attempt"])==run["GITHUB_RUN_ATTEMPT"],"Same source attempt")


def readback(args):
    workspace,runner,plan,path,views,out,request,request_path,generator,ancestor_plan=context(args)
    run={k:os.environ.get(k) for k in RUN_KEYS}
    result=dict(schema=SCHEMA+"-necessary-v1",request_number=233,run=run,
        source=identity(__file__),plan=identity(path),source_preparation_complete=False,
        necessary_readback_complete=False,current_source_record=None,
        original_R547_readback=None,original_R547_transport=None,
        original_R547_complete_necessary=None,complete_current_source_stderr=[],
        source_stdout_identities=[],metadata_read_errors=[],
        numerical_acceptance_inferred=False,
        all_scientific_raw_outside_this_source_scope=True,
        scope=dict(whole_original_R547_necessary_selection_consumed=True,
            actual_child70_and_original_false_transport_preserved=True,
            full_retained_overflow_body_bound_before_selection=True,
            named_reversible_source_inventory_and_literal_identity_tables=True,
            all_actual_errors_and_ungenerated_suffixes_retained=True,
            original_scientific_necessary_selector_not_modified=True,
            no_scientific_arrays_or_generic_tree_codec=True))
    code=2;records=[];tables=NamedSourceTables(request,request_path,plan)
    try:
        require(out.is_dir() and not out.is_symlink(),"Actual current source directory")
        current_path=out/"source-views.json"
        require(current_path.is_file() and not current_path.is_symlink(),
                "Actual current source record returned")
        current=json.loads(current_path.read_bytes())
        require(current.get("schema")==SCHEMA and current.get("run")==run
                and current.get("source")==identity(__file__) and current.get("plan")==result["plan"],
                "This actual source preparation, source and plan")
        result["current_source_record"]=dict(actual=identity(current_path),record=None)
        records.append(dict(role="R554-current-source-record",
                            actual=identity(current_path),value=current))
        result["source_preparation_complete"]=current.get("complete") is True
        result["actual_exit"]=current.get("actual_exit")
        result["error"]=current.get("error")
        result["not_generated"]=current.get("not_generated")
        result["source_counts"]=current.get("source_counts")
        original_out=runner/"request231-source-preparation"
        source_path=original_out/"source-views.json"
        if isinstance(current.get("ancestor_child"),dict):
            desc=current["ancestor_child"].get("actual_source_receipt")
            if desc is not None:
                require(source_path.is_file() and not source_path.is_symlink()
                        and identity(source_path)==desc,
                        "Actual same-job ancestor source record remains exactly bound")
        command=[sys.executable,"-u",str(generator),"readback",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(original_out)]
        child=dict(command=command,reader_source=identity(generator),
            original_plan=identity(ancestor_plan),started=False,returned=False,
            actual_exit=None,scientific_child=False,starts_new_session=False)
        result["original_R547_readback"]=child
        stdout_path=out/"R547-readback.stdout.log"
        stderr_path=out/"R547-readback.stderr.log"
        child["started"]=True
        with stdout_path.open("xb") as stdout,stderr_path.open("xb") as stderr:
            completed=subprocess.run(command,stdout=stdout,stderr=stderr,
                check=False,start_new_session=False)
        child.update(returned=True,actual_exit=completed.returncode,
            stdout=identity(stdout_path),stderr=identity(stderr_path))
        transport_path=runner/"request231-source-preparation-necessary.json"
        require(transport_path.is_file() and not transport_path.is_symlink(),
                "Original R547 necessary transport object returned")
        transport_raw=transport_path.read_bytes()
        transport=json.loads(transport_raw)
        require(transport.get("schema")==LINEAGE[0][2]+"-necessary-v1"
                and transport.get("run")==run and transport.get("request_number")==231
                and transport.get("source")==identity(generator)
                and transport.get("plan")==identity(ancestor_plan),
                "Same actual frozen R547 reader/run/source/plan")
        result["original_R547_transport"]=dict(actual=identity(transport_path),
            original_reader_exit=completed.returncode,
            original_necessary_readback_complete=transport.get("necessary_readback_complete"),
            original_source_preparation_complete=transport.get("source_preparation_complete"),
            original_transport_exit_code=transport.get("transport_exit_code"),
            original_transport_body=None)
        if transport.get("transport_exit_code")==70:
            require(completed.returncode==70
                and transport.get("necessary_readback_complete") is False,
                "The actual original70 and false transport are retained, not changed")
            desc=transport["complete_local_necessary_object"]
            complete_path=original_out/"necessary-source-overflow.json"
            require(Path(desc["file"])==complete_path and complete_path.is_file()
                    and not complete_path.is_symlink() and identity(complete_path)==desc,
                    "Complete same-job original overflow file bytes/SHA, not only its descriptor")
            complete_raw=complete_path.read_bytes()
            require(len(complete_raw)==transport["attempted_bytes"]
                and hashlib.sha256(complete_raw).hexdigest()==transport["attempted_sha256"],
                "Every original attempted byte is read and bound")
            complete=json.loads(complete_raw)
            result["original_R547_transport"]["original_transport_body"]=transport
            full_from_retained_overflow=True
        else:
            require(completed.returncode in (0,2) and "transport_exit_code" not in transport,
                    "Explicit ordinary original reader return")
            complete_path=transport_path;complete_raw=transport_raw;complete=transport
            full_from_retained_overflow=False
        require(complete.get("schema")==LINEAGE[0][2]+"-necessary-v1"
                and complete.get("run")==run and complete.get("request_number")==231
                and complete.get("source")==identity(generator)
                and complete.get("plan")==identity(ancestor_plan),
                "The complete original necessary object has the same real source and run")
        result["original_R547_complete_necessary"]=dict(actual=identity(complete_path),
            from_retained_overflow=full_from_retained_overflow,
            complete_original_necessary_readback_complete=complete.get("necessary_readback_complete"),
            original_record=None)
        records.append(dict(role="R547-complete-original-necessary",
                            actual=identity(complete_path),value=complete))
        if not full_from_retained_overflow:
            result["original_R547_transport"]["original_transport_body"]={
                "same_actual_complete_original_necessary":True,
                "actual":identity(complete_path),
                "inverse":"Use the complete original necessary object in original_R547_complete_necessary, not a new inferred value."}
        # Complete actual source-only stderr; duplicate stdout bodies stay identified.
        for log in (out/"R547.stderr.log",stderr_path):
            if log.is_file() and not log.is_symlink():
                if log.stat().st_size:
                    result["complete_current_source_stderr"].append(dict(actual=identity(log),
                        complete_text=log.read_bytes().decode("utf-8","surrogateescape"),
                        encoding="UTF-8-surrogateescape in ASCII JSON; original bytes retained"))
        for log in (out/"R547.stdout.log",stdout_path):
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
    references=[dict(role=row["role"],actual=row["actual"],ordered=ordered_metadata(row["value"]))
                for row in records]
    for row in records:
        selected=selected_source_record(row["value"],references,tables)
        if row["role"]=="R554-current-source-record":
            result["current_source_record"]["record"]=selected
        else:result["original_R547_complete_necessary"]["original_record"]=selected
    result["named_source_identity_catalogue"]=tables.describe()
    raw=canonical(result)
    if len(raw)>LIMIT:
        full=out/"necessary-source-overflow.json" if out.is_dir() else None
        if full is not None:write(full,result)
        result=dict(schema=SCHEMA+"-necessary-v1",request_number=233,source=identity(__file__),
            run=run,plan=result["plan"],necessary_readback_complete=False,
            source_preparation_complete=False,transport_exit_code=70,
            attempted_bytes=len(raw),attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=identity(full) if full is not None else None,
            original_R547_readback_exit=(result.get("original_R547_readback") or {}).get("actual_exit"),
            original_R547_transport=(result.get("original_R547_transport") or {}).get("actual"),
            original_R547_complete_necessary=(result.get("original_R547_complete_necessary") or {}).get("actual"),
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
            stream.write("source_readback_complete="+str(result["necessary_readback_complete"]).lower()+"\n")
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
    except Exception as error:
        print(json.dumps(dict(event="R554_source_preparation_unreturned",schema=SCHEMA,
            source=identity(__file__),complete=False,cleanup_permitted=False,
            error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())),
            ensure_ascii=True),flush=True)
        return 2


if __name__=="__main__":
    raise SystemExit(main())

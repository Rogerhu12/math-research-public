#!/usr/bin/env python3
"""R565: complete236 source ancestry and one actual R564 owner compiler.

Only source and necessary metadata are processed. The unchanged R562 source
generator first reconstructs all417 ancestors. The unchanged R564 adapter
prepares complete R561/R550/R535 ancestry and two distinct lifted-product includes.
Ten explicit new callers retain the honest projected-model contract.
No scientific clock, scientific import, compilation or solve starts here;
the real owner installs R564 directly, with no R561/R550/R535 hook installed first.
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
SCHEMA="R565-root-lifted-product-current-owner-projected-model-source-preparation-v1"
PLAN_SCHEMA="R565-root-lifted-product-current-owner-projected-model-complete-source-plan-v1"
META_NAME="request237-source-preparation"
FRAME="R565_LIFTED_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY"
RUN_KEYS=("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")
REPOSITORY="Rogerhu12/math-research-public"
LIMIT=90000
ANCESTOR_SOURCE_SCHEMA="R562-root-dyadic-current-owner-projected-model-source-preparation-v1"
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
            "Actual complete R565 source plan")
    plan=json.loads(path.read_bytes())
    require(plan["schema"]==PLAN_SCHEMA and plan["repository"]==REPOSITORY,
            "R565 plan schema and public repository")
    checked(__file__,plan["generator"])
    views=plan["views"]
    require(len(views)==10 and len({v["role"] for v in views})==10
            and len({v["output"]["file"] for v in views})==10,
            "Ten distinct new callers; unchanged R534 mathematical consumers retained")
    ancestor=plan["ancestor"]
    req_path=checked(HERE/basename(ancestor["request"]["file"]),ancestor["request"])
    request=json.loads(req_path.read_bytes())
    require(request["schema"]=="public-live128-root-dyadic-projected-model-original-full112-FD-fullDN-request-v1"
            and request["request_number"]==236
            and len(request["source_sha256"])==417
            and len(request["generated_source_sha256"])==63,
            "Frozen complete236 source/input ancestry; not a new scientific call")
    require(request["source_generator"]==ancestor["generator"]
            and request["source_plan"]==ancestor["plan"]
            and request["ancestor_R534_core_source_plan"]==ancestor["core_plan"],
            "Exact actual R562 generator/plan and retained R534 core plan")
    generator=checked(HERE/basename(ancestor["generator"]["file"]),ancestor["generator"])
    ancestor_plan=topic_file(ancestor["plan"])
    topic_file(ancestor["core_plan"])
    root_plan=topic_file(plan["root_product_plan"])
    root_words=json.loads(root_plan.read_bytes())
    average_root_plan=topic_file(plan["ancestor_root_average_plan"])
    reuse_root_plan=topic_file(plan["ancestor_root_reuse_plan"])
    ancestor_root_plan=topic_file(plan["ancestor_root_word_plan"])
    require(root_words["schema"]=="R564-exact-lifted-factor-product-complete-source-plan-v1"
            and root_words["header"]==plan["root_product_header"]
            and root_words["ancestor_R561"]["source_plan"]==plan["ancestor_root_average_plan"]
            and request["root_average_source_plan"]==plan["ancestor_root_average_plan"]
            and root_words["ancestor_R561"]["root_reuse_source_plan"]==plan["ancestor_root_reuse_plan"]
            and request["root_reuse_source_plan"]==plan["ancestor_root_reuse_plan"]
            and root_words["ancestor_R561"]["root_word_source_plan"]==plan["ancestor_root_word_plan"]
            and request["root_word_source_plan"]==plan["ancestor_root_word_plan"]
            and [dict(role=v["role"],output=v["output"]) for v in root_words["views"]]
                ==plan["root_product_outputs"],
            "Complete R564 plan, unchanged R561/R550/R535 ancestry, and both distinct include views")
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve()
    require(out.parent==runner and out.name==META_NAME and not args.out.is_symlink(),
            "Exact independent source metadata directory")
    return workspace,plan,path,views,out,request,req_path,generator,ancestor_plan,root_plan,average_root_plan,reuse_root_plan,ancestor_root_plan

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
    workspace,plan,path,views,out,request,req_path,generator,ancestor_plan,root_plan,average_root_plan,reuse_root_plan,ancestor_root_plan=context(args)
    require(not out.exists(),"Fresh actual source preparation directory")
    out.mkdir(mode=0o700)
    record=dict(schema=SCHEMA,request_number=237,
        run={k:os.environ.get(k) for k in RUN_KEYS},
        source=identity(__file__),plan=identity(path),actual_computations=str(HERE),
        ancestor_request=identity(req_path),ancestor_plan=identity(ancestor_plan),
        root_product_plan=identity(root_plan),ancestor_root_average_plan=identity(average_root_plan),
        ancestor_root_reuse_plan=identity(reuse_root_plan),
        ancestor_root_word_plan=identity(ancestor_root_plan),
        complete=False,phase="bind-source-ancestry",error=None,
        original_published_files_modified=False,scientific_modules_imported=False,
        scientific_code_evaluated=False,compiler_started=False,
        scientific_clock_created=False,ancestor236_is_source_only=True,
        generated=[],not_generated=["R564/"+r["role"] for r in plan["root_product_outputs"]]
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
        for row in [r["output"] for r in plan["root_product_outputs"]]+[v["output"] for v in views]:
            target=HERE/basename(row["file"])
            require(not target.exists() and not target.is_symlink(),
                    "Do not overwrite an existing source: "+target.name)
        runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        ancestor_out=runner/"request236-source-preparation"
        require(not ancestor_out.exists(),"The unchanged R562 generator is called once")
        command=[sys.executable,"-u",str(generator),"prepare",
            "--plan",str(ancestor_plan),"--plan-sha256",plan["ancestor"]["plan"]["sha256"],
            "--computations",str(HERE),"--out",str(ancestor_out)]
        record["phase"]="R562-source-preparation"
        child=source_child(command,out,"R562_child",record,record_path)
        original_path=ancestor_out/"source-views.json"
        if original_path.is_file() and not original_path.is_symlink():
            original=json.loads(original_path.read_bytes())
            child["actual_source_receipt"]=identity(original_path)
            # The full actual ancestor record stays at its bound file.
            # Its complete original necessary selection is read by the old reader.
        else:original=None
        write(record_path,record,True)
        require(child["actual_exit"]==0 and isinstance(original,dict)
            and original.get("schema")==ANCESTOR_SOURCE_SCHEMA
            and original.get("complete") is True and original.get("error") is None
            and original.get("run")==record["run"]
            and original.get("actual_computations")==str(HERE),
            "Actual complete same-job R562 source preparation has returned")
        complete=dict(request["source_sha256"])
        record["verified_ancestor_sources"]=[]
        for name,digest in complete.items():
            source=HERE/basename(name)
            require(source.is_file() and not source.is_symlink() and sha(source)==digest,
                    "Every original417 source stays byte-identical: "+name)
            record["verified_ancestor_sources"].append(identity(source))
        for row in plan["additional_public_sources"]:
            require(row["file"] not in complete,"Distinct additional public source")
            checked(HERE/row["file"],row)
            complete[row["file"]]=row["sha256"]
        require(Path(__file__).name not in complete,"Distinct R565 generator")
        complete[Path(__file__).name]=sha(__file__)
        pending=[]
        for view in views:
            baseline=checked(HERE/basename(view["baseline"]["file"]),view["baseline"])
            require(complete.get(baseline.name)==view["baseline"]["sha256"],
                    "All literal bases belong to the unchanged complete R562 closure")
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
        for row in plan["root_product_outputs"]:
            desc=row["output"]
            require(desc["file"] not in complete,"Independent real R564 include source")
            complete[desc["file"]]=desc["sha256"]
        require(len(complete)==432 and plan["counts"]==dict(
            original236_public=354,original236_generated=63,
            additional_R564_public=2,additional_R564_generated=2,
            new_generator=1,new_caller_views=10,public=357,generated=75,complete=432),
            "The exact full432 source set, without an implicit import-completeness claim")
        record["source_counts"]=plan["counts"]
        record["phase"]="R564-source-generation"
        root_adapter=checked(HERE/plan["root_product_adapter"]["file"],plan["root_product_adapter"])
        root_out=out/"R564"
        root_out.mkdir(mode=0o700)
        binding_file=root_out/"source-binding.json"
        command=[sys.executable,"-u",str(root_adapter),"--source-plan",str(root_plan),
                 "--average-source-plan",str(average_root_plan),
                 "--reuse-source-plan",str(reuse_root_plan),
                 "--word-source-plan",str(ancestor_root_plan),
                 "--binding-out",str(binding_file)]
        root_child=source_child(command,out,"R564_child",record,record_path)
        root_child["observed_generated_sources"]=[]
        for item in plan["root_product_outputs"]:
            desc=item["output"];actual=HERE/desc["file"]
            observed=dict(role=item["role"],expected=desc,present=actual.exists(),
                actual=None,full_declared_source_matches=False)
            if actual.is_file() and not actual.is_symlink():
                observed["actual"]=identity(actual)
                observed["full_declared_source_matches"]=(
                    observed["actual"]["bytes"]==desc["bytes"]
                    and observed["actual"]["sha256"]==desc["sha256"])
                if observed["full_declared_source_matches"]:
                    record["generated"].append(dict(role="R564/"+item["role"],
                        actual=observed["actual"],original_R564_output_bytes_unchanged=True))
                    record["not_generated"].remove("R564/"+item["role"])
            root_child["observed_generated_sources"].append(observed)
        if binding_file.is_file() and not binding_file.is_symlink():
            root_child["actual_source_receipt"]=identity(binding_file)
            root_child["source_result"]=json.loads(binding_file.read_bytes())
        write(record_path,record,True)
        bound=root_child.get("source_result")
        require(root_child["actual_exit"]==0 and isinstance(bound,dict)
            and bound.get("schema")=="R564-exact-lifted-factor-product-source-binding-v1"
            and bound.get("source_preparation_complete") is True
            and bound.get("run")==record["run"]
            and bound.get("compiler_completed") is False
            and bound.get("scientific_evaluation_performed_by_preparation") is False
            and Path(bound["actual_source_root"]).resolve()==HERE
            and bound.get("actual_generated_sources")==[r["output"] for r in plan["root_product_outputs"]]
            and all(r["full_declared_source_matches"] for r in root_child["observed_generated_sources"]),
            "Actual complete R564 source binding; compilation has not yet occurred")
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
        generated.update({r["output"]["file"]:r["output"]["sha256"] for r in plan["root_product_outputs"]})
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
    print(json.dumps(dict(event="R565_source_preparation_return",complete=record["complete"],
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
        additions=plan["additional_public_sources"]+[plan["generator"]] \
            +[row["output"] for row in plan["root_product_outputs"]] \
            +[v["output"] for v in plan["views"]]
        for item in additions:
            require(item["file"] not in self.mapping,"Distinct source catalogue addition")
            self.mapping[item["file"]]=item["sha256"]
        self.names=sorted(self.mapping)
        self.indices={name:i for i,name in enumerate(self.names)}
        self.actual_bytes={}
        self.literal_sha256_values=[]
        self.definition=dict(schema="R565-named-source-identity-catalogue-v1",
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
        return dict(schema="R565-ordered-source-inventory-rows-v1",
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
        return dict(schema="R565-ordered-literal-change-identity-rows-v1",
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



def readback(args):
    workspace,plan,path,views,out,request,request_path,generator,ancestor_plan,root_plan,average_root_plan,reuse_root_plan,ancestor_root_plan=context(args)
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    run={k:os.environ.get(k) for k in RUN_KEYS}
    result=dict(schema=SCHEMA+"-necessary-v1",request_number=237,run=run,
        source=identity(__file__),plan=identity(path),source_preparation_complete=False,
        necessary_readback_complete=False,current_source_record=None,
        original_R562_readback=None,original_R562_transport=None,
        original_R562_complete_necessary=None,complete_current_source_stderr=[],
        source_stdout_identities=[],metadata_read_errors=[],
        numerical_acceptance_inferred=False,
        all_scientific_raw_outside_this_source_scope=True,
        scope=dict(whole_original_R562_necessary_selection_consumed=True,
            complete_current_R564_child_binding_and_partial_sources_retained=True,
            original_R562_source_result_not_duplicated_in_current_preparation_record=True,
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
        records.append(dict(role="R565-current-source-record",
                            actual=identity(current_path),value=current))
        result["source_preparation_complete"]=current.get("complete") is True
        result["actual_exit"]=current.get("actual_exit")
        result["error"]=current.get("error")
        result["not_generated"]=current.get("not_generated")
        result["source_counts"]=current.get("source_counts")
        original_out=runner/"request236-source-preparation"
        source_path=original_out/"source-views.json"
        if isinstance(current.get("R562_child"),dict):
            desc=current["R562_child"].get("actual_source_receipt")
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
        result["original_R562_readback"]=child
        stdout_path=out/"R562-readback.stdout.log"
        stderr_path=out/"R562-readback.stderr.log"
        child["started"]=True
        with stdout_path.open("xb") as stdout,stderr_path.open("xb") as stderr:
            completed=subprocess.run(command,stdout=stdout,stderr=stderr,
                check=False,start_new_session=False)
        child.update(returned=True,actual_exit=completed.returncode,
            stdout=identity(stdout_path),stderr=identity(stderr_path))
        transport_path=runner/"request236-source-preparation-necessary.json"
        require(transport_path.is_file() and not transport_path.is_symlink(),
                "Original R562 necessary transport object returned")
        transport_raw=transport_path.read_bytes()
        transport=json.loads(transport_raw)
        require(transport.get("schema")==ANCESTOR_SOURCE_SCHEMA+"-necessary-v1"
                and transport.get("run")==run and transport.get("request_number")==236
                and transport.get("source")==identity(generator)
                and transport.get("plan")==identity(ancestor_plan),
                "Same actual frozen R562 reader/run/source/plan")
        result["original_R562_transport"]=dict(actual=identity(transport_path),
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
            result["original_R562_transport"]["original_transport_body"]=transport
            full_from_retained_overflow=True
        else:
            require(completed.returncode in (0,2) and "transport_exit_code" not in transport,
                    "Explicit ordinary original reader return")
            complete_path=transport_path;complete_raw=transport_raw;complete=transport
            full_from_retained_overflow=False
        require(complete.get("schema")==ANCESTOR_SOURCE_SCHEMA+"-necessary-v1"
                and complete.get("run")==run and complete.get("request_number")==236
                and complete.get("source")==identity(generator)
                and complete.get("plan")==identity(ancestor_plan),
                "The complete original necessary object has the same real source and run")
        result["original_R562_complete_necessary"]=dict(actual=identity(complete_path),
            from_retained_overflow=full_from_retained_overflow,
            complete_original_necessary_readback_complete=complete.get("necessary_readback_complete"),
            original_record=None)
        records.append(dict(role="R562-complete-original-necessary",
                            actual=identity(complete_path),value=complete))
        if not full_from_retained_overflow:
            result["original_R562_transport"]["original_transport_body"]={
                "same_actual_complete_original_necessary":True,
                "actual":identity(complete_path),
                "inverse":"Use the complete original necessary object in original_R562_complete_necessary, not a new inferred value."}
        # Complete actual source-only stderr; duplicate stdout bodies stay identified.
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
    references=[dict(role=row["role"],actual=row["actual"],ordered=ordered_metadata(row["value"]))
                for row in records]
    for row in records:
        selected=selected_source_record(row["value"],references,tables)
        if row["role"]=="R565-current-source-record":
            result["current_source_record"]["record"]=selected
        else:result["original_R562_complete_necessary"]["original_record"]=selected
    result["named_source_identity_catalogue"]=tables.describe()
    raw=canonical(result)
    if len(raw)>LIMIT:
        full=out/"necessary-source-overflow.json" if out.is_dir() else None
        if full is not None:write(full,result)
        result=dict(schema=SCHEMA+"-necessary-v1",request_number=237,source=identity(__file__),
            run=run,plan=result["plan"],necessary_readback_complete=False,
            source_preparation_complete=False,transport_exit_code=70,
            attempted_bytes=len(raw),attempted_sha256=hashlib.sha256(raw).hexdigest(),
            complete_local_necessary_object=identity(full) if full is not None else None,
            original_R562_readback_exit=(result.get("original_R562_readback") or {}).get("actual_exit"),
            original_R562_transport=(result.get("original_R562_transport") or {}).get("actual"),
            original_R562_complete_necessary=(result.get("original_R562_complete_necessary") or {}).get("actual"),
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
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("prepare","readback"))
    parser.add_argument("--plan",type=Path,required=True)
    parser.add_argument("--plan-sha256",required=True)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    try:return prepare(args) if args.mode=="prepare" else readback(args)
    except Exception as error:
        print(json.dumps(dict(event="R565_source_preparation_unreturned",schema=SCHEMA,
            source=identity(__file__),complete=False,cleanup_permitted=False,
            error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())),
            ensure_ascii=True),flush=True)
        return 2


if __name__=="__main__":
    raise SystemExit(main())

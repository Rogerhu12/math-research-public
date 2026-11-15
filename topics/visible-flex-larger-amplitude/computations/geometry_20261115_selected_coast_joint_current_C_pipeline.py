#!/usr/bin/env python3
"""Request197: restore actual180, bind fresh C, then form joint nominal Q/Pi rows from complete R380 families.

The only old scientific result reused is the actual whole-root-family domain
statement at the same exact nine-parameter point. The two selected files are
reconstructed and checked against their actual180 byte identities. The fresh
factory result is produced by the unchanged original factory; it is not
forged. All C sampling, current numerical compilation, H/J/FD/full453 and final
native audit remain original same-job work. No new nonlinear gate is added.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import runpy
import signal
import subprocess
import sys
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request197-selected-coast-fresh-C-construction-v1"
REQUEST_SCHEMA="public-selected-coast-current-C-pruefer-joint-full453-request-v1"
NAMESPACE="visible-selected-coast-joint-current-C-full453197"
LIMIT=90000
TIMESTAMP=re.compile(rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ")
TOKENS=("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN")
SELECTION_NAME="geometry_20261115_accurate_coast_three_coefficient_repair.py"
SELECTION_SHA="595bf01cd89690629ca167d5be9d674951d9959d7fd61717a296ecbd3fcd8c4c"
FACTORY_NAME="geometry_20261115_continuous_nine_scalar_factory_v3.py"
FACTORY_SHA="0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
SUMMARY_SCHEMA="request180-accurate-R323-coast-three-coefficient-repair-v1"

class ResourceStop(RuntimeError):
    pass

def require(ok,message):
    if not ok:raise ValueError(message)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=True,allow_nan=False)+"\n").encode("ascii")

def unique(pairs):
    value={}
    for key,item in pairs:
        require(key not in value,"Duplicate JSON key: "+key)
        value[key]=item
    return value

def parse(raw):
    return json.loads(raw,object_pairs_hook=unique,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))

def identity(path):
    path=Path(path)
    raw=path.read_bytes()
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))

def write(path,value):
    raw=canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))

def read(path,expected=None):
    raw=Path(path).read_bytes()
    record=dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))
    if expected is not None:
        require(record["bytes"]==expected["bytes"] and record["sha256"]==expected["sha256"],
            "Actual complete file identity differs: "+str(path))
    return parse(raw),record

def checked_source(comp,request,name):
    path=comp/name
    require(Path(name).name==name and path.is_file() and not path.is_symlink(),
        "Original pinned source must be a regular basename")
    require(sha(path.read_bytes())==request["source_sha256"][name],
        "Actual source pin differs: "+name)
    return path

def checked_parameter(comp,item):
    path=comp/item["file"]
    require(Path(item["file"]).name==item["file"],"Original parameter basename")
    read(path,item)
    return path

def call(comp,request,name,argv,rows,timeout,transport=False):
    source=checked_source(comp,request,name)
    command=[sys.executable,"-u",str(source),*map(str,argv)]
    row=dict(source=identity(source),argv=command,maximum_seconds=timeout,
        started=False,joined=False,returncode=None,resource_partial=False)
    rows.append(row)
    print(json.dumps(dict(event="request197_original_child_dispatch",**row)),flush=True)
    environment=dict(os.environ) if transport else {
        k:v for k,v in os.environ.items() if k not in TOKENS}
    start=time.monotonic()
    row["started"]=True
    try:
        done=subprocess.run(command,env=environment,timeout=timeout,check=False)
        row["joined"]=True;row["returncode"]=done.returncode
    except subprocess.TimeoutExpired:
        # subprocess.run kills and joins this direct Python child. Every
        # scientific subprocess also inherits the original rule-runner PGID.
        row["joined"]=True;row["resource_partial"]=True;row["returncode"]=124
    finally:
        row["elapsed_seconds"]=time.monotonic()-start
        print(json.dumps(dict(event="request197_original_child_return",**row)),flush=True)
    return row["returncode"]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

def official_request(path,token):
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"request197-actual180-selected-input-recovery",
        "Accept-Encoding":"identity","Authorization":"Bearer "+token}
    return urllib.request.Request("https://api.github.com/repos/"+REPOSITORY+path,headers=headers)

def official_metadata(path,token):
    with urllib.request.build_opener(NoRedirect()).open(
            official_request(path,token),timeout=45) as response:
        require(response.status==200,"Official metadata HTTP200")
        raw=response.read(2097153)
        require(len(raw)<=2097152,"Bounded official metadata")
    return parse(raw),dict(endpoint=path,bytes=len(raw),sha256=sha(raw))

def open_report(job,token):
    request=official_request("/actions/jobs/"+str(job)+"/logs",token)
    try:
        response=urllib.request.build_opener(NoRedirect()).open(request,timeout=60)
    except urllib.error.HTTPError as error:
        if error.code not in (301,302,303,307,308):raise
        location=error.headers.get("Location")
        target=urllib.parse.urlparse(location or "")
        require(target.scheme=="https" and target.hostname and not target.username,
            "Only official HTTPS redirect is followed")
        response=urllib.request.urlopen(urllib.request.Request(location,headers={
            "User-Agent":"request197-actual180-selected-input-recovery",
            "Accept-Encoding":"identity"}),timeout=60)
        return response,dict(official_redirect_status=error.code,
            bearer_token_not_forwarded=True,signed_URL_not_recorded=True)
    return response,dict(official_redirect_status=None,
        bearer_token_not_forwarded=True,signed_URL_not_recorded=True)

def original_selection(comp,base,request,report):
    wanted=request["actual180_selection"]
    require(wanted["run_id"]==43753422569
        and wanted["report_job_id"]==132932432397
        and wanted["source_commit"]=="636bbc30601cb577266219ed66bb2759d285badc",
        "Use the actual completed180 tuple, not a future result")
    token=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    require(bool(token),"Official API token stays in process environment")
    def alarm(signum,frame):
        raise ResourceStop("bounded-actual180-report-transport")
    previous=signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,180)
    response=None
    try:
        run,runr=official_metadata("/actions/runs/"+str(wanted["run_id"]),token)
        job,jobr=official_metadata("/actions/jobs/"+str(wanted["report_job_id"]),token)
        require(run["id"]==wanted["run_id"] and run["head_sha"]==wanted["source_commit"]
            and run["status"]=="completed","Official completed original180 run")
        require(job["id"]==wanted["report_job_id"] and job["run_id"]==wanted["run_id"]
            and job["status"]=="completed","Official completed original180 report")
        response,transport=open_report(wanted["report_job_id"],token)
        require(response.status==200
            and response.headers.get("Content-Encoding") in (None,"","identity"),
            "Read the original unencoded report log")
        raw=response.read(wanted["report_log"]["bytes"]+1)
        require(len(raw)==wanted["report_log"]["bytes"]
            and sha(raw)==wanted["report_log"]["sha256"],"Whole original180 report bytes/SHA")
        report["original180_official_transport"]=dict(run=runr,job=jobr,
            run_conclusion=run.get("conclusion"),job_conclusion=job.get("conclusion"),
            whole_original_log=wanted["report_log"],transport=transport,
            whole_original_log_not_written=True)
    finally:
        if response is not None:response.close()
        signal.setitimer(signal.ITIMER_REAL,0)
        signal.signal(signal.SIGALRM,previous)
    begin=wanted["summary"]["begin"].encode("ascii")
    end=wanted["summary"]["end"].encode("ascii")
    frame=None;frames=[];bom=0
    for number,line in enumerate(raw.splitlines(keepends=True),1):
        require(len(line)<=200000,"Bounded original report physical line")
        view=line
        if view.startswith(b"\xef\xbb\xbf"):
            view=view[3:];bom+=1
        view=TIMESTAMP.sub(b"",view,count=1).rstrip(b"\r\n")
        if view==begin:
            require(frame is None,"No overlapping original summary frame")
            frame=[];start_line=number
        elif view==end:
            require(frame is not None,"Original summary end has a begin")
            payload=b"\n".join(frame)
            frames.append((payload,dict(first_physical_line=start_line,last_physical_line=number)))
            frame=None
        elif frame is not None:
            frame.append(view)
    require(frame is None and len(frames)==1,"Exactly one complete original necessary180 frame")
    payload,location=frames[0]
    expected=wanted["summary"]
    require(len(payload)==expected["bytes"] and sha(payload)==expected["sha256"],
        "Original necessary180 ASCII JSON excludes only the separator LF")
    selected=parse(payload)
    require(selected["schema"]==SUMMARY_SCHEMA
        and str(selected["run_id"])==str(wanted["run_id"])
        and selected["source_commit"]==wanted["source_commit"]
        and selected.get("summary_complete") is True,
        "Actual180 complete necessary summary identity")
    require(selected.get("full_accurate_nine_domain_proved") is True,
        "Actual180 did not supply the declared complete domain result")
    point=selected["selected_profile"]
    require(point["nine_parameters_exact"]==wanted["nine_parameters_exact"]
        and point["beta_exact"]==wanted["beta_exact"],"Original selected exact parameter words")
    for key,source_key in (("recipe","selected_recipe"),("accurate_definition","selected_definition")):
        for field in ("bytes","sha256"):
            require(point[key][field]==wanted[source_key][field],
                "Original selected complete file descriptor differs")
    path=base/"selection-summary.json"
    with path.open("xb") as stream:
        stream.write(payload);stream.flush();os.fsync(stream.fileno())
    report["actual_selection_summary"]=dict(file=path.name,bytes=len(payload),sha256=sha(payload),
        parsing_view_only_single_physical_BOM_then_timestamp=True,
        physical_line_BOM_count=bom,location=location,hash_excludes_separator_LF=True)
    return path

def recover(comp,base,request,report):
    selection=original_selection(comp,base,request,report)
    old_request=checked_parameter(comp,request["original180_request"])
    rows=report["original_child_calls"]
    status=call(comp,request,"root_20261115_restore_actual165_coast_inputs.py",
        ["--request",old_request,"--out",base/"restored165"],rows,660,transport=True)
    recovery=base/"restored165"/"recovery-result.json"
    if recovery.is_file():
        value,receipt=read(recovery);report["actual_original165_recovery"]=receipt
        report["actual_original165_recovery_complete"]=value.get("complete") is True
    if status!=0:
        report["unstarted_scope"]=["selected-file-reconstruction","fresh-original-factory",
            "semantic-input-binding","current-profile-BVP"]
        return status
    item=request["selected_file_reconstruction"]
    accepted=request["construction_inputs"]["accepted"]
    config=request["inputs"]["config"]
    argv=["--request",old_request,"--request-sha256",request["original180_request"]["sha256"],
        "--selection-summary",selection,"--selection-summary-sha256",request["actual180_selection"]["summary"]["sha256"],
        "--restored-directory",base/"restored165","--accepted-core",base/"original-inputs"/accepted["runtime_basename"],
        "--config",base/"original-inputs"/config["runtime_basename"],"--code-directory",comp,
        "--maximum-seconds","300","--out",base/"restored-selection"]
    status=call(comp,request,item["file"],argv,rows,330)
    path=base/"restored-selection"/"restoration-result.json"
    if path.is_file():
        value,receipt=read(path);report["actual_selected_file_restoration"]=receipt
        report["selected_files_reconstructed"]=value.get("reconstruction_complete") is True
    if status==0:
        for key in ("selected_recipe","selected_definition"):
            expected=request["actual180_selection"][key]
            read(base/"restored-selection"/expected["file"],expected)
        report["selected_files_reconstructed"]=True
    return status

def bind_pruefer_recipe(comp,base,request,current,current_receipt,binding_receipt):
    """Explicit identity adaptation after the unchanged e5ab semantic binder.

    Only provider names/pins, independent schema and descriptive metadata
    change. All nine words, actual point provenance, original native controls,
    full453/FD tolerances, trial budgets and actual initial state origin remain.
    """
    spec=request["pruefer_provider"]
    require(current.get("schema")==request["current_BVP_recipe"]["schema"],
        "The e5ab output must still be the original179 recipe protocol")
    require(current.get("request_number")==197,"Actual selected experiment number")
    native=parse(canonical(current["native_configuration"]))
    old_sources=dict(native["source_sha256"])
    actual=dict(old_sources)
    changed=[]
    for item in spec["native_source_replacements"]:
        require(actual.get(item["original_file"])==item["original_sha256"],
            "Original179 native source identity must match before explicit replacement")
        require(item["file"] not in actual,"No hidden provider source overwrite")
        del actual[item["original_file"]]
        checked_source(comp,request,item["file"])
        require(request["source_sha256"][item["file"]]==item["sha256"],
            "Actual new provider source pin differs")
        actual[item["file"]]=item["sha256"]
        changed.append(dict(item))
    for name,expected in spec["new_native_source_additions"].items():
        require(name not in actual,"New dependency must be an explicit addition")
        checked_source(comp,request,name)
        require(request["source_sha256"][name]==expected,"Actual new kernel pin differs")
        actual[name]=expected
    require(actual==spec["complete_current_native_source_sha256"],
        "Bind the complete new native source closure")
    native["source_sha256"]=actual
    out=parse(canonical(current))
    out["schema"]=spec["recipe_schema"]
    out["native_configuration"]=native
    original_execution=dict(out["execution"])
    renamed_execution={}
    for name in ("riccati_sampling_declared_linear_seconds",
                 "riccati_sampling_declared_point_seconds",
                 "riccati_sampling_startup_reserves_original_BVP_seconds"):
        require(name in out["execution"],"Original sampling budget metadata required")
        target=name.replace("riccati_","pruefer_",1)
        renamed_execution[name]=target
        out["execution"][target]=out["execution"].pop(name)
    scope=dict(out["acceptance_scope"])
    require(scope.pop("R375_original_deep_family_recomputed_not_previous_pivot_box_shrunk") is True,
        "Original complete inherited deep-family responsibility is required")
    require(scope.pop("two_closed_comparison_barriers_and_full_inherited_ratio_retained") is True,
        "Original comparison responsibility is required")
    scope.update(joint_nominal_parameter_box_point_not_claimed_to_be_a_global_C_member=True,
        complete_original_unit_row_family_to_actual_binary64_error_enclosures_retained=True,
        nominal_row_formation_does_not_add_a_native_acceptance_gate=True,
        R380_original_deep_family_recomputed_no_angle_or_root_subfamily_selected=True,
        two_global_angle_barriers_full_real_lift_and_positive_amplitude_retained=True,
        actual_same_angle_physical_and_original_QPi_unit_rows_enclosed=True,
        nonzero_QPi_row_bound_uses_complete_invertible_actual_coordinate_map=True)
    out["acceptance_scope"]=scope
    out["original_semantic_adapter_recipe"]=current_receipt
    out["current_pruefer_provider_identity"]=dict(
        schema=spec["schema"],sampler=spec["sampler"],kernel=spec["kernel"],
        R380_proof=spec["R380_proof"],driver=spec["driver"],
        positive_endpoint_helper=spec["positive_endpoint_helper"],
        joint_nominal_row_helper=spec["joint_nominal_row_helper"],
        original187_provider_identity=spec["original187_provider_identity"],
        exact_parameter_box_nominal_point_not_a_selected_global_C_member=True,
        all_current_family_to_actual_word_error_enclosures_retained=True,
        original184_provider_identity=spec["original184_provider_identity"],
        original179_provider_is_provenance_not_a_current_input=True,
        original_semantic_adapter_result=binding_receipt,
        only_source_protocol_and_descriptive_metadata_adapted=True,
        actual_positive_mu_must_come_from_this_jobs_far_sample=True)
    protected=set(current)-{"schema","native_configuration","execution","acceptance_scope"}
    require(all(canonical(out[k])==canonical(current[k]) for k in protected),
        "A selected point, original control or input origin was changed")
    require(all(canonical(native[k])==canonical(current["native_configuration"][k])
        for k in native if k!="source_sha256"),"Original native mathematics or policy changed")
    restored_execution=dict(out["execution"])
    for old,new in renamed_execution.items():restored_execution[old]=restored_execution.pop(new)
    require(canonical(restored_execution)==canonical(original_execution),
        "Original execution resource values changed during identity adaptation")
    directory=base/"pruefer-BVP-input";directory.mkdir(exist_ok=False)
    recipe_id=write(directory/"current-coast-selected-pruefer-BVP-recipe.json",out)
    receipt=dict(schema=SCHEMA+"-pruefer-input-binding",
        source_sha256=sha(Path(__file__).read_bytes()),repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        direct_BVP_input_created=True,generated_BVP_recipe=recipe_id,
        original_semantic_adapter_result=binding_receipt,
        original_semantic_adapter_recipe=current_receipt,
        original179_template=request["current_BVP_recipe"],
        native_source_replacements=changed,
        explicit_new_native_source_additions=spec["new_native_source_additions"],
        complete_current_native_source_sha256=actual,
        actual_new_initial_nine_parameters=out["initial_nine_parameters"],
        complete_protected_original_recipe_fields=sorted(protected),
        original_all_nine_words_and_parameter_origin_unchanged=True,
        original_native_full453_FD_and_final_audit_policies_unchanged=True,
        changed_execution_keys_only=renamed_execution,
        old_e5ab_recipe_and_receipt_retained_without_relabeling=True,
        old_R375_sampler_not_executed_as_new_input=True,
        old187_independent_final_coefficient_centers_not_executed=True,
        joint_nominal_row_helper=spec["joint_nominal_row_helper"],
        original_complete112_family_required_before_numeric_row_formation=True,
        no_new_small_error_or_BVP_acceptance_gate=True)
    receipt_id=write(directory/"result.json",receipt)
    return out,recipe_id,receipt_id

def construct(comp,base,request,report):
    selected=request["actual180_selection"]
    recipe=base/"restored-selection"/selected["selected_recipe"]["file"]
    definition=base/"restored-selection"/selected["selected_definition"]["file"]
    summary=base/"selection-summary.json"
    read(recipe,selected["selected_recipe"]);read(definition,selected["selected_definition"])
    read(summary,selected["summary"])
    recovery,rr=read(base/"restored-selection"/"restoration-result.json")
    require(recovery.get("reconstruction_complete") is True,"Actual selected files not reconstructed")
    report["actual_reconstruction_receipt"]=rr
    cover=base/"continuous-E"/"result.json"
    cut=base/"cut-twojet-readout"/"cut-twojet-readout.json"
    require(cover.is_file() and cut.is_file(),"Fresh actual C and complete cut readout required")
    cover_id=identity(cover);cut_id=identity(cut)
    original=request["construction_inputs"]["accepted"]
    core=base/"original-inputs"/original["runtime_basename"]
    factory=base/"construction"/"factory"
    rows=report["original_child_calls"]
    policy=request["selected_construction"]
    proof=Path(os.environ["GITHUB_WORKSPACE"])/request["construction"]["R300_proof"]["file"]
    argv=["--core-file",core,"--core-file-sha256",original["sha256"],
        "--core-geometry-pointer",request["construction"]["core_geometry_pointer"],
        "--tail-cover-directory",cover.parent,"--tail-result-sha256",cover_id["sha256"],
        "--cut-twojet-readout",cut,"--cut-twojet-readout-sha256",cut_id["sha256"],
        "--model-recipe",recipe,"--model-recipe-sha256",selected["selected_recipe"]["sha256"],
        "--code-directory",comp,"--r300-proof",proof,
        "--sqrt-bits","256","--max-domain-cells","65536","--max-domain-depth","32",
        "--domain-budget-seconds","300","--out",factory]
    factory_code=call(comp,request,FACTORY_NAME,argv,rows,policy["maximum_factory_seconds"])
    report["actual_factory_returncode"]=factory_code
    if not (factory/"result.json").is_file():
        report["unstarted_scope"]=["semantic-input-binding","current-profile-BVP"]
        return factory_code or 2
    produced,factory_receipt=read(factory/"result.json")
    report["actual_original_factory_result"]=factory_receipt
    report["original_factory_exact_definition_created"]=produced.get("exact_model_definition_created") is True
    report["fresh_factory_current_parameter_domain_complete"]=produced.get("full_current_nine_domain_certificate_complete")
    report["fresh_factory_interval_domain_flag_not_used_as_BVP_gate"]=True
    if factory_code not in (0,70) or produced.get("exact_model_definition_created") is not True:
        report["unstarted_scope"]=["semantic-input-binding","current-profile-BVP"]
        return factory_code or 2
    adapter=request["semantic_adapter"]
    template=checked_parameter(comp,request["current_BVP_recipe"])
    argv=["--selection-summary",summary,"--selection-summary-sha256",selected["summary"]["sha256"],
        "--selection-source",comp/SELECTION_NAME,"--selection-source-sha256",SELECTION_SHA,
        "--selected-recipe",recipe,"--selected-definition",definition,
        "--factory-directory",factory,"--factory-result-sha256",factory_receipt["sha256"],
        "--template-bvp-recipe",template,"--code-directory",comp,
        "--bvp-request-number","197","--out",base/"selected-BVP-input"]
    adapter_code=call(comp,request,adapter["file"],argv,rows,policy["maximum_adapter_seconds"])
    report["actual_semantic_adapter_returncode"]=adapter_code
    adapter_result=base/"selected-BVP-input"/"result.json"
    if not adapter_result.is_file():
        report["unstarted_scope"]=["current-profile-BVP"]
        return adapter_code or 2
    binding,binding_receipt=read(adapter_result)
    report["actual_semantic_adapter_result"]=binding_receipt
    if binding.get("direct_BVP_input_created") is not True:
        report["unstarted_scope"]=["current-profile-BVP"]
        return adapter_code or 2
    descriptor=binding["generated_BVP_recipe"]
    require(Path(descriptor["file"]).name==descriptor["file"],"Generated BVP basename")
    current,current_receipt=read(base/"selected-BVP-input"/descriptor["file"],descriptor)
    require(current["request_number"]==197,"The new input declares the actual experiment")
    current,current_receipt,provider_receipt=bind_pruefer_recipe(
        comp,base,request,current,current_receipt,binding_receipt)
    report["actual_pruefer_provider_input_binding"]=provider_receipt
    deadline,deadline_id=read(base/"job-science-deadline.json")
    require(deadline["schema"]=="request197-owned-job-science-deadline-v1"
        and deadline["run_id"]==os.environ["GITHUB_RUN_ID"]
        and deadline["source_commit"]==os.environ["GITHUB_SHA"]
        and deadline["template_recipe_sha256"]==request["current_BVP_recipe"]["sha256"],
        "Original namespace plan belongs to this current job")
    # The new launch identity preserves the original owned-process algorithm
    # and checks this actual197 deadline with the new complete provider recipe.
    actual_deadline=dict(deadline)
    actual_deadline["recipe_sha256"]=current_receipt["sha256"]
    actual_deadline["actual_request_number"]=197
    actual_deadline["source_namespace_deadline"]=deadline_id
    actual_deadline["actual_semantic_adapter_result"]=binding_receipt
    actual_deadline["actual_pruefer_provider_input_binding"]=provider_receipt
    report["actual_current_launcher_deadline"]=write(base/"current-BVP-deadline.json",actual_deadline)
    report.update(direct_BVP_input_created=True,generated_BVP_recipe=current_receipt,
        actual_new_initial_nine_parameters=current["initial_nine_parameters"],
        old_full_domain_only_transferred_to_same_accurate_initial_point=True,
        fresh_numeric_shadow_J_FD_fullDN_native_and_final_audit_not_inherited=True,
        actual_BVP_call_count_in_this_helper=0,
        explicit_R380_recipe_and_current197_deadline_used_by_thin_launch_identity=True,
        no_old179_factory_wrapper_width_selection_performed=True)
    return 0 if factory_code==adapter_code==0 else 70

def selected(value,names):
    return {name:value[name] for name in names if isinstance(value,dict) and name in value}

def domain_scope(value):
    if not isinstance(value,dict):return None
    answer=selected(value,("complete","error","all_closed_segments_visited",
        "proved_leaves","processed_nodes","stop_reason","minimum_enclosed_radius",
        "speed_lower","speed_upper"))
    for key in ("unresolved_leaves","rigorously_refuted_leaves","complete_unvisited_suffix"):
        member=value.get(key)
        answer[key+"_count"]=len(member) if isinstance(member,list) else None
    table=value.get("piece_table")
    answer["complete_original_piece_table_count"]=len(table) if isinstance(table,list) else None
    answer["complete_original_domain_canonical_sha256"]=sha(canonical(value))
    answer["successful_leaf_bounds_and_large_piece_table_not_exported"]=True
    return answer

def factory_domain_scope(directory,value):
    """Read original unpaid addresses, never recompute a, a_s or a_ss."""
    if not isinstance(value,dict):return value
    answer=dict(value)
    answer["complete_original_domain_canonical_sha256"]=sha(canonical(value))
    answer["unpaid_addresses_not_scientific_bounds_recomputed"]=True
    unresolved=value.get("unresolved_terminal_leaves")
    unvisited=value.get("unvisited_stack_entries")
    if unresolved==0 and unvisited==0:
        answer["complete_unresolved_closed_ranges"]=[]
        answer["complete_unvisited_closed_ranges"]=[]
        answer["original_unpaid_address_scope_complete"]=True
        return answer
    descriptor=value.get("ledger")
    require(isinstance(descriptor,dict),"Original factory unpaid domain requires its actual ledger")
    relative=Path(descriptor["file"])
    require(not relative.is_absolute() and ".." not in relative.parts,
        "Original factory ledger must stay inside the actual factory directory")
    path=(directory/relative).resolve()
    require(directory.resolve() in path.parents and not path.is_symlink(),
        "Actual original domain ledger path differs")
    payload,receipt=read(path,descriptor)
    leaves=payload.get("leaves");pending=payload.get("whole_unvisited_stack")
    require(isinstance(leaves,list) and isinstance(pending,list),
        "Original factory must retain all leaf and unvisited addresses")
    failures=[row for row in leaves if row.get("proved") is not True]
    require(len(failures)==unresolved and len(pending)==unvisited,
        "Original factory unpaid address counts differ from its result")
    def ranges(rows):
        result=[]
        for row in rows:
            interval=row.get("closed_local_interval")
            require(isinstance(interval,list) and len(interval)==2
                and all(isinstance(x,str) for x in interval),
                "Every original closed address must be explicit")
            item=dict(piece=row["piece"],closed_local_interval=list(interval),
                original_entry_count=1,original_depths=[row["depth"]])
            if row.get("name") is not None:item["name"]=row["name"]
            if (result and result[-1]["piece"]==item["piece"]
                    and result[-1].get("name")==item.get("name")
                    and result[-1]["closed_local_interval"][1]==interval[0]):
                previous=result[-1]
                previous["closed_local_interval"][1]=interval[1]
                previous["original_entry_count"]+=1
                if row["depth"] not in previous["original_depths"]:
                    previous["original_depths"].append(row["depth"])
            else:result.append(item)
        return result
    answer.update(actual_original_domain_ledger=receipt,
        complete_unresolved_closed_ranges=ranges(failures),
        complete_unvisited_closed_ranges=ranges(pending),
        original_unpaid_address_scope_complete=True,
        adjacent_addresses_merged_only_by_exact_original_endpoint_string_equality=True,
        all_closed_shared_endpoints_retained=True,
        unresolved_is_not_a_strict_invalid_geometry_claim=True,
        original_a_ap_app_bounds_not_exported=True)
    return answer

def necessary_readback(comp,base,request):
    owner=checked_source(comp,request,request["execution"]["owned_process_helper"]["file"])
    observed=runpy.run_path(str(owner),run_name="_request197_selection_readback_owner")["observe"]()
    require(observed["quiescent"],"Original owned scientific processes are live or unknown")
    summary=dict(schema=SCHEMA+"-necessary-readback",repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        no_scientific_module_imported_or_scientific_value_recomputed=True,
        original180_selection=request["actual180_selection"],
        complete_necessary_scope=False,actual_BVP_acceptance_not_inferred=True,
        files=[],missing_files=[],read_errors=[],source_sha256=sha(Path(__file__).read_bytes()))
    paths=[
        ("selection-summary.json","selection"),
        ("selected-recovery-result.json","procedure"),
        ("restored165/recovery-result.json","recovery"),
        ("restored-selection/restoration-result.json","restoration"),
        ("construction/procedure-result.json","procedure"),
        ("construction/factory/result.json","factory"),
        ("selected-BVP-input/result.json","adapter"),
        ("pruefer-BVP-input/result.json","provider"),
        ("current-BVP-deadline.json","deadline")]
    keys={
      "procedure":("schema","phase","process_exit_code","elapsed_seconds","error","resource_partial",
        "selected_files_reconstructed","actual_original165_recovery_complete","original_child_calls",
        "direct_BVP_input_created","generated_BVP_recipe","actual_new_initial_nine_parameters",
        "actual_factory_returncode","actual_semantic_adapter_returncode","unstarted_scope",
        "fresh_factory_current_parameter_domain_complete","fresh_factory_interval_domain_flag_not_used_as_BVP_gate",
        "actual_pruefer_provider_input_binding","actual_current_launcher_deadline"),
      "recovery":("schema","complete","resource_partial","error","original_run_id","original_job_id",
        "original_source_commit","elapsed_seconds","exit_code"),
      "restoration":("schema","reconstruction_complete","process_exit_code","error","resource_partial",
        "original180_domain_certificate_only_reused_not_recomputed","new_C_or_factory_result_not_created",
        "native_or_fullDN_call_count","elapsed_seconds"),
      "factory":("schema","source_sha256","run_id","source_commit","actual_model_recipe","model_definition",
        "construction_conditions","base_domain","requested_parameter_domain","exact_model_definition_created",
        "nonempty_family_conditions_paid","full_current_nine_domain_certificate_complete","starting_parameters",
        "root_choice_is_new_model_declaration","construction_is_uniform_over_all_retained_semantic_leaf_values",
        "interval_domain_budget_seconds_per_pass","maximum_domain_passes","error"),
      "adapter":("schema","source_sha256","run_id","source_commit","complete_source_parameter_readback",
        "direct_BVP_input_created","generated_BVP_recipe","changed_BVP_recipe_fields",
        "actual_selected_recipe","actual_selected_definition","actual_same_job_original_factory_result",
        "actual_same_job_original_factory_definition","complete_mathematical_definition_equal",
        "accurate_initial_domain_certificate_transfer","original_factory_parameter_domain_complete",
        "original_factory_domain_status_used_as_new_BVP_gate","error"),
      "provider":("schema","source_sha256","run_id","source_commit","direct_BVP_input_created",
        "generated_BVP_recipe","original_semantic_adapter_result","original_semantic_adapter_recipe",
        "actual_new_initial_nine_parameters","complete_protected_original_recipe_fields",
        "original_all_nine_words_and_parameter_origin_unchanged",
        "original_native_full453_FD_and_final_audit_policies_unchanged","changed_execution_keys_only",
        "old_e5ab_recipe_and_receipt_retained_without_relabeling","old_R375_sampler_not_executed_as_new_input",
        "old187_independent_final_coefficient_centers_not_executed","joint_nominal_row_helper",
        "original_complete112_family_required_before_numeric_row_formation","no_new_small_error_or_BVP_acceptance_gate"),
      "deadline":("schema","run_id","source_commit","request_sha256","template_recipe_sha256","recipe_sha256",
        "namespace_created_unix_seconds","science_seconds_from_namespace","readback_reserve_seconds",
        "actual_request_number","source_namespace_deadline")}
    for relative,kind in paths:
        path=base/relative
        if not path.is_file():
            summary["missing_files"].append(relative);continue
        try:
            value,receipt=read(path)
            if kind=="selection":
                chosen=selected(value,("schema","run_id","source_commit","summary_complete",
                    "phase","selected_beta_exact","full_accurate_nine_domain_proved",
                    "unchanged_target_geometry"))
                chosen["all418_unchanged_piece_domain"]=domain_scope(value.get("all418_unchanged_piece_domain"))
                point=value.get("selected_profile")
                chosen["selected_profile"]=selected(point,("parameter_order","nine_parameters_exact",
                    "beta_exact","recipe","accurate_definition","factory_source_sha256",
                    "new_selection_source_sha256","semantic_C_remains_original_all_root_family",
                    "full_length_expression_unchanged","binary64_projection"))
                plan=value.get("candidate_plan",[])
                chosen["actual_original_candidate_scope"]=[
                    dict(selected(x,("beta_exact","status","whole_accurate_nine_domain_proved")),
                         complete_coast_domain=domain_scope(x.get("complete_coast_domain")))
                    for x in plan]
            else:
                chosen=selected(value,keys[kind])
                if kind=="factory":
                    for field in ("base_domain","requested_parameter_domain"):
                        chosen[field]=factory_domain_scope(path.parent,value.get(field))
            summary["files"].append(dict(file=relative,identity=receipt,necessary_original_values=chosen,
                omitted_original_member_tree_not_exported=True))
        except Exception as error:
            summary["read_errors"].append(dict(file=relative,type=type(error).__name__,message=str(error)))
    # These original identities are retained without exporting the scientific
    # definition, expression DAG, full domains or numeric compilation arrays.
    for relative in ("selection-summary.json","restored-selection/selected-accurate-nine-recipe.json",
            "restored-selection/selected-accurate-nine-definition.json",
            "selected-BVP-input/current-coast-selected-BVP-recipe.json",
            "pruefer-BVP-input/current-coast-selected-pruefer-BVP-recipe.json"):
        path=base/relative
        if path.is_file():
            summary.setdefault("complete_parameter_file_identities",[]).append(
                dict(file=relative,identity=identity(path)))
    summary["complete_necessary_scope"]=not summary["read_errors"]
    summary["missing_output_means_unstarted_or_failed_scope_not_scientific_completion"]=True
    summary["complete_large_scientific_arrays_or_domain_ledgers_not_exported"]=True
    raw=canonical(summary)
    if len(raw)>LIMIT:
        print(json.dumps(dict(event="request197_selected_construction_readback_over_limit",
            bytes=len(raw),sha256=sha(raw),complete_necessary_scope=False,
            data_not_split_or_encoded=True,owned_cleanup_must_be_skipped=True)),flush=True)
        return 70
    write(base/"construction-necessary-summary.json",summary)
    print("BEGIN_REQUEST197_SELECTED_CONSTRUCTION_NECESSARY_SUMMARY",flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_REQUEST197_SELECTED_CONSTRUCTION_NECESSARY_SUMMARY",flush=True)
    print(json.dumps(dict(event="request197_selected_construction_summary_identity",
        bytes=len(raw),sha256=sha(raw),hash_scope="ASCII JSON including final LF")),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("construction_summary="+raw.decode("ascii").rstrip("\n")+"\n")
            stream.write("construction_summary_bytes="+str(len(raw))+"\n")
            stream.write("construction_summary_sha256="+sha(raw)+"\n")
    if not summary["complete_necessary_scope"]:return 2
    write(base/"construction-readback-complete.json",dict(
        schema=SCHEMA+"-readback-marker",repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        complete=True,necessary_summary=dict(bytes=len(raw),sha256=sha(raw)),
        original_scientific_success_not_inferred=True))
    return 0

def main(argv=None):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"This public Actions repository only")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase",choices=("selection","construction","readback"))
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--base",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    args=parser.parse_args(argv)
    comp=args.code_directory.resolve();base=args.base.resolve()
    require(base.parent==Path(os.environ["RUNNER_TEMP"]).resolve()
        and base.name==NAMESPACE and not args.base.is_symlink(),"This exclusive request197 namespace")
    request,_=read(args.request)
    require(request["schema"]==REQUEST_SCHEMA and request["request_number"]==197
        and request["repository"]==REPOSITORY,"Original197 dispatch request")
    checked_source(comp,request,Path(__file__).name)
    if args.phase=="readback":
        return necessary_readback(comp,base,request)
    report=dict(schema=SCHEMA+"-procedure",phase=args.phase,repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=identity(__file__),original_child_calls=[],error=None,resource_partial=False,
        direct_BVP_input_created=False,selected_files_reconstructed=False,
        old_full_domain_not_recomputed=True,actual_BVP_call_count_in_this_helper=0,
        original179_BVP_native_FD_final_scientific_gates_unchanged=True)
    start=time.monotonic();code=2
    destination=base/"selected-recovery-result.json"
    if args.phase=="construction":
        directory=base/"construction";directory.mkdir(exist_ok=False)
        destination=directory/"procedure-result.json"
    try:
        code=(recover if args.phase=="selection" else construct)(comp,base,request,report)
    except BaseException as error:
        code=3 if isinstance(error,ResourceStop) else 2
        report["resource_partial"]=isinstance(error,ResourceStop)
        if isinstance(error,(urllib.error.HTTPError,urllib.error.URLError)):
            detail=dict(type=type(error).__name__,HTTP_status=getattr(error,"code",None),
                message="Original official transport failed; signed URL and bearer omitted")
        else:
            message=str(error);stack=traceback.format_exc()
            for key in TOKENS:
                token=os.environ.get(key)
                if token:
                    message=message.replace(token,"[redacted]");stack=stack.replace(token,"[redacted]")
            detail=dict(type=type(error).__name__,message=message,traceback=stack)
        report["error"]=detail
    report["elapsed_seconds"]=time.monotonic()-start;report["process_exit_code"]=code
    original=write(destination,report)
    packed=canonical(report)
    if len(packed)>LIMIT:
        print(json.dumps(dict(event="request197_original_procedure_readback_over_limit",
            original_result=original,complete_necessary_scope=False,no_part_transport=True)),flush=True)
        return 70
    print(json.dumps(dict(event="request197_original_procedure_result",original_result=original,
        necessary_procedure=report)),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Request205: actual202 words as a NEW accurate-ten candidate, real current C.

The published187 recovery supplies only the actual180 structural recipe and
its original byte provenance. No selected180 domain or finite202 acceptance
is transferred. R449 prepare explicitly declares a binary64 projection and
the exact dyadics defining the new accurate family point. The real72c factory
runs on this point. After the complete current197 joint sampler returns, bind
creates its actual native config and asks R449 to generate the final BVP
recipe. The sampling reserve is explicit before this final identity exists.
The original namespace clock is extended by receipts, never restarted.

This pipeline neither solves the full453/450 problems nor clears their raw.
The independent205 launcher and postsolve tuple must execute the full current
problems and closed consumers before final quiet/readback/owned cleanup.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import runpy
import sys
import time
import traceback

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request205-actual202-accurate-ten-construction-v1"
REQUEST_SCHEMA="public-actual202-accurate-ten450-closed-geometry-request-v1"
NAMESPACE="visible-current-C-actual202-ten450-closed-geometry205"
DEADLINE_SCHEMA="request205-owned-job-science-deadline-v1"
RECIPE_SCHEMA="R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1"
CANDIDATE_NAME="geometry_20261116_actual202_accurate_ten_candidate.py"
CANDIDATE_SHA="ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38"
CANDIDATE_SCHEMA="R449-actual202-new-accurate-ten-candidate-adapter-v1"
DRIVER_NAME="geometry_20261116_actual202_accurate_ten_full453_frozen450.py"
DRIVER_SHA="56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615"
FACTORY_NAME="geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA="72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
FACTORY_SCHEMA="R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1"
MODEL_SCHEMA="R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
MODEL_RECIPE_SCHEMA="R300-new-continuous-ten-fixed-support1-power4-model-recipe-v1"
LEGACY_NAME="geometry_20261115_selected_coast_positive_current_C_pipeline.py"
LEGACY_SHA="1738fbb7fe1ca5211fb09442d14e740b2363c7d6c5d5daa14dd26c5f60a60d9b"
INPUT_NAME="actual202-accurate-ten-candidate-input.json"
INPUT_SHA="c980e9d4c6e15455459dc91a890b4fd9d8b02bced26eecd5d632ff9d250dbd4d"
INPUT_BYTES=2165
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3","xi"]
LIMIT=90000

def require(ok,message):
    if not ok:raise ValueError(message)
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=True,allow_nan=False)+"\n").encode("ascii")
def unique(pairs):
    result={}
    for k,v in pairs:
        require(k not in result,"Duplicate JSON key: "+k);result[k]=v
    return result
def parse(raw):return json.loads(raw,object_pairs_hook=unique,
    parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def identity(path):
    path=Path(path);raw=path.read_bytes()
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))
def read(path,descriptor=None):
    raw=Path(path).read_bytes();r=dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))
    if descriptor is not None:
        require(all(r[k]==descriptor[k] for k in ("bytes","sha256")),"Actual original identity differs: "+str(path))
    return parse(raw),r
def write(path,value):
    raw=canonical(value)
    with Path(path).open("xb") as f:f.write(raw);f.flush();os.fsync(f.fileno())
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))
def load(comp,name,digest,alias):
    path=comp/name
    require(sha(path.read_bytes())==digest,"Frozen source differs: "+name)
    spec=importlib.util.spec_from_file_location(alias,path)
    module=importlib.util.module_from_spec(spec);sys.modules[alias]=module
    try:spec.loader.exec_module(module)
    except BaseException:sys.modules.pop(alias,None);raise
    return module
def same_payload(a,b):
    return (isinstance(a,dict) and isinstance(b,dict)
        and all(a.get(k)==b.get(k) for k in ("bytes","sha256")))
def current_job(value,label):
    require(value.get("repository")==REPOSITORY
        and str(value.get("run_id"))==os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit")==os.environ["GITHUB_SHA"],
        "Require this job's actual "+label)
def member(directory,rec):
    name=PurePosixPath(rec["file"])
    require(not name.is_absolute() and ".." not in name.parts,
        "Use an actual safe relative output member")
    path=directory/str(name)
    require(not path.is_symlink() and path.resolve().is_relative_to(directory.resolve()),
        "The actual output member must remain inside its source directory")
    return read(path,rec)

def candidate_contract(L,comp,request):
    policy=request["actual202_candidate"]
    for item,name,digest in ((policy["adapter"],CANDIDATE_NAME,CANDIDATE_SHA),
                            (policy["driver"],DRIVER_NAME,DRIVER_SHA)):
        require(item["file"]==name and item["sha256"]==digest,
            "The independent R449 candidate source identity differs")
        path=L.checked_source(comp,request,name)
        require(identity(path)["bytes"]==item["bytes"],"Candidate source byte count differs")
    original=policy["parameter_input"]
    require(original["file"]==INPUT_NAME and original["sha256"]==INPUT_SHA
        and original["bytes"]==INPUT_BYTES,"Keep the published original202 ten-word input")
    path=L.checked_parameter(comp,original)
    maximum=policy["maximum_adapter_seconds"]
    require(type(maximum) in (int,float) and maximum>0,
        "Declare the adapter's finite resource allowance")
    reserve=request["execution"]["sampling_future_BVP_reserve_seconds"]
    require(reserve==3600 and type(reserve) is int,
        "Request205 explicitly uses the declared3600 sampling startup reserve")
    return path,maximum,reserve

def construct(L,comp,base,request,report):
    parameter_path,adapter_seconds,reserve=candidate_contract(L,comp,request)
    selected=request["actual180_selection"]
    old_recipe_path=base/"restored-selection"/selected["selected_recipe"]["file"]
    _,old_recipe_id=read(old_recipe_path,selected["selected_recipe"])
    restoration,restoration_id=read(base/"restored-selection"/"restoration-result.json")
    require(restoration.get("reconstruction_complete") is True,
        "Restore the original structural recipe bytes; no old field is assumed")
    construction=base/"construction"
    preparation=construction/"candidate-preparation"
    code=L.call(comp,request,CANDIDATE_NAME,
        ["prepare","--parameter-input",parameter_path,
         "--model-recipe-template",old_recipe_path,"--out",preparation],
        report["original_child_calls"],adapter_seconds)
    report.update(actual_candidate_preparation_returncode=code,
        actual_structural_template=old_recipe_id,actual_template_restoration=restoration_id,
        original180_selected_point_and_domain_not_transferred=True,
        explicit_sampling_startup_reserve_seconds=reserve)
    if code!=0 or not (preparation/"adapter-result.json").is_file():
        report["unstarted_scope"]=["accurate-ten-factory","current-native-config-binding",
            "complete453","complete450","closed-postsolve"]
        return code or 2
    prepared,prepared_id=read(preparation/"adapter-result.json")
    current_job(prepared,"R449 candidate preparation")
    require(prepared.get("schema")==CANDIDATE_SCHEMA
        and prepared.get("source_sha256")==CANDIDATE_SHA
        and prepared.get("phase")=="candidate-prepared"
        and prepared.get("process_exit_code")==0,"Require the actual R449 preparation")
    model,model_id=member(preparation,prepared["actual_ten_model_recipe"])
    require(model.get("schema")==MODEL_RECIPE_SCHEMA
        and model.get("parameter_order")==PARAMETERS,"Use the new accurate ten recipe")
    model_path=preparation/model_id["file"]
    point,point_id=member(preparation,prepared["candidate_parameters"])
    report.update(actual_candidate_preparation=prepared_id,actual_candidate_point=point_id,
        actual_ten_model_recipe=model_id,
        actual_new_initial_ten_parameters=point["projected_binary64_parameters"],
        actual_new_accurate_ten_parameters=point["new_accurate_ten_parameters"])
    cover=base/"continuous-E"/"result.json"
    cut=base/"cut-twojet-readout"/"cut-twojet-readout.json"
    require(cover.is_file() and cut.is_file(),"Fresh original C and complete cut readout are required")
    cover_id,cut_id=identity(cover),identity(cut)
    source=request["construction_inputs"]["accepted"]
    core=base/"original-inputs"/source["runtime_basename"]
    factory=construction/"factory"
    proof=Path(os.environ["GITHUB_WORKSPACE"])/request["construction"]["R300_proof"]["file"]
    argv=["--core-file",core,"--core-file-sha256",source["sha256"],
        "--core-geometry-pointer",request["construction"]["core_geometry_pointer"],
        "--tail-cover-directory",cover.parent,"--tail-result-sha256",cover_id["sha256"],
        "--cut-twojet-readout",cut,"--cut-twojet-readout-sha256",cut_id["sha256"],
        "--model-recipe",model_path,"--model-recipe-sha256",model_id["sha256"],
        "--code-directory",comp,"--r300-proof",proof,
        "--sqrt-bits","256","--max-domain-cells","65536","--max-domain-depth","32",
        "--domain-budget-seconds","300","--out",factory]
    code=L.call(comp,request,FACTORY_NAME,argv,report["original_child_calls"],
        request["selected_construction"]["maximum_factory_seconds"])
    report["actual_ten_factory_returncode"]=code
    if not (factory/"result.json").is_file():
        report["unstarted_scope"]=["current-native-config-binding","complete453","complete450","closed-postsolve"]
        return code or 2
    result,factory_id=read(factory/"result.json")
    report.update(actual_ten_factory_result=factory_id,
        fresh_factory_current_parameter_domain_complete=result.get("full_current_ten_domain_certificate_complete"),
        fresh_interval_domain_flag_not_used_as_new_BVP_gate=True)
    if code not in (0,70) or result.get("exact_model_definition_created") is not True:
        report["unstarted_scope"]=["current-native-config-binding","complete453","complete450","closed-postsolve"]
        return code or 2
    current_job(result,"independent72c factory")
    require(result.get("schema")==FACTORY_SCHEMA and result.get("source_sha256")==FACTORY_SHA
        and same_payload(result["actual_model_recipe"],model_id)
        and result["actual_tail_result_sha256"]==cover_id["sha256"],
        "Do not relabel the old selected factory as the current candidate")
    fresh,fresh_id=member(factory,result["model_definition"])
    require(fresh.get("schema")==MODEL_SCHEMA and fresh.get("source_sha256")==FACTORY_SHA
        and same_payload(fresh["model_recipe_input"],model_id),
        "Retain the actual new candidate definition")
    report.update(actual_new_ten_definition=fresh_id,current_accurate_definition_created=True,
        candidate_binding_not_attempted_until_actual_native_config_exists=True,
        original_factory_not_forged_or_selected_result_relabelled=True,
        no_actual_BVP_or_native_solve_performed_by_this_phase=True)
    return 0 if code==0 else 70

def bind_current_inputs(L,comp,base,request,report):
    _,adapter_seconds,reserve=candidate_contract(L,comp,request)
    preparation=base/"construction"/"candidate-preparation"
    prepared,prepared_id=read(preparation/"adapter-result.json")
    current_job(prepared,"candidate preparation")
    factory=base/"construction"/"factory"
    factory_result,factory_id=read(factory/"result.json")
    model,model_id=member(preparation,prepared["actual_ten_model_recipe"])
    geometry=base/"current-geometry"/"result.json"
    if not geometry.is_file():
        report.update(actual_current_geometry_present=False,
            unstarted_scope=["current-native-config-binding","complete453","complete450","closed-postsolve"])
        return 2
    gr,geometry_id=read(geometry)
    current_job(gr,"current joint geometry")
    report.update(actual_current_geometry_result=geometry_id,
        actual_current_geometry_completed=gr.get("completed"),
        actual_current_geometry_native_ready=gr.get("native_geometry_ready"),
        actual_current_geometry_error=gr.get("error"))
    if gr.get("completed") is not True or gr.get("native_geometry_ready") is not True:
        # This is the existing original current-native prerequisite, not a new
        # candidate radius/slope/rank or certificate threshold.
        report["unstarted_scope"]=["current-native-config-binding","complete453","complete450","closed-postsolve"]
        return 2
    template_path=L.checked_parameter(comp,request["current_BVP_recipe"])
    template,template_id=read(template_path,request["current_BVP_recipe"])
    configuration=copy.deepcopy(template["native_configuration"])
    sources=dict(configuration["source_sha256"])
    for item in request["pruefer_provider"]["native_source_replacements"]:
        require(sources.pop(item["original_file"])==item["original_sha256"],
            "Keep the exact original native source baseline")
        require(item["file"] not in sources,"No silent source-role overwrite")
        sources[item["file"]]=item["sha256"]
    for name,digest in request["pruefer_provider"]["new_native_source_additions"].items():
        require(name not in sources,"Explicit native source addition already exists")
        sources[name]=digest
    require(sources==request["pruefer_provider"]["complete_current_native_source_sha256"],
        "The complete current joint native source map differs")
    configuration["source_sha256"]=sources
    configuration.update(schema="current-C-complete112-client-config-v1",
        model_schema="R286-original-stored-continuous-model-convention-C-v1",
        repository=REPOSITORY,computations=str(comp),source_topic=os.environ["VISIBLE_SOURCE_TOPIC"],
        geometry_directory=str(geometry.parent),geometry_result_sha256=geometry_id["sha256"],
        actual_policy_template=template_id,actual_candidate_preparation=prepared_id,
        actual_candidate_model_recipe=model_id,original_actual_geometry_result=geometry_id,
        actual_physical_height_source="Actual first453 and then actual450 complete endpoints; each formed inside its original solve",
        no_explicit_zero_or_old_anchor_request=True,
        final_BVP_recipe_formed_after_this_config_and_bound_to_its_actual_SHA=True,
        not_a_fabricated_preexisting_execution_recipe_receipt=True)
    require("original_execution_recipe" not in configuration,
        "Do not create a circular or fictitious final BVP recipe identity")
    config_path=base/"current-C-BVP-client-config.json"
    config_id=write(config_path,configuration)
    folder=base/"actual202-ten-BVP-input"
    cover=base/"continuous-E"/"result.json"
    cut=base/"cut-twojet-readout"/"cut-twojet-readout.json"
    cover_id,cut_id=identity(cover),identity(cut)
    argv=["bind","--preparation-result",preparation/"adapter-result.json",
        "--preparation-result-sha256",prepared_id["sha256"],
        "--factory-directory",factory,"--factory-result-sha256",factory_id["sha256"],
        "--current-C-directory",cover.parent,"--current-C-result-sha256",cover_id["sha256"],
        "--cut-twojet-readout",cut,"--cut-twojet-readout-sha256",cut_id["sha256"],
        "--BVP-recipe-template",template_path,"--tail-config",config_path,
        "--tail-config-sha256",config_id["sha256"],"--code-directory",comp,
        "--candidate-driver-sha256",DRIVER_SHA,"--request-number","205",
        "--sampling-startup-reserve-seconds",str(reserve),"--out",folder]
    code=L.call(comp,request,CANDIDATE_NAME,argv,report["original_child_calls"],adapter_seconds)
    report.update(actual_candidate_binding_returncode=code,
        actual_current_native_configuration=config_id,
        explicit_sampling_startup_reserve_seconds=reserve)
    if code!=0 or not (folder/"adapter-result.json").is_file():
        report["unstarted_scope"]=["complete453","complete450","closed-postsolve"]
        return code or 2
    bound,bound_id=read(folder/"adapter-result.json")
    current_job(bound,"R449 final candidate binding")
    require(bound.get("schema")==CANDIDATE_SCHEMA and bound.get("source_sha256")==CANDIDATE_SHA
        and bound.get("phase")=="BVP-input-bound" and bound.get("process_exit_code")==0
        and same_payload(bound["actual_current_native_configuration"],config_id),
        "Keep the real R449 config/factory/recipe binding")
    recipe,recipe_id=member(folder,bound["generated_BVP_recipe"])
    require(recipe.get("schema")==RECIPE_SCHEMA and recipe.get("request_number")==205
        and recipe["execution"]["pruefer_sampling_startup_reserves_original_BVP_seconds"]==reserve
        and bound["explicit_resource_binding"]["actual_sampling_startup_reserve_seconds"]==reserve,
        "The same explicit reserve must be bound before final recipe identity")
    definition_id=bound["actual_factory_definition"]
    binding=dict(schema=SCHEMA+"-actual-BVP-input",source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        direct_BVP_input_created=True,generated_BVP_recipe=recipe_id,
        actual_candidate_binding=bound_id,actual_candidate_preparation=prepared_id,
        actual_ten_factory_result=factory_id,actual_ten_definition=definition_id,
        actual_ten_model_recipe=model_id,actual_current_native_configuration=config_id,
        actual_current_geometry_result=geometry_id,
        all_ten_initial_parameters=recipe["initial_ten_parameters"],
        actual_projected_binary64le=bound["projected_binary64le"],
        actual_new_accurate_ten_parameters=bound["new_accurate_ten_parameters"],
        candidate_policy=recipe["initial_parameter_origin"]["candidate_policy"],
        explicit_resource_binding=bound["explicit_resource_binding"],
        original202_finite_Gauss_or_actual180_domain_not_inherited=True,
        complete_native_source_sha256=sources,
        one_raw_owner_two_real_problems_no_parent_response_as_second_anchor=True)
    binding_id=write(folder/"result.json",binding)
    deadline,deadline_id=read(base/"job-science-deadline.json")
    request_id=identity(base/"dispatch-request.json")
    require(deadline["schema"]==DEADLINE_SCHEMA and deadline["repository"]==REPOSITORY
        and deadline["run_id"]==os.environ["GITHUB_RUN_ID"]
        and deadline["source_commit"]==os.environ["GITHUB_SHA"]
        and deadline["template_recipe_sha256"]==template_id["sha256"]
        and deadline["request_sha256"]==request_id["sha256"],
        "The original namespace clock must belong to this job and request")
    actual_deadline=dict(deadline,recipe_sha256=recipe_id["sha256"],
        actual_request_number=205,source_namespace_deadline=deadline_id,
        actual_ten_input_binding=binding_id,actual_candidate_binding=bound_id)
    report.update(direct_BVP_input_created=True,generated_BVP_recipe=recipe_id,
        actual_ten_input_binding=binding_id,actual_candidate_binding=bound_id,
        actual_current_launcher_deadline=write(base/"current-BVP-deadline.json",actual_deadline),
        actual_new_initial_ten_parameters=recipe["initial_ten_parameters"],
        original_namespace_start_and_deadline_not_restarted=True,
        no_actual_BVP_or_native_solve_performed_by_this_phase=True)
    return 0

def necessary_readback(L,comp,base,request):
    owner=L.checked_source(comp,request,request["execution"]["owned_process_helper"]["file"])
    observed=runpy.run_path(str(owner),run_name="_request205_original_owned_readback")["observe"]()
    require(observed["quiescent"],"Owned scientific processes must be quiet before reading")
    summary=dict(schema=SCHEMA+"-necessary",source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        complete_necessary_scope=False,files=[],missing_files=[],read_errors=[],
        no_scientific_module_imported_or_new_scientific_arithmetic=True,
        actual_BVP_acceptance_not_inferred=True,large_recomputable_fields_identity_only=True,
        old180_domain_and_finite202_acceptance_not_transferred=True)
    keys={
      "procedure":("schema","phase","process_exit_code","elapsed_seconds","error","resource_partial",
        "selected_files_reconstructed","actual_original165_recovery_complete","original_child_calls",
        "direct_BVP_input_created","generated_BVP_recipe","actual_ten_model_recipe",
        "actual_candidate_preparation","actual_candidate_point","actual_structural_template",
        "actual_template_restoration","actual_candidate_preparation_returncode",
        "actual_candidate_binding_returncode","actual_candidate_binding","actual_ten_input_binding",
        "actual_ten_factory_returncode","actual_ten_factory_result","actual_new_ten_definition",
        "unstarted_scope","fresh_factory_current_parameter_domain_complete",
        "fresh_interval_domain_flag_not_used_as_new_BVP_gate","current_accurate_definition_created",
        "actual_current_geometry_present","actual_current_geometry_result","actual_current_geometry_completed",
        "actual_current_geometry_native_ready","actual_current_geometry_error",
        "actual_current_native_configuration","explicit_sampling_startup_reserve_seconds",
        "actual_current_launcher_deadline","original_namespace_start_and_deadline_not_restarted"),
      "factory":("schema","source_sha256","run_id","source_commit","actual_model_recipe","model_definition",
        "construction_conditions","base_domain","requested_parameter_domain","exact_model_definition_created",
        "nonempty_family_conditions_paid","full_current_ten_domain_certificate_complete","starting_parameters",
        "complete_control_terms","construction_is_uniform_over_all_retained_semantic_leaf_values",
        "maximum_domain_passes","interval_domain_budget_seconds_per_pass","error"),
      "preparation":("schema","source_sha256","run_id","source_commit","phase","process_exit_code",
        "candidate_input","original_parameter_origin","structural_template","copied_structural_fields",
        "candidate_parameters","actual_ten_model_recipe","candidate_policy","original_decimal50_words",
        "projected_binary64le","new_accurate_ten_parameters","projection_rows",
        "accurate_C_factory_domain_or_BVP_called","actual_design453_accepted","actual_frozen450_accepted",
        "exception","traceback"),
      "candidate_binding":("schema","source_sha256","run_id","source_commit","phase","process_exit_code",
        "actual_preparation","actual_candidate_point","actual_ten_model_recipe","actual_factory_result",
        "actual_factory_definition","actual_same_job_C","actual_cut_twojet_readout",
        "actual_current_native_configuration","actual_joint_geometry_result","actual_BVP_template",
        "actual_candidate_driver","generated_BVP_recipe","actual_request_number","explicit_resource_binding",
        "original_factory_full_current_ten_domain_complete","coast_center_necessary_diagnostic",
        "factory_interval_domain_complete_not_used_as_an_extra_BVP_gate","actual_native_calls","actual_BVP_calls",
        "actual_design453_accepted","actual_frozen450_accepted","exception","traceback"),
      "input":("schema","source_sha256","run_id","source_commit","direct_BVP_input_created",
        "generated_BVP_recipe","actual_candidate_binding","actual_candidate_preparation",
        "actual_ten_factory_result","actual_ten_definition","actual_ten_model_recipe",
        "actual_current_native_configuration","actual_current_geometry_result","explicit_resource_binding",
        "original202_finite_Gauss_or_actual180_domain_not_inherited"),
      "restoration":("schema","reconstruction_complete","process_exit_code","error","resource_partial",
        "original180_domain_certificate_only_reused_not_recomputed","new_C_or_factory_result_not_created"),
      "recovery":("schema","complete","resource_partial","error","original_run_id","original_job_id",
        "original_source_commit","elapsed_seconds","exit_code"),
      "deadline":("schema","run_id","source_commit","request_sha256","template_recipe_sha256","recipe_sha256",
        "namespace_created_unix_seconds","science_seconds_from_namespace","readback_reserve_seconds",
        "actual_request_number","source_namespace_deadline","actual_candidate_binding")}
    paths=[("selected-recovery-result.json","procedure"),("restored165/recovery-result.json","recovery"),
        ("restored-selection/restoration-result.json","restoration"),
        ("construction/procedure-result.json","procedure"),
        ("construction/candidate-preparation/adapter-result.json","preparation"),
        ("construction/factory/result.json","factory"),
        ("candidate-binding-procedure-result.json","procedure"),
        ("actual202-ten-BVP-input/adapter-result.json","candidate_binding"),
        ("actual202-ten-BVP-input/result.json","input"),("current-BVP-deadline.json","deadline")]
    for relative,kind in paths:
        path=base/relative
        if not path.is_file():summary["missing_files"].append(relative);continue
        try:
            value,rec=read(path);chosen={k:value[k] for k in keys[kind] if k in value}
            if kind=="factory":
                for key in ("base_domain","requested_parameter_domain"):
                    chosen[key]=L.factory_domain_scope(path.parent,value.get(key))
            summary["files"].append(dict(file=relative,identity=rec,necessary_original_values=chosen))
        except Exception as error:
            summary["read_errors"].append(dict(file=relative,type=type(error).__name__,message=str(error)))
    for relative in ("selection-summary.json","restored-selection/selected-accurate-nine-recipe.json",
        "restored-selection/selected-accurate-nine-definition.json",
        "construction/candidate-preparation/candidate-ten-parameters.json",
        "construction/candidate-preparation/actual202-projected-accurate-ten-model-recipe.json",
        "actual202-ten-BVP-input/actual202-accurate-ten-full453-frozen450-recipe.json",
        "current-C-BVP-client-config.json"):
        path=base/relative
        if path.is_file():summary.setdefault("complete_parameter_file_identities",[]).append(
            dict(file=relative,identity=identity(path)))
    summary["complete_necessary_scope"]=not summary["read_errors"]
    summary["missing_outputs_are_unstarted_or_failed_not_completed_science"]=True
    raw=canonical(summary)
    if len(raw)>LIMIT:
        print(json.dumps(dict(event="request205_construction_necessary_over_limit",bytes=len(raw),
            sha256=sha(raw),complete_necessary_scope=False,cleanup_must_skip=True)),flush=True)
        return 70
    write(base/"construction-necessary-summary.json",summary)
    print("BEGIN_REQUEST205_ACTUAL202_TEN_CONSTRUCTION_NECESSARY",flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_REQUEST205_ACTUAL202_TEN_CONSTRUCTION_NECESSARY",flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            for k,v in (("construction_summary",raw.decode("ascii").rstrip("\n")),
                        ("construction_summary_bytes",len(raw)),("construction_summary_sha256",sha(raw))):
                stream.write(str(k)+"="+str(v)+"\n")
    if not summary["complete_necessary_scope"]:return 2
    write(base/"construction-readback-complete.json",dict(schema=SCHEMA+"-marker",
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        complete=True,necessary_summary=dict(bytes=len(raw),sha256=sha(raw)),
        no_actual_BVP_or_native_acceptance_inferred=True,
        other_readbacks_and_postsolve_still_required_before_cleanup=True))
    return 0

def main(argv=None):
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "This source/parameter construction executes only in public Actions")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase",choices=("selection","construction","binding","readback"))
    for key in ("request","base","code-directory"):parser.add_argument("--"+key,type=Path,required=True)
    args=parser.parse_args(argv)
    comp,base=args.code_directory.resolve(),args.base.resolve()
    require(base.parent==Path(os.environ["RUNNER_TEMP"]).resolve() and base.name==NAMESPACE
        and not args.base.is_symlink(),"Use this independent exclusive temporary namespace")
    request,_=read(args.request)
    require(request["schema"]==REQUEST_SCHEMA and request["request_number"]==205
        and request["repository"]==REPOSITORY,"Use the actual independent205 request")
    require(sha(Path(__file__).read_bytes())==request["source_sha256"][Path(__file__).name],
        "Current pipeline source differs")
    L=load(comp,LEGACY_NAME,LEGACY_SHA,"_request205_original_template_recovery")
    if args.phase=="readback":return necessary_readback(L,comp,base,request)
    report=dict(schema=SCHEMA+"-procedure",phase=args.phase,repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=identity(__file__),original_child_calls=[],error=None,resource_partial=False,
        direct_BVP_input_created=False,selected_files_reconstructed=False,
        recovered180_point_and_domain_not_current_candidate_evidence=True,
        old202_finite_Gauss_state_J_domain_or_acceptance_not_inherited=True,
        actual_BVP_call_count_in_helper=0,
        original_native_FD_BC_RMS_and_final_scientific_gates_unchanged=True,
        final_closed_postsolve_and_quiet_readback_required_before_owned_cleanup=True)
    start=time.monotonic();code=2
    destination=base/"selected-recovery-result.json"
    if args.phase=="construction":
        directory=base/"construction";directory.mkdir()
        destination=directory/"procedure-result.json"
    elif args.phase=="binding":destination=base/"candidate-binding-procedure-result.json"
    try:
        if args.phase=="selection":code=L.recover(comp,base,request,report)
        elif args.phase=="construction":code=construct(L,comp,base,request,report)
        else:code=bind_current_inputs(L,comp,base,request,report)
    except BaseException as error:
        code=3 if isinstance(error,L.ResourceStop) else 2
        report["resource_partial"]=isinstance(error,L.ResourceStop)
        message=str(error);stack=traceback.format_exc()
        for key in L.TOKENS:
            token=os.environ.get(key)
            if token:message=message.replace(token,"[redacted]");stack=stack.replace(token,"[redacted]")
        if isinstance(error,(L.urllib.error.HTTPError,L.urllib.error.URLError)):
            message="Official original-log transport failed; signed URL and bearer omitted"
            stack=None
        report["error"]=dict(type=type(error).__name__,message=message,traceback=stack)
    report["elapsed_seconds"]=time.monotonic()-start;report["process_exit_code"]=code
    original=write(destination,report)
    print(json.dumps(dict(event="request205_actual_candidate_construction_returned",original_result=original,
        phase=args.phase,process_exit_code=code,direct_BVP_input_created=report["direct_BVP_input_created"],
        error=report["error"],resource_partial=report["resource_partial"])),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())

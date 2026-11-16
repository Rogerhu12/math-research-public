#!/usr/bin/env python3
"""Request203 source recovery, real ten construction and joint-provider binding.

Reuse the frozen187 official actual180/165 byte recovery without re-solving
the selected coast domain. Run the independent ten factory in this job at
the exact selected nine point plus xi=0. Bind its actual complete definition:
the common expression DAG, pieces, supports, accurate core and full C root
family agree with the recovered nine restriction. Different current enclosure
boxes and numeric compilations remain different evidence, not target changes.
No original nine factory result is relabelled as a ten result or a BVP field.
The frozen187 pipeline is used only for original byte recovery/child transport;
current geometry and live native sources are the explicit published197 joint
provider. Its nominal box point is not claimed to be a global exact-C member.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import runpy
import sys
import time
import traceback

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request203-selected-coast-continuous-ten-joint-construction-v1"
REQUEST_SCHEMA="public-current-C-ten450-joint-closed-geometry-request-v1"
NAMESPACE="visible-current-C-ten450-joint-closed-geometry203"
RECIPE_SCHEMA="explicit-current-C-continuous-ten-joint-live-full453-to-frozen450-recipe-v1"
FACTORY_NAME="geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA="72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
FACTORY_SCHEMA="R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1"
MODEL_SCHEMA="R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
MODEL_RECIPE_SCHEMA="R300-new-continuous-ten-fixed-support1-power4-model-recipe-v1"
LEGACY_NAME="geometry_20261115_selected_coast_positive_current_C_pipeline.py"
LEGACY_SHA="1738fbb7fe1ca5211fb09442d14e740b2363c7d6c5d5daa14dd26c5f60a60d9b"
SEMANTIC_NAME="geometry_20261115_accurate_coast_selected_bvp_inputs.py"
SEMANTIC_SHA="e5ab2a8cd5e6f787b9ef37121b1adfba9ea3236ee227b93f31f1f78577b494f2"
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3","xi"]
CONTROL_TERMS=[dict(parameter_index=3*j+i,support_index=i,power=j)
    for j in range(3) for i in range(3)]+[dict(parameter_index=9,support_index=1,power=4)]
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

def restriction_binding(S,old,fresh,old_recipe,ten_recipe,exact):
    """Only semantic/metadata algebra; no numerical model or new C evaluation."""
    require(old.get("schema")==S.MODEL_SCHEMA and old.get("source_sha256")==S.FACTORY_SHA,
        "Retain the recovered actual180 accurate nine definition")
    require(fresh.get("schema")==MODEL_SCHEMA and fresh.get("source_sha256")==FACTORY_SHA,
        "Require the actual new ten factory definition, never a relabelled nine record")
    require(old.get("parameter_order")==S.PARAMETERS and fresh.get("parameter_order")==PARAMETERS,
        "Preserve the declared nine restriction and independent ten order")
    require(fresh.get("control_terms")==CONTROL_TERMS,
        "The tenth coordinate is only the declared support1 power4 radius shape")
    require(fresh.get("source_text_baseline",{}).get("sha256")==S.FACTORY_SHA,
        "The original accurate nine factory baseline differs")
    require([S.q(v) for v in fresh["ten_parameters"]]==exact+[S.q(0)]
        and [S.q(v) for v in old["nine_parameters"]]==exact,
        "The explicit xi=0 restriction must retain every exact selected coefficient")
    added=fresh["added_term"]
    for key,wanted in (("parameter_index",9),("support_index",1),("power",4),
            ("zero_xi_restriction_is_original_accurate_nine_family",True),
            ("derivatives_are_same_radius_polynomial_derivatives",True),
            ("endpoint_zero_two_jets_follow_from_order3_factors",True),
            ("no_parameter_dependent_support_or_natural_length",True)):
        require(added.get(key)==wanted,"Independent ten term contract differs: "+key)
    common=[key for key in S.MATHEMATICAL_KEYS if key not in
        ("schema","source_sha256","parameter_order")]
    checked={}
    for key in common:
        require(key in old and key in fresh,"Missing accurate common expression field: "+key)
        require(canonical(old[key])==canonical(fresh[key]),"The accurate nine restriction differs: "+key)
        checked[key]=dict(equal=True,canonical_sha256=sha(canonical(old[key])))
    for key in ("core_end","cut_radius"):
        require(S.q(old[key])==S.q(fresh[key]),"Accurate natural coordinate or cut changed")
        checked[key]=dict(equal=True,exact_rational=str(S.q(old[key])))
    for key,function in (("complete_C_semantics",S.accurate_C_signature),
                         ("selected_exact_core",S.accurate_core_signature)):
        a,b=function(old),function(fresh)
        require(canonical(a)==canonical(b),"Actual accurate source target differs: "+key)
        checked[key]=dict(equal=True,canonical_sha256=sha(canonical(a)))
    original=S.accurate_recipe_signature(old_recipe)
    as_nine=copy.deepcopy(ten_recipe)
    as_nine["schema"]=S.MODEL_RECIPE_SCHEMA
    as_nine["parameter_order"]=S.PARAMETERS
    as_nine["nine_parameters"]=as_nine.pop("ten_parameters")[:9]
    as_nine.pop("control_terms")
    require(canonical(original)==canonical(S.accurate_recipe_signature(as_nine)),
        "New ten recipe changes the selected accurate nine restriction")
    checked["exact_recipe_restriction"]=dict(equal=True,canonical_sha256=sha(canonical(original)))
    for key in ("support_left_expression","support_width_expression"):
        counterpart="left" if key=="support_left_expression" else "width"
        require(added[key]==fresh["three_true_supports"][1][counterpart],
            "The tenth support is not the declared exact first velocity transition")
    return checked

def construct(L,S,comp,base,request,report):
    selected=request["actual180_selection"]
    old_recipe_path=base/"restored-selection"/selected["selected_recipe"]["file"]
    old_definition_path=base/"restored-selection"/selected["selected_definition"]["file"]
    old_recipe,old_recipe_id=read(old_recipe_path,selected["selected_recipe"])
    old_definition,old_definition_id=read(old_definition_path,selected["selected_definition"])
    summary,summary_id=read(base/"selection-summary.json",selected["summary"])
    restoration,restoration_id=read(base/"restored-selection"/"restoration-result.json")
    require(restoration.get("reconstruction_complete") is True,"Actual selected files not recovered")
    point=summary["selected_profile"]
    require(summary["schema"]==S.SELECTION_SCHEMA and summary.get("summary_complete") is True
        and summary.get("full_accurate_nine_domain_proved") is True
        and summary["all418_unchanged_piece_domain"]["complete"] is True
        and summary["unchanged_target_geometry"]["complete_accurate_piece_count"]==419,
        "Preserve actual180 whole419 accurate-family evidence at its selected point")
    projected,exact,projections,exact_words=S.parameter_projection(point)
    require(exact_words,"This request requires the declared exact binary64 direct selected point")
    require([S.q(x) for x in old_recipe["nine_parameters"]]==exact
        and [S.q(x) for x in old_definition["nine_parameters"]]==exact,
        "All recovered accurate coefficient words must agree")
    recipe=copy.deepcopy(old_recipe)
    recipe["schema"]=MODEL_RECIPE_SCHEMA;recipe["parameter_order"]=PARAMETERS
    recipe.pop("nine_parameters")
    recipe["ten_parameters"]=projected+[0.0];recipe["control_terms"]=CONTROL_TERMS
    recipe["explicit_zero_xi_source"]=dict(actual180_selection_summary=summary_id,
        selected_nine_recipe=old_recipe_id,selected_nine_definition=old_definition_id,
        all_nine_exact_projection_rows=projections,
        zero_xi_restriction_not_old_numerical_shadow_word_equivalence=True)
    construction=base/"construction"
    ten_recipe_path=construction/"selected-accurate-ten-xi0-recipe.json"
    ten_recipe_id=write(ten_recipe_path,recipe)
    report.update(actual_reconstruction_receipt=restoration_id,
        actual_ten_model_recipe=ten_recipe_id,
        actual_exact_initial_ten=[str(q) for q in exact]+["0"])
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
        "--model-recipe",ten_recipe_path,"--model-recipe-sha256",ten_recipe_id["sha256"],
        "--code-directory",comp,"--r300-proof",proof,
        "--sqrt-bits","256","--max-domain-cells","65536","--max-domain-depth","32",
        "--domain-budget-seconds","300","--out",factory]
    code=L.call(comp,request,FACTORY_NAME,argv,report["original_child_calls"],
        request["selected_construction"]["maximum_factory_seconds"])
    report["actual_ten_factory_returncode"]=code
    if not (factory/"result.json").is_file():
        report["unstarted_scope"]=["semantic-ten-binding","complete453","complete450"]
        return code or 2
    result,factory_id=read(factory/"result.json")
    report["actual_ten_factory_result"]=factory_id
    report["fresh_factory_current_parameter_domain_complete"]=result.get("full_current_ten_domain_certificate_complete")
    report["fresh_interval_domain_flag_not_used_as_new_BVP_gate"]=True
    if code not in (0,70) or result.get("exact_model_definition_created") is not True:
        report["unstarted_scope"]=["semantic-ten-binding","complete453","complete450"]
        return code or 2
    require(result.get("schema")==FACTORY_SCHEMA and result.get("source_sha256")==FACTORY_SHA
        and result.get("repository")==REPOSITORY and str(result.get("run_id"))==os.environ["GITHUB_RUN_ID"]
        and result.get("source_commit")==os.environ["GITHUB_SHA"],
        "The independent ten factory must have actually run in this job")
    fresh,fresh_id=S.safe_member(factory,result["model_definition"])
    require(result["actual_model_recipe"]["sha256"]==ten_recipe_id["sha256"]
        and fresh["model_recipe_input"]["sha256"]==ten_recipe_id["sha256"]
        and result["actual_tail_result_sha256"]==cover_id["sha256"]
        and [S.q(v) for v in result["starting_parameters"]]==exact+[S.q(0)],
        "Bind the actual new factory, recipe, cut source and exact point")
    common=restriction_binding(S,old_definition,fresh,old_recipe,recipe,exact)
    transfer=dict(schema=SCHEMA+"-zero-xi-accurate-restriction",
        original_selected_full419_domain_statement_retained=True,
        common_exact_base_DAG_pieces_supports_core_cut_and_all_C_roots=True,
        complete_exact_selected_nine_plus_zero_xi=True,
        new_ten_family_source_and_definition_not_relabelled_as_old_nine=True,
        same_initial_accurate_point_not_any_later_active_p_or_xi=True,
        equal_old_fresh_enclosure_boxes_not_required=True,
        original_or_new_numeric_domain_J_FD_BVP_or_metric_not_paid_by_transfer=True,
        original_certificate_bound_to_full_root_family_not_independent_box_points=True)
    report.update(actual_new_ten_definition=fresh_id,
        common_accurate_restriction_field_identities=common,
        initial_domain_transfer=transfer,
        separate_selected_and_fresh_evidence=dict(selected=S.actual_definition_evidence(old_definition),
            fresh=S.actual_definition_evidence(fresh)))
    template_path=L.checked_parameter(comp,request["current_BVP_recipe"])
    template,template_id=read(template_path,request["current_BVP_recipe"])
    require(template["schema"]==S.BVP_RECIPE_SCHEMA and template["parameter_order"]==S.PARAMETERS,
        "Use the exact original179 BVP resource/algorithm template")
    current=copy.deepcopy(template)
    current.update(schema=RECIPE_SCHEMA,request_number=203,parameter_order=PARAMETERS,
        frozen_parameter_indices=[3,4,5,6,7,8,9],initial_ten_parameters=projected+[0.0],
        second_problem="same-ten-words-complete450-K0-k0",second_state_dimension=450,
        two_phases_share_one_original_process_clock=True)
    current.pop("initial_nine_parameters")
    current["initial_parameter_origin"]=dict(
        kind="actual180-selected-accurate-nine-with-explicit-zero-xi",
        selection_summary=summary_id,selected_nine_recipe=old_recipe_id,
        selected_nine_definition=old_definition_id,
        actual_ten_model_recipe=ten_recipe_id,actual_same_job_ten_factory=factory_id,
        actual_same_job_ten_definition=fresh_id,all_nine_original_projection_rows=projections,
        original_template_parameter_origin=template["initial_parameter_origin"],
        accurate_zero_xi_restriction=transfer,
        old_numeric_shadow_or_old_fullDN_not_inherited=True)
    native=current["native_configuration"]
    new_sources=dict(native["source_sha256"])
    for item in request["pruefer_provider"]["native_source_replacements"]:
        require(new_sources.pop(item["original_file"])==item["original_sha256"],
            "Original native baseline differs before explicit current provider binding")
        require(item["file"] not in new_sources,"No implicit source overwrite")
        new_sources[item["file"]]=item["sha256"]
    for name,digest in request["pruefer_provider"]["new_native_source_additions"].items():
        require(name not in new_sources,"Explicit native source addition differs")
        new_sources[name]=digest
    require(new_sources==request["pruefer_provider"]["complete_current_native_source_sha256"],
        "Retain the complete explicit current-C joint-nominal native source responsibilities")
    native["source_sha256"]=new_sources
    execution=current["execution"]
    for key in ("sampling_declared_linear_seconds","sampling_declared_point_seconds",
                "sampling_startup_reserves_original_BVP_seconds"):
        execution["pruefer_"+key]=execution.pop("riccati_"+key)
    execution["algorithmic_protocol_solve_entry_upper_bound"]=36
    execution["two_phases_use_one_original_BVP_process_budget"]=True
    current["acceptance_scope"].pop("all_nine_fixed450_same_g_refinement_and_closed_geometry_not_supplied")
    current["acceptance_scope"].pop("R375_original_deep_family_recomputed_not_previous_pivot_box_shrunk")
    current["acceptance_scope"].pop("two_closed_comparison_barriers_and_full_inherited_ratio_retained")
    current["acceptance_scope"].update(
        R380_original_deep_family_recomputed_not_previous_endpoint_box_shrunk=True,
        positive_endpoint_projective_continuation_with_uniform_R357_unit_row_rule=True,
        joint_nominal_parameter_box_point_not_claimed_to_be_a_global_C_member=True,
        complete_original_unit_row_family_to_actual_binary64_error_enclosures_retained=True,
        nominal_row_formation_does_not_add_a_native_acceptance_gate=True)
    current["acceptance_scope"].update(independent_real_complete450_after_real453=True,
        original_current_H_FD_native_fullJ_final_audit_required_for_each_phase=True,
        closed_geometry_and_continuous_metric_not_supplied=True,
        new_ten_numeric_compilation_not_old_nine_word_equivalence=True)
    # Record the published joint-nominal provider independently, without
    # borrowing the old semantic adapter's generated nine recipe/schema.
    current["current_pruefer_provider_identity"]=copy.deepcopy(request["pruefer_provider"])
    current["actual_continuous_ten_restriction_binding"]=dict(
        source_sha256=sha(Path(__file__).read_bytes()),actual_original_template=template_id,
        complete_common_accurate_field_identity=common,initial_domain_transfer=transfer)
    folder=base/"continuous-ten-BVP-input";folder.mkdir()
    recipe_id=write(folder/"current-selected-ten-full453-frozen450-recipe.json",current)
    binding=dict(schema=SCHEMA+"-actual-BVP-input",source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        direct_BVP_input_created=True,generated_BVP_recipe=recipe_id,
        actual_ten_factory_result=factory_id,actual_ten_definition=fresh_id,
        actual_ten_model_recipe=ten_recipe_id,actual_selection_summary=summary_id,
        all_ten_initial_parameters=current["initial_ten_parameters"],
        actual_ten_float64_words_are_selected_exact_rationals=True,
        initial_accurate_restriction_binding=transfer,
        complete_native_source_sha256=new_sources,
        one_raw_owner_two_real_problems_no_parent_response_as_second_anchor=True)
    binding_id=write(folder/"result.json",binding)
    deadline,deadline_id=read(base/"job-science-deadline.json")
    require(deadline["schema"]=="request203-owned-job-science-deadline-v1"
        and deadline["run_id"]==os.environ["GITHUB_RUN_ID"]
        and deadline["source_commit"]==os.environ["GITHUB_SHA"]
        and deadline["template_recipe_sha256"]==template_id["sha256"],
        "The original namespace clock must belong to this job")
    actual_deadline=dict(deadline,recipe_sha256=recipe_id["sha256"],
        actual_request_number=203,source_namespace_deadline=deadline_id,
        actual_ten_input_binding=binding_id)
    report.update(direct_BVP_input_created=True,generated_BVP_recipe=recipe_id,
        actual_ten_input_binding=binding_id,
        actual_current_launcher_deadline=write(base/"current-BVP-deadline.json",actual_deadline),
        actual_new_initial_ten_parameters=current["initial_ten_parameters"],
        no_actual_BVP_or_native_solve_performed=True,
        original_factory_not_forged_or_nine_result_relabelled=True)
    return 0 if code==0 else 70

def necessary_readback(L,comp,base,request):
    owner=L.checked_source(comp,request,request["execution"]["owned_process_helper"]["file"])
    observed=runpy.run_path(str(owner),run_name="_request203_original_owned_readback")["observe"]()
    require(observed["quiescent"],"Owned scientific processes must be quiet before reading")
    summary=dict(schema=SCHEMA+"-necessary",source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        complete_necessary_scope=False,files=[],missing_files=[],read_errors=[],
        no_scientific_module_imported_or_new_scientific_arithmetic=True,
        actual_BVP_acceptance_not_inferred=True,large_recomputable_fields_identity_only=True)
    keys={
      "procedure":("schema","phase","process_exit_code","elapsed_seconds","error","resource_partial",
        "selected_files_reconstructed","actual_original165_recovery_complete","original_child_calls",
        "direct_BVP_input_created","generated_BVP_recipe","actual_ten_model_recipe",
        "actual_exact_initial_ten","actual_ten_factory_returncode","actual_ten_factory_result",
        "actual_new_ten_definition","unstarted_scope","fresh_factory_current_parameter_domain_complete",
        "fresh_interval_domain_flag_not_used_as_new_BVP_gate","initial_domain_transfer",
        "actual_ten_input_binding","actual_new_initial_ten_parameters","actual_current_launcher_deadline"),
      "factory":("schema","source_sha256","run_id","source_commit","actual_model_recipe","model_definition",
        "construction_conditions","base_domain","requested_parameter_domain","exact_model_definition_created",
        "nonempty_family_conditions_paid","full_current_ten_domain_certificate_complete","starting_parameters",
        "complete_control_terms","construction_is_uniform_over_all_retained_semantic_leaf_values",
        "maximum_domain_passes","interval_domain_budget_seconds_per_pass","error"),
      "input":("schema","source_sha256","run_id","source_commit","direct_BVP_input_created",
        "generated_BVP_recipe","actual_ten_factory_result","actual_ten_definition","actual_ten_model_recipe",
        "actual_selection_summary","all_ten_initial_parameters","initial_accurate_restriction_binding"),
      "restoration":("schema","reconstruction_complete","process_exit_code","error","resource_partial",
        "original180_domain_certificate_only_reused_not_recomputed","new_C_or_factory_result_not_created"),
      "recovery":("schema","complete","resource_partial","error","original_run_id","original_job_id",
        "original_source_commit","elapsed_seconds","exit_code"),
      "deadline":("schema","run_id","source_commit","request_sha256","template_recipe_sha256","recipe_sha256",
        "namespace_created_unix_seconds","science_seconds_from_namespace","readback_reserve_seconds",
        "actual_request_number","source_namespace_deadline")
    }
    paths=[("selected-recovery-result.json","procedure"),("restored165/recovery-result.json","recovery"),
        ("restored-selection/restoration-result.json","restoration"),
        ("construction/procedure-result.json","procedure"),("construction/factory/result.json","factory"),
        ("continuous-ten-BVP-input/result.json","input"),("current-BVP-deadline.json","deadline")]
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
        "restored-selection/selected-accurate-nine-definition.json","construction/selected-accurate-ten-xi0-recipe.json",
        "continuous-ten-BVP-input/current-selected-ten-full453-frozen450-recipe.json"):
        path=base/relative
        if path.is_file():summary.setdefault("complete_parameter_file_identities",[]).append(
            dict(file=relative,identity=identity(path)))
    summary["complete_necessary_scope"]=not summary["read_errors"]
    summary["missing_outputs_are_unstarted_or_failed_not_completed_science"]=True
    raw=canonical(summary)
    if len(raw)>LIMIT:
        print(json.dumps(dict(event="request203_construction_necessary_over_limit",bytes=len(raw),
            sha256=sha(raw),complete_necessary_scope=False,cleanup_must_skip=True)),flush=True)
        return 70
    write(base/"construction-necessary-summary.json",summary)
    print("BEGIN_REQUEST203_CONTINUOUS_TEN_CONSTRUCTION_NECESSARY",flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_REQUEST203_CONTINUOUS_TEN_CONSTRUCTION_NECESSARY",flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            for k,v in (("construction_summary",raw.decode("ascii").rstrip("\n")),
                        ("construction_summary_bytes",len(raw)),("construction_summary_sha256",sha(raw))):
                stream.write(str(k)+"="+str(v)+"\n")
    if not summary["complete_necessary_scope"]:return 2
    write(base/"construction-readback-complete.json",dict(schema=SCHEMA+"-marker",
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        complete=True,necessary_summary=dict(bytes=len(raw),sha256=sha(raw)),
        no_actual_BVP_or_native_acceptance_inferred=True))
    return 0

def main(argv=None):
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "This source/parameter construction executes only in public Actions")
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase",choices=("selection","construction","readback"))
    for key in ("request","base","code-directory"):parser.add_argument("--"+key,type=Path,required=True)
    args=parser.parse_args(argv)
    comp,base=args.code_directory.resolve(),args.base.resolve()
    require(base.parent==Path(os.environ["RUNNER_TEMP"]).resolve() and base.name==NAMESPACE
        and not args.base.is_symlink(),"Use this independent exclusive temporary namespace")
    request,_=read(args.request)
    require(request["schema"]==REQUEST_SCHEMA and request["request_number"]==203
        and request["repository"]==REPOSITORY,"Use the actual independent203 request")
    require(sha(Path(__file__).read_bytes())==request["source_sha256"][Path(__file__).name],
        "Current pipeline source differs")
    L=load(comp,LEGACY_NAME,LEGACY_SHA,"_request203_original_selected_recovery")
    if args.phase=="readback":return necessary_readback(L,comp,base,request)
    S=load(comp,SEMANTIC_NAME,SEMANTIC_SHA,"_request203_original_semantic_functions")
    report=dict(schema=SCHEMA+"-procedure",phase=args.phase,repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=identity(__file__),original_child_calls=[],error=None,resource_partial=False,
        direct_BVP_input_created=False,selected_files_reconstructed=False,
        old_complete_domain_not_recomputed_by_recovery=True,actual_BVP_call_count_in_helper=0,
        original_native_FD_BC_RMS_and_final_scientific_gates_unchanged=True)
    start=time.monotonic();code=2
    destination=base/"selected-recovery-result.json"
    if args.phase=="construction":
        directory=base/"construction";directory.mkdir()
        destination=directory/"procedure-result.json"
    try:
        code=(L.recover(comp,base,request,report) if args.phase=="selection"
              else construct(L,S,comp,base,request,report))
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
    print(json.dumps(dict(event="request203_actual_construction_returned",original_result=original,
        phase=args.phase,process_exit_code=code,direct_BVP_input_created=report["direct_BVP_input_created"],
        error=report["error"],resource_partial=report["resource_partial"])),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())

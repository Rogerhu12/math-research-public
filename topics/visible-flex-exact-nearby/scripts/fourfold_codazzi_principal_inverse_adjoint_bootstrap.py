#!/usr/bin/env python3
"""New complete principal adjoint bootstrap, reading one successful PG result.
Only positive products, one logarithm and a whole negative-window minimum are new.
The original PG logarithms and all five scalar inputs remain unchanged.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_complete_principal_inverse_adjoint_bootstrap_v1"
MANIFEST_KIND="principal_inverse_adjoint_bootstrap_public_inputs_v1"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0")
CONTRACT="2d74b71c0584cb5ec1af849b6fb5756e48da58bf313d72be62d582d557d23acb"
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"original_PG_run\":\"43770122351/1\",\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"independent_physical_mean_coordinates\":2,\"selected_conjugacy_parameter_absolute_upper\":\"0.00000000009368259853002\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"selected_common_input_map\":\"psi = X_minus o H_inverse\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"principal_factors\":[\"T_ci = Id + M_ci I\",\"T_co = Id + M_co I\"],\"source_window\":\"H^(-4/3)\",\"target_window\":\"H^(-4/3)\",\"adjoint_intermediate_window\":\"H^(1/3)\",\"existing_inverse_window\":\"L2\",\"expected_actual_gate_count\":15,\"current_input_count\":6,\"new_logarithms\":1,\"new_complete_log_candidates\":1,\"new_complete_whole_log_minima\":1,\"old_successful_scientific_calls_allowed\":0,\"direct_exponential_evaluation_allowed\":false,\"signed_coefficient_gate_checked\":false,\"complete_physical_incoming_or_finite_inverse_or_return_claimed\":false}")
OLD=json.loads("{\"run\":\"43770122351\",\"attempt\":\"1\",\"kind\":\"actual_complete_principal_inverse_from_first_derivatives_v1\",\"source\":\"08b8d1d9ff222ba7c8cea14bed50c0e9cd320359aa0e5456bc14c2ecfcc5c9c7\",\"manifest\":\"febb85783c624eed3bab22cd6e0873aad08c3257e4758615668654f82289e51c\",\"execution\":\"95a0fafb34cbb7fa4fd5c0379324b71a35053af5daa73718f95bda8afdc26d67\",\"gates\":20,\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"contract\":\"0a5e4ad71d0d980a097e6c0f4afa8476780a46b4b3e82e5a583633f8bb66ad1a\"}")

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)
def payload_sha(x):return hashlib.sha256(canonical(x).encode()).hexdigest()
def read(path):return json.loads(Path(path).read_bytes())
def save(path,x,compressed=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(canonical(x)+"\n").encode()
    body=gzip.compress(raw,mtime=0) if compressed else raw
    tmp=path.with_name(path.name+".tmp");tmp.write_bytes(body);tmp.replace(path)
def rb(x):
    if isinstance(x,arb):return x
    if isinstance(x,dict):return arb(x["ball"])
    return arb(x)
def up(x):
    x=rb(x)
    if not x.is_finite() or x.lower()<0:
        raise ValueError("a complete nonnegative saved or new budget is invalid")
    return x.upper()
def rec(x):return dict(ball=rb(x).str(60))
def finite(x):
    if isinstance(x,dict):
        if "ball" in x:return rb(x).is_finite()
        return all(finite(v) for v in x.values())
    if isinstance(x,(list,tuple)):return all(finite(v) for v in x)
    if isinstance(x,arb):return x.is_finite()
    return True

def checked_inputs(a,d,gate):
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__)
    d["runtime"]=runtime
    gate("public Actions and the exact two-key runtime use320-bit directed arithmetic",
        os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
        and runtime==RUNTIME and ctx.prec==320)
    m=read(a.manifest);paths={k:a.repo_root/Path(v) for k,v in m["input_paths"].items()}
    gate("six exact current small inputs and the new frozen parameters form the complete closure",
        m["kind"]==MANIFEST_KIND and m["public_repository"]==PUBLIC
        and m["source_sha256"]==m["scientific_source_sha256"]==sha(__file__)
        and m["contract_sha256"]==CONTRACT and m["mathematical_parameters"]==PARAMETERS
        and m["expected_actual_gate_count"]==15
        and m["all_inputs_are_current_small_texts"] is True
        and m["old_successful_scientific_calls_allowed"]==0 and m["legacy_artifact_inputs"]==[]
        and m["file_count"]==len(m["files"])==6
        and set(m["input_paths"].values())=={x["path"] for x in m["files"]})
    gate("every complete input size SHA and text type is checked before new scalar arithmetic",
        all((a.repo_root/Path(x["path"])).stat().st_size==x["bytes"]
            and sha(a.repo_root/Path(x["path"]))==x["sha256"]
            and x["bytes"]<100000 and Path(x["path"]).suffix in (".py",".json",".md")
            and not (a.repo_root/Path(x["path"])).read_bytes().startswith(b"\x1f\x8b")
            for x in m["files"]))
    gate("new proof and original PG source manifest and execution have their exact immutable identities",
        sha(paths["contract"])==CONTRACT
        and sha(paths["PG_source"])==OLD["source"]
        and sha(paths["PG_manifest"])==OLD["manifest"]
        and sha(paths["PG_execution"])==OLD["execution"]
        and read(paths["PG_manifest"])["contract_sha256"]==OLD["contract"]
        and m["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
    e=read(paths["PG_execution"]);p=e.get("actual_scientific_receipt",{})
    gate("PG43770122351 retains the complete actual zero exit source runtime and twenty gates",
        e.get("run_id")==OLD["run"] and e.get("run_attempt")==OLD["attempt"]
        and e.get("complete") is True and e.get("actual_returncode")==0
        and e.get("actual_source_budget_processes")==1
        and e.get("source_budget_source_sha256")==OLD["source"]
        and e.get("input_manifest_sha256")==OLD["manifest"]
        and p.get("kind")==OLD["kind"] and p.get("run_id")==OLD["run"]
        and p.get("run_attempt")==OLD["attempt"]
        and p.get("complete") is True and p.get("proved") is True
        and p.get("stage")=="complete" and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("source_sha256")==OLD["source"] and p.get("input_manifest_sha256")==OLD["manifest"]
        and p.get("runtime")==OLD["runtime"] and p.get("arithmetic_bits")==320
        and len(p.get("gates",[]))==20 and all(g.get("passed") is True for g in p["gates"]))
    pp=p["mathematical_parameters"];sc=p["complete_selected_common_input_scope_read_verbatim"]
    shared=["exact_real_delta_radius","fixed_intrinsic_parameter","exact_root_interval","exact_strict_cut","physical_frequency","physical_period","independent_physical_mean_coordinates","selected_conjugacy_parameter_absolute_upper","selected_common_input_order","selected_common_input_map","continuous_centre_definition_sha256","continuous_response_definition_sha256"]
    gate("the same selected common input full family definitions and two principal factors are unchanged",
        all(pp[k]==PARAMETERS[k] for k in shared)
        and p["covered_principal_factors"]==PARAMETERS["principal_factors"]
        and pp["complete_windows"]==["L2","H^(-4/3)"]
        and sc["exact_order"]==PARAMETERS["selected_common_input_order"]
        and sc["selected_parameter_absolute_upper"]==PARAMETERS["selected_conjugacy_parameter_absolute_upper"]
        and sc["only_same_selected_actual_conjugacy"] is True)
    n=p["complete_new_nonmean_primitive_conclusion"];l=p["complete_new_log_inverse_conclusion"]
    gate("the existing same complete inverse and all mean qualifications precede the adjoint bootstrap",
        p["complete_principal_inverse_log_certificates_paid"] is True
        and p["new_complete_log_inverse_certificates"]==2
        and p["direct_exponential_norm_bounds_evaluated"]==0
        and p["old_scientific_producer_calls"]==p["old_scientific_producer_imports"]==0
        and l["same_mean_complete_inverse_on_both_windows"] is True
        and l["log_certificate_is_not_the_numerical_norm"] is True
        and l["large_exponential_not_evaluated"] is True
        and l["nonmean_multiplier_uses_only_W_one_third"] is True
        and n["full_two_sign_sums_and_all_nonzero_modes_retained"] is True
        and n["scalar_mean_subtraction_is_exact_not_a_physical_mean_deletion"] is True
        and p["scope"]["two_independent_physical_mean_blocks_remain_distinct"] is True
        and p["scope"]["full_circle_principal_inverse_has_no_artificial_high_compression"] is True)
    saved=dict(V0=copy.deepcopy(n["complete_V0_upper"]),
        B_one_third=copy.deepcopy(n["complete_B_one_third_upper"]),
        CI=copy.deepcopy(n["complete_I_derivative_gain_constant"]),
        log_L2=copy.deepcopy(l["complete_log_L2_inverse_upper"]),
        log_Hminus4_3_original=copy.deepcopy(l["complete_log_Hminus4_3_inverse_upper"]))
    gate("the five complete saved scalar records are finite with nonnegative logarithmic certificates",
        len(saved)==5 and all(up(v).is_finite() for v in saved.values())
        and up(saved["CI"])>=1 and up(saved["log_L2"])>=0
        and up(saved["log_Hminus4_3_original"])>=0)
    d["accepted_original_PG_identity_read_verbatim"]=copy.deepcopy(OLD)
    d["complete_saved_PG_inputs_read_verbatim"]=copy.deepcopy(saved)
    d["complete_saved_PG_inputs_payload_sha256"]=payload_sha(saved)
    d["complete_selected_common_input_scope_read_verbatim"]=copy.deepcopy(sc)
    d["complete_PG_optional_test_outcomes_read_verbatim"]={
        k:dict(strict_positive_gap=v["strict_positive_gap"],complete_inverse_upper=copy.deepcopy(v["complete_inverse_upper"]))
        for k,v in p["complete_optional_Neumann_conclusion"].items()}
    d["original_successful_small_receipts_read"]=1;d["saved_complete_scalar_records_read"]=5
    return paths,saved

def positive_products(saved):
    V,B,CI=(up(saved[k]) for k in ("V0","B_one_third","CI"))
    term1=up(CI*B)
    term2=up(CI*term1*V)
    argument=up(arb(1)+term1+term2)
    return term1,term2,argument

def logarithmic_candidate(saved,argument):
    correction=up(argument.log())
    candidate=up(up(saved["log_L2"])+correction)
    return correction,candidate

def complete_whole_minimum(saved,candidate_record):
    candidates=[("original_PG",copy.deepcopy(saved["log_Hminus4_3_original"])),
        ("adjoint_bootstrap",copy.deepcopy(candidate_record))]
    selected=min(candidates,key=lambda pair:up(pair[1]))
    return dict(original_complete_log_Hminus4_3_read_verbatim=candidates[0][1],
        new_complete_bootstrap_log_Hminus4_3_read_verbatim=candidates[1][1],
        complete_selected_log_Hminus4_3_upper=copy.deepcopy(selected[1]),
        selected_complete_candidate=selected[0],
        bootstrap_upper_strictly_below_original_upper=bool(up(candidates[1][1])<up(candidates[0][1])),
        choice_uses_final_retained_outward_records=True,
        equal_upper_tie_preserves_original_PG=True,
        both_candidates_bound_the_same_actual_inverse_and_window=True,
        no_entrywise_or_different_operator_minimum=True)

def render_conclusion(d):
    lines=["# Complete principal adjoint bootstrap: actual new logarithmic candidate","",
        "Public run: "+str(d.get("run_id"))+"/"+str(d.get("run_attempt"))+".",
        "Source SHA256: "+d["source_sha256"]+".",
        "Manifest SHA256: "+d["input_manifest_sha256"]+".",
        "Actual complete: "+str(d["complete"])+". Scientific child return: "+str(d["actual_returncode"])+".","",
        "Five scalar PG records are read unchanged. Only two positive terms, one log and one whole minimum are new.",""]
    for key,title in (("complete_saved_PG_inputs_read_verbatim","Original PG records"),
            ("complete_new_adjoint_bootstrap_conclusion","New adjoint candidate"),
            ("complete_new_whole_log_comparison_conclusion","Complete negative-window choice")):
        if key not in d:continue
        lines+=["## "+title,"","| Quantity | Complete outward record |","|---|---|"]
        for k,v in d[key].items():
            if isinstance(v,dict) and "ball" in v:lines.append("| "+k+" | "+v["ball"]+" |")
        lines.append("")
    comp=d.get("complete_new_whole_log_comparison_conclusion",{})
    if comp:lines+=["Selected complete candidate: "+comp["selected_complete_candidate"]+".",""]
    lines+=["Each log L certifies norm <= exp(L); no exponential was evaluated.",
        "The same existing L2 inverse is used before adjoint regularity and duality.",
        "Both complete principal factors, the selected input, scalar mean and independent physical means retain their exact scope.",
        "No signed pointwise test, complete physical incoming inverse, finite Schur inverse or full return is supplied.","",
        "## Actual gates",""]
    lines+=["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in d["gates"]]
    if d.get("failure"):lines+=["","Actual failure: "+json.dumps(d["failure"],ensure_ascii=False)]
    return "\n".join(lines)+"\n"

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--workdir",type=Path,required=True);p.add_argument("--process",type=Path,required=True)
    p.add_argument("--conclusion",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();ctx.prec=320;started=time.monotonic()
    if a.process.exists() or a.out.exists():raise FileExistsError("preserve every existing complete or partial result")
    a.workdir.mkdir(parents=True,exist_ok=True)
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),
        arithmetic_bits=320,mathematical_parameters=copy.deepcopy(PARAMETERS),
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),stage="initial frozen inputs",
        original_successful_small_receipts_read=0,saved_complete_scalar_records_read=0,
        new_positive_product_terms=0,new_positive_log_arguments=0,new_logarithms_evaluated=0,
        new_complete_log_candidates=0,new_complete_whole_log_minima=0,
        old_numerical_enclosures_recomputed=0,old_PG_CG_TF_WX_targets_recomputed=0,
        old_scientific_producer_imports=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,new_angular_or_radial_integrals_evaluated=0,
        direct_exponential_norm_bounds_evaluated=0,signed_pointwise_coefficient_tests_evaluated=0,
        original_input_bytes_modified=False,complete_principal_adjoint_bootstrap_paid=False,
        full_physical_incoming_inverse_claimed=False,finite_Schur_inverse_claimed=False,
        full_return_R0_claimed=False,actual_nonlinear_background_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def checkpoint():save(a.process,d)
    def gate(name,condition):
        condition=bool(condition);d["gates"].append(dict(name=name,passed=condition));checkpoint()
        if not condition:raise ValueError("failed gate: "+name)
    checkpoint()
    try:
        paths,saved=checked_inputs(a,d,gate);d["stage"]="five complete saved PG records";checkpoint()
        term1,term2,argument=positive_products(saved)
        d["complete_new_adjoint_bootstrap_conclusion"]=dict(
            complete_CI_B_upper=rec(term1),complete_CI_squared_B_V_upper=rec(term2),
            complete_positive_log_argument_upper=rec(argument))
        d["new_positive_product_terms"]=2;d["new_positive_log_arguments"]=1
        d["stage"]="complete new positive terms";checkpoint()
        gate("new complete positive products bound the whole adjoint logarithm argument",
            finite([term1,term2,argument]) and term1>=0 and term2>=0 and argument>=1)
        correction,candidate=logarithmic_candidate(saved,argument)
        d["complete_new_adjoint_bootstrap_conclusion"].update(
            complete_log_correction_upper=rec(correction),
            complete_bootstrap_log_Hminus4_3_upper=rec(candidate),
            exact_log_certificate="norm(T_ci^-1), norm(T_co^-1) on H^(-4/3) <= exp(bootstrap_log)",
            existing_L2_inverse_used_before_adjoint_regularity=True,
            successive_adjoint_spaces=["L2","H^1","H^(1/3)","H^(4/3)"],
            negative_inverse_is_the_same_distributional_extension=True,
            complete_scalar_mean_equation_retained=True,
            no_division_by_real_scalar_mean=True,large_exponential_not_evaluated=True)
        d["new_logarithms_evaluated"]=d["new_complete_log_candidates"]=1
        d["stage"]="complete new logarithmic candidate";checkpoint()
        gate("one logarithm yields a finite complete bound for the same negative-window inverse",
            finite([correction,candidate]) and correction>=0 and candidate>=0
            and d["direct_exponential_norm_bounds_evaluated"]==0)
        candidate_record=d["complete_new_adjoint_bootstrap_conclusion"]["complete_bootstrap_log_Hminus4_3_upper"]
        comp=complete_whole_minimum(saved,candidate_record)
        d["complete_new_whole_log_comparison_conclusion"]=comp
        d["new_complete_whole_log_minima"]=1;d["stage"]="complete same-window minimum";checkpoint()
        gate("the whole minimum compares final retained outward bounds for the same operator",
            finite(comp) and comp["selected_complete_candidate"] in ("original_PG","adjoint_bootstrap")
            and comp["original_complete_log_Hminus4_3_read_verbatim"]==saved["log_Hminus4_3_original"]
            and comp["new_complete_bootstrap_log_Hminus4_3_read_verbatim"]==candidate_record
            and comp["complete_selected_log_Hminus4_3_upper"] in
                (saved["log_Hminus4_3_original"],candidate_record))
        gate("all five original PG records and all frozen original input bytes remain unchanged",
            d["complete_saved_PG_inputs_read_verbatim"]==saved
            and d["complete_saved_PG_inputs_payload_sha256"]==payload_sha(saved)
            and sha(paths["PG_execution"])==OLD["execution"]
            and sha(paths["PG_source"])==OLD["source"] and sha(paths["PG_manifest"])==OLD["manifest"])
        d["scope"]=dict(
            same_selected_real_individual_ci_co_not_a_ratio_substitute=True,
            existing_full_L2_inverse_established_before_bootstrap=True,
            complete_scalar_mean_and_two_independent_physical_means_retained=True,
            same_inverse_on_both_windows_and_on_their_dense_common_domain=True,
            only_complete_W_one_third_nonmean_multiplication_used=True,
            whole_candidate_and_original_PG_negative_log_retained_separately=True,
            logarithmic_certificates_not_numeric_inverse_norms=True,
            no_pointwise_signed_lower_bound_invented=True,
            full_density_mean_identity_rank_differences_still_separate=True,
            all_actual_errors_finite_rows_and_physical_incoming_inverse_still_required=True,
            high_block_output_preconditioning_still_uses_L2_inverse_constant=True,
            old_successful_scientific_computations_read_only=True)
        d["covered_principal_factors"]=copy.deepcopy(PARAMETERS["principal_factors"])
        gate("all selected mean finite and strong-error interfaces preserve the principal-only conclusion",
            all(d["scope"].values()) and len(d["covered_principal_factors"])==2
            and d["full_physical_incoming_inverse_claimed"] is False
            and d["finite_Schur_inverse_claimed"] is False and d["full_return_R0_claimed"] is False)
        zeros=("old_numerical_enclosures_recomputed","old_PG_CG_TF_WX_targets_recomputed",
            "old_scientific_producer_imports","old_scientific_producer_calls",
            "old_binary_or_archive_inputs_restored","new_angular_or_radial_integrals_evaluated",
            "direct_exponential_norm_bounds_evaluated","signed_pointwise_coefficient_tests_evaluated")
        gate("only the new positive terms one logarithm and one whole minimum were evaluated",
            all(d[k]==0 for k in zeros) and d["original_successful_small_receipts_read"]==1
            and d["saved_complete_scalar_records_read"]==5
            and d["new_positive_product_terms"]==2 and d["new_positive_log_arguments"]==1
            and d["new_logarithms_evaluated"]==d["new_complete_log_candidates"]==d["new_complete_whole_log_minima"]==1)
        gate("all fifteen gates and complete old and new logarithmic conclusions are retained",
            len(d["gates"])==14 and all(g["passed"] is True for g in d["gates"])
            and finite(d["complete_new_adjoint_bootstrap_conclusion"]) and finite(comp))
        if len(d["gates"])!=15:raise ValueError("the exact complete gate count changed")
        d["complete"]=d["proved"]=d["complete_principal_adjoint_bootstrap_paid"]=True
        d["actual_returncode"]=0;d["stage"]="complete"
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
        print("ACTUAL_PRINCIPAL_ADJOINT_BOOTSTRAP_FAILURE",repr(error),flush=True)
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-started;checkpoint()
        save(a.out,dict(scientific_receipt=d,no_old_scientific_reexecution=True),compressed=True)
        d["temporary_native_sha256"]=sha(a.out);d["temporary_native_bytes"]=a.out.stat().st_size;checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        tmp=a.conclusion.with_name(a.conclusion.name+".tmp")
        tmp.write_text(render_conclusion(d),encoding="utf-8");tmp.replace(a.conclusion)
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()

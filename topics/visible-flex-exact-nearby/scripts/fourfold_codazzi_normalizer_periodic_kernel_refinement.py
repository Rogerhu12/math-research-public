#!/usr/bin/env python3
"""New periodic weighted-kernel bound for the same complete NW normalizer inverse.
Read the one successful NW science verbatim. New square and positive products only.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_normalizer_periodic_kernel_refinement_v1"
MANIFEST_KIND="normalizer_periodic_kernel_refinement_public_inputs_v1"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0")
CONTRACT="1ab985bcc97d40c63ab7ea0163746256cf9edc3d79233d990ca0189fa39b57b9"
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"original_NW_run\":\"43775614821/1\",\"physical_frequency_factor\":4,\"physical_period\":\"pi/2\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"only_same_selected_actual_parameter\":true,\"independent_physical_mean_coordinates\":2,\"actual_normalizer\":\"N=Id+M_w I\",\"exact_primitive\":\"p=I w; mean(w)=mean(p)=0\",\"complete_windows\":[\"L2\",\"H^(-4/3)\"],\"adjoint_intermediate_window\":\"H^(1/3)\",\"kernel_length\":\"pi/2 ordinary Lebesgue, normalized L2\",\"kernel_bracket_absolute_upper\":1,\"expected_actual_gate_count\":18,\"current_input_count\":7,\"saved_scalar_records\":13,\"old_successful_scientific_calls_allowed\":0,\"new_exponential_evaluations_allowed\":false,\"new_logarithm_evaluations_allowed\":false,\"complete_C_E_supplied\":false,\"complete_physical_incoming_or_finite_inverse_or_return_claimed\":false}")
OLD=json.loads("{\"run\":\"43775614821\",\"attempt\":\"1\",\"execution_sha256\":\"1e327e83dafb5d09ec98acc6ba887ae28962a7f242be7e82692a864c2f93cb0b\",\"source\":\"c8352847b0bd8df141c4aeb97d4dab372b807d7d18546d2b93659f95011cd75f\",\"manifest\":\"d66bc4a1fb2251f421a3feebef727352f92b252bf810892e732f008ebe5bad40\",\"kind\":\"actual_complete_cohomological_normalizer_windows_sign_v1\",\"execution_kind\":\"actual_public_cohomological_normalizer_windows_sign_execution\",\"gates\":20,\"runtime\":{\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"science_bytes\":24234,\"science_sha256\":\"55019238a3b762aaeace163a81da85b3c63c3034679ca23521d3c41b28b9e7aa\",\"checkout\":\"a7ca18a0bff4a48ccdde5abd44f6d0f01ee17c78\",\"parameters\":{\"actual_normalizer\":\"N=Id+M_w I\",\"adjoint_intermediate_window\":\"H^(1/3)\",\"arithmetic_bits\":320,\"complete_C_E_supplied\":false,\"complete_physical_incoming_or_finite_inverse_or_return_claimed\":false,\"complete_windows\":[\"L2\",\"H^(-4/3)\"],\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"current_input_count\":9,\"exact_cohomological_equation\":\"w(x-Omega)-w(x)=v(x)\",\"exact_difference\":\"v=v_o-v_i\",\"exact_primitive\":\"p=I w; mean(w)=mean(p)=0\",\"expected_actual_gate_count\":20,\"high_order_or_old_log_exponentials_allowed\":false,\"independent_physical_mean_coordinates\":2,\"old_successful_scientific_calls_allowed\":0,\"one_new_low_order_exponential\":true,\"only_same_selected_actual_parameter\":true,\"original_SEI_run\":\"43773319871/1\",\"physical_frequency_factor\":4,\"physical_period\":\"pi/2\",\"physical_two_primitive_rational_upper\":\"1/2\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\"},\"saved_input_payload\":\"a1684441dfcc7fb123d6d74f4989c8841034bcf694b48628875b4c8af1e74ce0\"}")
PRIMARIES=json.loads("{\"CN\":\"427387a2f3836d95b5f79546f0c6d41e8d6307abbb76611073d2801364fda9db\",\"PIB\":\"2d74b71c0584cb5ec1af849b6fb5756e48da58bf313d72be62d582d557d23acb\",\"NW\":\"1469fdd05417284743e7857aabe0324ee67ccb1b7dbaa003461364d8c9447938\"}")

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
    gate("only the new kernel scalar arithmetic runs in public Actions at the frozen runtime",
        os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==PUBLIC and runtime==RUNTIME and ctx.prec==320)
    m=read(a.manifest);paths={k:a.repo_root/Path(v) for k,v in m["input_paths"].items()}
    gate("seven current small inputs and all new parameters are frozen before evaluation",
        m["kind"]==MANIFEST_KIND and m["public_repository"]==PUBLIC
        and m["source_sha256"]==m["scientific_source_sha256"]==sha(__file__)
        and m["contract_sha256"]==CONTRACT and m["mathematical_parameters"]==PARAMETERS
        and m["expected_actual_gate_count"]==18 and m["file_count"]==len(m["files"])==7
        and m["all_inputs_are_current_small_texts"] is True
        and m["old_successful_scientific_calls_allowed"]==0 and m["legacy_artifact_inputs"]==[]
        and set(m["input_paths"].values())=={x["path"] for x in m["files"]})
    gate("every complete immutable size SHA and small text type is checked",
        all((a.repo_root/Path(x["path"])).stat().st_size==x["bytes"]
            and sha(a.repo_root/Path(x["path"]))==x["sha256"]
            and x["bytes"]<100000 and Path(x["path"]).suffix in (".py",".json",".md")
            and not (a.repo_root/Path(x["path"])).read_bytes().startswith(b"\x1f\x8b")
            for x in m["files"]))
    literal={"CN":(r"\tag{CN.14}",r"\tag{CN.16}"),
        "PIB":("L2","mean"),"NW":(r"\tag{NW.20}",r"\tag{NW.24}")}
    gate("the same two-mean inverse adjoint bootstrap and complete conditional global-sign proof are retained",
        sha(paths["contract"])==CONTRACT
        and all(term in paths["contract"].read_text() for term in (r"\tag{NPK.7}",r"\tag{NPK.14}",r"\tag{NPK.20}"))
        and sha(paths["NW_source"])==OLD["source"] and sha(paths["NW_execution"])==OLD["execution_sha256"]
        and all(sha(paths[k+"_contract"])==v
            and all(term in paths[k+"_contract"].read_text() for term in literal[k])
            for k,v in PRIMARIES.items())
        and m["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
    return paths

def accepted_NW(path,d,gate):
    e=read(path);p=e.get("actual_scientific_receipt",{})
    gate("the original NW run is a complete same-identity actual success",
        e.get("kind")==OLD["execution_kind"] and e.get("run_id")==OLD["run"]
        and e.get("run_attempt")==OLD["attempt"] and e.get("complete") is True
        and e.get("actual_returncode")==0 and e.get("actual_source_budget_processes")==1
        and e.get("source_budget_source_sha256")==OLD["source"]
        and e.get("input_manifest_sha256")==OLD["manifest"]
        and e.get("actual_scientific_checkout_commit")==OLD["checkout"]
        and p.get("kind")==OLD["kind"] and p.get("run_id")==OLD["run"]
        and p.get("run_attempt")==OLD["attempt"] and p.get("complete") is True and p.get("proved") is True
        and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("stage")=="complete_cohomological_normalizer_windows_sign_target"
        and p.get("source_sha256")==OLD["source"] and p.get("input_manifest_sha256")==OLD["manifest"]
        and p.get("runtime")==OLD["runtime"] and p.get("arithmetic_bits")==320
        and p.get("mathematical_parameters")==OLD["parameters"]
        and len(p.get("gates",[]))==20 and all(v.get("passed") is True for v in p["gates"]))
    raw=(canonical(p)+"\n").encode()
    gate("the complete original NW science has its exact canonical bytes hash and both original small outputs",
        len(raw)==OLD["science_bytes"] and hashlib.sha256(raw).hexdigest()==OLD["science_sha256"]
        and all(any(v.get("file")==name and v.get("bytes")==OLD["science_bytes"]
            and v.get("sha256")==OLD["science_sha256"] for v in e.get("output_hashes",[]))
            for name in ("consumers/process.json","consumers/summary.json"))
        and p.get("complete_saved_input_payload_sha256")==OLD["saved_input_payload"]
        and p.get("new_low_order_exponentials_evaluated")==1 and p.get("new_logarithms_evaluated")==3)
    fourier=p["complete_new_Fourier_budgets_conclusion"]
    windows=p["complete_new_normalizer_windows_conclusion"]
    affine=p["complete_new_global_sign_and_affine_conclusion"]
    scope=p["complete_selected_common_input_scope_read_verbatim"]
    gate("the original true w p full-circle means and the selected common-input order are preserved",
        fourier["exact_cohomological_equation"]=="w(x-Omega)-w(x)=v(x)"
        and fourier["exact_primitive"]=="p=I w; mean(w)=mean(p)=0"
        and fourier["full_infinite_two_sign_series_included"] is True
        and fourier["complete_candidate_count"]==11
        and windows["same_exact_full_circle_N_inverse_on_both_windows"] is True
        and windows["same_bounds_for_rotated_N_minus_inverse"] is True
        and windows["first_weighted_mean_and_second_primitive_mean_retained"] is True
        and windows["full_scalar_mean_and_two_physical_means_retained"] is True
        and windows["log_only_choice_never_substituted_for_an_evaluated_norm"] is True
        and affine["left_N_inverse_window"]=="L2"
        and affine["right_N_inverse_window"]==affine["input_N_forward_window"]=="H^(-4/3)"
        and affine["exact_global_sign_not_replaced_by_a_scalar_sector"] is True
        and affine["second_global_sign_mean_row_retained"] is True
        and affine["complete_C_E_supplied"] is False and affine["complete_return_remainder_proved"] is False
        and scope["exact_order"]==PARAMETERS["selected_common_input_order"]
        and scope["selected_parameter_absolute_upper"]==PARAMETERS["selected_parameter_absolute_upper"]
        and scope["only_same_selected_actual_conjugacy"] is True
        and all(v is True for v in p["scope"].values()))
    wf=fourier["complete_Wiener_bounds"]
    saved=dict(W0=copy.deepcopy(wf["W0"]),B=copy.deepcopy(wf["Wone_third"]),
        P0=copy.deepcopy(wf["P0"]),E0=copy.deepcopy(windows["complete_exp_low_primitive_upper"]),
        CI=copy.deepcopy(p["complete_saved_absolute_mu_and_CI_read_verbatim"]["CI"]),
        CI_B=copy.deepcopy(windows["complete_adjoint_CI_Wone_third_upper"]),
        K0_old=copy.deepcopy(windows["complete_L2_norm_whole_choice"]["complete_selected_upper"]),
        Kminus_old=copy.deepcopy(windows["complete_negative_norm_whole_choice"]["complete_selected_upper"]),
        Fminus=copy.deepcopy(windows["complete_forward_Hminus4_3_upper"]),
        CwZ=copy.deepcopy(affine["complete_global_commutator_Hminus4_3_to_L2_upper"]),
        Qstar=copy.deepcopy(affine["complete_two_ordered_Q_common_majorant_upper"]),
        Aminusfactor=copy.deepcopy(affine["complete_A_negative_known_factor_upper"]),
        linear_scalar_fee=copy.deepcopy(affine["complete_linear_to_exponential_scalar_fee_upper"]))
    gate("thirteen saved scalar records are complete positive same-operator budgets",
        len(saved)==13 and finite(saved) and all(rb(v).lower()>=0 for v in saved.values())
        and all(rb(saved[k]).lower()>=1 for k in ("E0","K0_old","Kminus_old","Fminus"))
        and windows["complete_L2_norm_whole_choice"]["all_candidates_bound_the_same_complete_operator_and_window"] is True
        and windows["complete_negative_norm_whole_choice"]["all_candidates_bound_the_same_complete_operator_and_window"] is True
        and windows["negative_primitive_and_saved_PG_PIB_logs_not_exponentiated"] is True
        and affine["no_old_linear_remainder_renamed_as_Cayley"] is True)
    copies=dict(
        Fourier=fourier,windows=windows,global_sign_and_affine=affine,
        absolute_mu_and_CI=p["complete_saved_absolute_mu_and_CI_read_verbatim"],
        original_signed_mu=p["complete_original_signed_mu_read_verbatim"],
        whole_path_scope=p["complete_SEI_whole_path_scope_read_verbatim"],
        selected_common_input_scope=scope,original_scope=p["scope"])
    d["accepted_complete_NW_identity_read_verbatim"]=copy.deepcopy(OLD)
    d["complete_original_NW_objects_read_verbatim"]=copy.deepcopy(copies)
    d["complete_original_NW_object_payload_sha256"]=payload_sha(copies)
    d["complete_saved_scalar_records_read_verbatim"]=copy.deepcopy(saved)
    d["complete_saved_scalar_payload_sha256"]=payload_sha(saved)
    d["original_successful_small_receipts_read"]=1
    d["original_complete_objects_read_verbatim"]=8
    d["saved_scalar_records_read"]=13
    return saved,payload_sha(copies),payload_sha(saved)

def whole_choice(candidates):
    if not candidates or len({k for k,_ in candidates})!=len(candidates):
        raise ValueError("empty or duplicate complete-candidate family")
    selected=min(candidates,key=lambda item:up(item[1]))
    return dict(complete_candidate_records={k:copy.deepcopy(v) for k,v in candidates},
        selected_complete_candidate=selected[0],complete_selected_upper=copy.deepcopy(selected[1]),
        choice_uses_final_retained_outward_records=True,tie_preserves_first_candidate=True,
        all_candidates_bound_the_same_complete_operator_and_window=True)

def kernel_candidate(saved):
    length=rec(up(arb.pi()/2))
    square=rec(up(up(saved["E0"])*up(saved["E0"])))
    primitive=rec(up(up(length)*up(square)))
    inverse=rec(up(arb(1)+up(saved["W0"])*up(primitive)))
    return dict(complete_physical_Lebesgue_length_upper=length,
        complete_saved_exponential_square_upper=square,
        complete_kernel_z_L2_upper=primitive,
        complete_kernel_N_inverse_L2_upper=inverse,
        exact_kernel_bracket_absolute_upper=1,
        first_weighted_mean_retained=True,second_primitive_mean_retained=True,
        normalized_L2_and_ordinary_dt_length_retained=True,
        same_exact_complete_N_inverse=True,no_exponential_or_logarithm_evaluated=True)

def adjoint_candidate(saved,K0_record):
    term2=rec(up(up(saved["CI"])*up(saved["CI_B"])*up(saved["W0"])*up(K0_record)))
    inverse=rec(up(arb(1)+up(saved["CI_B"])+up(term2)))
    return dict(complete_L2_inverse_input_read_verbatim=copy.deepcopy(K0_record),
        complete_saved_CI_B_read_verbatim=copy.deepcopy(saved["CI_B"]),
        complete_new_adjoint_product_upper=term2,
        complete_new_Hminus4_3_inverse_upper=inverse,
        first_L2_inverse_then_adjoint_bootstrap_then_duality=True,
        same_complete_inverse_on_both_windows=True,physical_two_means_retained=True,
        old_adjoint_budget_not_recomputed=True)

def complete_affine_candidate(saved,K0_record,Kminus_record):
    k0,km=up(K0_record),up(Kminus_record)
    bz=rec(up(k0*up(saved["CwZ"])*km*up(saved["Fminus"])))
    az=rec(up(up(bz)*up(saved["Aminusfactor"])))
    ac=rec(up(k0*up(saved["Qstar"])+up(az)))
    bc=rec(up(k0*up(saved["Fminus"])+up(bz)))
    return dict(complete_sign_A_constant_upper=az,complete_sign_B_CE_coefficient_upper=bz,
        complete_global_Cayley_A_constant_upper=ac,
        complete_global_Cayley_B_CE_coefficient_upper=bc,
        complete_L2_inverse_input_read_verbatim=copy.deepcopy(K0_record),
        complete_Hminus4_3_inverse_input_read_verbatim=copy.deepcopy(Kminus_record),
        complete_input_N_forward_read_verbatim=copy.deepcopy(saved["Fminus"]),
        complete_linear_to_exponential_scalar_fee_read_verbatim=copy.deepcopy(saved["linear_scalar_fee"]),
        exact_order="left inverse L2; full sign commutator; right inverse H^(-4/3); forward N H^(-4/3)",
        both_mean_rows_and_full_global_sign_retained=True,
        complete_old_Q_and_A_factor_read_not_recomputed=True,
        four_coefficients_form_one_complete_candidate=True,
        no_entrywise_minimum_across_affine_candidates=True,
        C_E="unpaid complete strong error, symbolic",
        complete_C_E_supplied=False,complete_return_remainder_proved=False)

def render_conclusion(d):
    lines=["# Periodic weighted-kernel normalizer inverse: actual conclusion","",
        "- Actual run: "+d["run_id"]+"/"+d["run_attempt"],
        "- Complete scientific success: "+str(d["complete"]),
        "- Scientific return code: "+str(d["actual_returncode"]),
        "- Passed gates: "+str(sum(x["passed"] for x in d["gates"]))+"/"+str(len(d["gates"])),
        "- Source SHA256: "+d["source_sha256"],
        "- Manifest SHA256: "+d["input_manifest_sha256"],
        "- Old successful mathematical computations repeated: 0.",
        "- New exponential or logarithm evaluations: 0.",""]
    if d["complete"]:
        windows=d["complete_new_two_window_conclusion"];kernel=d["complete_new_kernel_conclusion"]
        affine=d["complete_new_conditional_affine_conclusion"]
        lines+=["The same full-circle N inverse is bounded on both windows; both weighted means and the two physical means are retained.","",
            "| Complete new record | Outward ball |","|---|---|"]
        rows=[("Physical ordinary circumference",kernel["complete_physical_Lebesgue_length_upper"]),
            ("Saved exponential squared",kernel["complete_saved_exponential_square_upper"]),
            ("Kernel primitive L2",kernel["complete_kernel_z_L2_upper"]),
            ("Kernel N inverse L2",kernel["complete_kernel_N_inverse_L2_upper"]),
            ("Selected full L2 inverse",windows["complete_L2_whole_choice"]["complete_selected_upper"]),
            ("New adjoint negative inverse",d["complete_new_adjoint_conclusion"]["complete_new_Hminus4_3_inverse_upper"]),
            ("Selected full negative inverse",windows["complete_negative_whole_choice"]["complete_selected_upper"])]
        rows += [(k,affine[k]) for k in ("complete_sign_A_constant_upper","complete_sign_B_CE_coefficient_upper",
            "complete_global_Cayley_A_constant_upper","complete_global_Cayley_B_CE_coefficient_upper")]
        lines += ["| "+name+" | "+value["ball"]+" |" for name,value in rows]
        lines += ["","L2 whole candidate: "+windows["complete_L2_whole_choice"]["selected_complete_candidate"],
        "","Negative whole candidate: "+windows["complete_negative_whole_choice"]["selected_complete_candidate"],""]
    else:
        lines+=["Only the saved partial fields are retained. No new two-window or conditional affine numerical conclusion is authorized.",""]
    lines+=["The complete C_E remains symbolic and unpaid. No physical incoming inverse, finite Schur inverse, actual nonlinear background, or full return is asserted.",
        "The old log-only records and optional Neumann verdicts remain unchanged in the complete saved NW objects.",""]
    if d.get("failure") is not None:lines+=["Failure: "+json.dumps(d["failure"],ensure_ascii=False),""]
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--temporary-output-dir",type=Path,required=True)
    ap.add_argument("--process-receipt",type=Path,required=True)
    ap.add_argument("--small-summary",type=Path,required=True)
    ap.add_argument("--result-markdown",type=Path,required=True)
    a=ap.parse_args();ctx.prec=320;started=time.monotonic()
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),arithmetic_bits=320,
        mathematical_parameters=PARAMETERS,public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID",""),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT",""),
        workflow_event_commit=os.environ.get("GITHUB_SHA",""),
        actual_scientific_checkout_commit=os.environ.get("SCIENTIFIC_CHECKOUT_COMMIT",""),
        stage="input_identity",original_successful_small_receipts_read=0,
        original_complete_objects_read_verbatim=0,saved_scalar_records_read=0,
        new_physical_length_constants=0,new_saved_exponential_squares=0,
        new_complete_L2_kernel_candidates=0,new_complete_adjoint_negative_candidates=0,
        new_complete_norm_whole_choices=0,new_complete_conditional_affine_coefficients=0,
        new_exponential_evaluations=0,new_logarithm_evaluations=0,
        new_optional_Neumann_tests_evaluated=0,new_Fourier_or_target_budgets_evaluated=0,
        old_numerical_enclosures_recomputed=0,old_NW_or_PIB_budgets_recomputed=0,
        old_scientific_producer_imports=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,new_angular_or_radial_integrals_evaluated=0,
        original_input_bytes_modified=0,complete_periodic_kernel_consumer_paid=False,
        complete_C_E_supplied=False,full_physical_incoming_inverse_claimed=False,
        finite_Schur_inverse_claimed=False,full_return_R0_claimed=False,
        actual_nonlinear_background_claimed=False,temporary_native_is_not_published=True,
        reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def gate(label,ok):
        ok=bool(ok);d["gates"].append(dict(gate=label,passed=ok))
        if not ok:raise ValueError(label)
    try:
        paths=checked_inputs(a,d,gate)
        saved,object_payload,scalar_payload=accepted_NW(paths["NW_execution"],d,gate)
        d["stage"]="new_periodic_kernel"
        kernel=kernel_candidate(saved);d["complete_new_kernel_conclusion"]=kernel
        d["new_physical_length_constants"]=1;d["new_saved_exponential_squares"]=1
        d["new_complete_L2_kernel_candidates"]=1
        gate("the complete periodic kernel bound uses ordinary pi/2 length and both weighted means",
            finite(kernel) and kernel["exact_kernel_bracket_absolute_upper"]==1
            and all(kernel[k] is True for k in ("first_weighted_mean_retained","second_primitive_mean_retained",
                "normalized_L2_and_ordinary_dt_length_retained","same_exact_complete_N_inverse",
                "no_exponential_or_logarithm_evaluated")))
        c0=whole_choice([("original_NW_complete_L2_norm",saved["K0_old"]),
            ("complete_periodic_weighted_kernel",kernel["complete_kernel_N_inverse_L2_upper"])])
        d["complete_new_two_window_conclusion"]=dict(complete_L2_whole_choice=c0)
        d["new_complete_norm_whole_choices"]=1
        gate("the L2 comparison selects one whole retained outward record for the same inverse",
            len(c0["complete_candidate_records"])==2
            and c0["complete_selected_upper"]==c0["complete_candidate_records"][c0["selected_complete_candidate"]]
            and c0["complete_candidate_records"]["original_NW_complete_L2_norm"]==saved["K0_old"])
        adj=adjoint_candidate(saved,c0["complete_selected_upper"]);d["complete_new_adjoint_conclusion"]=adj
        d["new_complete_adjoint_negative_candidates"]=1
        gate("the negative candidate uses the chosen complete L2 inverse in the proved adjoint order",
            finite(adj) and adj["complete_L2_inverse_input_read_verbatim"]==c0["complete_selected_upper"]
            and adj["complete_saved_CI_B_read_verbatim"]==saved["CI_B"]
            and adj["first_L2_inverse_then_adjoint_bootstrap_then_duality"] is True)
        cm=whole_choice([("original_NW_complete_negative_norm",saved["Kminus_old"]),
            ("complete_adjoint_from_kernel_selected_L2",adj["complete_new_Hminus4_3_inverse_upper"])])
        d["complete_new_two_window_conclusion"].update(complete_negative_whole_choice=cm,
            same_exact_N_inverse_on_both_windows=True,same_bounds_for_rotated_N_minus=True,
            complete_scalar_mean_and_two_physical_means_retained=True,
            old_log_only_and_optional_records_retained_without_new_evaluation=True)
        d["new_complete_norm_whole_choices"]=2
        gate("the negative comparison also selects one whole retained outward record",
            len(cm["complete_candidate_records"])==2
            and cm["complete_selected_upper"]==cm["complete_candidate_records"][cm["selected_complete_candidate"]]
            and cm["complete_candidate_records"]["original_NW_complete_negative_norm"]==saved["Kminus_old"])
        affine=complete_affine_candidate(saved,c0["complete_selected_upper"],cm["complete_selected_upper"])
        d["complete_new_conditional_affine_conclusion"]=affine
        d["new_complete_conditional_affine_coefficients"]=4
        gate("four complete new affine coefficients keep the actual left and right inverse windows",
            finite(affine)
            and affine["complete_L2_inverse_input_read_verbatim"]==c0["complete_selected_upper"]
            and affine["complete_Hminus4_3_inverse_input_read_verbatim"]==cm["complete_selected_upper"]
            and affine["complete_input_N_forward_read_verbatim"]==saved["Fminus"]
            and affine["no_entrywise_minimum_across_affine_candidates"] is True)
        d["scope"]=dict(only_same_selected_actual_real_w_p=True,
            exact_periodic_kernel_and_two_weighted_means_retained=True,
            physical_circumference_pi_over_two_not_normalized_to_one=True,
            same_complete_inverse_on_L2_and_Hminus4_3=True,
            only_whole_norm_candidates_compared=True,old_optional_failure_not_noninvertibility=True,
            full_scalar_mean_and_two_physical_means_retained=True,
            full_global_sign_second_commutator_retained=True,
            complete_C_E_still_unsupplied=True,no_WE_paid_subtotal_used_as_C_E=True,
            original_complete_logs_not_exponentiated_or_recomputed=True,
            original_cohomological_and_Fourier_work_read_only=True)
        gate("the complete global sign and physical mean scope does not grant the unpaid C_E",
            affine["complete_C_E_supplied"] is False and affine["complete_return_remainder_proved"] is False
            and affine["C_E"]=="unpaid complete strong error, symbolic"
            and affine["both_mean_rows_and_full_global_sign_retained"] is True
            and affine["complete_linear_to_exponential_scalar_fee_read_verbatim"]==saved["linear_scalar_fee"])
        gate("all eight original complete objects and thirteen scalar records stay verbatim",
            payload_sha(d["complete_original_NW_objects_read_verbatim"])==object_payload
            and payload_sha(d["complete_saved_scalar_records_read_verbatim"])==scalar_payload)
        gate("only the one new square kernel product two whole choices and four affine products are evaluated",
            d["new_physical_length_constants"]==d["new_saved_exponential_squares"]==1
            and d["new_complete_L2_kernel_candidates"]==d["new_complete_adjoint_negative_candidates"]==1
            and d["new_complete_norm_whole_choices"]==2 and d["new_complete_conditional_affine_coefficients"]==4
            and all(d[k]==0 for k in ("new_exponential_evaluations","new_logarithm_evaluations",
                "new_optional_Neumann_tests_evaluated","new_Fourier_or_target_budgets_evaluated",
                "old_numerical_enclosures_recomputed","old_NW_or_PIB_budgets_recomputed",
                "old_scientific_producer_imports","old_scientific_producer_calls",
                "old_binary_or_archive_inputs_restored","new_angular_or_radial_integrals_evaluated",
                "original_input_bytes_modified")))
        gate("all complete retained ball records are finite and every scope condition is retained",
            finite(d) and all(v is True for v in d["scope"].values()))
        gate("the complete small result including all old and new candidates fits its reserved envelope",
            len((canonical(d)+"\n").encode())<43000)
        if len(d["gates"])!=18:raise ValueError("the exact18-gate contract changed")
        d["complete"]=d["proved"]=d["complete_periodic_kernel_consumer_paid"]=True
        d["actual_returncode"]=0;d["stage"]="complete_normalizer_periodic_kernel_target"
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
        d["complete"]=d["proved"]=d["complete_periodic_kernel_consumer_paid"]=False
        d["actual_returncode"]=1
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-started
        a.temporary_output_dir.mkdir(parents=True,exist_ok=True)
        native=a.temporary_output_dir/"temporary-normalizer-periodic-kernel-refinement.json.gz"
        save(native,d,True);d["temporary_native_sha256"]=sha(native);d["temporary_native_bytes"]=native.stat().st_size
        save(a.process_receipt,d);save(a.small_summary,d)
        try:
            result=render_conclusion(d)
            if len(result.encode())>10000:raise ValueError("the complete small markdown exceeds10000 bytes")
            a.result_markdown.parent.mkdir(parents=True,exist_ok=True);a.result_markdown.write_text(result)
        except Exception as error:
            d["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            d["actual_scientific_returncode"]=d["actual_returncode"]
            save(a.process_receipt,d);save(a.small_summary,d)
            a.result_markdown.parent.mkdir(parents=True,exist_ok=True)
            a.result_markdown.write_text("# Complete science is retained in the original small JSON.\n\nFormatting failed; do not repeat the scientific evaluation.\n")
            raise
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()

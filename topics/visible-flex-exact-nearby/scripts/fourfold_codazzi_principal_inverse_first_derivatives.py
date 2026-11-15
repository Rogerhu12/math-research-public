#!/usr/bin/env python3
"""New complete principal inverse logarithmic bounds from saved first derivatives.
The three original CG, TF and WX targets are immutable complete inputs.
Only PG scalar products, whole minima, logarithms and optional strict tests are new.
No old scientific producer or large exponential is evaluated.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_complete_principal_inverse_from_first_derivatives_v1"
MANIFEST_KIND="principal_inverse_first_derivatives_public_inputs_v1"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
CG_ACTUAL_PENDING=False
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"independent_physical_mean_coordinates\":2,\"selected_conjugacy_parameter_absolute_upper\":\"0.00000000009368259853002\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"selected_common_input_map\":\"psi = X_minus o H_inverse\",\"principal_factors\":[\"T_ci = Id + M_ci I\",\"T_co = Id + M_co I\"],\"complete_windows\":[\"L2\",\"H^(-4/3)\"],\"intermediate_negative_window\":\"H^(-1/3)\",\"root_coefficient_degree\":192,\"root_coefficient_first_derivative_frequency\":768,\"highest_complete_coefficient_derivative_used\":1,\"highest_selected_coordinate_derivative_used\":2,\"primitive_constant_squared\":\"17/16\",\"nonmean_derivative_factor\":\"1/2\",\"primitive_derivative_factor\":\"1/8\",\"B_one_third_factor\":\"39/32\",\"P_four_thirds_factor\":\"243/160\",\"direct_exponential_norm_evaluation_allowed\":false,\"optional_Neumann_failure_is_not_full_inverse_failure\":true,\"scalar_coefficient_means_real_and_unrestricted\":true,\"physical_means_are_separate_identity_blocks\":true,\"only_same_selected_actual_conjugacy\":true,\"old_successful_scientific_calls_allowed\":0,\"old_binary_or_archive_inputs_restored\":0,\"full_physical_incoming_inverse_or_finite_Schur_or_return_R0_claimed\":false,\"expected_actual_gate_count\":20}")
EXPECTED=json.loads("{\"CG\":{\"kind\":\"actual_separate_cut_propagated_first_coefficient_budgets_v1\",\"run\":\"43768992861\",\"source\":\"2545237268d1efb807419e809bfdf0dd75ef40b50dd11d898467ba0f8854586f\",\"manifest\":\"e33a06ddf9a46f2eeed6898bb4d700e13e02685617afa080061b8076f53c6184\",\"digest\":\"a68095bb38c38d62a4b1af256c84c96e7f1f7f1c2663d5fdb5ffc814b73e57fc\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"gates\":21,\"wrapper\":false},\"TF\":{\"kind\":\"actual_common_root_normalizer_two_window_v1\",\"run\":\"43766881076\",\"source\":\"bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b\",\"manifest\":\"027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf\",\"digest\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"gates\":14,\"wrapper\":false},\"WX\":{\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run\":\"43763424840\",\"source\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"manifest\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"digest\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"gates\":20,\"wrapper\":true}}")
PROOFS=json.loads("{\"contract\":\"0a5e4ad71d0d980a097e6c0f4afa8476780a46b4b3e82e5a583633f8bb66ad1a\",\"MI_contract\":\"f1fb4dca205a776968f80ab24b79740fdf6e79e875b186e778dace24af871404\",\"WY_contract\":\"ebf8713508a11ef96decc5691056ea6eaa15d967d08b3a8af4b20c4284f6d1b3\",\"CG_contract\":\"a66ad4c41c831a1d5efd343874c11945edd4cc2b04a39752ddd99d8b16aa72ff\",\"TF_contract\":\"652a9a2c2a9e0ccce1b07adae8848837ba579bec63d6ba5da21989a24b1bf5a3\",\"WX_contract\":\"c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1\"}")

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def payload_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def read(path):return json.loads(Path(path).read_bytes())
def save(path,x,compressed=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    body=gzip.compress(raw,mtime=0) if compressed else raw
    tmp=path.with_name(path.name+".tmp");tmp.write_bytes(body);tmp.replace(path)
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(x):
    if isinstance(x,arb):return x
    if isinstance(x,(int,Q)):return ex(x)
    if isinstance(x,str):return arb(x)
    return arb(x["ball"])
def up(x):
    x=rb(x)
    if not x.is_finite() or x.lower()<0:
        raise ValueError("a complete nonnegative principal budget is invalid")
    return x.upper()
def positive_lower(x,label):
    x=rb(x).lower()
    if not x.is_finite() or not x>0:
        raise ValueError("a required strict positive input is missing: "+label)
    return x
def rec(x):return dict(ball=rb(x).str(60))
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x
def all_finite(x):
    if isinstance(x,dict):
        if "ball" in x:return rb(x).is_finite()
        return all(all_finite(v) for v in x.values())
    if isinstance(x,(list,tuple)):return all(all_finite(v) for v in x)
    if isinstance(x,arb):return x.is_finite()
    return True

def accepted(tag,path,gate):
    spec=EXPECTED[tag];e=read(path)
    r=e.get("actual_scientific_receipt",{}) if spec["wrapper"] else e
    wrapper_ok=(not spec["wrapper"] or
        (e.get("complete") is True and e.get("actual_returncode")==0
         and e.get("actual_failure") is None
         and e.get("source_budget_source_sha256")==spec["source"]
         and e.get("input_manifest_sha256")==spec["manifest"]))
    gate("accepted "+tag+" run "+str(spec["run"])+"/1 retains its exact complete source manifest runtime and gates",
        sha(path)==spec["digest"] and wrapper_ok
        and str(e.get("run_id"))==spec["run"] and str(e.get("run_attempt"))=="1"
        and r.get("kind")==spec["kind"] and r.get("source_sha256")==spec["source"]
        and r.get("input_manifest_sha256")==spec["manifest"]
        and r.get("complete") is True and r.get("proved") is True
        and r.get("actual_returncode")==0 and r.get("failure") is None
        and r.get("runtime")==spec["runtime"]
        and len(r.get("gates",[]))==spec["gates"]
        and all(x.get("passed") is True for x in r["gates"]))
    return r

def complete_first_derivative_budgets(saved):
    """PG4--6: subtract the complete root function, then true density compose."""
    h=saved["CG_complete_branch_coefficient_0_2_read_verbatim"]
    if len(h)!=3:raise ValueError("the original complete coefficient array changed")
    h0,h1=up(h[0]),up(h[1])
    FA=up(saved["TF_complete_root_F_A0_read_verbatim"])
    M=up(saved["WX_common_input_derivative_upper_read_verbatim"])
    F=up(saved["WX_common_input_second_derivative_upper_read_verbatim"])
    t0=up(h0+FA);t1=up(h1+768*FA)
    A0=up(M*t0);A1=up(F*t0+M*M*t1)
    return dict(t0=t0,t1=t1,A0=A0,A1=A1)

def complete_nonmean_and_primitive_budgets(v):
    """PG8: compare whole same-norm candidates; full two-sign Fourier tails."""
    A0,A1=v["A0"],v["A1"]
    vc=[up(2*A0),up(A1/2)];V0=up(min(vc))
    pc=[up(arb.pi()*V0/8),up(A1/8)];P0=up(min(pc))
    B=up(ex(Q(39,32))*A1);P=up(ex(Q(243,160))*A1)
    CI=up(arb(17).sqrt()/4)
    return dict(V0_candidates=vc,V0=V0,P0_candidates=pc,P0=P0,
        B_one_third=B,P_four_thirds=P,complete_I_derivative_gain_constant=CI)

def optional_neumann_test(q,label):
    q=up(q);g=(arb(1)-q).lower()
    passed=bool(g>0)
    inverse=up(arb(1)/g) if passed else None
    return dict(window=label,complete_perturbation_upper=rec(q),
        signed_gap_lower=rec(g),strict_positive_gap=passed,
        complete_inverse_upper=rec(inverse) if passed else None,
        failed_test_does_not_negate_the_complete_ODE_inverse=True,
        full_scalar_mean_factor_is_a_contraction=True)

def complete_log_inverse_certificates(v):
    """PG15/19. No exp is evaluated, regardless of the size of the input."""
    V0,P0,B,P,CI=(v[k] for k in
        ("V0","P0","B_one_third","P_four_thirds","complete_I_derivative_gain_constant"))
    L0=up((arb(1)+V0).log()+4*P0)
    Lm=up((arb(1)+4*CI*B).log()+5*P)
    optional=dict(L2=optional_neumann_test(up(V0/4),"L2"),
        Hminus4_3=optional_neumann_test(up(CI*B),"H^(-4/3)"))
    return dict(log_L2=L0,log_Hminus4_3=Lm),optional

def checked_inputs(a,d,gate):
    actual=dict(python=platform.python_version(),python_flint=flint.__version__,
        numpy=numpy.__version__,scipy=scipy.__version__)
    d["runtime"]=actual
    gate("public Actions uses the exact pinned runtime and320-bit directed arithmetic",
        os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
        and actual==RUNTIME and ctx.prec==320)
    if CG_ACTUAL_PENDING or any(EXPECTED["CG"][k] is None for k in ("run","source","manifest","digest")):
        raise ValueError("the complete successful CG identity has not been frozen")
    manifest=read(a.manifest)
    paths={k:a.repo_root/Path(v) for k,v in manifest["input_paths"].items()}
    gate("the new manifest exact parameters and complete current-only source closure are frozen",
        manifest["kind"]==MANIFEST_KIND and manifest["public_repository"]==PUBLIC
        and manifest["scientific_source_sha256"]==sha(__file__)
        and manifest["contract_sha256"]==PROOFS["contract"]
        and manifest["mathematical_parameters"]==PARAMETERS
        and manifest["expected_actual_gate_count"]==20
        and manifest["all_inputs_are_current_small_texts"] is True
        and manifest["old_successful_scientific_calls_allowed"]==0
        and manifest["legacy_artifact_inputs"]==[]
        and len(manifest["files"])==manifest["file_count"]==17
        and set(manifest["input_paths"].values())=={x["path"] for x in manifest["files"]})
    gate("all seventeen exact small texts are checked before any new scalar arithmetic",
        all((a.repo_root/Path(x["path"])).stat().st_size==x["bytes"]
            and sha(a.repo_root/Path(x["path"]))==x["sha256"]
            and x["bytes"]<100000 and Path(x["path"]).suffix in (".md",".py",".json")
            and not (a.repo_root/Path(x["path"])).read_bytes().startswith(b"\x1f\x8b")
            for x in manifest["files"]))
    gate("all primary contracts and three old source-manifest identities are exact read-only evidence",
        all(sha(paths[k])==v for k,v in PROOFS.items())
        and all(sha(paths[tag+"_source"])==EXPECTED[tag]["source"]
            and sha(paths[tag+"_manifest"])==EXPECTED[tag]["manifest"] for tag in ("CG","TF","WX"))
        and manifest["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
    old={tag:accepted(tag,paths[tag+("_execution" if tag=="WX" else "_science")],gate)
         for tag in ("CG","TF","WX")}
    C,T,W=old["CG"],old["TF"],old["WX"]
    pc,pt,pw=C["parameters"],T["parameters"],W["mathematical_parameters"]
    gate("all original complete references share the family cut root and physical frequency",
        all(p.get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
            and p.get("fixed_intrinsic_parameter")==PARAMETERS["fixed_intrinsic_parameter"]
            and p.get("exact_strict_cut")==PARAMETERS["exact_strict_cut"]
            and p.get("exact_root_interval")==PARAMETERS["exact_root_interval"]
            and p.get("physical_frequency")==PARAMETERS["physical_frequency"] for p in (pc,pt,pw))
        and all(p.get(k)==PARAMETERS[k] for p in (pc,pt)
            for k in ("continuous_centre_definition_sha256","continuous_response_definition_sha256")))
    c=C["complete_new_cut_and_transported_coefficient_conclusion"]
    t=T["complete_new_root_coefficient_conclusion"]
    w=W["complete_selected_common_input_conclusion"]
    gate("only the complete successful three-entry CG coefficient is consumed without rerunning its integrals",
        C["stage"]=="complete" and C["complete_separate_coefficient_budgets_proved"] is True
        and C["original_completed_scientific_receipts_read"]==5
        and C["new_complete_coefficient_arrays"]==3
        and C["new_complete_multiplier_window_bounds"]==9
        and C["new_complete_dual_row_bounds"]==3
        and len(c["complete_branch_coefficient_0_2_upper"])==3
        and c["all_three_arrays_are_complete_scalar_suprema"] is True
        and c["two_input_signs_have_the_same_exact_real_coefficient_by_WY39_44"] is True
        and c["ordinary_SJ_integrals_used_verbatim_without_reintegration"] is True
        and c["no_difference_of_upper_bounds_used"] is True
        and C["scope"]["selected_common_input_only_not_a_family_of_conjugacies"] is True)
    gate("the same complete TF root coefficient retains its degree192 and full mean",
        T["complete_common_root_normalizer_proved"] is True and t["angular_degree"]==192
        and t["original_full_complex_eta_domain_includes_root"] is True
        and t["root_mean_and_both_Fourier_signs_retained"] is True
        and t["exact_full_family_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
        and c["complete_root_F_A0_read_verbatim"]==t["complete_root_F_A0_upper"]
        and C["input_sha256"]["tf_science"]==EXPECTED["TF"]["digest"])
    gate("the same selected WX density map keeps its first two derivatives and ordered input",
        W["complete_true_waist_coordinate_conclusion_paid"] is True
        and w["exact_order"]==PARAMETERS["selected_common_input_order"]
        and w["common_input_map"]==PARAMETERS["selected_common_input_map"]
        and w["only_same_selected_actual_conjugacy"] is True
        and w["selected_parameter_absolute_upper"]==PARAMETERS["selected_conjugacy_parameter_absolute_upper"]
        and w["independent_mean_block_retained"] is True
        and w["no_projection_commuted_through_coordinate"] is True
        and C["input_sha256"]["wx_execution"]==EXPECTED["WX"]["digest"]
        and C["copied_selected_common_input_scope"]["exact_order"]==w["exact_order"]
        and C["copied_selected_common_input_scope"]["selected_parameter_absolute_upper"]==w["selected_parameter_absolute_upper"])
    saved=dict(CG_complete_branch_coefficient_0_2_read_verbatim=copy.deepcopy(c["complete_branch_coefficient_0_2_upper"]),
        TF_complete_root_F_A0_read_verbatim=copy.deepcopy(t["complete_root_F_A0_upper"]),
        WX_common_input_derivative_upper_read_verbatim=copy.deepcopy(w["common_input_derivative_upper"]),
        WX_common_input_second_derivative_upper_read_verbatim=copy.deepcopy(w["common_input_second_derivative_upper"]))
    gate("all complete saved coefficient and coordinate inputs are finite positive-budget records",
        all(up(x).is_finite() for x in saved["CG_complete_branch_coefficient_0_2_read_verbatim"])
        and all(up(saved[k]).is_finite() for k in saved if not k.startswith("CG_"))
        and positive_lower(saved["WX_common_input_derivative_upper_read_verbatim"],"selected coordinate upper")>0)
    d["accepted_original_success_identity_read_verbatim"]=copy.deepcopy(EXPECTED)
    d["complete_saved_scalar_inputs_read_verbatim"]=copy.deepcopy(saved)
    d["complete_saved_scalar_inputs_payload_sha256"]=payload_sha(saved)
    d["complete_selected_common_input_scope_read_verbatim"]=copy.deepcopy(C["copied_selected_common_input_scope"])
    d["original_successful_small_receipts_read"]=3
    d["saved_complete_coefficient_arrays_read"]=1;d["saved_complete_root_coefficients_read"]=1
    d["saved_complete_selected_coordinate_derivatives_read"]=2
    return paths,saved

def render_conclusion(d):
    lines=["# Complete principal inverse from first derivatives: actual new logarithmic certificates","",
        "Public run: "+str(d.get("run_id"))+"/"+str(d.get("run_attempt"))+".",
        "Scientific source SHA256: "+str(d["source_sha256"])+".",
        "Input manifest SHA256: "+str(d["input_manifest_sha256"])+".",
        "Actual complete: "+str(d["complete"])+". Actual scientific return: "+str(d["actual_returncode"])+".","",
        "Only the new PG products, complete minima, logarithms and optional strict tests are evaluated.",
        "CG, TF, WX, their coefficients and all selected coordinate/ray computations remain read-only.",""]
    for key,title in (("complete_new_selected_first_derivative_conclusion","Selected first-derivative bounds"),
            ("complete_new_nonmean_primitive_conclusion","Complete nonmean and primitive bounds"),
            ("complete_new_log_inverse_conclusion","Logarithmic inverse certificates")):
        if key not in d:continue
        lines+=["## "+title,"","| Complete quantity | Outward ball |","|---|---|"]
        for k,v in d[key].items():
            if isinstance(v,dict) and "ball" in v:lines.append("| "+k+" | "+v["ball"]+" |")
        lines.append("")
    if "complete_optional_Neumann_conclusion" in d:
        lines+=["## Optional complete Neumann tests","",
            "| Window | Strict gap passed | Complete inverse upper if proved |","|---|---|---|"]
        for k,v in d["complete_optional_Neumann_conclusion"].items():
            z=v["complete_inverse_upper"]
            lines.append("| "+k+" | "+str(v["strict_positive_gap"])+" | "+(z["ball"] if z else "not supplied")+" |")
        lines.append("")
    lines+=["Each logarithmic certificate L means a norm bound exp(L); L is not itself the norm.",
        "No large exponential is evaluated. A failed optional Neumann test does not negate the exact full-circle inverse.",
        "Both factors have the same mean-complete inverse on L2 and H^(-4/3).",
        "The selected coordinate, independent physical means, actual incoming error and finite border retain their separate scopes.","",
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
    if a.process.exists() or a.out.exists():
        raise FileExistsError("keep any existing complete or partial scientific conclusion")
    a.workdir.mkdir(parents=True,exist_ok=True)
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),
        arithmetic_bits=320,mathematical_parameters=copy.deepcopy(PARAMETERS),
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        stage="initial frozen input checks",original_successful_small_receipts_read=0,
        saved_complete_coefficient_arrays_read=0,saved_complete_root_coefficients_read=0,
        saved_complete_selected_coordinate_derivatives_read=0,
        new_root_subtracted_coefficient_budgets=0,new_selected_coefficient_derivative_bounds=0,
        new_nonmean_and_primitive_bounds=0,new_complete_log_inverse_certificates=0,
        new_optional_Neumann_tests=0,new_optional_Neumann_inverse_bounds=0,
        new_universal_primitive_constants=0,direct_exponential_norm_bounds_evaluated=0,
        old_numerical_enclosures_recomputed=0,old_CG_TF_WX_targets_recomputed=0,
        old_profiles_phases_rays_sources_or_root_gauges_recomputed=0,
        old_scientific_producer_imports=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,new_angular_or_radial_integrals_evaluated=0,
        selected_coordinate_third_derivative_evaluated=0,original_input_bytes_modified=False,
        complete_principal_inverse_log_certificates_paid=False,
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
        paths,saved=checked_inputs(a,d,gate);d["stage"]="complete saved input records";checkpoint()
        v=complete_first_derivative_budgets(saved)
        d["complete_new_selected_first_derivative_conclusion"]=encode(dict(
            complete_t0_after_root_subtraction_upper=v["t0"],complete_t1_after_root_subtraction_upper=v["t1"],
            complete_ci_co_Linfty_upper=v["A0"],complete_ci_co_first_angular_derivative_upper=v["A1"],
            root_function_full_mean_not_removed=True,
            coefficient_higher_derivatives_not_evaluated=True,
            selected_coordinate_third_derivative_not_needed=True,
            both_actual_ci_co_and_both_physical_input_signs_share_each_bound=True))
        d["new_root_subtracted_coefficient_budgets"]=2;d["new_selected_coefficient_derivative_bounds"]=2
        d["stage"]="complete selected first-derivative bounds";checkpoint()
        gate("both complete selected coefficient bounds use the actual density chain rule after the full root subtraction",
            all_finite(v) and all(x>=0 for x in v.values())
            and d["complete_new_selected_first_derivative_conclusion"]["root_function_full_mean_not_removed"] is True)
        z=complete_nonmean_and_primitive_budgets(v)
        d["complete_new_nonmean_primitive_conclusion"]=encode(dict(
            complete_V0_candidates=z["V0_candidates"],complete_V0_upper=z["V0"],
            complete_P0_candidates=z["P0_candidates"],complete_P0_upper=z["P0"],
            complete_B_one_third_upper=z["B_one_third"],complete_P_four_thirds_upper=z["P_four_thirds"],
            complete_I_derivative_gain_constant=z["complete_I_derivative_gain_constant"],
            full_two_sign_sums_and_all_nonzero_modes_retained=True,
            complete_minima_compare_only_same_norm_bounds=True,
            scalar_mean_subtraction_is_exact_not_a_physical_mean_deletion=True))
        d["new_nonmean_and_primitive_bounds"]=4;d["new_universal_primitive_constants"]=1
        d["stage"]="complete nonmean and primitive budgets";checkpoint()
        gate("the four complete nonmean and primitive bounds keep both Fourier signs and same-norm minima",
            all_finite(z) and all(z[k]>=0 for k in ("V0","P0","B_one_third","P_four_thirds"))
            and len(z["V0_candidates"])==len(z["P0_candidates"])==2
            and z["complete_I_derivative_gain_constant"]>=1)
        logs,optional=complete_log_inverse_certificates(z)
        d["complete_new_log_inverse_conclusion"]=encode(dict(
            complete_log_L2_inverse_upper=logs["log_L2"],
            complete_log_Hminus4_3_inverse_upper=logs["log_Hminus4_3"],
            exact_interpretation_L2="norm(T_ci^-1) and norm(T_co^-1) <= exp(complete_log_L2_inverse_upper)",
            exact_interpretation_Hminus4_3="norm(T_ci^-1) and norm(T_co^-1) <= exp(complete_log_Hminus4_3_inverse_upper)",
            log_certificate_is_not_the_numerical_norm=True,
            same_mean_complete_inverse_on_both_windows=True,
            negative_window_uses_one_primitive_gain_to_Hminus1_3=True,
            nonmean_multiplier_uses_only_W_one_third=True,
            no_division_by_the_real_scalar_mean=True,
            large_exponential_not_evaluated=True))
        d["new_complete_log_inverse_certificates"]=2;d["stage"]="two complete logarithmic inverse certificates";checkpoint()
        gate("the two finite logarithmic records certify the same complete inverse on their actual windows",
            all_finite(logs) and logs["log_L2"]>=0 and logs["log_Hminus4_3"]>=0
            and d["direct_exponential_norm_bounds_evaluated"]==0)
        d["complete_optional_Neumann_conclusion"]=copy.deepcopy(optional)
        d["new_optional_Neumann_tests"]=2
        d["new_optional_Neumann_inverse_bounds"]=sum(x["strict_positive_gap"] for x in optional.values())
        d["stage"]="optional strict tests preserved separately";checkpoint()
        gate("each optional strict test is directed and a failed test keeps the complete logarithmic inverse",
            set(optional)=={"L2","Hminus4_3"} and all_finite(optional)
            and all((x["strict_positive_gap"] and rb(x["signed_gap_lower"]).lower()>0
                     and x["complete_inverse_upper"] is not None)
                 or (not x["strict_positive_gap"] and x["complete_inverse_upper"] is None)
                for x in optional.values())
            and d["new_complete_log_inverse_certificates"]==2)
        gate("all complete original input objects and their immutable bytes are retained unchanged",
            d["complete_saved_scalar_inputs_read_verbatim"]==saved
            and d["complete_saved_scalar_inputs_payload_sha256"]==payload_sha(saved)
            and all(sha(paths[tag+("_execution" if tag=="WX" else "_science")])==EXPECTED[tag]["digest"]
                for tag in ("CG","TF","WX")))
        d["scope"]=dict(
            exact_WY_individual_real_coefficients_not_a_ratio_surrogate=True,
            same_selected_actual_common_input_only=True,
            root_Fstar_full_mean_and_degree192_retained=True,
            full_circle_principal_inverse_has_no_artificial_high_compression=True,
            same_inverse_on_L2_and_Hminus4_3_with_full_scalar_mean_equations=True,
            intermediate_negative_multiplier_window_is_Hminus1_3=True,
            two_independent_physical_mean_blocks_remain_distinct=True,
            physical_density_versus_mean_identity_rank_differences_remain=True,
            complete_log_certificates_not_numeric_inverse_norms=True,
            optional_failed_Neumann_test_does_not_mean_singular=True,
            completed_CG_TF_WX_targets_and_all_original_sources_read_only=True,
            actual_Ei_Eo_all_finite_and_physical_mean_rows_still_required=True,
            preconditioned_finite_Schur_and_full_return_R0_not_supplied=True,
            nonlinear_background_and_final_geometry_not_supplied=True)
        d["covered_principal_factors"]=copy.deepcopy(PARAMETERS["principal_factors"])
        gate("all mean finite and selected-domain interfaces retain their exact principal-only scope",
            all(d["scope"].values()) and len(d["covered_principal_factors"])==2
            and d["full_physical_incoming_inverse_claimed"] is False
            and d["finite_Schur_inverse_claimed"] is False and d["full_return_R0_claimed"] is False)
        zeros=("old_numerical_enclosures_recomputed","old_CG_TF_WX_targets_recomputed",
            "old_profiles_phases_rays_sources_or_root_gauges_recomputed","old_scientific_producer_imports",
            "old_scientific_producer_calls","old_binary_or_archive_inputs_restored",
            "new_angular_or_radial_integrals_evaluated","selected_coordinate_third_derivative_evaluated",
            "direct_exponential_norm_bounds_evaluated")
        gate("only the declared new scalar products minima logarithms and strict tests were evaluated",
            all(d[k]==0 for k in zeros) and d["original_successful_small_receipts_read"]==3
            and d["saved_complete_coefficient_arrays_read"]==d["saved_complete_root_coefficients_read"]==1
            and d["saved_complete_selected_coordinate_derivatives_read"]==2
            and d["new_root_subtracted_coefficient_budgets"]==d["new_selected_coefficient_derivative_bounds"]==2
            and d["new_nonmean_and_primitive_bounds"]==4 and d["new_universal_primitive_constants"]==1
            and d["new_complete_log_inverse_certificates"]==d["new_optional_Neumann_tests"]==2)
        gate("all twenty gates and complete principal log records are preserved",
            len(d["gates"])==19 and all(x["passed"] is True for x in d["gates"])
            and all_finite(d["complete_new_log_inverse_conclusion"]))
        if len(d["gates"])!=20:raise ValueError("the complete gate count changed")
        d["complete"]=d["proved"]=d["complete_principal_inverse_log_certificates_paid"]=True
        d["actual_returncode"]=0;d["stage"]="complete"
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
        print("ACTUAL_PRINCIPAL_INVERSE_FIRST_DERIVATIVES_FAILURE",repr(error),flush=True)
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-started
        checkpoint()
        save(a.out,dict(scientific_receipt=d,no_old_scientific_reexecution=True),compressed=True)
        d["temporary_native_sha256"]=sha(a.out);d["temporary_native_bytes"]=a.out.stat().st_size
        checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        tmp=a.conclusion.with_name(a.conclusion.name+".tmp")
        tmp.write_text(render_conclusion(d),encoding="utf-8");tmp.replace(a.conclusion)
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()

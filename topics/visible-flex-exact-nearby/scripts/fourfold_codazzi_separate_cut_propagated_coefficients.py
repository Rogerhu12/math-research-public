#!/usr/bin/env python3
"""New separate cut/transported first-coefficient scalar budgets.
All five previous successful targets are read only. The complete SJ terminal
and the TF after-right factors are immutable inputs, not reevaluated targets.
No numerical producer, native array, ray, profile or radial integral is rerun.
"""
from __future__ import annotations
import argparse,copy,hashlib,importlib.metadata,json,os,platform,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
PRODUCER=TOPIC+"scripts/fourfold_codazzi_separate_cut_propagated_coefficients.py"
KIND="actual_separate_cut_propagated_first_coefficient_budgets_v1"
MANIFEST_KIND="separate_cut_propagated_first_coefficient_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=21
SJ_ACTUAL_PENDING=False
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"physical_frequency\":\"n=4|j|\",\"input_cutoff_abs_j\":97,\"physical_input_signs\":[-1,1],\"physical_waves\":[-1,1],\"independent_physical_means\":2,\"reference_column\":\"same terminal Ai free P8 first column\",\"complete_SJ_terminal_required\":true,\"coefficient_arrays_are_complete_scalar_suprema\":true,\"full_two_sign_Wiener_sums\":true,\"cut_leading_inverse\":\"KL saved common numerator divided by FA same-cut ng lower once\",\"root_right_factors\":\"TF saved after-right two-primitive and finite fees; only Cproj receives an additional KF\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"ordinary_radial_integrals_recomputed\":0,\"old_successful_producer_calls\":0,\"old_binary_or_archive_restored\":0,\"state_error_included\":false,\"full_incoming_finite_inverse_or_R0_claimed\":false,\"expected_gate_count\":21}")
PINNED=json.loads("{\"fa_science\":\"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2\",\"kl_science\":\"1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee\",\"wx_execution\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"tf_science\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"sj_execution\":\"2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88\",\"cg_contract\":\"a66ad4c41c831a1d5efd343874c11945edd4cc2b04a39752ddd99d8b16aa72ff\"}")
EXPECTED=json.loads("{\"fa_science\":{\"kind\":\"actual_complete_free_Airy_first_omitted_cut_scalars_v1\",\"run\":\"43763658978\",\"gates\":24,\"source\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"manifest\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\",\"runtime\":{\"Python\":\"3.12.14\",\"arithmetic_bits\":320,\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"kl_science\":{\"kind\":\"actual_correlated_terminal_Ai_leading_scalar_v1\",\"run\":\"43766439345\",\"gates\":16,\"source\":\"1f9dd122c7de8a990f5c60d0f405b2e3b3e51420b807ded9be58e8715fd480d6\",\"manifest\":\"810a13c2e1e0d3fb85f00129ca3e826e00e264d78269e25b78408bc1f67b99c7\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"wx_execution\":{\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run\":\"43763424840\",\"gates\":20,\"source\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"manifest\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"tf_science\":{\"kind\":\"actual_common_root_normalizer_two_window_v1\",\"run\":\"43766881076\",\"gates\":14,\"source\":\"bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b\",\"manifest\":\"027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"sj_execution\":{\"kind\":\"actual_complete_strict_radial_first_symbol_defect_v1\",\"run\":\"43768006977\",\"gates\":26,\"source\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\",\"manifest\":\"31602b830279bc5141950f3c34b70442f5a2997f872179b45effccb0ff3cdb48\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true}}")
def exact(x):
    v=Fraction(x)
    return arb(v.numerator)/v.denominator
def ball(x):
    y=arb(x["ball"]) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite complete scalar")
    return y
def upper(x):
    y=ball(x).upper()
    if not y>=0:raise ValueError("negative positive-budget upper")
    return y
def lower(x):
    y=ball(x).lower()
    if not y>0:raise ValueError("a required strict denominator is not positive")
    return y
def complete_min(xs):
    return min(upper(v) for v in xs)
def vec(v):
    if len(v)!=3:raise ValueError("exactly three complete angular derivatives are required")
    return [upper(x) for x in v]
def encode(x):
    if isinstance(x,arb):return {"ball":x.str(60)}
    if isinstance(x,list):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

def cut_and_propagated_coefficients(saved):
    a=vec(saved["FA_A1_jets"])
    z=vec(saved["FA_inverse_phase_jets"])
    cp=vec(saved["SJ_complete_cprop_integrals"])
    Linv=upper(upper(saved["KL_common_numerator"])/lower(saved["FA_same_cut_ng_lower"]))
    D=[upper(Linv*a[0]*z[0]),
       upper(Linv*(a[1]*z[0]+a[0]*z[1])),
       upper(Linv*(a[2]*z[0]+2*a[1]*z[1]+a[0]*z[2]))]
    cut=[D[0],upper(D[1]*z[0]),
         upper(D[2]*z[0]**2+D[1]*z[0]*z[1])]
    transported=[upper(z[0]*cp[0]),
       upper(z[0]*z[1]*cp[0]+z[0]**2*cp[1]),
       upper((z[0]*z[1]**2+z[0]**2*z[2])*cp[0]
             +3*z[0]**2*z[1]*cp[1]+z[0]**3*cp[2])]
    total=[upper(cut[k]+transported[k]) for k in range(3)]
    return dict(cut_leading_inverse=Linv,own_coefficient_original_phi=D,
                cut_coefficient=cut,propagated_coefficient=transported,
                complete_branch_coefficient=total)

def separate_multiplier_windows(f):
    f=vec(f)
    direct13=upper(f[0]+exact("39/32")*f[1])
    direct43=upper(f[0]+exact("243/160")*f[2])
    wholeH2=upper(3*(f[0]+arb(2).sqrt().upper()*f[1]+f[2]))
    return dict(L2=f[0],Hminus1_3=complete_min([direct13,wholeH2]),
        Hminus4_3=complete_min([direct43,wholeH2]),
        complete_direct_Hminus1_3=direct13,complete_direct_Hminus4_3=direct43,
        complete_alternative_H2=wholeH2,
        zero_mode_and_scalar_component_convention_retained=True)

def complete_dual_rows(saved,coeff):
    z=vec(saved["FA_inverse_phase_jets"])
    CI2=upper((arb(17).log()*exact("2/3")).exp()/16)
    R1=upper(z[0]*z[1])
    PH=upper(CI2*R1)
    candidates=[upper(arb.pi()*(z[0]+1)/8),upper(R1/8)]
    e=upper(upper(saved["FA_x_deviation"])
        +upper(saved["FA_T_holomorphic"]).sqrt().upper()*upper(saved["FA_y_holomorphic"]))
    optional=None
    if e<1:
        optional=upper(arb.pi()*e/(8*lower(arb(1)-e)))
        candidates.append(optional)
    PC=upper(CI2*(coeff["cut_coefficient"][1]+coeff["propagated_coefficient"][1]))
    return dict(C_I2_L2_to_H4_3_upper=CI2,inverse_second_derivative_upper=R1,
        inverse_displacement_H4_3=PH,inverse_displacement_Linfty=complete_min(candidates),
        complete_Linfty_candidates=candidates,phase_derivative_deviation=e,
        optional_positive_deviation_gate=bool(e<1),optional_complete_bound=optional,
        complete_IC_H4_3=PC,mean_annihilated_only_by_the_exact_primitive=True)

def ordered_coefficient_only_fees(saved,coeff,mult,dual):
    g0=coeff["propagated_coefficient"][0]
    m13=mult["cut"]["Hminus1_3"];m43=mult["cut"]["Hminus4_3"]
    Rtwo=upper(exact("17/16")*g0*m13)
    Rrank=upper(g0*(dual["inverse_displacement_H4_3"]+
        dual["inverse_displacement_Linfty"])*(1+m43/4))
    Ralg=upper(Rtwo+Rrank)
    BX=upper(saved["WX_inverse_waist_density_L2"])
    Cproj=upper((1+BX)*Ralg+BX*dual["complete_IC_H4_3"])
    tilde=upper(coeff["complete_branch_coefficient"][0]+upper(saved["TF_F_A0"]))
    S0=upper(saved["WX_common_input_L2"])
    Sinv=upper(saved["WX_common_input_inverse_Hminus4_3"])
    KF=upper(saved["TF_inverse_Hminus4_3"])
    Rprincipal=upper(S0*tilde*(upper(saved["WX_common_input_displacement_H4_3"])
                           +upper(saved["WX_common_input_displacement_Linfty"])))
    # TF's complete factors already contain the right inverse. Read, do not redo them.
    root_two=upper(tilde*upper(saved["TF_two_I_after_right_inverse"]))
    root_finite=upper(saved["TF_finite_after_right_inverse"])
    pre_selected=upper(KF*Cproj+root_two+root_finite)
    total=upper(S0*Sinv*pre_selected+Rprincipal)
    return dict(algebra_two_primitive=Rtwo,algebra_two_complete_ranks=Rrank,
        algebra_complete=Ralg,complete_waist_projection_fee=Cproj,
        complete_tilde_C_supremum=tilde,
        root_two_primitive_after_one_right_inverse=root_two,
        root_finite_after_one_right_inverse_read_verbatim=saved["TF_finite_after_right_inverse"],
        complete_principal_two_rank_fee=Rprincipal,
        coefficient_only_common_input_strong_fee=total,
        right_TF_inverse_applied_once=True,
        state_only_exact_left_coordinate_cancellation_not_used=True,
        full_state_error_other_rows_and_finite_inverse_not_claimed=True)

def canonical(x):
    return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),
        allow_nan=False)+"\n").encode("utf-8")
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(doc);tmp=path.with_name(path.name+".partial")
    tmp.write_bytes(raw);tmp.replace(path)
    return raw
def gate(doc,name,passed):
    doc["gates"].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ValueError("separate coefficient gate failed: "+name)
def finite_nonnegative(x):
    if isinstance(x,arb):return x.is_finite() and x>=0
    if isinstance(x,dict):return all(finite_nonnegative(v) for v in x.values())
    if isinstance(x,(tuple,list)):return all(finite_nonnegative(v) for v in x)
    return True
def accepted(role,paths,doc):
    info=EXPECTED[role];outer=read(paths[role])
    rec=outer["actual_scientific_receipt"] if info["wrapper"] else outer
    wrapper_ok=True
    if info["wrapper"]:
        wrapper_ok=(outer.get("complete") is True and outer.get("actual_returncode")==0
            and outer.get("actual_failure") is None
            and outer.get("source_budget_source_sha256")==info["source"]
            and outer.get("input_manifest_sha256")==info["manifest"])
    gate(doc,"completed original "+role+" exact source runtime manifest and all gates",
         wrapper_ok and rec.get("kind")==info["kind"]
         and rec.get("complete") is True and rec.get("proved") is True
         and rec.get("actual_returncode")==0 and rec.get("failure") is None
         and str(rec.get("run_id"))==info["run"] and str(rec.get("run_attempt"))=="1"
         and rec.get("source_sha256")==info["source"]
         and rec.get("input_manifest_sha256")==info["manifest"]
         and rec.get("runtime")==info["runtime"]
         and len(rec.get("gates",[]))==info["gates"]
         and all(g.get("passed") is True for g in rec["gates"]))
    return rec

def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),
            "python_flint":importlib.metadata.version("python-flint")}
    doc["runtime"]=actual;doc["arithmetic_bits"]=ctx.prec
    gate(doc,"public pinned runtime and320-bit directed arithmetic",
         actual==RUNTIME and a.bits==320 and ctx.prec==320
         and os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==PUBLIC)
    if SJ_ACTUAL_PENDING or any(v is None for v in PINNED.values()):
        raise ValueError("the complete SJ terminal identity has not been frozen")
    m=read(a.manifest);paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"exact current-only manifest source and six mathematical input identities",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS
         and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==value for k,value in PINNED.items()))
    gate(doc,"every read input is a bounded original small text and no native is restored",
         len(paths)==6 and all(p.stat().st_size<100000 for p in paths.values())
         and all(p.suffix in (".json",".md") for p in paths.values())
         and all(not p.read_bytes().startswith(b"\x1f\x8b") for p in paths.values()))
    old={role:accepted(role,paths,doc) for role in EXPECTED}
    fa=old["fa_science"];kl=old["kl_science"];wx=old["wx_execution"]
    tf=old["tf_science"];sj=old["sj_execution"]
    params=[fa["mathematical_parameters"],kl["parameters"],wx["mathematical_parameters"],
            tf["parameters"],sj["mathematical_parameters"]]
    gate(doc,"all five targets have the same real family fixed eta root and strict cut",
         all(p.get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
             and p.get("exact_strict_cut")==PARAMETERS["exact_strict_cut"]
             and p.get("exact_root_interval")==PARAMETERS["exact_root_interval"]
             and p.get("fixed_intrinsic_parameter")==PARAMETERS["fixed_intrinsic_parameter"] for p in params)
         and fa["mathematical_parameters"]["reference_column"]==PARAMETERS["reference_column"]
         and kl["parameters"]["reference_column"]==PARAMETERS["reference_column"])
    frame=fa["complete_new_first_frame_and_leading_conclusion"]
    domain=fa["complete_new_cut_domain_conclusion"]
    lead=kl["complete_new_leading_scalar_conclusion"]
    tcoef=tf["complete_new_root_coefficient_conclusion"]
    tnorm=tf["complete_new_root_normalizer_conclusion"]
    tstrong=tf["complete_new_strong_scalar_factors"]
    trans=sj["complete_new_transported_coefficient_conclusion"]
    same=sj["complete_saved_scalar_inputs_read_verbatim"]
    common=wx["complete_selected_common_input_conclusion"]
    wrank=wx["complete_full_primitive_rank_conclusion"]["selected_common_input"]
    waist=wx["complete_waist_density_coordinate_conclusion"]
    gate(doc,"FA original component-sum first amplitudes inverse phases and all means are complete",
         len(frame["complete_common_each_sign_each_branch_A1_angular_jets"])==3
         and len(frame["complete_phase_reciprocal_angular_jets"])==3
         and frame["vector_H2_is_scalar_component_sum"] is True
         and frame["inverse_U_Phi_Hminus4_3_not_substituted"] is True
         and frame["independent_external_physical_means_and_all_finite_cross_blocks_retained"] is True
         and frame["input_cutoff_abs_j"]==97
         and frame["moving_normalizer_cutoff_abs_j"]==268435456
         and frame["waist_leading_receiver_incoming_outgoing_or_full_R0_claimed"] is False)
    gate(doc,"KL common numerator is the same Ai column and has no endpoint or second strict factor",
         lead["common_numerator_has_no_endpoint_ng_division"] is True
         and lead["root_mean_residual_retained_in_exact_log_derivative"] is True
         and lead["reference_column"]==PARAMETERS["reference_column"]
         and lead["second_Bi_or_other_genuine_root_column_covered"] is False
         and lead["no_sector_sum_or_extra_sqrt2"] is True
         and kl["input_sha256"]["fa_science"]==PINNED["fa_science"])
    gate(doc,"TF original full root domain and saved after-right factors are read unchanged",
         tf["complete_common_root_normalizer_proved"] is True
         and tf["input_sha256"]["fa_science"]==PINNED["fa_science"]
         and tcoef["complete_original_eta_lower_used_verbatim"]==domain["complete_eta_full_complex_lower"]
         and tcoef["original_full_complex_eta_domain_includes_root"] is True
         and tnorm["same_inverse_on_both_windows"] is True
         and tnorm["right_transformed_finite_rows_keep_actual_dual_norms"] is True
         and tnorm["right_transformed_finite_input_support_not_claimed"] is True
         and tnorm["finite_original_input_and_output_support_abs_j"]==tnorm["actual_J_F"]+191
         and tstrong["two_primitive_fee_requires_separate_complete_tilde_C_supremum"] is True
         and tstrong["finite_fee_is_one_complete_branch_fee_with_full_mean"] is True)
    gate(doc,"only the successful complete SJ ordinary cover and integral terminal are consumed",
         sj["stage"]=="complete" and sj["complete_strict_first_symbol_defect_paid"] is True
         and sj["original_consumed_body_rows"]==3071
         and sj["new_transported_angular_rows"]==3071
         and sj["new_complete_interface_rows"]==3070
         and sj["new_complete_waist_error_bounds"]==1
         and len(trans["common_both_branch_complete_c_0_2_integrals"])==3
         and trans["new_ordinary_integrals_use_true_radial_lengths_once"] is True
         and trans["all_complete_coefficient_means_retained"] is True
         and trans["general_composed_coefficients_not_assigned_finite_Fourier_support"] is True
         and same["FA_corrected_Kc_minus_read_verbatim"]==frame["complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once"]
         and same["FA_already_forward_restored_cut_error_read_verbatim"]==frame["complete_same_TN_forward_L2_times_free_cut_upper"]
         and sj["accepted_success_identity_read_verbatim"]["WX"]["digest"]==PINNED["wx_execution"])
    gate(doc,"WX true waist inverse selected common input and full displacement rows keep their order",
         waist["same_actual_inverse_on_L2_and_Hminus4_3"] is True
         and waist["independent_physical_mean_block_is_identity"] is True
         and common["exact_order"]==PARAMETERS["selected_common_input_order"]
         and common["only_same_selected_actual_conjugacy"] is True
         and common["independent_mean_block_retained"] is True
         and wrank["both_finite_rank_terms_and_the_full_mean_retained"] is True
         and wrank["mean_identity_extension_differs_from_full_density_by_explicit_rank"] is True)
    saved=dict(FA_A1_jets=frame["complete_common_each_sign_each_branch_A1_angular_jets"],
        FA_inverse_phase_jets=frame["complete_phase_reciprocal_angular_jets"],
        FA_same_cut_ng_lower=frame["same_cut_ng_lower_read_verbatim"],
        FA_x_deviation=domain["complete_x_deviation_holomorphic"],
        FA_y_holomorphic=domain["complete_y_holomorphic"],
        FA_T_holomorphic=domain["complete_T_holomorphic_upper_read_from_original_full_Ap"],
        KL_common_numerator=lead["complete_saved_root_short_common_numerator_upper"],
        SJ_complete_cprop_integrals=trans["common_both_branch_complete_c_0_2_integrals"],
        TF_F_A0=tcoef["complete_root_F_A0_upper"],
        TF_inverse_L2=tnorm["complete_inverse_L2_upper"],
        TF_inverse_Hminus4_3=tnorm["complete_inverse_Hminus4_3_upper"],
        TF_two_I_before_right_inverse=tstrong["complete_two_primitive_left_multiplier_fee_before_right_inverse"],
        TF_two_I_after_right_inverse=tstrong["complete_two_primitive_left_multiplier_fee_after_right_inverse"],
        TF_finite_before_right_inverse=tstrong["complete_finite_map_fee_before_right_inverse"],
        TF_finite_after_right_inverse=tstrong["complete_finite_map_fee_after_right_inverse"],
        WX_inverse_waist_density_L2=waist["complete_inverse_density_L2_upper"],
        WX_common_input_L2=common["complete_common_input_L2_upper"],
        WX_common_input_inverse_Hminus4_3=common["complete_common_input_inverse_Hminus4_3_upper"],
        WX_common_input_displacement_H4_3=wrank["complete_zero_mean_displacement_H2_and_H4_3_upper"],
        WX_common_input_displacement_Linfty=wrank["complete_zero_mean_displacement_Linfty_upper"])
    gate(doc,"all complete copied scalar inputs are finite and the actual cut denominator is positive",
         len(vec(saved["FA_A1_jets"]))==len(vec(saved["FA_inverse_phase_jets"]))==
             len(vec(saved["SJ_complete_cprop_integrals"]))==3
         and lower(saved["FA_same_cut_ng_lower"])>0
         and all(upper(v).is_finite() for k,v in saved.items() if not isinstance(v,list)))
    doc["complete_original_receipt_identities"]=copy.deepcopy(EXPECTED)
    doc["input_sha256"]=copy.deepcopy(PINNED)
    doc["copied_complete_scalar_inputs_read_verbatim"]=copy.deepcopy(saved)
    doc["copied_complete_tf_structure"]=copy.deepcopy({
        "actual_J_F":tnorm["actual_J_F"],
        "finite_original_input_and_output_support_abs_j":tnorm["finite_original_input_and_output_support_abs_j"],
        "right_transformed_finite_rows_keep_actual_dual_norms":True,
        "right_transformed_finite_input_support_not_claimed":True})
    doc["copied_selected_common_input_scope"]=copy.deepcopy({
        "exact_order":common["exact_order"],
        "inverse_order":common["inverse_order"],
        "selected_parameter_absolute_upper":common["selected_parameter_absolute_upper"],
        "only_same_selected_actual_conjugacy":True})
    return paths,saved

def run(a,doc):
    ctx.prec=a.bits
    paths,saved=checked_inputs(a,doc)
    doc.update(stage="complete saved inputs",original_completed_scientific_receipts_read=5)
    save(a.out,doc)
    coeff=cut_and_propagated_coefficients(saved)
    gate(doc,"new cut and propagated complete coefficients retain all three derivatives and the mean",
         finite_nonnegative(coeff) and coeff["cut_leading_inverse"]>0
         and all(len(coeff[k])==3 for k in
             ("own_coefficient_original_phi","cut_coefficient",
              "propagated_coefficient","complete_branch_coefficient")))
    doc["complete_new_cut_and_transported_coefficient_conclusion"]=encode({
        "complete_cut_leading_inverse_upper":coeff["cut_leading_inverse"],
        "complete_original_phi_own_coefficient_0_2_upper":coeff["own_coefficient_original_phi"],
        "complete_cut_coefficient_0_2_upper":coeff["cut_coefficient"],
        "complete_propagated_coefficient_0_2_upper":coeff["propagated_coefficient"],
        "complete_branch_coefficient_0_2_upper":coeff["complete_branch_coefficient"],
        "complete_root_F_A0_read_verbatim":saved["TF_F_A0"],
        "all_three_arrays_are_complete_scalar_suprema":True,
        "two_input_signs_have_the_same_exact_real_coefficient_by_WY39_44":True,
        "original_branch_and_input_sign_normalization_retained":True,
        "KL_numerator_divided_by_cut_ng_lower_exactly_once":True,
        "no_saved_waist_KLambda_or_WX_radial_forward_applied":True,
        "ordinary_SJ_integrals_used_verbatim_without_reintegration":True,
        "no_difference_of_upper_bounds_used":True,
        "reference_column":PARAMETERS["reference_column"],
        "second_reference_column_not_covered":True})
    doc.update(new_complete_coefficient_arrays=3,new_cut_leading_inverse_count=1,
        stage="complete cut and transported derivative arrays")
    save(a.out,doc)
    mult={name:separate_multiplier_windows(coeff[key]) for name,key in
          (("cut","cut_coefficient"),("propagated","propagated_coefficient"),
           ("complete","complete_branch_coefficient"))}
    gate(doc,"three complete multiplier windows for each separate coefficient keep the zero Fourier mode",
         finite_nonnegative(mult) and set(mult)=={"cut","propagated","complete"}
         and all(v["zero_mode_and_scalar_component_convention_retained"] is True for v in mult.values()))
    doc["complete_new_multiplier_conclusion"]=encode(mult)
    doc.update(new_complete_multiplier_window_bounds=9,stage="complete separate multiplier windows")
    save(a.out,doc)
    dual=complete_dual_rows(saved,coeff)
    gate(doc,"complete dual rows retain both ranks and use the optional phase gate only when strict",
         finite_nonnegative(dual)
         and dual["mean_annihilated_only_by_the_exact_primitive"] is True
         and len(dual["complete_Linfty_candidates"])==
             (3 if dual["optional_positive_deviation_gate"] else 2)
         and (dual["optional_positive_deviation_gate"] or dual["optional_complete_bound"] is None))
    doc["complete_new_dual_row_conclusion"]=encode(dual)
    doc.update(new_complete_dual_row_bounds=3,stage="complete inverse displacement and primitive dual rows")
    save(a.out,doc)
    fees=ordered_coefficient_only_fees(saved,coeff,mult,dual)
    gate(doc,"all coefficient-only terms keep the complete two primitive windows ranks and ordered right factors",
         finite_nonnegative(fees)
         and fees["right_TF_inverse_applied_once"] is True
         and fees["state_only_exact_left_coordinate_cancellation_not_used"] is True
         and fees["full_state_error_other_rows_and_finite_inverse_not_claimed"] is True
         and fees["root_finite_after_one_right_inverse_read_verbatim"]==saved["TF_finite_after_right_inverse"])
    doc["complete_new_ordered_coefficient_fee_conclusion"]=encode(fees)
    doc["complete_selected_coefficient_only_Hminus4_3_to_L2_upper"]=encode(
        fees["coefficient_only_common_input_strong_fee"])
    doc["complete_sign_wave_scope"]=[dict(physical_input_sign=e,physical_wave=s,
        same_common_bound_applies_without_sum_over_input_signs=True)
        for s in PARAMETERS["physical_waves"] for e in PARAMETERS["physical_input_signs"]]
    doc["scope"]=dict(
        complete_cut_and_propagated_coefficients_kept_separately=True,
        complete_real_family_coefficients_and_full_means_retained=True,
        same_terminal_Ai_reference_column_not_a_full_free_basis=True,
        no_derivative_inferred_from_a_whole_norm=True,
        no_total_upper_subtracted_to_obtain_a_summand=True,
        full_physical_4j_Fourier_sums_used=True,
        conditional_deviation_candidate_does_not_replace_failed_domain_gate=True,
        two_complete_density_primitive_ranks_retained=True,
        waist_projection_rank_is_independent_of_FA_and_SJ_primitive_errors=True,
        TF_completed_after_right_factors_read_without_second_KF=True,
        selected_common_input_only_not_a_family_of_conjugacies=True,
        coefficient_only_fee_not_the_complete_state_error=True,
        original_low_mean_other_sign_and_finite_border_rows_remain_separate=True,
        exact_right_order_Lambda_inverse_TF_inverse_S_inverse_retained=True,
        no_state_only_exact_left_angle_cancellation_used=True,
        no_new_incoming_inverse_Schur_inverse_or_full_R0_claimed=True)
    gate(doc,"full means finite maps selected scope and all original independent error terms remain",
         all(doc["scope"].values()) and len(doc["complete_sign_wave_scope"])==4
         and doc["independent_physical_mean_coordinates"]==2
         and doc["old_completed_SJ_integrals_or_FA_KL_WX_TF_targets_recomputed"]==0
         and doc["old_scientific_source_imports"]==0
         and doc["old_binary_native_or_archive_restored"]==0)
    doc.update(new_complete_coefficient_only_fee_count=1,stage="complete coefficient-only assembly")
    save(a.out,doc)
    gate(doc,"all twenty-one gates preserve the five successful originals and exact six small input bytes",
         len(doc["gates"])==20 and all(x["passed"] is True for x in doc["gates"])
         and all(sha(paths[k])==v for k,v in PINNED.items())
         and doc["original_completed_scientific_receipts_read"]==5
         and doc["new_complete_coefficient_arrays"]==3
         and doc["new_complete_multiplier_window_bounds"]==9
         and doc["new_complete_dual_row_bounds"]==3
         and doc["new_complete_coefficient_only_fee_count"]==1)
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete structural gate count changed")
    doc.update(complete=True,proved=True,actual_returncode=0,stage="complete",
        complete_separate_coefficient_budgets_proved=True)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete or partial conclusion")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        parameters=copy.deepcopy(PARAMETERS),arithmetic_bits=a.bits,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        stage="initial immutable input checks",original_completed_scientific_receipts_read=0,
        new_cut_leading_inverse_count=0,new_complete_coefficient_arrays=0,
        new_complete_multiplier_window_bounds=0,new_complete_dual_row_bounds=0,
        new_complete_coefficient_only_fee_count=0,
        complete_separate_coefficient_budgets_proved=False,
        old_completed_SJ_integrals_or_FA_KL_WX_TF_targets_recomputed=0,
        old_scientific_source_imports=0,old_binary_native_or_archive_restored=0,
        original_input_bytes_modified=False,new_recomputable_arrays_persisted=False,
        independent_physical_mean_coordinates=2,
        full_incoming_inverse_proved=False,finite_Schur_inverse_proved=False,
        complete_state_error_proved=False,full_return_R0_proved=False,
        actual_nonlinear_background_proved=False,final_surface_proved=False)
    save(a.out,doc)
    try:run(a,doc)
    except Exception as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(error_type=type(error).__name__,message=str(error)))
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=save(a.out,doc)
    print("SEPARATE_CUT_PROPAGATED_COEFFICIENT_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=sha_bytes(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("SEPARATE_CUT_PROPAGATED_COEFFICIENT_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>40000:raise ValueError("saved complete coefficient science exceeds40000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())

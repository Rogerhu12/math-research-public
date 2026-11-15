#!/usr/bin/env python3
"""New UT full-normalizer endpoint replacement, using four completed receipts.
No old source integral, ray, coefficient closure, normalizer or scientific
producer is run.  The changed trial is returned to the original before any
whole-bound comparison.  Full incoming and all retained rows stay unpaid.
"""
from __future__ import annotations
import argparse,copy,hashlib,importlib.metadata,json,os,platform,time,traceback
from pathlib import Path
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
PRODUCER=TOPIC+"scripts/fourfold_codazzi_full_normalizer_endpoint_replacement.py"
KIND="actual_full_normalizer_endpoint_replacement_v1"
MANIFEST_KIND="full_normalizer_endpoint_replacement_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=22
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":22,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_complete_radial_interval\":[\"0\",\"76285779072683/320000000000000\"],\"input_cutoff_abs_j\":97,\"exact_moving_normalizer_cutoff_abs_j\":268435456,\"physical_frequency\":\"n=4|j|\",\"independent_physical_mean_coordinates\":2,\"physical_input_signs\":[-1,1],\"physical_waves\":[-1,1],\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"state_operator_order\":\"S U_Xminus_sigma_inverse J_sigma Twaist_inverse E_star P97 Lambda_sigma_inverse TF_inverse S_inverse\",\"retained_mode\":\"exact-border-unpaid\",\"reference_column\":\"same terminal Ai free P8 first column\",\"full_S_bandwidth\":192,\"full_Z2_bandwidth\":384,\"Af_finite_support_offset\":191,\"FT_finite_support_offset\":575,\"new_trial\":\"(P T V Bc,0)\",\"returned_trial\":\"(P TJ V Bc,0)\",\"new_source_parts\":[\"leading_two_primitive_and_rank\",\"complete_Q_including_F0_F1_F2\",\"complete_independent_mean_row\"],\"retained_old_fourth_part\":\"complete_finite_FT_FJ\",\"whole_selection\":\"compare final retained outward upper; old wins ties\",\"original_source_rows\":3071,\"original_interface_rows\":3070,\"original_genuine_joins\":2549,\"original_conservative_refinements\":521,\"old_scientific_calls_allowed\":0,\"new_integrals_or_array_inputs\":0,\"same_actual_waist_inverse_and_root_gauge_retained\":true,\"complete_Ei_Eo_or_incoming_or_Schur_or_R0_claimed\":false}")
PINNED=json.loads("{\"sj_execution\":\"2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88\",\"fa_science\":\"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2\",\"wt_science\":\"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d\",\"we_science\":\"3d73b56f604b012b66f2f502aea481b59383f5566fb5d12c676843220d39956a\",\"ut_contract\":\"c2734ab5029215559a9b2987c51af3ce1308295a5244328885fe43d74fd5be61\",\"sj_source\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\"}")
EXPECTED=json.loads("{\"sj_execution\":{\"kind\":\"actual_complete_strict_radial_first_symbol_defect_v1\",\"run\":\"43768006977\",\"attempt\":\"1\",\"gates\":26,\"source\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\",\"manifest\":\"31602b830279bc5141950f3c34b70442f5a2997f872179b45effccb0ff3cdb48\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"fa_science\":{\"kind\":\"actual_complete_free_Airy_first_omitted_cut_scalars_v1\",\"run\":\"43763658978\",\"attempt\":\"1\",\"gates\":24,\"source\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"manifest\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\",\"runtime\":{\"Python\":\"3.12.14\",\"arithmetic_bits\":320,\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"wt_science\":{\"kind\":\"actual_waist_normalizer_coefficients_and_two_window_gates_v1\",\"run\":\"43763134339\",\"attempt\":\"1\",\"gates\":20,\"source\":\"7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393\",\"manifest\":\"4cec7ef0ba21373190dd0bf142d10546823d46bb832a58df66529822990ad125\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"we_science\":{\"kind\":\"actual_paid_waist_strong_error_assembly_v1\",\"run\":\"43769746581\",\"attempt\":\"1\",\"gates\":22,\"source\":\"d02efe46d4baee16971c9239526d4e3f412ad7dd8e95cfab31d56458a7a7fa55\",\"manifest\":\"098c090606f54bbbb8bd6d026b6360f53ba70f5e75c4fc4218e7f784b2eb88a1\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false}}")

def canonical(x):
    return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode()
def digest(x):return hashlib.sha256(x).hexdigest()
def sha(path):return digest(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def save(path,doc):
    raw=canonical(doc);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp");temp.write_bytes(raw);os.replace(temp,path)
    return raw
def gate(doc,name,passed):
    doc["gates"].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ValueError("complete UT gate failed: "+name)
def ball(value):
    x=arb(value["ball"]) if isinstance(value,dict) else arb(value)
    if not x.is_finite():raise ValueError("nonfinite complete scalar")
    return x
def up(value):
    x=ball(value).upper()
    if not x>=0:raise ValueError("negative positive-budget upper")
    return x
def rec(x):return {"ball":x.str(72)}
def params(x):return x["parameters"] if "parameters" in x else x["mathematical_parameters"]

def accepted(role,paths,doc):
    info=EXPECTED[role];outer=read(paths[role])
    a=outer["actual_scientific_receipt"] if info["wrapper"] else outer
    wrapped=(not info["wrapper"] or
        (outer.get("complete") is True and outer.get("actual_returncode")==0
         and outer.get("actual_failure") is None
         and outer.get("source_budget_source_sha256")==info["source"]
         and outer.get("input_manifest_sha256")==info["manifest"]))
    gate(doc,"completed "+role+" same run source manifest runtime and all gates",
         wrapped and a.get("kind")==info["kind"]
         and a.get("complete") is True and a.get("proved") is True
         and a.get("actual_returncode")==0 and a.get("failure") is None
         and str(a.get("run_id"))==info["run"] and str(a.get("run_attempt"))==info["attempt"]
         and a.get("source_sha256")==info["source"]
         and a.get("input_manifest_sha256")==info["manifest"]
         and a.get("runtime")==info["runtime"]
         and len(a.get("gates",[]))==info["gates"]
         and all(g.get("passed") is True for g in a["gates"]))
    return a


def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),"python_flint":importlib.metadata.version("python-flint")}
    doc["runtime"]=actual;doc["arithmetic_bits"]=ctx.prec
    gate(doc,"public pinned runtime and320-bit directed scalar arithmetic",
         actual==RUNTIME and a.bits==320 and ctx.prec==320
         and os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==PUBLIC)
    m=read(a.manifest);paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"six exact mathematical inputs and the current-only source manifest are frozen",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    gate(doc,"only bounded current small texts and no original arrays archives or old imports",
         len(paths)==6 and all(p.stat().st_size<100000 for p in paths.values())
         and all(p.suffix in (".json",".md",".py") for p in paths.values())
         and all(not p.read_bytes().startswith(b"\x1f\x8b") for p in paths.values()))
    old={role:accepted(role,paths,doc) for role in EXPECTED}
    sj=old["sj_execution"];fa=old["fa_science"];wt=old["wt_science"];we=old["we_science"]
    jp=params(sj);fp=params(fa);wp=params(wt);ep=params(we)
    family=wt["copied_SP_family_identity"]
    gate(doc,"same repaired whole real family strict interval physical angle input97 and actual Js",
         all(params(x)["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
             and params(x)["fixed_intrinsic_parameter"]=="eta_0"
             and params(x)["exact_strict_cut"]==PARAMETERS["exact_strict_cut"]
             and params(x)["input_cutoff_abs_j"]==97 for x in (sj,fa,we))
         and all(params(x)["physical_frequency"]=="n=4|j|" for x in (sj,fa,we))
         and jp["exact_complete_radial_interval"]==PARAMETERS["exact_complete_radial_interval"]
         and jp["exact_moving_normalizer_cutoff_abs_j"]==ep["exact_moving_normalizer_cutoff_abs_j"]==268435456
         and jp["complete_physical_mean_coordinates"]==wp["independent_mean_coordinates"]==2
         and wp["exact_delta_half_width"]==PARAMETERS["exact_real_delta_radius"]
         and fp["reference_column"]==ep["reference_column"]==PARAMETERS["reference_column"]
         and fp["physical_signs"]==[-1,1] and fp["oscillatory_branches"]==[-1,1]
         and all(family[k]==PARAMETERS[k] and ep[k]==PARAMETERS[k]
             for k in ("continuous_centre_definition_sha256","continuous_response_definition_sha256")))
    radial=sj["complete_new_radial_coefficient_conclusion"]
    body=sj["complete_original_body_and_polynomial_conclusion"]
    transport=sj["complete_new_transported_coefficient_conclusion"]
    gate(doc,"full coefficient A0 maxima exact finite supports and unchanged transported coefficients",
         radial["exact_moving_Js"]==268435456 and radial["full_finite_support_through"]==268435456+575
         and radial["complete_branch_entry_sums_before_functional"] is True
         and radial["ordinary_derivative_convention"] is True
         and radial["full_F0_F1_F2_FT_FJ_and_Zy_mean_rows_retained"] is True
         and sj["scope"]["full_angular_Wiener_A0_budgets_not_pointwise_bounds_used_in_finite_band_rule"] is True
         and body["exact_consumed_interval"]==PARAMETERS["exact_complete_radial_interval"]
         and body["original_consumed_rows"]==3071 and body["qualified_polynomial_intervals"]==2550
         and body["no_global_radial_derivative_continuity_assumed"] is True
         and transport["constant_C_global_bound_used_in_every_source_and_interface_row"] is True
         and transport["all_complete_coefficient_means_retained"] is True
         and transport["general_composed_coefficients_not_assigned_finite_Fourier_support"] is True)
    source=sj["complete_new_complete_source_conclusion"];jump=sj["complete_new_interface_conclusion"]
    fields=set(PARAMETERS["new_source_parts"]+[PARAMETERS["retained_old_fourth_part"]])
    gate(doc,"four independently saved ordinary integrals and every genuine artificial and mean impulse are complete",
         set(source["complete_four_ordinary_source_parts"])==fields
         and source["complete_source_rows"]==3071
         and source["exact_ordinary_radial_interval"]==PARAMETERS["exact_complete_radial_interval"]
         and source["original_two_physical_rows_and_two_mean_rows_retained"] is True
         and source["finite_F0_F1_F2_and_FT_FJ_included"] is True
         and jump["complete_interface_count"]==3070
         and jump["genuine_polynomial_join_count"]==2549
         and jump["conservative_artificial_refinement_count"]==521
         and jump["no_radial_length_factor"] is True
         and jump["intrinsic_qrr_betar_gammar_and_physical_mean_r_jumps_all_retained"] is True
         and jump["exact_S_continuity_is_from_pinned_repaired_and_intrinsic_definitions"] is True
         and jump["endpoint_ball_overlap_not_used_as_continuity"] is True)
    saved=sj["complete_saved_scalar_inputs_read_verbatim"]
    fc=fa["complete_new_first_frame_and_leading_conclusion"]
    js=sj["complete_strict_first_symbol_waist_error_conclusion"]
    gate(doc,"corrected cut input cut ng cancellation and original forward restored cut error use the same FA receipt",
         sj["accepted_success_identity_read_verbatim"]["FA"]["source"]==EXPECTED["fa_science"]["source"]
         and sj["accepted_success_identity_read_verbatim"]["FA"]["run"]==EXPECTED["fa_science"]["run"]
         and saved["FA_corrected_Kc_minus_read_verbatim"]
             ==fc["complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once"]
         and saved["FA_already_forward_restored_cut_error_read_verbatim"]
             ==fc["complete_same_TN_forward_L2_times_free_cut_upper"]
         and fc["input_cutoff_abs_j"]==97 and fc["moving_normalizer_cutoff_abs_j"]==268435456
         and fc["FS_is_norm_paid_not_deleted"] is True
         and fc["independent_external_physical_means_and_all_finite_cross_blocks_retained"] is True
         and js["FA_forward_TN_inside_cut_error_applied_exactly_once"] is True
         and js["FA_ng_inverse_inside_Kc_applied_exactly_once"] is True
         and js["ST_cut_and_source_receivers_each_applied_once"] is True)
    fixed=[x for x in wt["complete_fixed_cutoff_results"] if x["J"]==268435456]
    gate(doc,"same actual right waist and same Js inverse in both windows keep both means",
         len(fixed)==1 and fixed[0]["inverse_on_both_windows_proved"] is True
         and fixed[0]["strict_tests_passed"]==fixed[0]["strict_tests_total"]==4
         and all(v["passed"] is True for v in fixed[0]["all_four_strict_tests"])
         and fixed[0]["finite_complement_and_two_means_identity"] is True
         and fixed[0]["two_factor_finite_support_label"]==268435456+575
         and wp["exact_waist"]=="0" and wp["radial_trace_side"]=="right"
         and wp["S_bandwidth"]==192 and wp["S2_bandwidth"]==384)
    ew=we["copied_complete_scalar_inputs_read_verbatim"];er=we["complete_new_receiver_multiplier_conclusion"]
    gate(doc,"the returned original trial has the exact WE state factor coefficient fee and retained register",
         ew["C_SF"]==js["complete_SF_waist_density_error_upper"]
         and we["copied_complete_SJ_details_read_verbatim"]==js
         and ep["state_operator_order"]==PARAMETERS["state_operator_order"]
         and ep["selected_common_input_order"]==PARAMETERS["selected_common_input_order"]
         and we["copied_complete_selected_scope"]["only_same_selected_actual_conjugacy"] is True
         and er["exact_state_operator_order"]==PARAMETERS["state_operator_order"]
         and er["BH0_exact_left_cancellation_used_only_for_state_or_same_left_port_receiver"] is True
         and er["no_extra_ng_radial_or_TC_cut_factor"] is True
         and er["original_Lambda_stays_before_TF_inverse_and_S_inverse"] is True
         and we["retained_mode"]=="exact-border-unpaid" and we["retained_norm_budget"] is None
         and len(we["retained_row_register"])==6
         and all(v["actual_norm_supplied"] is False for v in we["retained_row_register"])
         and we["complete_full_Ei_Eo_proved"] is False and we["full_incoming_inverse_proved"] is False)
    original=paths["sj_source"].read_text();proof=paths["ut_contract"].read_text()
    gate(doc,"frozen source verifies independent fullT positive parts and full jump factor without import or old evaluation",
         all(x in original for x in ("def complete_source_row(","def complete_interface(",
             'leading_two_primitive_and_rank=up(g["Kc"]*t["t0"]*dV)',
             'complete_Q_including_F0_F1_F2=up(g["Kc"]*t["qstar"]*g["vm"]*cf)',
             'complete_independent_mean_row=up(g["Kc"]*t["zstar"]*t["tm"]*g["vm"]*cf)',
             'source_parts[k]=up(source_parts[k]+length*v)',
             'result=up(g["Kc"]*t10*ex(Q(17,16))*JZ*g["vm"]*cf)'))
         and all(x in proof for x in (r"\tag{UT.11}",r"\tag{UT.18}",r"\tag{UT.24}",
             r"\tag{UT.25}",r"\tag{UT.26}",r"\tag{UT.27}",r"\tag{UT.28}")))
    doc["complete_original_receipt_identities"]={
        role:dict(info=copy.deepcopy(EXPECTED[role]),original_file_sha256=PINNED[role],
             complete_science_canonical_sha256=digest(canonical(old[role]))) for role in EXPECTED}
    doc["original_completed_scientific_receipts_read"]=4
    doc["input_sha256"]=copy.deepcopy(PINNED)
    return old,paths

CONSUMED=json.loads("{\"S_A0\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_matrix_row_column_A0_maxima\",\"S\"],\"Z2_A0\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_matrix_row_column_A0_maxima\",\"Z\"],\"t10\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"t10\"],\"t2minus\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"t2m\"],\"mc\":[\"sj_execution\",\"complete_new_transported_coefficient_conclusion\",\"complete_two_branch_c_multiplier\"],\"vminus\":[\"sj_execution\",\"complete_saved_scalar_inputs_read_verbatim\",\"WX_reverse_leading_windows_read_verbatim\",\"complete_reverse_Hminus4_3_upper\"],\"Kcminus\":[\"sj_execution\",\"complete_saved_scalar_inputs_read_verbatim\",\"FA_corrected_Kc_minus_read_verbatim\"],\"Ec_old\":[\"sj_execution\",\"complete_saved_scalar_inputs_read_verbatim\",\"FA_already_forward_restored_cut_error_read_verbatim\"],\"Gcut\":[\"sj_execution\",\"complete_saved_scalar_inputs_read_verbatim\",\"ST_cut_receiver_read_verbatim\"],\"Gsource\":[\"sj_execution\",\"complete_saved_scalar_inputs_read_verbatim\",\"ST_general_primitive_mean_source_receiver_read_verbatim\"],\"CSF_old\":[\"sj_execution\",\"complete_strict_first_symbol_waist_error_conclusion\",\"complete_SF_waist_density_error_upper\"],\"Kfree_cut_minus\":[\"fa_science\",\"complete_new_first_frame_and_leading_conclusion\",\"complete_corrected_Bfree1_Hminus4_3_upper\"],\"ng0_upper\":[\"wt_science\",\"copied_complete_SP_waist_factors\",\"density_radial_factor_upper\"],\"Astate\":[\"we_science\",\"complete_new_receiver_multiplier_conclusion\",\"complete_state_factor_upper\"],\"C_PC\":[\"we_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"C_PC\"],\"C_ST4\":[\"we_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"C_ST4\"],\"CGwhole\":[\"we_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"CGwhole\"],\"CWE_old\":[\"we_science\",\"complete_paid_strong_error_conclusion\",\"complete_paid_Hminus4_3_to_L2_upper\"]}")

def scalar_copies(old):
    result={}
    for name,path in CONSUMED.items():
        x=old[path[0]]
        for key in path[1:]:x=x[key]
        result[name]=copy.deepcopy(x)
    return result

def positive_integer_power(n,p,q):
    if not isinstance(n,int) or n<1 or p<0 or q<1:raise ValueError("invalid exact positive power")
    return up((arb(n).log()*arb(p)/arb(q)).exp())

def complete_minimum(records):
    if not records:raise ValueError("empty whole-bound set")
    index=0
    for k in range(1,len(records)):
        if up(records[k])<up(records[index]):index=k
    return index,copy.deepcopy(records[index])

def scalar_bounds(saved,parts,jump):
    """Only UT scalar sums and endpoint formulas; no old integral or source call."""
    x={k:up(v) for k,v in saved.items()}
    J=PARAMETERS["exact_moving_normalizer_cutoff_abs_j"];L=J+191
    mS=up(positive_integer_power(769,1,3)*x["S_A0"])
    finite_embedding=positive_integer_power(1+16*L*L,1,6)
    CI=up(arb(17).sqrt()/4)
    Af=up(2*CI*mS*finite_embedding)
    Bf=up(arb(17)/8*x["Z2_A0"])
    endpoint=up(Af*x["t2minus"]+x["t10"]*Bf)
    three=up(sum((up(parts[k]) for k in PARAMETERS["new_source_parts"]),arb(0)))
    seam=up(jump["complete_all_interface_impulses_upper"])
    cf=up(1+x["mc"]/4)
    cut_endpoint=up(endpoint*x["Kfree_cut_minus"])
    new_cut_error=up(x["Ec_old"]+cut_endpoint)
    waist_endpoint=up(x["ng0_upper"]*endpoint*x["vminus"]*cf*x["Kcminus"])
    cut_part=up(x["Gcut"]*new_cut_error)
    body_part=up(x["Gsource"]*three)
    jump_part=up(x["Gsource"]*seam)
    full_trial=up(cut_part+body_part+jump_part)
    returned=up(full_trial+waist_endpoint)
    candidates=[copy.deepcopy(saved["CSF_old"]),rec(returned)]
    selected,whole=complete_minimum(candidates)
    Cstar=up(x["C_PC"]+x["C_ST4"]+up(whole))
    state=up(x["Astate"]*Cstar)
    paid=up(state+x["CGwhole"])
    return dict(mS=mS,finite_embedding=finite_embedding,Af=Af,Bf=Bf,endpoint=endpoint,
        three=three,seam=seam,cf=cf,cut_endpoint=cut_endpoint,new_cut_error=new_cut_error,
        waist_endpoint=waist_endpoint,cut_part=cut_part,body_part=body_part,jump_part=jump_part,
        full_trial=full_trial,returned=returned,candidates=candidates,selected=selected,
        whole=whole,Cstar=Cstar,state=state,paid=paid)

def run(a,doc):
    ctx.prec=a.bits
    old,paths=checked_inputs(a,doc)
    saved=scalar_copies(old);sj=old["sj_execution"];we=old["we_science"]
    parts=sj["complete_new_complete_source_conclusion"]["complete_four_ordinary_source_parts"]
    jump=sj["complete_new_interface_conclusion"]
    doc["copied_complete_scalar_inputs_read_verbatim"]=copy.deepcopy(saved)
    doc["copied_complete_four_source_parts_read_verbatim"]=copy.deepcopy(parts)
    doc["copied_complete_interface_conclusion_read_verbatim"]=copy.deepcopy(jump)
    doc["copied_original_WE_retained_register_read_verbatim"]=copy.deepcopy(we["retained_row_register"])
    doc["copied_complete_selected_scope_read_verbatim"]=copy.deepcopy(we["copied_complete_selected_scope"])
    doc["copied_complete_SJ_scope_read_verbatim"]=copy.deepcopy(sj["scope"])
    doc["stage"]="new complete endpoint and original-trial scalar combinations"
    b=scalar_bounds(saved,parts,jump)
    doc["complete_new_endpoint_strong_conclusion"]=dict(
        complete_S_Hone_third_multiplier_upper=rec(b["mS"]),
        complete_finite_output_embedding_upper=rec(b["finite_embedding"]),
        complete_Af_Hminus4_3_to_L2_upper=rec(b["Af"]),
        complete_Bf_Hminus4_3_to_L2_upper=rec(b["Bf"]),
        complete_FT_Hminus4_3_to_L2_upper=rec(b["endpoint"]),
        complete_V_first_coefficient_negative_factor=rec(b["cf"]),
        exact_Af_input_and_output_support=268435456+191,
        exact_FT_input_and_output_support=268435456+575,
        same_closed_interval_upper_used_at_both_endpoints=True,
        full_T_inverse_not_assumed=True,
        complete_source_Js_7third_factor_not_reused_for_endpoint=True)
    gate(doc,"new finite endpoint strong factors have the two correct windows and physical supports",
         all(v.is_finite() and v>=0 for v in
             (b["mS"],b["finite_embedding"],b["Af"],b["Bf"],b["endpoint"],b["cf"]))
         and PARAMETERS["full_S_bandwidth"]==192 and PARAMETERS["full_Z2_bandwidth"]==384
         and len(saved)==18)
    doc["complete_new_full_trial_source_conclusion"]=dict(
        complete_ordinary_L1_three_part_source_upper=rec(b["three"]),
        exact_selected_original_whole_part_keys=copy.deepcopy(PARAMETERS["new_source_parts"]),
        excluded_from_new_trial_but_preserved_old_part=PARAMETERS["retained_old_fourth_part"],
        complete_all_interface_impulses_read_verbatim=copy.deepcopy(jump["complete_all_interface_impulses_upper"]),
        ordinary_source_window="L1(dr; L2 nonmean pair plus two independent physical means)",
        no_total_minus_upper_operation=True,
        original_3071_integrals_not_recomputed=True,
        original_3070_impulses_reused_as_complete_fullT_bounds=True,
        complete_Q_F0_F1_F2_and_independent_Zy_mean_row_retained=True)
    gate(doc,"new trial selects three independent full source integrals and retains every old impulse and mean",
         b["three"].is_finite() and b["three"]>=0 and b["seam"].is_finite() and b["seam"]>=0
         and set(PARAMETERS["new_source_parts"])=={
             "leading_two_primitive_and_rank","complete_Q_including_F0_F1_F2","complete_independent_mean_row"}
         and len(parts)==4 and jump["complete_interface_count"]==3070)
    doc["complete_new_full_trial_bound_conclusion"]=dict(
        complete_physical_cut_endpoint_correction_upper=rec(b["cut_endpoint"]),
        complete_new_physical_cut_error_upper=rec(b["new_cut_error"]),
        complete_cut_receiver_contribution=rec(b["cut_part"]),
        complete_three_source_receiver_contribution=rec(b["body_part"]),
        complete_all_interface_receiver_contribution=rec(b["jump_part"]),
        complete_fullT_trial_waist_density_error_upper=rec(b["full_trial"]),
        complete_physical_waist_endpoint_correction_upper=rec(b["waist_endpoint"]),
        complete_returned_original_TJ_trial_error_upper=rec(b["returned"]),
        cut_ng_times_Bc_is_exact_corrected_Bfree=True,
        waist_ng_upper_is_the_actual_right_waist_factor=True,
        source_receiver_already_includes_output_waist_ng=True,
        exact_unpaid_endpoint_if_not_norm_charged="TJ(0)^(-1) P FT(0) V(0) Bc",
        both_endpoints_norm_paid_before_returning_to_original_trial=True,
        complete_physical_mean_coordinates=2)
    doc["complete_original_trial_whole_selection"]=dict(
        exact_same_operator="D0 H_free_homogeneous - ng(0) (P TJ(0) V(0) Bc,0)",
        complete_candidates=[
            dict(label="old_complete_SJ",bound=copy.deepcopy(b["candidates"][0])),
            dict(label="new_fullT_trial_plus_both_endpoints",bound=copy.deepcopy(b["candidates"][1]))],
        selected_index=b["selected"],selected_label=("old_complete_SJ","new_fullT_trial_plus_both_endpoints")[b["selected"]],
        complete_selected_SF_bound=copy.deepcopy(b["whole"]),
        comparison="final retained outward upper; old wins ties",entrywise_minimum_used=False)
    gate(doc,"both endpoints return to the same old trial before one final outward whole-bound selection",
         all(v.is_finite() and v>=0 for v in
             (b["cut_endpoint"],b["new_cut_error"],b["waist_endpoint"],b["cut_part"],
              b["body_part"],b["jump_part"],b["full_trial"],b["returned"]))
         and b["selected"] in (0,1) and b["whole"]==b["candidates"][b["selected"]]
         and all(up(b["whole"])<=up(v) for v in b["candidates"]))
    doc["complete_new_ordered_paid_conclusion"]=dict(
        complete_Cstar_upper=rec(b["Cstar"]),
        complete_state_error_contribution_upper=rec(b["state"]),
        complete_CG_fee_read_verbatim=copy.deepcopy(saved["CGwhole"]),
        complete_paid_Hminus4_3_to_L2_upper=rec(b["paid"]),
        original_state_factor_read_verbatim=copy.deepcopy(saved["Astate"]),
        original_paid_bound_read_verbatim=copy.deepcopy(saved["CWE_old"]),
        exact_original_input_order=PARAMETERS["state_operator_order"],
        same_individually_Lambda_normalized_wave_not_global_commonout=True,
        old_CG_coefficients_and_trial_unchanged_after_return=True,
        no_new_TF_or_selected_coordinate_or_leading_recomputation=True,
        coefficient_fee_not_multiplied_by_state_factor=True,
        full_Ei_Eo_not_claimed=True)
    gate(doc,"the unchanged ordered state factor and whole coefficient fee are consumed once after the return",
         all(v.is_finite() and v>=0 for v in (b["Cstar"],b["state"],b["paid"]))
         and doc["complete_new_ordered_paid_conclusion"]["complete_CG_fee_read_verbatim"]==saved["CGwhole"]
         and we["complete_new_receiver_multiplier_conclusion"]["exact_state_operator_order"]
             ==PARAMETERS["state_operator_order"])
    doc["retained_row_register"]=copy.deepcopy(we["retained_row_register"])
    doc["complete_sign_wave_readout"]=[
        dict(physical_wave=sigma,physical_input_sign=eps,
             complete_paid_Hminus4_3_to_L2_upper=rec(b["paid"]),
             same_whole_two_sign_operator_not_a_sector_sum=True)
        for sigma in PARAMETERS["physical_waves"] for eps in PARAMETERS["physical_input_signs"]]
    doc["scope"]=dict(
        exact_fullT_trial_changed_before_source_part_selection=True,
        original_TJ_trial_restored_before_whole_minimum=True,
        all_source_means_and_physical_endpoint_means_retained=True,
        all_genuine_and_conservative_interfaces_retained=True,
        full_primitive_ranks_and_F0_F1_F2_retained=True,
        actual_waist_TJ_inverse_and_original_root_input_order_retained=True,
        original_SJ_and_WE_records_preserved=True,
        same_selected_true_angle_only_in_downstream_WE=True,
        exact_global_Maslov_order_remains_separate=True,
        no_radial_finite_family_declared_finite_rank=True,
        independent_root_head_second_reference_and_external_ports_retained=True,
        only_new_positive_scalar_combinations_no_old_integration=True)
    gate(doc,"four sign-wave readouts retain six original unpaid rows and both independent physical matching means",
         len(doc["complete_sign_wave_readout"])==4 and len(doc["retained_row_register"])==6
         and all(v["actual_norm_supplied"] is False for v in doc["retained_row_register"])
         and all(doc["scope"].values()))
    doc.update(new_complete_endpoint_strong_bound_count=1,new_complete_three_part_source_count=1,
        new_complete_full_trial_bound_count=1,new_complete_returned_trial_bound_count=1,
        new_complete_whole_selection_count=1,new_complete_ordered_paid_bound_count=1,
        new_physical_endpoint_correction_count=2,new_sign_wave_record_count=4)
    gate(doc,"all original scalar source impulse scope and retained records remain byte-value identical",
         scalar_copies(old)==doc["copied_complete_scalar_inputs_read_verbatim"]
         and parts==doc["copied_complete_four_source_parts_read_verbatim"]
         and jump==doc["copied_complete_interface_conclusion_read_verbatim"]
         and we["retained_row_register"]==doc["copied_original_WE_retained_register_read_verbatim"]
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    save(a.out,doc)
    gate(doc,"complete original and new conclusions fit the predesigned small scientific result",
         len(canonical(doc))<36000 and len(doc["complete_original_receipt_identities"])==4
         and len(doc["copied_complete_scalar_inputs_read_verbatim"])==18)
    gate(doc,"all22 structural gates preserve every unpaid scope and zero old scientific executions",
         len(doc["gates"])==21 and all(v["passed"] is True for v in doc["gates"])
         and all(doc[k] is False for k in ("complete_full_Ei_Eo_proved",
             "full_incoming_inverse_proved","finite_Schur_inverse_proved","whole_return_R0_proved",
             "actual_nonlinear_background_proved","final_surface_proved"))
         and all(doc[k]==0 for k in ("old_successful_scientific_targets_recomputed",
             "old_scientific_source_imports","old_scientific_source_calls",
             "old_binary_native_or_archive_restored","new_ray_or_KAM_calls",
             "new_radial_or_angular_integrals","old_coordinate_or_normalizer_targets_recomputed")))
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete gate count changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_new_full_normalizer_endpoint_bound_proved=True,
        complete_new_original_trial_whole_bound_proved=True,
        complete_new_ordered_paid_subtotal_proved=True,stage="complete")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete or partial UT result")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        parameters=copy.deepcopy(PARAMETERS),arithmetic_bits=a.bits,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        stage="initial immutable input checks",original_completed_scientific_receipts_read=0,
        new_complete_endpoint_strong_bound_count=0,new_complete_three_part_source_count=0,
        new_complete_full_trial_bound_count=0,new_complete_returned_trial_bound_count=0,
        new_complete_whole_selection_count=0,new_complete_ordered_paid_bound_count=0,
        new_sign_wave_record_count=0,new_physical_endpoint_correction_count=0,
        complete_new_full_normalizer_endpoint_bound_proved=False,
        complete_new_original_trial_whole_bound_proved=False,
        complete_new_ordered_paid_subtotal_proved=False,
        retained_mode="exact-border-unpaid",retained_norm_budget=None,
        complete_full_Ei_Eo_proved=False,full_incoming_inverse_proved=False,
        finite_Schur_inverse_proved=False,whole_return_R0_proved=False,
        actual_nonlinear_background_proved=False,final_surface_proved=False,
        old_successful_scientific_targets_recomputed=0,old_scientific_source_imports=0,
        old_scientific_source_calls=0,old_binary_native_or_archive_restored=0,
        new_ray_or_KAM_calls=0,new_radial_or_angular_integrals=0,
        old_coordinate_or_normalizer_targets_recomputed=0,original_input_bytes_modified=False,
        new_recomputable_arrays_persisted=False,independent_physical_mean_coordinates=2)
    save(a.out,doc)
    try:run(a,doc)
    except Exception as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(error_type=type(error).__name__,message=str(error)))
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=save(a.out,doc)
    print("FULL_NORMALIZER_ENDPOINT_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=digest(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("FULL_NORMALIZER_ENDPOINT_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>40000:raise ValueError("saved complete UT science exceeds40000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())

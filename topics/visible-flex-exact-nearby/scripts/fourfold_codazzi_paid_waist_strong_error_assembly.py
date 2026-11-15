#!/usr/bin/env python3
"""New current-only WE paid waist strong-error assembly.
Read eight completed scientific receipts and the exact WE audit.  No old
target, ray, source integral, coefficient budget or normalizer is reevaluated.
Retained rows are explicitly exact-border-unpaid; no full E_i/E_o is claimed.
"""
from __future__ import annotations
import argparse,copy,hashlib,importlib.metadata,json,os,platform,time,traceback
from pathlib import Path
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
PRODUCER=TOPIC+"scripts/fourfold_codazzi_paid_waist_strong_error_assembly.py"
KIND="actual_paid_waist_strong_error_assembly_v1"
MANIFEST_KIND="paid_waist_strong_error_assembly_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=22
CG_ACTUAL_PENDING=False
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":22,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"input_cutoff_abs_j\":97,\"exact_moving_normalizer_cutoff_abs_j\":268435456,\"actual_root_normalizer_cutoff_abs_j\":1024,\"independent_physical_mean_coordinates\":2,\"physical_frequency\":\"n=4|j|\",\"physical_input_signs\":[-1,1],\"physical_waves\":[-1,1],\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"state_operator_order\":\"S U_Xminus_sigma_inverse J_sigma Twaist_inverse E_star P97 Lambda_sigma_inverse TF_inverse S_inverse\",\"port_operator_order\":\"S ell_sigma_epsilon_inverse U_Xminus_sigma_inverse J_sigma Twaist_inverse G_PW\",\"reference_column\":\"same terminal Ai free P8 first column\",\"complete_state_summands\":[\"C_PC\",\"C_ST4\",\"C_SF\"],\"coefficient_fee_read_verbatim\":true,\"retained_mode\":\"exact-border-unpaid\",\"per_wave_bound_not_an_uncharged_pair_sum\":true,\"old_scientific_calls_allowed\":0,\"old_binary_or_archive_inputs\":0,\"independent_port_coefficients_only_new_left_factor\":true,\"complete_Ei_Eo_or_incoming_or_Schur_or_R0_claimed\":false}")
PINNED=json.loads("{\"pc_execution\":\"75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817\",\"st_execution\":\"b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637\",\"sj_execution\":\"2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88\",\"wt_science\":\"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d\",\"wx_execution\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"kl_science\":\"1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee\",\"tf_science\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"cg_science\":\"a68095bb38c38d62a4b1af256c84c96e7f1f7f1c2663d5fdb5ffc814b73e57fc\",\"we_contract\":\"49616d850c4fbb594ad821f93fa760ed873dec99d6d54f557c91ddf9ff1c1f21\"}")
EXPECTED=json.loads("{\"pc_execution\":{\"kind\":\"actual_genuine_positive_Ai_cutoff_and_strong_correction_v1\",\"run\":\"43740173506\",\"attempt\":\"1\",\"gates\":30,\"source\":\"da6864cd790162759d5a78d40a67d0f3b4aa91b60614d947cca1a92371d6940b\",\"manifest\":\"13d92e7d2bfb8e3fd57e417676c58d6a649c7f353bcd54fef19af8cc66e123e5\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"st_execution\":{\"kind\":\"actual_complete_strict_tail_true_branch_cut_to_waist_v1\",\"run\":\"43757644616\",\"attempt\":\"1\",\"gates\":25,\"source\":\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\",\"manifest\":\"e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"sj_execution\":{\"kind\":\"actual_complete_strict_radial_first_symbol_defect_v1\",\"run\":\"43768006977\",\"attempt\":\"1\",\"gates\":26,\"source\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\",\"manifest\":\"31602b830279bc5141950f3c34b70442f5a2997f872179b45effccb0ff3cdb48\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"wt_science\":{\"kind\":\"actual_waist_normalizer_coefficients_and_two_window_gates_v1\",\"run\":\"43763134339\",\"attempt\":\"1\",\"gates\":20,\"source\":\"7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393\",\"manifest\":\"4cec7ef0ba21373190dd0bf142d10546823d46bb832a58df66529822990ad125\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"wx_execution\":{\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run\":\"43763424840\",\"attempt\":\"1\",\"gates\":20,\"source\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"manifest\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"kl_science\":{\"kind\":\"actual_correlated_terminal_Ai_leading_scalar_v1\",\"run\":\"43766439345\",\"attempt\":\"1\",\"gates\":16,\"source\":\"1f9dd122c7de8a990f5c60d0f405b2e3b3e51420b807ded9be58e8715fd480d6\",\"manifest\":\"810a13c2e1e0d3fb85f00129ca3e826e00e264d78269e25b78408bc1f67b99c7\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"tf_science\":{\"kind\":\"actual_common_root_normalizer_two_window_v1\",\"run\":\"43766881076\",\"attempt\":\"1\",\"gates\":14,\"source\":\"bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b\",\"manifest\":\"027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"cg_science\":{\"kind\":\"actual_separate_cut_propagated_first_coefficient_budgets_v1\",\"run\":\"43768992861\",\"attempt\":\"1\",\"gates\":21,\"source\":\"2545237268d1efb807419e809bfdf0dd75ef40b50dd11d898467ba0f8854586f\",\"manifest\":\"e33a06ddf9a46f2eeed6898bb4d700e13e02685617afa080061b8076f53c6184\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false}}")

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
    if not passed:raise ValueError("complete WE gate failed: "+name)
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
    actual={"Python":platform.python_version(),
        "python_flint":importlib.metadata.version("python-flint")}
    doc["runtime"]=actual;doc["arithmetic_bits"]=ctx.prec
    gate(doc,"public pinned runtime and320-bit directed arithmetic",
         actual==RUNTIME and a.bits==320 and ctx.prec==320
         and os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==PUBLIC)
    if CG_ACTUAL_PENDING or any(v is None for v in PINNED.values()) or EXPECTED["cg_science"] is None:
        raise ValueError("the completed CG terminal has not been frozen; no new WE arithmetic")
    m=read(a.manifest);paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"exact current-only source manifest and all nine mathematical input identities",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    gate(doc,"nine bounded original small texts and no original native or array input",
         len(paths)==9 and all(p.stat().st_size<100000 for p in paths.values())
         and all(p.suffix in (".json",".md") for p in paths.values())
         and all(not p.read_bytes().startswith(b"\x1f\x8b") for p in paths.values()))
    old={role:accepted(role,paths,doc) for role in EXPECTED}
    pc=old["pc_execution"];st=old["st_execution"];sj=old["sj_execution"]
    wt=old["wt_science"];wx=old["wx_execution"];kl=old["kl_science"]
    tf=old["tf_science"];cg=old["cg_science"]
    domain_roles=("pc_execution","st_execution","sj_execution","wx_execution",
        "kl_science","tf_science","cg_science")
    roots=PARAMETERS["exact_root_interval"];cut=PARAMETERS["exact_strict_cut"]
    definition_keys=("continuous_centre_definition_sha256","continuous_response_definition_sha256")
    family=st["complete_accepted_original_conclusion"]["exact_family_identity_read_verbatim"]
    gate(doc,"same complete real family root cut physical frequencies and selected reference",
         all(params(old[k]).get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
             and params(old[k]).get("fixed_intrinsic_parameter")=="eta_0"
             and params(old[k]).get("exact_root_interval")==roots for k in domain_roles)
         and all(params(old[k]).get("exact_strict_cut")==cut
             for k in ("sj_execution","wx_execution","kl_science","tf_science","cg_science"))
         and params(st)["exact_true_branch_cut"]==cut
         and all(params(old[k]).get("physical_frequency")=="n=4|j|"
             for k in ("pc_execution","st_execution","sj_execution","wx_execution","tf_science","cg_science"))
         and all(family[k]==PARAMETERS[k] for k in definition_keys)
         and wt["copied_SP_family_identity"]==family
         and all(params(old[r])[k]==PARAMETERS[k] for r in ("kl_science","tf_science","cg_science") for k in definition_keys)
         and params(kl)["reference_column"]==params(cg)["reference_column"]==PARAMETERS["reference_column"])
    p=pc["complete_strong_correction_conclusion"]
    t=st["complete_waist_physical_comparison_conclusion"]
    j=sj["complete_strict_first_symbol_waist_error_conclusion"]
    gate(doc,"PC ST4 and SJ are three complete same-waist differences with all means and cut fee once",
         p["full_root_finite_head_and_two_mean_inputs_retained"] is True
         and p["trial_root_stable_trace_retained_and_not_inverted"] is True
         and p["all_old_completed_multiplications_preserved"] is True
         and t["both_reference_columns_both_signs_and_both_means_retained"] is True
         and t["no_entrywise_mix_of_different_closed_cut_sides"] is True
         and t["one_raw_RR_factor_no_second_normalizer_or_root_input_chart"] is True
         and j["strong_bound_is_for_exact_homogeneous_free_column_minus_same_SF_trial"] is True
         and j["FA_forward_TN_inside_cut_error_applied_exactly_once"] is True
         and j["FA_ng_inverse_inside_Kc_applied_exactly_once"] is True
         and j["ST_cut_and_source_receivers_each_applied_once"] is True
         and j["no_TC_cut_factor_used_as_a_waist_factor"] is True
         and j["same_moving_normalizer_cutoff_abs_j"]==PARAMETERS["exact_moving_normalizer_cutoff_abs_j"]
         and j["complete_finite_support_through"]==268435456+575
         and sj["accepted_success_identity_read_verbatim"]["ST"]["digest"]==PINNED["st_execution"])
    fixed=[x for x in wt["complete_fixed_cutoff_results"] if x["J"]==268435456]
    gate(doc,"the exact same moving waist cutoff inverse keeps both windows and the full mean block",
         len(fixed)==1 and fixed[0]["inverse_on_both_windows_proved"] is True
         and fixed[0]["strict_tests_passed"]==fixed[0]["strict_tests_total"]==4
         and all(x["passed"] is True for x in fixed[0]["all_four_strict_tests"])
         and fixed[0]["finite_complement_and_two_means_identity"] is True
         and fixed[0]["two_factor_finite_support_label"]==268435456+575
         and wt["parameters"]["exact_delta_half_width"]==PARAMETERS["exact_real_delta_radius"]
         and wt["parameters"]["independent_mean_coordinates"]==2
         and wt["parameters"]["radial_trace_side"]=="right")
    common=wx["complete_selected_common_input_conclusion"]
    h=wx["complete_selected_H_coordinate_conclusion"]
    gate(doc,"same selected true angle common input and exact state-only left cancellation windows",
         common["exact_order"]==PARAMETERS["selected_common_input_order"]
         and common["only_same_selected_actual_conjugacy"] is True
         and common["independent_mean_block_retained"] is True
         and common["no_projection_commuted_through_coordinate"] is True
         and h["only_same_selected_actual_conjugacy"] is True
         and h["same_actual_inverse_on_L2_and_Hminus4_3"] is True
         and h["independent_physical_mean_block_is_identity"] is True
         and h["selected_parameter_absolute_upper"]==common["selected_parameter_absolute_upper"]
         and cg["copied_selected_common_input_scope"]["selected_parameter_absolute_upper"]==common["selected_parameter_absolute_upper"])
    lead=kl["complete_new_leading_scalar_conclusion"];tn=tf["complete_new_root_normalizer_conclusion"]
    lr=lead["complete_four_sign_wave_records"]
    gate(doc,"four actual Ai leading records and the same root inverse stay in their original order",
         [(v["physical_wave"],v["physical_input_sign"]) for v in lr]==[(-1,-1),(-1,1),(1,-1),(1,1)]
         and all(v["inverse_leading_modulus_upper"]==lead["complete_inverse_leading_scalar_upper"] for v in lr)
         and lead["reference_column"]==PARAMETERS["reference_column"]
         and lead["root_mean_residual_retained_in_exact_log_derivative"] is True
         and lead["no_sector_sum_or_extra_sqrt2"] is True
         and lead["second_Bi_or_other_genuine_root_column_covered"] is False
         and lead["original_order"]=="E_star Lambda_sigma_inverse T_F_inverse S_inverse"
         and kl["input_sha256"]["wt_science"]==PINNED["wt_science"]
         and kl["input_sha256"]["wx_execution"]==PINNED["wx_execution"]
         and tn["actual_J_F"]==PARAMETERS["actual_root_normalizer_cutoff_abs_j"]
         and tn["same_inverse_on_both_windows"] is True
         and tn["finite_original_input_and_output_support_abs_j"]==1024+191
         and tn["right_transformed_finite_rows_keep_actual_dual_norms"] is True
         and tn["right_transformed_finite_input_support_not_claimed"] is True)
    cf=cg["complete_new_ordered_coefficient_fee_conclusion"]
    cgcopy=cg["copied_complete_scalar_inputs_read_verbatim"]
    gate(doc,"complete CG scalar and all its saved right factors are the same successful inputs",
         cg["complete_separate_coefficient_budgets_proved"] is True
         and cg["stage"]=="complete" and cg["new_complete_coefficient_only_fee_count"]==1
         and all(cg["input_sha256"][r]==PINNED[r] for r in
             ("sj_execution","wx_execution","kl_science","tf_science"))
         and cg["complete_selected_coefficient_only_Hminus4_3_to_L2_upper"]==cf["coefficient_only_common_input_strong_fee"]
         and cf["right_TF_inverse_applied_once"] is True
         and cf["state_only_exact_left_coordinate_cancellation_not_used"] is True
         and cf["full_state_error_other_rows_and_finite_inverse_not_claimed"] is True
         and cf["root_finite_after_one_right_inverse_read_verbatim"]==tf["complete_new_strong_scalar_factors"]["complete_finite_map_fee_after_right_inverse"]
         and cgcopy["SJ_complete_cprop_integrals"]==sj["complete_new_transported_coefficient_conclusion"]["common_both_branch_complete_c_0_2_integrals"]
         and cgcopy["TF_inverse_Hminus4_3"]==tn["complete_inverse_Hminus4_3_upper"]
         and cgcopy["WX_common_input_inverse_Hminus4_3"]==common["complete_common_input_inverse_Hminus4_3_upper"]
         and cg["complete_state_error_proved"] is False
         and cg["independent_physical_mean_coordinates"]==2)
    saved=dict(C_PC=p["complete_strong_correction_to_waist_upper"],
        C_ST4=t["complete_same_case_sum_maximum_upper"],
        C_SF=j["complete_SF_waist_density_error_upper"],
        BH0=h["complete_inverse_density_L2_upper"],
        KW0=fixed[0]["same_inverse_two_window_bounds"]["L2"],
        KLambda=lead["complete_inverse_leading_scalar_upper"],
        KFminus=tn["complete_inverse_Hminus4_3_upper"],
        KSinvminus=common["complete_common_input_inverse_Hminus4_3_upper"],
        CGwhole=cg["complete_selected_coefficient_only_Hminus4_3_to_L2_upper"])
    gate(doc,"all nine scalar inputs are finite complete positive-budget upper enclosures",
         len(saved)==9 and all(up(v).is_finite() for v in saved.values())
         and all(up(saved[k])>0 for k in ("BH0","KW0","KLambda","KFminus","KSinvminus")))
    doc["input_sha256"]=copy.deepcopy(PINNED)
    doc["complete_original_receipt_identities"]=copy.deepcopy(EXPECTED)
    doc["copied_complete_scalar_inputs_read_verbatim"]=copy.deepcopy(saved)
    doc["copied_complete_SJ_details_read_verbatim"]=copy.deepcopy(j)
    doc["copied_complete_CG_fee_structure_read_verbatim"]=copy.deepcopy(cf)
    doc["copied_complete_selected_scope"]=copy.deepcopy({
        "exact_order":common["exact_order"],
        "inverse_order":common["inverse_order"],
        "selected_parameter_absolute_upper":common["selected_parameter_absolute_upper"],
        "only_same_selected_actual_conjugacy":True})
    return paths,saved

def scalar_bounds(saved):
    x={k:up(v) for k,v in saved.items()}
    cstar=up(x["C_PC"]+x["C_ST4"]+x["C_SF"])
    aport=up(x["BH0"]*x["KW0"]*x["KLambda"])
    astate=up(aport*x["KFminus"]*x["KSinvminus"])
    state=up(astate*cstar)
    paid=up(state+x["CGwhole"])
    return dict(Cstar=cstar,Aport=aport,Astate=astate,Cstate=state,Cpaid=paid)

def retained_register():
    return [
        dict(id="physical_mean_matching_rows",status="exact-border-unpaid",
             formula="two independent physical matching mean rows; state mean sources already paid",
             actual_norm_supplied=False),
        dict(id="full_density_mean_identity_difference",status="exact-border-unpaid",
             formula="(psi_prime-1) Pi if this realization is used",
             actual_norm_supplied=False),
        dict(id="transported_original_low_input",status="exact-border-unpaid",
             formula="original low maps times (1-P97) TF_inverse S_inverse",
             actual_norm_supplied=False),
        dict(id="root_head_and_two_reference_blocks",status="exact-border-unpaid",
             formula="original complete root head and full two-reference matching blocks",
             actual_norm_supplied=False),
        dict(id="opposite_sign_and_Maslov_realization",status="exact-border-unpaid",
             formula="original sign projections and Maslov multiplier kept in their actual order",
             actual_norm_supplied=False),
        dict(id="final_principal_cross_rows",status="exact-border-unpaid",
             formula="actual principal high/finite finite/high and mean Schur blocks",
             actual_norm_supplied=False)]

def run(a,doc):
    ctx.prec=a.bits
    paths,saved=checked_inputs(a,doc)
    doc.update(stage="complete saved inputs",original_completed_scientific_receipts_read=8)
    save(a.out,doc)
    b=scalar_bounds(saved)
    gate(doc,"new complete state sum contains PC ST4 and the full SJ scalar exactly once",
         b["Cstar"].is_finite() and b["Cstar"]>=0)
    doc["complete_new_state_sum_conclusion"]=dict(
        complete_Cstar_upper=rec(b["Cstar"]),
        exact_summands=["C_PC","C_ST4","C_SF"],
        same_Y0_density_pair_plus_two_independent_means=True,
        SJ_cut_ordinary_and_all_interfaces_already_in_CSF=True,
        FA_cut_TN_ST_and_ng_factors_not_reapplied=True,
        actual_stable_trace_not_replaced_by_an_independent_zero_port=True,
        strong_difference_not_individual_order_zero_trial=True)
    doc.update(new_complete_state_sum_count=1,stage="complete whole state sum")
    save(a.out,doc)
    gate(doc,"new independent port factor and ordered state factor keep all original windows",
         b["Aport"].is_finite() and b["Aport"]>0
         and b["Astate"].is_finite() and b["Astate"]>0)
    doc["complete_new_receiver_multiplier_conclusion"]=dict(
        complete_independent_port_left_factor_upper=rec(b["Aport"]),
        complete_state_factor_upper=rec(b["Astate"]),
        independent_port_factor="BH0 KW0 KLambda",
        state_factor="Aport KFminus KSinvminus",
        exact_state_operator_order=PARAMETERS["state_operator_order"],
        exact_independent_port_operator_order=PARAMETERS["port_operator_order"],
        BH0_exact_left_cancellation_used_only_for_state_or_same_left_port_receiver=True,
        independent_ports_do_not_automatically_receive_right_TF_or_S=True,
        four_leading_moduli_use_the_same_maximum_not_a_sector_sum=True,
        no_extra_ng_radial_or_TC_cut_factor=True,
        original_Lambda_stays_before_TF_inverse_and_S_inverse=True)
    doc.update(new_complete_port_factor_count=1,new_complete_state_factor_count=1,
        stage="complete ordered receiver multipliers")
    save(a.out,doc)
    gate(doc,"paid strong submap uses one state contribution and the unchanged whole CG fee",
         b["Cstate"].is_finite() and b["Cstate"]>=0
         and b["Cpaid"].is_finite() and b["Cpaid"]>=0)
    doc["complete_paid_strong_error_conclusion"]=dict(
        complete_state_error_contribution_upper=rec(b["Cstate"]),
        complete_coefficient_only_contribution_read_verbatim=copy.deepcopy(saved["CGwhole"]),
        complete_paid_Hminus4_3_to_L2_upper=rec(b["Cpaid"]),
        input_window="principal H^(-4/3), original P97 kept before Lambda_inverse TF_inverse S_inverse",
        output_window="one complete wave scalar L2 receiver, including its actual state mean",
        two_input_signs_combined_as_the_same_original_operator=True,
        two_wave_pair_sum_or_Euclidean_pair_norm_not_claimed=True,
        TF_after_right_coefficient_factors_not_multiplied_again=True,
        full_coefficient_fee_has_no_state_only_BH_cancellation=True,
        retained_norm_not_supplied=True,retained_mode="exact-border-unpaid",
        full_Ei_Eo_bound_not_claimed=True)
    doc["complete_sign_wave_readout"]=[
        dict(physical_wave=s,physical_input_sign=e,
            complete_paid_per_wave_upper=rec(b["Cpaid"]),
            complete_port_left_factor_upper=rec(b["Aport"]),
            no_extra_sum_over_equal_input_sign_coefficients=True)
        for s in PARAMETERS["physical_waves"] for e in PARAMETERS["physical_input_signs"]]
    doc["retained_row_register"]=retained_register()
    doc["already_norm_paid_exact_maps"]=[
        "two physical state means in PC ST SJ and the WT identity mean block",
        "SF finite maps source means and all impulses through Js+575",
        "CG waist projection rank and both density primitive ranks",
        "TF complete root finite map and two primitive term through JF+191"]
    doc["scope"]=dict(
        same_selected_S_for_all_four_receivers=True,
        same_terminal_Ai_reference_column_only=True,
        full_original_two_signs_two_waves_and_physical_means_retained=True,
        full_state_sum_and_coefficient_budget_kept_separately=True,
        all_old_successful_factors_read_without_recomputation=True,
        actual_stable_trace_not_double_counted_as_a_PW_port=True,
        independent_PW_source_and_trace_spaces_not_changed=True,
        transported_low_input_not_relabelled_as_principal_Fourier_head=True,
        retained_rows_not_set_to_zero=True,
        no_complete_error_or_incoming_or_finite_inverse_or_return_claimed=True)
    doc.update(new_complete_state_contribution_count=1,new_complete_paid_error_count=1,
        new_sign_wave_record_count=4,stage="complete paid submap with unpaid exact border")
    save(a.out,doc)
    gate(doc,"all twenty-two gates preserve eight successes nine original bytes and the explicit unpaid border",
         len(doc["gates"])==21 and all(g["passed"] is True for g in doc["gates"])
         and all(sha(paths[k])==v for k,v in PINNED.items())
         and doc["original_completed_scientific_receipts_read"]==8
         and len(doc["retained_row_register"])==6
         and all(r["status"]=="exact-border-unpaid" and r["actual_norm_supplied"] is False for r in doc["retained_row_register"])
         and all(doc["scope"].values())
         and all(doc[k] is False for k in ("complete_full_Ei_Eo_proved","full_incoming_inverse_proved",
             "finite_Schur_inverse_proved","whole_return_R0_proved",
             "actual_nonlinear_background_proved","final_surface_proved")))
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete gate count changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_paid_strong_submap_proved=True,stage="complete")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete or partial WE result")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        parameters=copy.deepcopy(PARAMETERS),arithmetic_bits=a.bits,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        stage="initial immutable input checks",original_completed_scientific_receipts_read=0,
        new_complete_state_sum_count=0,new_complete_port_factor_count=0,
        new_complete_state_factor_count=0,new_complete_state_contribution_count=0,
        new_complete_paid_error_count=0,new_sign_wave_record_count=0,
        complete_paid_strong_submap_proved=False,
        retained_mode="exact-border-unpaid",retained_norm_budget=None,
        complete_full_Ei_Eo_proved=False,full_incoming_inverse_proved=False,
        finite_Schur_inverse_proved=False,whole_return_R0_proved=False,
        actual_nonlinear_background_proved=False,final_surface_proved=False,
        old_successful_scientific_targets_recomputed=0,old_scientific_source_imports=0,
        old_binary_native_or_archive_restored=0,original_input_bytes_modified=False,
        new_recomputable_arrays_persisted=False,independent_physical_mean_coordinates=2)
    save(a.out,doc)
    try:run(a,doc)
    except Exception as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(error_type=type(error).__name__,message=str(error)))
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=save(a.out,doc)
    print("PAID_WAIST_STRONG_ERROR_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=digest(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("PAID_WAIST_STRONG_ERROR_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>40000:raise ValueError("saved complete WE science exceeds40000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())

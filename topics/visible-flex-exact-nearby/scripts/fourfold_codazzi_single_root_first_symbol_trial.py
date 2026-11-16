#!/usr/bin/env python3
"""New SW single complete root first-symbol trial, from five completed small receipts.
Only new positive scalar combinations are evaluated. Original enclosures,
rays, integrals, jumps, normalizers and all successful targets remain frozen.
The complete Q and both means remain; only whole paid objects are compared.
"""
from __future__ import annotations
import argparse,copy,hashlib,importlib.metadata,json,os,platform,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
PRODUCER=TOPIC+"scripts/fourfold_codazzi_single_root_first_symbol_trial.py"
KIND="actual_single_complete_root_first_symbol_trial_v1"
MANIFEST_KIND="single_complete_root_first_symbol_trial_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=24
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":24,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_complete_radial_interval\":[\"0\",\"76285779072683/320000000000000\"],\"input_cutoff_abs_j\":97,\"exact_moving_normalizer_cutoff_abs_j\":268435456,\"physical_frequency\":\"n=4|j|\",\"independent_physical_mean_coordinates\":2,\"physical_input_signs\":[-1,1],\"physical_waves\":[-1,1],\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"state_operator_order\":\"S U_Xminus_sigma_inverse J_sigma Twaist_inverse E_star P97 Lambda_sigma_inverse TF_inverse S_inverse\",\"retained_mode\":\"exact-border-unpaid\",\"reference_column\":\"same terminal Ai free P8 first column\",\"new_trial\":\"(P T W,0)\",\"returned_trial\":\"(P TJ W,0)\",\"exact_single_first_symbol\":\"W=A(1+M_C I)Lc with complete C including Fstar and full mean\",\"exact_source\":\"(P[T DW-Q W], -Zy T W)\",\"complete_Q_F0_F1_T1F2_retained\":true,\"old_CG_reuse\":\"forward domination of identified positive terms\",\"original_source_rows\":3071,\"original_interface_rows\":3070,\"original_genuine_joins\":2549,\"original_conservative_refinements\":521,\"whole_selection\":\"compare final retained outward complete paid upper; old wins ties\",\"source_bound\":\"one complete global maximum times exact rc\",\"jump_bound\":\"all3070 interfaces times a complete one-sided two-Z maximum; no length\",\"old_scientific_calls_allowed\":0,\"new_grid_integrals_or_array_inputs\":0,\"new_complete_global_ordinary_source_bound_count\":1,\"full_Ei_Eo_or_incoming_or_Schur_or_R0_claimed\":false}")
PINNED=json.loads("{\"fa_science\":\"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2\",\"wx_execution\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"sj_execution\":\"2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88\",\"cg_science\":\"a68095bb38c38d62a4b1af256c84c96e7f1f7f1c2663d5fdb5ffc814b73e57fc\",\"ut_science\":\"3817fbeca91e87e63298cc3e52161af6167465eef62b9af3d3b4da3940ce139e\",\"sw_contract\":\"72bb6b3c9a7ae6ac660ded4d08ac67a986a43d58fcd3d1d7a95e3deb14d0ae6d\",\"sj_source\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\",\"cg_source\":\"2545237268d1efb807419e809bfdf0dd75ef40b50dd11d898467ba0f8854586f\"}")
EXPECTED=json.loads("{\"fa_science\":{\"kind\":\"actual_complete_free_Airy_first_omitted_cut_scalars_v1\",\"run\":\"43763658978\",\"attempt\":\"1\",\"gates\":24,\"source\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"manifest\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\",\"runtime\":{\"Python\":\"3.12.14\",\"arithmetic_bits\":320,\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"wx_execution\":{\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run\":\"43763424840\",\"attempt\":\"1\",\"gates\":20,\"source\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"manifest\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"sj_execution\":{\"kind\":\"actual_complete_strict_radial_first_symbol_defect_v1\",\"run\":\"43768006977\",\"attempt\":\"1\",\"gates\":26,\"source\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\",\"manifest\":\"31602b830279bc5141950f3c34b70442f5a2997f872179b45effccb0ff3cdb48\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"cg_science\":{\"kind\":\"actual_separate_cut_propagated_first_coefficient_budgets_v1\",\"run\":\"43768992861\",\"attempt\":\"1\",\"gates\":21,\"source\":\"2545237268d1efb807419e809bfdf0dd75ef40b50dd11d898467ba0f8854586f\",\"manifest\":\"e33a06ddf9a46f2eeed6898bb4d700e13e02685617afa080061b8076f53c6184\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"ut_science\":{\"kind\":\"actual_full_normalizer_endpoint_replacement_v1\",\"run\":\"43776528869\",\"attempt\":\"1\",\"gates\":22,\"source\":\"0144305da1dc2587be8801ef2f2175530e7f3e8e5cee0c670677f522550a0afc\",\"manifest\":\"983ffcea0cf9a03899cdd56143e4dce6784b482194dcf7445322b280d5bc905f\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false}}")
CONSUMED=json.loads("{\"a0\":[\"fa_science\",\"complete_new_first_frame_and_leading_conclusion\",\"complete_common_each_sign_each_branch_A0_angular_jets\",0],\"z0\":[\"fa_science\",\"complete_new_first_frame_and_leading_conclusion\",\"complete_phase_reciprocal_angular_jets\",0],\"ngc_lower\":[\"fa_science\",\"complete_new_first_frame_and_leading_conclusion\",\"same_cut_ng_lower_read_verbatim\"],\"Ucut_minus\":[\"fa_science\",\"complete_new_first_frame_and_leading_conclusion\",\"complete_U_Phi_Hminus4_3_upper_read_verbatim\"],\"v0\":[\"wx_execution\",\"complete_ungauged_leading_flow_conclusion\",\"complete_reverse_L2_upper\"],\"vminus\":[\"wx_execution\",\"complete_ungauged_leading_flow_conclusion\",\"complete_reverse_Hminus4_3_upper\"],\"Mchi\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_derivative_upper\"],\"Fchi\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_second_derivative_upper\"],\"m13\":[\"cg_science\",\"complete_new_multiplier_conclusion\",\"complete\",\"Hminus1_3\"],\"m43\":[\"cg_science\",\"complete_new_multiplier_conclusion\",\"complete\",\"Hminus4_3\"],\"ephase\":[\"cg_science\",\"complete_new_dual_row_conclusion\",\"phase_derivative_deviation\"],\"Hc2\":[\"cg_science\",\"complete_new_dual_row_conclusion\",\"inverse_second_derivative_upper\"],\"CI2dual\":[\"cg_science\",\"complete_new_dual_row_conclusion\",\"C_I2_L2_to_H4_3_upper\"],\"bcut0\":[\"sj_execution\",\"complete_new_transported_coefficient_conclusion\",\"common_both_branch_b_0_2_maxima\",0],\"t0\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"t0\"],\"tminus\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"tm\"],\"qstar\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"qstar\"],\"zstar\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"zstar\"],\"t10\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_finite_and_two_primitive_scalar_maxima\",\"t10\"],\"Zmax\":[\"sj_execution\",\"complete_new_radial_coefficient_conclusion\",\"complete_matrix_row_column_A0_maxima\",\"Z\"],\"FT\":[\"ut_science\",\"complete_new_endpoint_strong_conclusion\",\"complete_FT_Hminus4_3_to_L2_upper\"],\"Ecut\":[\"ut_science\",\"complete_new_full_trial_bound_conclusion\",\"complete_new_physical_cut_error_upper\"],\"ng0\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"ng0_upper\"],\"Gcut\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"Gcut\"],\"Gsource\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"Gsource\"],\"Astate\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"Astate\"],\"C_PC\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"C_PC\"],\"C_ST4\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"C_ST4\"],\"CGwhole\":[\"ut_science\",\"copied_complete_scalar_inputs_read_verbatim\",\"CGwhole\"],\"oldpaid\":[\"ut_science\",\"complete_new_ordered_paid_conclusion\",\"complete_paid_Hminus4_3_to_L2_upper\"]}")

def canonical(x):
    return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True,allow_nan=False)+"\n").encode()
def digest(x):return hashlib.sha256(x).hexdigest()
def sha(path):return digest(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def save(path,doc):
    raw=canonical(doc);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp");temp.write_bytes(raw);os.replace(temp,path)
    return raw
def gate(doc,name,passed):
    doc["gates"].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ValueError("complete SW gate failed: "+name)
def ball(value):
    x=arb(value["ball"]) if isinstance(value,dict) else arb(value)
    if not x.is_finite():raise ValueError("nonfinite complete scalar")
    return x
def up(value):
    x=ball(value).upper()
    if not x>=0:raise ValueError("negative positive-budget upper")
    return x
def lower(value):
    x=ball(value).lower()
    if not x>0:raise ValueError("a required true lower denominator is not positive")
    return x
def sqrt_up(x):return up(up(x).sqrt())
def ex(value):
    q=Fraction(value);return arb(q.numerator)/q.denominator
def rec(x):return {"ball":x.str(72)}
def params(x):return x["parameters"] if "parameters" in x else x["mathematical_parameters"]
def lookup(x,path):
    for key in path:x=x[key]
    return x
def scalar_copies(old):
    return {key:copy.deepcopy(lookup(old,path)) for key,path in CONSUMED.items()}

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
    gate(doc,"eight exact current mathematical texts source parameters and manifest are frozen",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    gate(doc,"only bounded current small texts and no arrays archives or old scientific imports",
         len(paths)==8 and all(p.stat().st_size<100000 for p in paths.values())
         and all(p.suffix in (".json",".md",".py") for p in paths.values())
         and all(not p.read_bytes().startswith(b"\x1f\x8b") for p in paths.values()))
    old={role:accepted(role,paths,doc) for role in EXPECTED}
    fa=old["fa_science"];wx=old["wx_execution"];sj=old["sj_execution"]
    cg=old["cg_science"];ut=old["ut_science"]
    gate(doc,"same full real repaired family original cut intrinsic parameter physical labels and input97",
         all(params(x)["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
             and params(x)["fixed_intrinsic_parameter"]=="eta_0"
             and params(x)["exact_strict_cut"]==PARAMETERS["exact_strict_cut"]
             and params(x)["physical_frequency"]=="n=4|j|" for x in old.values())
         and all(params(x)["input_cutoff_abs_j"]==97 for x in (fa,sj,cg,ut))
         and all(params(x)["exact_complete_radial_interval"]==PARAMETERS["exact_complete_radial_interval"]
             for x in (wx,sj,ut))
         and params(cg)["reference_column"]==params(fa)["reference_column"]==params(ut)["reference_column"]
             ==PARAMETERS["reference_column"]
         and all(params(x)[k]==PARAMETERS[k] for x in (cg,ut)
             for k in ("continuous_centre_definition_sha256","continuous_response_definition_sha256"))
         and params(sj)["exact_moving_normalizer_cutoff_abs_j"]
             ==params(ut)["exact_moving_normalizer_cutoff_abs_j"]==268435456)
    frame=fa["complete_new_first_frame_and_leading_conclusion"]
    gate(doc,"FA complete own leading amplitudes true forward cut density and both input signs retain all cut errors",
         len(frame["complete_common_each_sign_each_branch_A0_angular_jets"])==3
         and len(frame["complete_phase_reciprocal_angular_jets"])==3
         and frame["input_cutoff_abs_j"]==97 and frame["moving_normalizer_cutoff_abs_j"]==268435456
         and params(fa)["physical_signs"]==[-1,1] and params(fa)["oscillatory_branches"]==[-1,1]
         and frame["vector_H2_is_scalar_component_sum"] is True
         and frame["inverse_U_Phi_Hminus4_3_not_substituted"] is True
         and frame["FS_is_norm_paid_not_deleted"] is True
         and frame["independent_external_physical_means_and_all_finite_cross_blocks_retained"] is True
         and frame["waist_leading_receiver_incoming_outgoing_or_full_R0_claimed"] is False)
    flow=wx["complete_shorter_flow_derivative_conclusion"]
    lead=wx["complete_ungauged_leading_flow_conclusion"]
    gate(doc,"WX leading reverse windows and true inverse flow hold on every shorter interval without hidden ng",
         flow["every_shorter_interval_and_both_orientations"] is True
         and flow["both_characteristic_branches_share_maximum_bound"] is True
         and flow["inverse_flow_has_its_own_same_directed_bounds"] is True
         and flow["true_radial_interval"]==PARAMETERS["exact_complete_radial_interval"]
         and lead["all_shorter_subintervals_and_both_branches"] is True
         and lead["true_radial_interval"]==PARAMETERS["exact_complete_radial_interval"]
         and lead["reverse_orientation"]=="b<=a"
         and lead["ungauged_primitive_density_convention"] is True
         and lead["ng_endpoint_ratio_not_absorbed_or_inverted"] is True
         and wx["scope"]["waist_and_shorter_flow_bounds_on_whole_original_real_family"] is True)
    radial=sj["complete_new_radial_coefficient_conclusion"]
    body=sj["complete_original_body_and_polynomial_conclusion"]
    trans=sj["complete_new_transported_coefficient_conclusion"]
    jump=sj["complete_new_interface_conclusion"]
    gate(doc,"SJ complete global Q including T1F2 two means and all3070 original interface locations remain",
         radial["exact_moving_Js"]==268435456 and radial["full_finite_support_through"]==268435456+575
         and radial["full_F0_F1_F2_FT_FJ_and_Zy_mean_rows_retained"] is True
         and radial["complete_branch_entry_sums_before_functional"] is True
         and body["original_consumed_rows"]==3071
         and body["exact_consumed_interval"]==PARAMETERS["exact_complete_radial_interval"]
         and trans["new_ordinary_integrals_use_true_radial_lengths_once"] is True
         and trans["all_complete_coefficient_means_retained"] is True
         and trans["general_composed_coefficients_not_assigned_finite_Fourier_support"] is True
         and trans["constant_C_global_bound_used_in_every_source_and_interface_row"] is True
         and len(trans["common_both_branch_b_0_2_maxima"])==3
         and len(trans["common_both_branch_complete_c_0_2_integrals"])==3
         and jump["complete_interface_count"]==3070 and jump["genuine_polynomial_join_count"]==2549
         and jump["conservative_artificial_refinement_count"]==521
         and jump["exact_S_continuity_is_from_pinned_repaired_and_intrinsic_definitions"] is True
         and jump["intrinsic_qrr_betar_gammar_and_physical_mean_r_jumps_all_retained"] is True
         and jump["no_radial_length_factor"] is True)
    cgsaved=cg["copied_complete_scalar_inputs_read_verbatim"]
    cgfee=cg["complete_new_ordered_coefficient_fee_conclusion"]
    gate(doc,"CG same FA SJ WX chain uses complete positive partial-integral multipliers and full coefficient-only fee",
         all(cg["input_sha256"][role]==PINNED[role]
             for role in ("fa_science","sj_execution","wx_execution"))
         and cgsaved["FA_inverse_phase_jets"]==frame["complete_phase_reciprocal_angular_jets"]
         and cgsaved["FA_same_cut_ng_lower"]==frame["same_cut_ng_lower_read_verbatim"]
         and cgsaved["SJ_complete_cprop_integrals"]==trans["common_both_branch_complete_c_0_2_integrals"]
         and cg["scope"]["complete_real_family_coefficients_and_full_means_retained"] is True
         and cg["scope"]["no_total_upper_subtracted_to_obtain_a_summand"] is True
         and cg["scope"]["selected_common_input_only_not_a_family_of_conjugacies"] is True
         and cg["complete_new_multiplier_conclusion"]["complete"]["zero_mode_and_scalar_component_convention_retained"] is True
         and cgfee["right_TF_inverse_applied_once"] is True
         and cgfee["state_only_exact_left_coordinate_cancellation_not_used"] is True
         and cgfee["coefficient_only_common_input_strong_fee"]
             ==cg["complete_selected_coefficient_only_Hminus4_3_to_L2_upper"])
    uc=ut["copied_complete_scalar_inputs_read_verbatim"]
    ep=ut["complete_new_endpoint_strong_conclusion"]
    ub=ut["complete_new_full_trial_bound_conclusion"]
    paid=ut["complete_new_ordered_paid_conclusion"]
    gate(doc,"UT identical cut full endpoint norm actual waist state order and original coefficient fee are read once",
         ut["input_sha256"]["fa_science"]==PINNED["fa_science"]
         and ut["input_sha256"]["sj_execution"]==PINNED["sj_execution"]
         and uc["CGwhole"]==cg["complete_selected_coefficient_only_Hminus4_3_to_L2_upper"]
         and uc["Gcut"]==sj["complete_saved_scalar_inputs_read_verbatim"]["ST_cut_receiver_read_verbatim"]
         and uc["Gsource"]==sj["complete_saved_scalar_inputs_read_verbatim"]["ST_general_primitive_mean_source_receiver_read_verbatim"]
         and uc["vminus"]==lead["complete_reverse_Hminus4_3_upper"]
         and uc["Z2_A0"]==radial["complete_matrix_row_column_A0_maxima"]["Z"]
         and ep["same_closed_interval_upper_used_at_both_endpoints"] is True
         and ep["full_T_inverse_not_assumed"] is True
         and ep["exact_FT_input_and_output_support"]==268435456+575
         and ub["cut_ng_times_Bc_is_exact_corrected_Bfree"] is True
         and ub["waist_ng_upper_is_the_actual_right_waist_factor"] is True
         and ub["source_receiver_already_includes_output_waist_ng"] is True
         and paid["exact_original_input_order"]==PARAMETERS["state_operator_order"]
         and paid["same_individually_Lambda_normalized_wave_not_global_commonout"] is True
         and ut["copied_complete_selected_scope_read_verbatim"]["exact_order"]==PARAMETERS["selected_common_input_order"]
         and ut["copied_complete_selected_scope_read_verbatim"]["only_same_selected_actual_conjugacy"] is True
         and ut["retained_mode"]=="exact-border-unpaid" and ut["retained_norm_budget"] is None
         and ut["complete_full_Ei_Eo_proved"] is False and ut["full_incoming_inverse_proved"] is False
         and len(ut["retained_row_register"])==6
         and all(v["actual_norm_supplied"] is False for v in ut["retained_row_register"]))
    sjtext=paths["sj_source"].read_text();cgtext=paths["cg_source"].read_text()
    proof=paths["sw_contract"].read_text()
    gate(doc,"frozen positive algorithms and exact single-symbol contract are read as text without old import",
         all(s in sjtext for s in ('def transported_coefficient_bounds(',
             'C[k]=up(C[k]+length*transported[k])',
             'common_both_branch_b_0_2_maxima=encode(bmax)',
             'complete_Q_including_F0_F1_F2=up(g["Kc"]*t["qstar"]*g["vm"]*cf)',
             'complete_independent_mean_row=up(g["Kc"]*t["zstar"]*t["tm"]*g["vm"]*cf)'))
         and all(s in cgtext for s in ('def cut_and_propagated_coefficients(',
             'cp=vec(saved["SJ_complete_cprop_integrals"])',
             'total=[upper(cut[k]+transported[k]) for k in range(3)]',
             'Cproj=upper((1+BX)*Ralg+BX*dual["complete_IC_H4_3"])'))
         and all(s in proof for s in (r"\tag{SW.6}",r"\tag{SW.12}",r"\tag{SW.16}",
             r"\tag{SW.25}",r"\tag{SW.26}",r"\tag{SW.29a}",r"\tag{SW.30}",r"\tag{SW.32}")))
    saved=scalar_copies(old)
    gate(doc,"all thirty original scalar records are finite positive budgets with a true ng lower denominator",
         len(saved)==30 and all(up(v).is_finite() for v in saved.values())
         and lower(saved["ngc_lower"])>0
         and all(up(cgfee[k]).is_finite() for k in
             ("algebra_complete","complete_waist_projection_fee","coefficient_only_common_input_strong_fee")))
    doc["complete_original_receipt_identities"]={
        role:dict(info=copy.deepcopy(EXPECTED[role]),original_file_sha256=PINNED[role],
            complete_science_canonical_sha256=digest(canonical(old[role]))) for role in EXPECTED}
    doc["original_completed_scientific_receipts_read"]=5
    doc["input_sha256"]=copy.deepcopy(PINNED)
    return old,paths,saved

def complete_minimum(records):
    best=0
    for i in range(1,len(records)):
        if up(records[i])<up(records[best]):best=i
    return best,copy.deepcopy(records[best])

def scalar_bounds(saved):
    """Only SW positive scalar combinations. No old source or coefficient is evaluated."""
    x={k:up(v) for k,v in saved.items()}
    nglower=lower(saved["ngc_lower"])
    CI2=arb(17)/16
    Lc=up(sqrt_up(arb(2))*x["a0"]*x["z0"]/nglower)
    A0=up(x["v0"]*sqrt_up(1+x["ephase"]))
    Aminus=up(x["vminus"]*x["Ucut_minus"])
    broot=up(x["z0"]*x["bcut0"])
    H2=up(x["Fchi"]*x["z0"]**2+x["Mchi"]*x["Hc2"])
    pdual=up(x["CI2dual"]*H2);pinf=up(H2/8)
    Froot=up(broot*(pdual+pinf))
    cf=up(1+x["m43"]/4)
    Wminus=up(Aminus*cf*Lc)
    two=up(CI2*broot*x["m13"]);ranks=up(Froot*cf)
    DW=up(A0*(two+ranks)*Lc)
    rc=ex(PARAMETERS["exact_strict_cut"])
    leading=up(rc*x["t0"]*DW)
    Qpart=up(rc*x["qstar"]*Wminus)
    meanpart=up(rc*x["zstar"]*x["tminus"]*Wminus)
    body=up(leading+Qpart+meanpart)
    jump=up(arb(PARAMETERS["original_interface_rows"])*x["t10"]*CI2*(2*x["Zmax"])*Wminus)
    waist=up(x["ng0"]*x["FT"]*Wminus)
    cut_contribution=up(x["Gcut"]*x["Ecut"])
    body_contribution=up(x["Gsource"]*body)
    jump_contribution=up(x["Gsource"]*jump)
    fulltrial=up(cut_contribution+body_contribution+jump_contribution)
    compressed=up(fulltrial+waist)
    Cstar=up(x["C_PC"]+x["C_ST4"]+compressed)
    state=up(x["Astate"]*Cstar)
    paid=up(state+x["CGwhole"])
    candidates=[copy.deepcopy(saved["oldpaid"]),rec(paid)]
    selected,whole=complete_minimum(candidates)
    return dict(Lc=Lc,A0=A0,Aminus=Aminus,broot=broot,H2=H2,pdual=pdual,pinf=pinf,
        Froot=Froot,cf=cf,Wminus=Wminus,two=two,ranks=ranks,DW=DW,
        leading=leading,Qpart=Qpart,meanpart=meanpart,body=body,jump=jump,
        waist=waist,cut_contribution=cut_contribution,body_contribution=body_contribution,
        jump_contribution=jump_contribution,fulltrial=fulltrial,compressed=compressed,
        Cstar=Cstar,state=state,paid=paid,candidates=candidates,selected=selected,whole=whole)

def finite_nonnegative(values):
    return all(v.is_finite() and v>=0 for v in values)

def run(a,doc):
    ctx.prec=a.bits
    old,paths,saved=checked_inputs(a,doc)
    sj=old["sj_execution"];cg=old["cg_science"];ut=old["ut_science"]
    doc["copied_complete_scalar_inputs_read_verbatim"]=copy.deepcopy(saved)
    doc["copied_complete_SJ_transported_conclusion"]=copy.deepcopy(sj["complete_new_transported_coefficient_conclusion"])
    doc["copied_complete_SJ_interface_conclusion"]=copy.deepcopy(sj["complete_new_interface_conclusion"])
    doc["copied_complete_CG_positive_fee_conclusion"]=copy.deepcopy(cg["complete_new_ordered_coefficient_fee_conclusion"])
    doc["copied_complete_CG_multiplier_complete"]=copy.deepcopy(cg["complete_new_multiplier_conclusion"]["complete"])
    doc["copied_complete_selected_scope"]=copy.deepcopy(ut["copied_complete_selected_scope_read_verbatim"])
    doc["retained_row_register"]=copy.deepcopy(ut["retained_row_register"])
    doc["stage"]="new single complete root first-symbol scalar combinations"
    save(a.out,doc)
    b=scalar_bounds(saved)
    doc["complete_new_leading_and_conjugation_conclusion"]=dict(
        complete_forward_root_leading_column_upper=rec(b["Lc"]),
        complete_root_leading_L2_upper=rec(b["A0"]),
        complete_root_leading_Hminus4_3_upper=rec(b["Aminus"]),
        complete_root_b_Linfty_upper=rec(b["broot"]),
        complete_root_inverse_phase_second_derivative_upper=rec(b["H2"]),
        complete_root_displacement_H4_3_upper=rec(b["pdual"]),
        complete_root_displacement_Linfty_upper=rec(b["pinf"]),
        complete_root_two_rank_strong_upper=rec(b["Froot"]),
        complete_single_C_negative_factor=rec(b["cf"]),
        complete_W_Hminus4_3_upper=rec(b["Wminus"]),
        complete_ordered_two_primitive_inside_DW_upper=rec(b["two"]),
        complete_ordered_two_rank_inside_DW_upper=rec(b["ranks"]),
        complete_DW_Hminus4_3_to_L2_upper=rec(b["DW"]),
        Lc_sqrt2_only_for_two_physical_waves=True,
        input_signs_orthogonal_before_coefficient_and_coordinate_maps=True,
        complete_CT_C_includes_Fstar_and_scalar_mean=True,
        actual_forward_leading_not_inverse_of_KL_upper=True,
        full_C_bounds_on_every_shorter_interval_from_original_positive_integrals=True,
        no_leading_or_sign_factor_commuted_through_C_TF_or_selected_S=True)
    gate(doc,"new forward leading uses true denominator and the two correctly directed complete windows",
         finite_nonnegative([b[k] for k in ("Lc","A0","Aminus")])
         and lower(saved["ngc_lower"])>0)
    gate(doc,"new complete root conjugation retains both ranks full C and their correct two-primitive windows",
         finite_nonnegative([b[k] for k in ("broot","H2","pdual","pinf","Froot","cf","Wminus","two","ranks","DW")]))
    doc["complete_new_source_and_interface_conclusion"]=dict(
        complete_ordinary_leading_defect_L1_upper=rec(b["leading"]),
        complete_ordinary_Q_F0_F1_T1F2_L1_upper=rec(b["Qpart"]),
        complete_ordinary_independent_mean_L1_upper=rec(b["meanpart"]),
        complete_ordinary_L1_source_upper=rec(b["body"]),
        complete_all_interface_impulses_upper=rec(b["jump"]),
        exact_ordinary_radial_interval=copy.deepcopy(PARAMETERS["exact_complete_radial_interval"]),
        complete_interface_count=3070,complete_genuine_interface_count=2549,
        complete_conservative_interface_count=521,
        both_genuine_and_artificial_locations_retained=True,
        jump_has_no_radial_length_factor=True,
        every_jump_uses_complete_two_one_sided_Z_bounds=True,
        original_full_Q_including_F0_F1_T1F2_retained=True,
        full_Zy_mean_row_retained=True,
        original_SJ_source_integrals_and_jump_sum_not_reused_for_changed_W=True,
        original_successful_source_integrals_and_jump_sum_not_recomputed=True,
        source_window="L1(dr; L2 nonmean pair plus two independent physical means)")
    gate(doc,"new complete global source and all3070 jumps keep full Q two means and exactly one body length",
         finite_nonnegative([b[k] for k in ("leading","Qpart","meanpart","body","jump")])
         and PARAMETERS["original_interface_rows"]==3070)
    doc["complete_new_full_and_compressed_trial_conclusion"]=dict(
        original_fullT_cut_error_read_verbatim=copy.deepcopy(saved["Ecut"]),
        original_complete_FT_strong_upper_read_verbatim=copy.deepcopy(saved["FT"]),
        complete_cut_receiver_contribution=rec(b["cut_contribution"]),
        complete_ordinary_source_receiver_contribution=rec(b["body_contribution"]),
        complete_all_interface_receiver_contribution=rec(b["jump_contribution"]),
        complete_fullT_singleW_waist_error_upper=rec(b["fulltrial"]),
        complete_physical_waist_FT_W_correction_upper=rec(b["waist"]),
        complete_TJ_singleW_waist_error_upper=rec(b["compressed"]),
        cut_trial_is_exactly_the_same_Bc=True,
        physical_cut_error_and_original_FA_ranks_read_once=True,
        source_receiver_already_contains_output_waist_ng=True,
        waist_ng_times_FT_W_paid_once=True,
        inverse_is_only_same_actual_TJ_not_full_T=True,
        intermediate_SF_bounds_for_different_trials_not_compared=True,
        complete_physical_mean_coordinates=2)
    gate(doc,"same cut plus new waist endpoint pay both ends before actual same-Js waist normalization",
         finite_nonnegative([b[k] for k in ("cut_contribution","body_contribution","jump_contribution","fulltrial","waist","compressed")])
         and doc["complete_new_full_and_compressed_trial_conclusion"]["original_fullT_cut_error_read_verbatim"]==saved["Ecut"])
    doc["complete_new_ordered_paid_conclusion"]=dict(
        complete_Cstar_singleW_upper=rec(b["Cstar"]),
        complete_state_error_singleW_upper=rec(b["state"]),
        complete_CG_fee_read_verbatim=copy.deepcopy(saved["CGwhole"]),
        complete_paid_singleW_Hminus4_3_to_L2_upper=rec(b["paid"]),
        original_state_factor_read_verbatim=copy.deepcopy(saved["Astate"]),
        CG_fee_reused_by_identified_positive_addend_domination=True,
        original_Ralg_not_subtracted_from_a_total_upper=True,
        changed_trial_state_and_coefficient_difference_exactly_recombine=True,
        state_only_left_angle_cancellation_not_applied_to_coefficient_fee=True,
        coefficient_fee_not_multiplied_by_state_factor_or_second_KF=True,
        exact_original_input_order=PARAMETERS["state_operator_order"],
        same_individually_normalized_branch_not_global_commonout=True,
        complete_Ei_Eo_not_claimed=True)
    doc["complete_paid_whole_selection"]=dict(
        exact_same_object="same individually Lambda-normalized actual paid branch; six retained rows unchanged",
        complete_candidates=[
            dict(label="old_complete_UTA_paid",bound=copy.deepcopy(b["candidates"][0])),
            dict(label="new_single_complete_root_first_symbol_paid",bound=copy.deepcopy(b["candidates"][1]))],
        selected_index=b["selected"],
        selected_label=("old_complete_UTA_paid","new_single_complete_root_first_symbol_paid")[b["selected"]],
        complete_selected_paid_bound=copy.deepcopy(b["whole"]),
        comparison="final retained outward upper; old wins ties",
        entrywise_minimum_used=False,different_trial_SF_minimum_used=False)
    gate(doc,"only complete same-actual paid candidates are compared after original CG and ordered state assembly",
         finite_nonnegative([b[k] for k in ("Cstar","state","paid")])
         and b["selected"] in (0,1) and b["whole"]==b["candidates"][b["selected"]]
         and all(up(b["whole"])<=up(v) for v in b["candidates"])
         and doc["complete_new_ordered_paid_conclusion"]["complete_CG_fee_read_verbatim"]==saved["CGwhole"])
    doc["complete_sign_wave_readout"]=[
        dict(physical_wave=sigma,physical_input_sign=eps,
             complete_selected_paid_Hminus4_3_to_L2_upper=copy.deepcopy(b["whole"]),
             same_whole_two_sign_operator_not_a_sector_sum=True)
        for sigma in PARAMETERS["physical_waves"] for eps in PARAMETERS["physical_input_signs"]]
    doc["scope"]=dict(
        same_terminal_Ai_and_original_root_input_not_a_different_basis=True,
        full_CT_coefficient_root_finite_part_and_scalar_mean_retained=True,
        complete_second_normalizer_and_Q_F0_F1_T1F2_retained=True,
        same_original_Bc_and_complete_cut_error=True,
        complete_changed_trial_source_and_all_interfaces_paid=True,
        same_WT_Js_inverse_after_new_physical_waist_FT_correction=True,
        only_complete_actual_paid_candidates_compared=True,
        no_old_source_integral_or_successful_target_repeated=True,
        complete_old_CG_positive_budget_used_without_subtracting_upper=True,
        two_physical_means_and_all_six_retained_rows_remain=True,
        selected_common_angle_only_at_same_original_selected_parameter=True,
        exact_Maslov_commonout_and_all_infinite_other_sign_blocks_remain_separate=True,
        no_radial_family_declared_finite_rank=True,
        incoming_finite_inverse_nonlinear_state_and_R0_not_claimed=True)
    gate(doc,"four sign-wave readouts preserve all six original unpaid rows both physical means and exact global order",
         len(doc["complete_sign_wave_readout"])==4 and len(doc["retained_row_register"])==6
         and all(v["actual_norm_supplied"] is False for v in doc["retained_row_register"])
         and all(doc["scope"].values()))
    doc.update(new_complete_leading_column_bound_count=1,new_complete_root_conjugation_bound_count=1,
        new_complete_global_ordinary_source_bound_count=1,new_complete_global_interface_bound_count=1,
        new_complete_changed_trial_bound_count=1,new_complete_waist_endpoint_correction_count=1,
        new_complete_ordered_paid_bound_count=1,new_complete_whole_paid_selection_count=1,
        new_sign_wave_record_count=4,saved_original_scalar_record_count=30)
    gate(doc,"all original scalar records scopes and retained rows remain unchanged and every input hash still matches",
         saved==scalar_copies(old)
         and doc["copied_complete_scalar_inputs_read_verbatim"]==saved
         and doc["copied_complete_SJ_transported_conclusion"]==sj["complete_new_transported_coefficient_conclusion"]
         and doc["copied_complete_CG_positive_fee_conclusion"]==cg["complete_new_ordered_coefficient_fee_conclusion"]
         and doc["retained_row_register"]==ut["retained_row_register"]
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    save(a.out,doc)
    gate(doc,"all24 structural gates fit the complete small receipt and leave every unproved scope false",
         len(doc["gates"])==23 and all(g["passed"] is True for g in doc["gates"])
         and len(canonical(doc))<39000
         and len(doc["complete_original_receipt_identities"])==5
         and len(doc["copied_complete_scalar_inputs_read_verbatim"])==30
         and all(doc[k] is False for k in ("complete_full_Ei_Eo_proved","full_incoming_inverse_proved",
             "finite_Schur_inverse_proved","whole_return_R0_proved","actual_nonlinear_background_proved","final_surface_proved"))
         and all(doc[k]==0 for k in ("old_successful_scientific_targets_recomputed","old_scientific_source_imports",
             "old_scientific_source_calls","old_binary_native_or_archive_restored",
             "new_ray_or_KAM_calls","new_radial_or_angular_grid_integrals","old_coordinate_or_normalizer_targets_recomputed")))
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete SW gate count changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_new_single_root_first_symbol_bound_proved=True,
        complete_new_ordered_paid_subtotal_proved=True,stage="complete")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete or partial SW result")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        parameters=copy.deepcopy(PARAMETERS),arithmetic_bits=a.bits,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        stage="initial immutable input checks",original_completed_scientific_receipts_read=0,
        saved_original_scalar_record_count=0,new_complete_leading_column_bound_count=0,
        new_complete_root_conjugation_bound_count=0,new_complete_global_ordinary_source_bound_count=0,
        new_complete_global_interface_bound_count=0,new_complete_changed_trial_bound_count=0,
        new_complete_waist_endpoint_correction_count=0,new_complete_ordered_paid_bound_count=0,
        new_complete_whole_paid_selection_count=0,new_sign_wave_record_count=0,
        complete_new_single_root_first_symbol_bound_proved=False,complete_new_ordered_paid_subtotal_proved=False,
        retained_mode="exact-border-unpaid",retained_norm_budget=None,
        complete_full_Ei_Eo_proved=False,full_incoming_inverse_proved=False,finite_Schur_inverse_proved=False,
        whole_return_R0_proved=False,actual_nonlinear_background_proved=False,final_surface_proved=False,
        old_successful_scientific_targets_recomputed=0,old_scientific_source_imports=0,old_scientific_source_calls=0,
        old_binary_native_or_archive_restored=0,new_ray_or_KAM_calls=0,new_radial_or_angular_grid_integrals=0,
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
    print("SINGLE_ROOT_FIRST_SYMBOL_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=digest(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("SINGLE_ROOT_FIRST_SYMBOL_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>40000:raise ValueError("saved complete SW science exceeds40000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())

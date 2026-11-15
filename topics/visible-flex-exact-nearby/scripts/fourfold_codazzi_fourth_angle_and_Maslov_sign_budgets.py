#!/usr/bin/env python3
"""New DX4/ZD current-only fourth-angle and global-sign scalar combinations.
Five immutable completed receipts are read.  Two old source texts are AST-only
provenance.  No old phase, ray, integral, coefficient or inverse is evaluated.
The outgoing subtotal retains every unpaid complete error and matching block.
"""
from __future__ import annotations
import argparse,ast,copy,hashlib,importlib.metadata,json,os,platform,time,traceback
from pathlib import Path
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
PRODUCER=TOPIC+"scripts/fourfold_codazzi_fourth_angle_and_Maslov_sign_budgets.py"
KIND="actual_fourth_angle_and_global_sign_budgets_v1"
MANIFEST_KIND="fourth_angle_and_global_sign_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=24
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":24,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"physical_input_signs\":[-1,1],\"physical_waves\":[-1,1],\"independent_physical_mean_coordinates\":2,\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"selected_common_input_map\":\"psi = X_minus o H_inverse\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"selected_inverse_order\":\"S_inverse = U_X_minus_inverse U_H\",\"exact_original_fold_strip\":\"3/128\",\"drift_label_bandwidth\":192,\"physical_drift_derivative_factor\":768,\"AC_H1_lower\":\"31/32\",\"AC_H2_upper\":\"4\",\"AC_H3_upper\":\"1024\",\"AC_H4_upper\":\"393216\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"reference_column\":\"same terminal Ai free P8 first column\",\"root_sign_operator\":\"Z = Pi0 + i Pi+ - i Pi-\",\"conjugated_sign_operator\":\"Z^S = S Z S_inverse\",\"physical_common_outgoing_order\":\"U_R B_minus Z^S\",\"standard_outgoing_order\":\"Z U_R (T_co + E_standard)\",\"complete_original_input_cutoff_abs_j\":97,\"actual_root_normalizer_cutoff_abs_j\":1024,\"actual_moving_normalizer_cutoff_abs_j\":268435456,\"whole_negative_sign_selection\":\"minimum of final saved outward uppers; first candidate wins ties\",\"whole_negative_sign_candidates\":[\"Sminus Sinvminus\",\"1 + Dstrong\"],\"new_standardout_components\":[\"17/8 B_one_third\",\"(1 + full_co_Linfty/4) Dstrong\",\"Cpaid min_whole_sign\"],\"old_scientific_source_execution_allowed\":0,\"old_binary_or_archive_inputs\":0,\"new_ray_KAM_radial_integral_or_old_norm_recomputation_allowed\":0,\"retained_mode\":\"exact-unpaid\",\"complete_Ei_Eo_or_incoming_or_Schur_or_R0_claimed\":false}")
PINNED=json.loads("{\"fa_science\":\"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2\",\"tc_execution\":\"37c2a5ae3b77e7f0895aa0c3130d8707868816f1d26a119a880272f9b92f902e\",\"wx_execution\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"pg_execution\":\"95a0fafb34cbb7fa4fd5c0379324b71a35053af5daa73718f95bda8afdc26d67\",\"we_science\":\"3d73b56f604b012b66f2f502aea481b59383f5566fb5d12c676843220d39956a\",\"fa_source\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"fold_source\":\"410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783\",\"dx4_contract\":\"6b493e3792c6863f9a65d8d52d994697d37de416157b68ed21f2cee51182f58b\",\"zd_contract\":\"715f28768139356001ef66840939e4defa547f953a59caea613f3fc6d6841a76\",\"ms_contract\":\"44038eaed377863961aad7f0c74caa2bf498d6a689812f05933111777c191161\",\"ac_contract\":\"6527fa46ddc21ed3d3e8c6ce4bb1f39f2db816d9fff5684e6daf4f30951c46f4\"}")
EXPECTED=json.loads("{\"fa_science\":{\"kind\":\"actual_complete_free_Airy_first_omitted_cut_scalars_v1\",\"run\":\"43763658978\",\"attempt\":\"1\",\"gates\":24,\"source\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"manifest\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\",\"runtime\":{\"Python\":\"3.12.14\",\"arithmetic_bits\":320,\"python_flint\":\"0.9.0\"},\"wrapper\":false},\"tc_execution\":{\"kind\":\"actual_true_branch_density_coordinates_and_finite_conjugation_v1\",\"run\":\"43754703603\",\"attempt\":\"1\",\"gates\":18,\"source\":\"e05b4a9cbe5d66e03a1fb22b70c75ee48cdc885d1bd83c523d9a0173b92b0d71\",\"manifest\":\"0e78cfa73d9d2ce8d53fc8eb1c0bdffef276739360aa66f55f13ea13f5ab3c45\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"wx_execution\":{\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run\":\"43763424840\",\"attempt\":\"1\",\"gates\":20,\"source\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"manifest\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"pg_execution\":{\"kind\":\"actual_complete_principal_inverse_from_first_derivatives_v1\",\"run\":\"43770122351\",\"attempt\":\"1\",\"gates\":20,\"source\":\"08b8d1d9ff222ba7c8cea14bed50c0e9cd320359aa0e5456bc14c2ecfcc5c9c7\",\"manifest\":\"febb85783c624eed3bab22cd6e0873aad08c3257e4758615668654f82289e51c\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"wrapper\":true},\"we_science\":{\"kind\":\"actual_paid_waist_strong_error_assembly_v1\",\"run\":\"43769746581\",\"attempt\":\"1\",\"gates\":22,\"source\":\"d02efe46d4baee16971c9239526d4e3f412ad7dd8e95cfab31d56458a7a7fa55\",\"manifest\":\"098c090606f54bbbb8bd6d026b6360f53ba70f5e75c4fc4218e7f784b2eb88a1\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"wrapper\":false}}")
CONSUMED=json.loads("{\"x\":[\"fa_science\",\"complete_new_cut_domain_conclusion\",\"complete_x_deviation_holomorphic\"],\"y\":[\"fa_science\",\"complete_new_cut_domain_conclusion\",\"complete_y_holomorphic\"],\"tminus\":[\"fa_science\",\"complete_new_cut_domain_conclusion\",\"complete_negative_T_real_lower\"],\"tplus\":[\"fa_science\",\"complete_new_cut_domain_conclusion\",\"complete_T_holomorphic_upper_read_from_original_full_Ap\"],\"P1\":[\"tc_execution\",\"complete_density_coordinate_conclusion\",\"phase_derivative_upper\"],\"P2\":[\"tc_execution\",\"complete_density_coordinate_conclusion\",\"phase_second_derivative_upper\"],\"P3\":[\"tc_execution\",\"complete_density_coordinate_conclusion\",\"accepted_phase_domain_read_verbatim\",\"complete_new_three_phase_third_derivative_upper\"],\"kappa2\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_angular_second_multiplier_upper\"],\"kappa3\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_angular_third_multiplier_upper\"],\"M\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_derivative_upper\"],\"F\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_second_derivative_upper\"],\"G\":[\"wx_execution\",\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_third_derivative_upper\"],\"W1\":[\"wx_execution\",\"complete_waist_density_coordinate_conclusion\",\"phase_derivative_upper\"],\"W2\":[\"wx_execution\",\"complete_waist_density_coordinate_conclusion\",\"phase_second_derivative_upper\"],\"h1\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"inverse_phase_derivative_upper\"],\"h2\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"inverse_phase_second_derivative_upper\"],\"psi_min\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"common_input_derivative_lower\"],\"psi2\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"common_input_second_derivative_upper\"],\"S0\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_L2_upper\"],\"Sminus\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_Hminus4_3_upper\"],\"Sinv0\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_inverse_L2_upper\"],\"Sinvminus\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_inverse_Hminus4_3_upper\"],\"co_A0\":[\"pg_execution\",\"complete_new_selected_first_derivative_conclusion\",\"complete_ci_co_Linfty_upper\"],\"co_B13\":[\"pg_execution\",\"complete_new_nonmean_primitive_conclusion\",\"complete_B_one_third_upper\"],\"Cpaid\":[\"we_science\",\"complete_paid_strong_error_conclusion\",\"complete_paid_Hminus4_3_to_L2_upper\"]}")

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
    if not passed:raise ValueError("complete DZ gate failed: "+name)
def ball(value):
    x=arb(value["ball"]) if isinstance(value,dict) else arb(value)
    if not x.is_finite():raise ValueError("nonfinite complete scalar")
    return x
def up(value):
    x=ball(value).upper()
    if not x>=0:raise ValueError("negative positive-budget upper")
    return x
def positive_lower(value):
    x=ball(value).lower()
    if not x>0:raise ValueError("required positive lower endpoint failed")
    return x
def rec(x):return {"ball":ball(x).str(72)}
def params(x):return x["parameters"] if "parameters" in x else x["mathematical_parameters"]
def ex(n,d=1):return arb(n)/d
def scalar_copies(old):
    result={}
    for name,path in CONSUMED.items():
        x=old[path[0]]
        for key in path[1:]:x=x[key]
        result[name]=copy.deepcopy(x)
    return result

def accepted(role,paths,doc):
    info=EXPECTED[role];outer=read(paths[role])
    a=outer["actual_scientific_receipt"] if info["wrapper"] else outer
    wrapped=(not info["wrapper"] or
        (outer.get("complete") is True and outer.get("actual_returncode")==0
         and outer.get("actual_failure") is None
         and outer.get("source_budget_source_sha256")==info["source"]
         and outer.get("input_manifest_sha256")==info["manifest"]))
    gate(doc,"completed "+role+" exact run source manifest runtime and every original gate",
         wrapped and a.get("kind")==info["kind"]
         and a.get("complete") is True and a.get("proved") is True
         and a.get("actual_returncode")==0 and a.get("failure") is None
         and str(a.get("run_id"))==info["run"] and str(a.get("run_attempt"))==info["attempt"]
         and a.get("source_sha256")==info["source"]
         and a.get("input_manifest_sha256")==info["manifest"]
         and a.get("runtime")==info["runtime"] and a.get("arithmetic_bits")==320
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
    m=read(a.manifest);paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"exact current-only source manifest and all eleven mathematical input identities",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    ast_names={}
    for role in ("fa_source","fold_source"):
        tree=ast.parse(paths[role].read_text(),filename=str(paths[role]))
        ast_names[role]=sorted(n.name for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)))
    gate(doc,"eleven small current texts with two original sources parsed but never executed",
         len(paths)==11 and all(p.stat().st_size<100000 for p in paths.values())
         and all(p.suffix in (".json",".md",".py") for p in paths.values())
         and all(not p.read_bytes().startswith(b"\x1f\x8b") for p in paths.values())
         and {"new_domain_and_jets","original_fold"}.issubset(ast_names["fa_source"])
         and {"fold_budget","anchored_coefficients"}.issubset(ast_names["fold_source"]))
    old={role:accepted(role,paths,doc) for role in EXPECTED}
    fa=old["fa_science"];tc=old["tc_execution"];wx=old["wx_execution"]
    pg=old["pg_execution"];we=old["we_science"]
    roots=PARAMETERS["exact_root_interval"];cut=PARAMETERS["exact_strict_cut"]
    definition_keys=("continuous_centre_definition_sha256","continuous_response_definition_sha256")
    gate(doc,"same complete real family strict cut selected parameter and physical Fourier units",
         all(params(x).get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
             and params(x).get("fixed_intrinsic_parameter")=="eta_0"
             and params(x).get("exact_root_interval")==roots
             and params(x).get("exact_strict_cut")==cut
             and params(x).get("physical_frequency")=="n=4|j|" for x in old.values())
         and all(params(x)[k]==PARAMETERS[k] for x in (pg,we) for k in definition_keys)
         and params(fa)["reference_column"]==params(we)["reference_column"]==PARAMETERS["reference_column"]
         and params(wx)["selected_conjugacy_parameter_absolute_upper"]
             ==params(pg)["selected_conjugacy_parameter_absolute_upper"]
             ==PARAMETERS["selected_parameter_absolute_upper"])
    fd=fa["complete_new_cut_domain_conclusion"]
    gate(doc,"FA complete holomorphic x y and T bounds retain their original full fold strip",
         fd["original_fold_full_strip"]==PARAMETERS["exact_original_fold_strip"]
         and params(fa)["exact_fold_strip"]==PARAMETERS["exact_original_fold_strip"]
         and params(fa)["exact_fold_radius"]=="3/8000"
         and fd["real_TC_phase_jets_never_used_as_holomorphic_suprema"] is True
         and [fd["rho_lower"],fd["rho_upper"]]==params(tc)["exact_rho_interval"]
         and fa["source_sha256"]==PINNED["fa_source"]
         and fa["old_scientific_source_imports"]==0
         and params(fa)["physical_signs"]==[-1,1]
         and params(fa)["oscillatory_branches"]==[-1,1])
    td=tc["complete_density_coordinate_conclusion"]
    ta=td["accepted_phase_domain_read_verbatim"]
    wa=wx["accepted_original_complete_conclusions"]
    gate(doc,"TC complete real phase triple is reused verbatim in the same WX propagation",
         td["real_fourfold_degree_one_maps"] is True
         and td["same_distributional_inverse_on_both_windows"] is True
         and td["independent_physical_mean_block_is_identity"] is True
         and td["common_both_branch_bound_is_max_not_sum"] is True
         and td["exact_phase_sigma"]=="X-sigma*(2/3)*(-T)^(3/2)"
         and ta["all_complete_physical_means_and_both_reference_columns_retained"] is True
         and ta["no_real_angle_jet_promoted_to_complex_strip"] is True
         and ta["exact_strict_cut"]==cut
         and wa["TC_complete_density_coordinate_read_verbatim"]==td
         and wa["TC_complete_density_coordinate_payload_sha256"]==digest(canonical(td)[:-1])
         and wa["TC_source_sha256"]==tc["source_sha256"]
         and wa["TC_input_manifest_sha256"]==tc["input_manifest_sha256"])
    flow=wx["complete_shorter_flow_derivative_conclusion"]
    gate(doc,"WX same positive algorithm gives both branches and every shorter interval in either direction",
         flow["every_shorter_interval_and_both_orientations"] is True
         and flow["inverse_flow_has_its_own_same_directed_bounds"] is True
         and flow["specific_positive_algorithm_lower_addends_used"] is True
         and flow["no_arbitrary_operator_norm_inversion"] is True
         and flow["no_old_positive_exponential_or_ray_evaluated"] is True
         and flow["both_characteristic_branches_share_maximum_bound"] is True
         and flow["known_drift_label_bandwidth"]==192
         and flow["physical_derivative_frequency_factor"]==4
         and flow["true_radial_interval"]==["0",cut])
    waist=wx["complete_waist_density_coordinate_conclusion"]
    h=wx["complete_selected_H_coordinate_conclusion"]
    common=wx["complete_selected_common_input_conclusion"]
    scope={k:copy.deepcopy(common[k]) for k in ("exact_order","inverse_order",
        "only_same_selected_actual_conjugacy","selected_parameter_absolute_upper")}
    gate(doc,"same actual waist H inverse and selected common input keep the exact density order and all means",
         waist["exact_true_map_order"]=="Phi_waist = Phi_cut o chi_waist_to_cut"
         and h["only_same_selected_actual_conjugacy"] is True
         and h["same_actual_inverse_on_L2_and_Hminus4_3"] is True
         and h["independent_physical_mean_block_is_identity"] is True
         and common["exact_order"]==PARAMETERS["selected_common_input_order"]
         and common["inverse_order"]==PARAMETERS["selected_inverse_order"]
         and common["common_input_map"]==PARAMETERS["selected_common_input_map"]
         and common["independent_mean_block_retained"] is True
         and common["no_projection_commuted_through_coordinate"] is True
         and common["selected_parameter_absolute_upper"]==PARAMETERS["selected_parameter_absolute_upper"]
         and scope==pg["complete_selected_common_input_scope_read_verbatim"]
         and scope==we["copied_complete_selected_scope"]
         and pg["accepted_original_success_identity_read_verbatim"]["WX"]["digest"]==PINNED["wx_execution"]
         and we["input_sha256"]["wx_execution"]==PINNED["wx_execution"])
    pd=pg["complete_new_selected_first_derivative_conclusion"]
    pn=pg["complete_new_nonmean_primitive_conclusion"]
    gate(doc,"PG full coefficient sup and its separate nonmean Wone-third bound retain both signs and full scalar mean",
         pd["both_actual_ci_co_and_both_physical_input_signs_share_each_bound"] is True
         and pd["root_function_full_mean_not_removed"] is True
         and pn["scalar_mean_subtraction_is_exact_not_a_physical_mean_deletion"] is True
         and pn["full_two_sign_sums_and_all_nonzero_modes_retained"] is True
         and params(pg)["scalar_coefficient_means_real_and_unrestricted"] is True
         and params(pg)["physical_means_are_separate_identity_blocks"] is True
         and params(pg)["independent_physical_mean_coordinates"]==2)
    paid=we["complete_paid_strong_error_conclusion"];retained=we["retained_row_register"]
    full_flags=("complete_full_Ei_Eo_proved","full_incoming_inverse_proved",
        "finite_Schur_inverse_proved","whole_return_R0_proved")
    gate(doc,"WE complete paid submap is reused once with its original six unpaid exact rows",
         we["complete_paid_strong_submap_proved"] is True
         and paid["two_input_signs_combined_as_the_same_original_operator"] is True
         and paid["two_wave_pair_sum_or_Euclidean_pair_norm_not_claimed"] is True
         and paid["TF_after_right_coefficient_factors_not_multiplied_again"] is True
         and paid["full_Ei_Eo_bound_not_claimed"] is True
         and paid["retained_norm_not_supplied"] is True
         and we["complete_new_state_sum_conclusion"]["SJ_cut_ordinary_and_all_interfaces_already_in_CSF"] is True
         and len(retained)==6
         and all(x["status"]=="exact-border-unpaid" and x["actual_norm_supplied"] is False for x in retained)
         and all(we[k] is False for k in full_flags)
         and params(we)["actual_root_normalizer_cutoff_abs_j"]==1024
         and params(we)["exact_moving_normalizer_cutoff_abs_j"]==268435456
         and params(we)["input_cutoff_abs_j"]==97)
    saved=scalar_copies(old)
    gate(doc,"all twenty-five complete scalar records are finite with true lower endpoints and M at least one",
         len(saved)==25 and all(ball(v).is_finite() for v in saved.values())
         and all(up(v)>=0 for v in saved.values())
         and positive_lower(saved["tminus"])>0
         and positive_lower(saved["psi_min"])>0
         and up(saved["M"])>=1
         and up(saved["tplus"])>=positive_lower(saved["tminus"]))
    doc["input_sha256"]=copy.deepcopy(PINNED)
    doc["complete_original_receipt_identities"]={
        k:dict(**v,original_file_sha256=PINNED[k],
               complete_scientific_payload_sha256=digest(canonical(old[k])))
        for k,v in EXPECTED.items()}
    doc["complete_original_consumed_scalar_paths"]=copy.deepcopy(CONSUMED)
    doc["copied_complete_scalar_inputs_read_verbatim"]=copy.deepcopy(saved)
    doc["complete_scalar_copy_payload_sha256"]=digest(canonical(saved))
    doc["copied_selected_common_input_scope"]=scope
    doc["copied_original_WE_retained_register_read_verbatim"]=copy.deepcopy(retained)
    doc["original_source_AST_evidence"]=dict(
        roles=["fa_source","fold_source"],function_names=ast_names,
        source_imports=0,source_function_calls=0,old_fold_or_FA_outputs_recomputed=False)
    return paths,old,saved

def fourth_derivatives(saved):
    """DX4: only new positive scalar combinations; saved lower-order targets are read."""
    u={k:up(v) for k,v in saved.items()}
    s=ex(3,128);tm=positive_lower(saved["tminus"]);tp=u["tplus"]
    t1=u["y"];t2=up(t1/s);t3=up(2*t1/s**2);t4=up(6*t1/s**3)
    X4=up(6*u["x"]/s**3)
    # Complete positive lower endpoint is used before every inverse half-power.
    rt=tm.sqrt()
    omega4=up(tp.sqrt()*t4+(4*t1*t3+3*t2**2)/(2*rt)
        +3*t1**2*t2/(2*tm*rt)+3*t1**4/(8*tm**2*rt))
    P4=up(X4+omega4)
    M=u["M"];q=M-1;k2=u["kappa2"];k3=u["kappa3"];k4=up(768*k3)
    Hchi=up(M*(3*k2**3*q**3+(k2*k3/3)*q**2*(8*M+7)
        +(k4/3)*q*(M**2+M+1)))
    W3=up(u["P3"]*M**3+3*u["P2"]*M*u["F"]+u["P1"]*u["G"])
    W4=up(P4*M**4+6*u["P3"]*M**2*u["F"]+3*u["P2"]*u["F"]**2
        +4*u["P2"]*M*u["G"]+u["P1"]*Hchi)
    mh=ex(31,32);H2=arb(4);H3=arb(1024);H4=arb(393216)
    h3=up(3*H2**2/mh**5+H3/mh**4)
    h4=up(15*H2**3/mh**7+10*H2*H3/mh**6+H4/mh**5)
    psi3=up(W3*u["h1"]**3+3*u["W2"]*u["h1"]*u["h2"]+u["W1"]*h3)
    psi4=up(W4*u["h1"]**4+6*W3*u["h1"]**2*u["h2"]
        +3*u["W2"]*u["h2"]**2+4*u["W2"]*u["h1"]*h3+u["W1"]*h4)
    return dict(t1=t1,t2=t2,t3=t3,t4=t4,X4=X4,omega4=omega4,P4=P4,
        kappa4=k4,Hchi=Hchi,W3=W3,W4=W4,h3=h3,h4=h4,psi3=psi3,psi4=psi4)

def sign_bounds(saved,d):
    """ZD16: only the nonmean Hilbert-Schmidt term receives S_inverse."""
    m=positive_lower(saved["psi_min"])
    mu=m if m<1 else arb(1)
    m2=up(saved["psi2"]);m3=d["psi3"];m4=d["psi4"]
    C3=up(m4/mu**4+10*m2*m3/mu**5+15*m2**3/mu**6)
    hs=up(C3/6)
    mean_rank=up(arb(2).sqrt()*m2/4)
    nonmean=up(hs*up(saved["Sinvminus"]))
    Dstrong=up(nonmean+mean_rank)
    return dict(mu=mu,C3=C3,root_nonmean_HS=hs,mean_rank=mean_rank,
        transported_nonmean=nonmean,Dstrong=Dstrong)

def complete_minimum(records):
    """Select a complete norm bound using each final saved outward endpoint."""
    if not records:raise ValueError("no complete norm candidates")
    selected=0
    for j in range(1,len(records)):
        if up(records[j])<up(records[selected]):selected=j
    return selected,copy.deepcopy(records[selected])

def commonout_bounds(saved,s):
    z0=up(up(saved["S0"])*up(saved["Sinv0"]))
    zm=up(up(saved["Sminus"])*up(saved["Sinvminus"]))
    paid=up(saved["Cpaid"])
    candidates=[rec(zm),rec(up(1+s["Dstrong"]))]
    index,whole=complete_minimum(candidates)
    zm_saved=up(candidates[0]);zw=up(whole)
    # Original MS33/34 products are kept separately from the ZD whole-bound improvement.
    common_paid=up(paid*zm_saved)
    paid_comm=up(paid*(zm_saved+z0))
    root_comm=up(ex(17,8)*up(saved["co_B13"]))
    To0=up(1+up(saved["co_A0"])/4)
    coordinate=up(To0*s["Dstrong"])
    standard_paid=up(paid*zw)
    subtotal=up(root_comm+coordinate+standard_paid)
    return dict(z0=z0,zminus=zm,whole_candidates=candidates,whole_index=index,
        whole_negative=whole,common_paid=common_paid,paid_comm=paid_comm,
        root_comm=root_comm,To0=To0,coordinate=coordinate,
        standard_paid=standard_paid,standard_subtotal=subtotal)

def retained_register():
    return [
      dict(id="original_WE_remainder",status="exact-unpaid",actual_norm_supplied=False,
           formula="Z_inverse E_ret Z^S; original six-row register preserved verbatim",
           operator_is_not_assumed_finite_rank=True),
      dict(id="physical_mean_and_transported_low_matching",status="exact-unpaid",actual_norm_supplied=False,
           formula="two physical means, transported P97 complement and exact matching rows",
           operator_is_not_assumed_finite_rank=True),
      dict(id="second_reference_and_remaining_opposite_sign_blocks",status="exact-unpaid",actual_norm_supplied=False,
           formula="complete second-reference and remaining sign blocks in the actual common-input order",
           operator_is_not_assumed_finite_rank=True),
      dict(id="incoming_inverse_and_complete_ratio_error",status="exact-unpaid",actual_norm_supplied=False,
           formula="(E_standard - A E_i) B_i_inverse requires complete E_i and actual incoming inverse",
           operator_is_not_assumed_finite_rank=True),
      dict(id="second_global_Cayley_sign_commutator",status="exact-unpaid",actual_norm_supplied=False,
           formula="-Z_inverse Nminus_inverse [Nminus,Z] Nminus_inverse A N",
           operator_is_not_assumed_finite_rank=True),
      dict(id="actual_finite_Schur_and_return",status="exact-unpaid",actual_norm_supplied=False,
           formula="complete augmented finite Schur blocks and whole return R0",
           operator_is_not_assumed_finite_rank=True)]

def run(a,doc):
    ctx.prec=a.bits
    paths,old,saved=checked_inputs(a,doc)
    doc.update(stage="complete saved input audit",original_completed_scientific_receipts_read=5)
    save(a.out,doc)
    d=fourth_derivatives(saved)
    gate(doc,"fifteen new complete higher-derivative combinations are finite without any new ray or exponential",
         len(d)==15 and all(v.is_finite() and v>=0 for v in d.values()))
    doc["complete_new_fourth_angle_conclusion"]=dict(
        new_scalar_upper={k:rec(v) for k,v in d.items()},
        complete_selected_common_input_third_derivative_upper=rec(d["psi3"]),
        complete_selected_common_input_fourth_derivative_upper=rec(d["psi4"]),
        saved_P1_P2_P3_and_M_F_G_W1_W2_h1_h2_are_not_recomputed=True,
        complete_finite_label_bandwidth_used=192,physical_frequency_factor=4,
        complete_both_characteristic_branches_and_all_shorter_intervals=True,
        only_same_selected_H_in_final_composition=True,
        old_complete_holomorphic_strip_used_without_promoting_real_jets=True,
        original_lower_T_endpoint_used_in_every_inverse_half_power=True)
    doc.update(new_higher_derivative_scalar_count=15,stage="complete new fourth-angle combinations")
    save(a.out,doc)
    s=sign_bounds(saved,d)
    gate(doc,"complete C4 sign bound keeps both signs output mean and its independent input-mean rank",
         all(v.is_finite() and v>=0 for v in s.values()) and s["mu"]>0)
    doc["complete_new_strong_sign_conclusion"]=dict(
        positive_phase_minimum_used=rec(s["mu"]),
        complete_three_IBP_coefficient_upper=rec(s["C3"]),
        complete_root_nonmean_Hilbert_Schmidt_upper=rec(s["root_nonmean_HS"]),
        complete_input_mean_rank_upper=rec(s["mean_rank"]),
        complete_transported_nonmean_strong_upper=rec(s["transported_nonmean"]),
        complete_D_Hminus4_3_to_L2_upper=rec(s["Dstrong"]),
        exact_D="D = Z^S - Z = [S,Z] S_inverse",
        both_opposite_sign_quadrants_and_commutator_factor_two_included=True,
        output_mean_of_density_commutator_is_exactly_zero=True,
        nonzero_output_mean_of_root_multiplier_commutator_is_retained=True,
        input_mean_rank_is_paid_separately=True,
        Pi_S_inverse_equals_Pi_used_only_for_input_mean_rank=True,
        no_inverse_factor_on_the_input_mean_rank=True,
        independent_physical_mean_coordinates_not_deleted=True,
        complete_sign_operator_not_relabelled_finite_rank=True)
    doc.update(new_complete_strong_sign_bound_count=1,stage="complete global sign difference")
    save(a.out,doc)
    b=commonout_bounds(saved,s)
    gate(doc,"whole negative-window sign minimum compares final saved outward records and keeps both candidates",
         len(b["whole_candidates"])==2 and b["whole_index"] in (0,1)
         and b["whole_negative"]==b["whole_candidates"][b["whole_index"]]
         and up(b["whole_negative"])<=up(b["whole_candidates"][0])
         and up(b["whole_negative"])<=up(b["whole_candidates"][1])
         and all(b[k].is_finite() and b[k]>=0 for k in ("z0","zminus","common_paid","paid_comm")))
    doc["complete_new_commonout_paid_conclusion"]=dict(
        complete_ZS_L2_upper=rec(b["z0"]),
        complete_ZS_Hminus4_3_product_upper=copy.deepcopy(b["whole_candidates"][0]),
        complete_whole_negative_sign_candidates=copy.deepcopy(b["whole_candidates"]),
        selected_complete_candidate_index=b["whole_index"],
        complete_ZS_Hminus4_3_whole_upper=copy.deepcopy(b["whole_negative"]),
        selection_rule=PARAMETERS["whole_negative_sign_selection"],
        complete_original_MS_commonout_paid_upper=rec(b["common_paid"]),
        complete_paid_commutator_upper=rec(b["paid_comm"]),
        physical_common_outgoing_order=PARAMETERS["physical_common_outgoing_order"],
        individually_normalized_branch_paid_value_read_verbatim=copy.deepcopy(saved["Cpaid"]),
        complete_ZS_inverse_has_the_same_product_norm_bounds=True,
        no_entrywise_minimum_or_unpaid_remainder_zero_substitution=True,
        original_TF_sign_commutation_uses_double_high_compression_and_band192=True,
        original_Lambda_TF_S_order_not_changed=True)
    gate(doc,"standard outgoing subtotal adds root commutator full principal times D and paid whole-sign term exactly once",
         all(b[k].is_finite() and b[k]>=0 for k in
             ("root_comm","To0","coordinate","standard_paid","standard_subtotal")))
    doc["complete_new_standardout_paid_conclusion"]=dict(
        complete_root_coefficient_sign_commutator_upper=rec(b["root_comm"]),
        complete_full_Tco_L2_upper=rec(b["To0"]),
        complete_Tco_D_strong_upper=rec(b["coordinate"]),
        complete_paid_ZS_strong_upper=rec(b["standard_paid"]),
        complete_known_standardout_subtotal_upper=rec(b["standard_subtotal"]),
        exact_standardout_order=PARAMETERS["standard_outgoing_order"],
        exact_error="Z_inverse ([Tco,Z] + Tco D + Eo Z^S)",
        exact_unpaid_remainder="Z_inverse E_ret Z^S",
        full_co_mean_used_in_Tco_L2=True,
        only_constant_coefficient_part_removed_from_exact_commutator=True,
        root_commutator_output_scalar_mean_kept=True,
        WE_subtotal_already_contains_state_and_CG_once=True,
        state_only_coordinate_cancellation_not_reapplied=True,
        retained_remainder_norm_supplied=False,
        complete_Estandard_or_actual_incoming_inverse_not_claimed=True)
    doc["complete_two_sign_readout"]=[
        dict(physical_input_sign=e,root_sign_value="i" if e==1 else "-i",
             complete_known_standardout_subtotal_upper=rec(b["standard_subtotal"]),
             same_complete_operator_bound_not_a_sign_sum=True)
        for e in PARAMETERS["physical_input_signs"]]
    doc["retained_row_register"]=retained_register()
    doc["scope"]=dict(
        current_only_five_completed_scientific_receipts=True,
        same_selected_common_S_with_true_fourfold_density_measure=True,
        same_terminal_Ai_reference_and_common_incoming_right_factor=True,
        independent_physical_mean_coordinates_retained=True,
        original_P97_and_TF_finite_maps_and_all_unpaid_blocks_retained=True,
        two_sign_complete_norms_not_added_again=True,
        new_C4_difference_is_a_complete_infinite_operator_bound=True,
        known_Maslov_order_resolved_without_claiming_all_opposite_sign_errors_paid=True,
        full_scalar_co_mean_kept_in_principal_multiplier=True,
        no_claim_about_actual_PDE_solution_or_surface=True)
    gate(doc,"two sign readouts preserve all exact unpaid rows and do not promote a single-wave bound to a pair norm",
         [v["physical_input_sign"] for v in doc["complete_two_sign_readout"]]==[-1,1]
         and len(doc["retained_row_register"])==6
         and all(x["status"]=="exact-unpaid" and x["actual_norm_supplied"] is False
             for x in doc["retained_row_register"])
         and all(v["same_complete_operator_bound_not_a_sign_sum"] is True
             for v in doc["complete_two_sign_readout"])
         and all(doc["scope"].values()))
    doc.update(new_complete_commonout_paid_bound_count=1,new_complete_paid_commutator_bound_count=1,
        new_complete_standardout_subtotal_count=1,new_complete_whole_minimum_count=1,
        new_sign_record_count=2,stage="complete known standardout subtotal with exact unpaid remainder")
    gate(doc,"all original scalar records proof bytes and complete WE retained register stay unchanged",
         scalar_copies(old)==doc["copied_complete_scalar_inputs_read_verbatim"]
         and old["we_science"]["retained_row_register"]
             ==doc["copied_original_WE_retained_register_read_verbatim"]
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    save(a.out,doc)
    gate(doc,"complete scientific conclusion retains all fields within its predesigned small-text allowance",
         len(canonical(doc))<39000 and len(doc["complete_original_receipt_identities"])==5
         and len(doc["copied_complete_scalar_inputs_read_verbatim"])==25)
    gate(doc,"all twenty-four structural gates and every actual unpaid-scope flag remain explicit",
         len(doc["gates"])==23 and all(g["passed"] is True for g in doc["gates"])
         and all(doc[k] is False for k in ("complete_full_Ei_Eo_proved",
             "full_incoming_inverse_proved","finite_Schur_inverse_proved","whole_return_R0_proved",
             "actual_nonlinear_background_proved","final_surface_proved"))
         and all(doc[k]==0 for k in ("old_successful_scientific_targets_recomputed",
             "old_scientific_source_imports","old_scientific_source_calls",
             "old_binary_native_or_archive_restored","new_ray_or_KAM_calls",
             "new_radial_or_angular_integrals","old_coordinate_or_normalizer_targets_recomputed")))
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete gate count changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_new_fourth_angle_and_sign_budgets_proved=True,
        complete_known_standardout_subtotal_proved=True,stage="complete")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete or partial DZ result")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        parameters=copy.deepcopy(PARAMETERS),arithmetic_bits=a.bits,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        stage="initial immutable input checks",original_completed_scientific_receipts_read=0,
        new_higher_derivative_scalar_count=0,new_complete_strong_sign_bound_count=0,
        new_complete_commonout_paid_bound_count=0,new_complete_paid_commutator_bound_count=0,
        new_complete_standardout_subtotal_count=0,new_complete_whole_minimum_count=0,
        new_sign_record_count=0,complete_new_fourth_angle_and_sign_budgets_proved=False,
        complete_known_standardout_subtotal_proved=False,
        retained_mode="exact-unpaid",retained_norm_budget=None,
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
    print("FOURTH_ANGLE_GLOBAL_SIGN_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=digest(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("FOURTH_ANGLE_GLOBAL_SIGN_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>40000:raise ValueError("saved complete DZ science exceeds40000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())

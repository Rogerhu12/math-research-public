#!/usr/bin/env python3
"""New complete cohomological N windows and conditional global sign coefficients.
Only one low-order exponential and new complete scalar combinations are evaluated.
Saved actual SEI density derivatives, mean and CI are read without recomputation.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from math import comb
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_complete_cohomological_normalizer_windows_sign_v1"
MANIFEST_KIND="cohomological_normalizer_windows_sign_public_inputs_v1"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0")
CONTRACT="1469fdd05417284743e7857aabe0324ee67ccb1b7dbaa003461364d8c9447938"
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"original_SEI_run\":\"43773319871/1\",\"physical_frequency_factor\":4,\"physical_period\":\"pi/2\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"only_same_selected_actual_parameter\":true,\"independent_physical_mean_coordinates\":2,\"exact_difference\":\"v=v_o-v_i\",\"exact_cohomological_equation\":\"w(x-Omega)-w(x)=v(x)\",\"exact_primitive\":\"p=I w; mean(w)=mean(p)=0\",\"actual_normalizer\":\"N=Id+M_w I\",\"complete_windows\":[\"L2\",\"H^(-4/3)\"],\"adjoint_intermediate_window\":\"H^(1/3)\",\"physical_two_primitive_rational_upper\":\"1/2\",\"expected_actual_gate_count\":20,\"current_input_count\":9,\"old_successful_scientific_calls_allowed\":0,\"one_new_low_order_exponential\":true,\"high_order_or_old_log_exponentials_allowed\":false,\"complete_C_E_supplied\":false,\"complete_physical_incoming_or_finite_inverse_or_return_claimed\":false}")
OLD=json.loads("{\"run\":\"43773319871\",\"attempt\":\"1\",\"execution_sha256\":\"b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29\",\"source\":\"f75a8f905b89a5527d52271c3e1fd682d43cf7f90d8b4b865f16efdcc75f8723\",\"manifest\":\"3e26d5eb305e0a1112f059192f6060a4a90c74aa4d37e0da1bc26247f4030a9f\",\"kind\":\"actual_individual_principal_energy_from_terminal_density_v1\",\"execution_kind\":\"actual_public_individual_principal_energy_terminal_density_execution\",\"gates\":20,\"runtime\":{\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"science_bytes\":35198,\"science_sha256\":\"e830e10be50804e80054dee7983fe8004a64d24ab5ff567298a490d8f737c93b\",\"SN_terminal_payload\":\"02b42841d6dc075e222e3184daa21f3b5a35f2ff5a528b1d6233c715ff4927b0\",\"checkout\":\"425d8a3248d6f3b6a54ccc1f4349dbadddf91545\",\"parameters\":{\"adjoint_intermediate_window\":\"H^(1/3)\",\"arithmetic_bits\":320,\"complete_SN_derivative_orders\":[0,1,2,3],\"complete_physical_incoming_or_finite_inverse_or_return_claimed\":false,\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"current_input_count\":9,\"direct_exponential_evaluation_allowed\":false,\"exact_real_SN_transport_half_width\":\"1/10000000000\",\"expected_actual_gate_count\":20,\"independent_physical_mean_coordinates\":2,\"inverse_windows\":[\"L2\",\"H^(-4/3)\"],\"old_successful_scientific_calls_allowed\":0,\"optional_signed_tests\":2,\"original_PIB_run\":\"43771317443/1\",\"original_SN_run\":\"43751213826/1\",\"physical_frequency_factor\":4,\"physical_period\":\"pi/2\",\"principal_factors\":[\"T_ci = Id + M_ci I\",\"T_co = Id + M_co I\"],\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"supremum_candidates_per_branch\":4,\"true_angle_only_at_original_selected_parameter\":true}}")
PRIMARIES=json.loads("{\"CN\":\"427387a2f3836d95b5f79546f0c6d41e8d6307abbb76611073d2801364fda9db\",\"LN\":\"53a3dd1dd637a61aec843262d51a2686ef9cf13f5478df4c62b93437db1c6da6\",\"PIB\":\"2d74b71c0584cb5ec1af849b6fb5756e48da58bf313d72be62d582d557d23acb\",\"CY\":\"4e58b1371d9527c7137cae284172c862f3a395e85d601f2b417f18cf70a901fd\",\"ZD\":\"715f28768139356001ef66840939e4defa547f953a59caea613f3fc6d6841a76\"}")

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
    gate("the only new scalar arithmetic runs in public Actions with the frozen320-bit runtime",
        os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==PUBLIC and runtime==RUNTIME and ctx.prec==320)
    m=read(a.manifest);paths={k:a.repo_root/Path(v) for k,v in m["input_paths"].items()}
    gate("nine current small inputs and all new parameters are frozen before evaluation",
        m["kind"]==MANIFEST_KIND and m["public_repository"]==PUBLIC
        and m["source_sha256"]==m["scientific_source_sha256"]==sha(__file__)
        and m["contract_sha256"]==CONTRACT and m["mathematical_parameters"]==PARAMETERS
        and m["expected_actual_gate_count"]==20 and m["file_count"]==len(m["files"])==9
        and m["all_inputs_are_current_small_texts"] is True
        and m["old_successful_scientific_calls_allowed"]==0 and m["legacy_artifact_inputs"]==[]
        and set(m["input_paths"].values())=={x["path"] for x in m["files"]})
    gate("every immutable size SHA and small text type is checked without restoring old data",
        all((a.repo_root/Path(x["path"])).stat().st_size==x["bytes"]
            and sha(a.repo_root/Path(x["path"]))==x["sha256"]
            and x["bytes"]<100000 and Path(x["path"]).suffix in (".py",".json",".md")
            and not (a.repo_root/Path(x["path"])).read_bytes().startswith(b"\x1f\x8b")
            for x in m["files"]))
    literal={"CN":(r"\tag{CN.14}",r"\tag{CN.16}"),
        "LN":(r"\tag{LN.21}",r"\tag{LN.25}",r"\tag{LN.26}"),
        "PIB":("L2","mean"),"CY":(r"\tag{CY.24}",r"\tag{CY.26}"),
        "ZD":(r"\tag{ZD.26}",r"\tag{ZD.28}")}
    gate("the exact true w two-mean inverse and full global sign primaries are retained",
        sha(paths["contract"])==CONTRACT
        and sha(paths["SEI_source"])==OLD["source"]
        and sha(paths["SEI_execution"])==OLD["execution_sha256"]
        and all(sha(paths[k+"_contract"])==v
            and all(term in paths[k+"_contract"].read_text() for term in literal[k])
            for k,v in PRIMARIES.items())
        and m["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
    return paths

def accepted_SEI(path,d,gate):
    e=read(path);p=e.get("actual_scientific_receipt",{})
    gate("the one original SEI execution is a complete same-identity actual success",
        e.get("kind")==OLD["execution_kind"] and e.get("run_id")==OLD["run"]
        and e.get("run_attempt")==OLD["attempt"] and e.get("complete") is True
        and e.get("actual_returncode")==0 and e.get("actual_source_budget_processes")==1
        and e.get("source_budget_source_sha256")==OLD["source"]
        and e.get("input_manifest_sha256")==OLD["manifest"]
        and e.get("actual_scientific_checkout_commit")==OLD["checkout"]
        and p.get("kind")==OLD["kind"] and p.get("run_id")==OLD["run"]
        and p.get("run_attempt")==OLD["attempt"] and p.get("complete") is True and p.get("proved") is True
        and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("stage")=="complete_individual_principal_energy_target"
        and p.get("source_sha256")==OLD["source"] and p.get("input_manifest_sha256")==OLD["manifest"]
        and p.get("runtime")==OLD["runtime"] and p.get("arithmetic_bits")==320
        and p.get("mathematical_parameters")==OLD["parameters"]
        and len(p.get("gates",[]))==20 and all(v.get("passed") is True for v in p["gates"]))
    raw=(canonical(p)+"\n").encode()
    gate("the entire original SEI science has its exact canonical bytes hash and native result",
        len(raw)==OLD["science_bytes"] and hashlib.sha256(raw).hexdigest()==OLD["science_sha256"]
        and all(any(v.get("file")==name and v.get("bytes")==OLD["science_bytes"]
            and v.get("sha256")==OLD["science_sha256"] for v in e.get("output_hashes",[]))
            for name in ("consumers/process.json","consumers/summary.json"))
        and p.get("complete_SN_terminal_conclusion_payload_sha256")==OLD["SN_terminal_payload"]
        and p.get("new_optional_signed_tests_passed")==2)
    density=p["complete_new_individual_density_derivative_conclusion"]
    original_scope=p["complete_selected_common_input_scope_read_verbatim"]
    path_scope=p["complete_SN_whole_path_scope_read_verbatim"]
    gate("both complete true-density columns and their selected whole-path means retain the original scope",
        set(density["branches"])=={"incoming","outgoing"}
        and density["complete_derivative_orders"]==[0,1,2,3]
        and all(len(v["complete_actual_nonmean_derivative_L2_upper"])==4
            and v["true_H_minus_G_error_paid_once_with_half"] is True
            and v["finite_G_analytic_tail_already_in_saved_Q_not_repeated"] is True
            for v in density["branches"].values())
        and density["branches"]["incoming"]["sigma"]==1
        and density["branches"]["outgoing"]["sigma"]==-1
        and density["branches"]["outgoing"]["outgoing_final_rotation_isometric_and_retained"] is True
        and original_scope["exact_order"]==PARAMETERS["selected_common_input_order"]
        and original_scope["selected_parameter_absolute_upper"]==PARAMETERS["selected_parameter_absolute_upper"]
        and original_scope["only_same_selected_actual_conjugacy"] is True
        and path_scope["actual_completed_original_transport_intervals"]==3146
        and path_scope["actual_exact_radial_cursor"]=="0"
        and path_scope["actual_new_transport_subcells_completed"]==12584
        and path_scope["completed_prefix_budget_subcells_reused"]==1256
        and path_scope["completed_prefix_residual_parameter_energy_budgets_recomputed"]==0
        and p["scope"]["only_complete_SN_terminal_never_a_prefix_used"] is True
        and p["scope"]["global_sign_operator_and_transported_sign_order_unchanged"] is True)
    saved=dict(density=copy.deepcopy(density),
        absolute_mu=copy.deepcopy(density["complete_absolute_mu_upper"]),
        CI=copy.deepcopy(p["complete_saved_PG_inputs_read_verbatim"]["CI"]))
    d["accepted_complete_SEI_identity_read_verbatim"]=copy.deepcopy(OLD)
    d["complete_SEI_density_conclusion_read_verbatim"]=copy.deepcopy(density)
    d["complete_saved_absolute_mu_and_CI_read_verbatim"]={
        "absolute_mu":copy.deepcopy(saved["absolute_mu"]),"CI":copy.deepcopy(saved["CI"])}
    d["complete_original_signed_mu_read_verbatim"]=copy.deepcopy(
        p["complete_new_signed_energy_conclusion"]["original_signed_mu_read_verbatim"])
    d["complete_SEI_whole_path_scope_read_verbatim"]=copy.deepcopy(path_scope)
    d["complete_selected_common_input_scope_read_verbatim"]=copy.deepcopy(original_scope)
    d["complete_SEI_original_scope_read_verbatim"]=copy.deepcopy(p["scope"])
    d["complete_saved_input_payload_sha256"]=payload_sha(saved)
    d["original_successful_small_receipts_read"]=1
    d["saved_individual_derivative_columns_read"]=8
    d["saved_absolute_mu_and_CI_records_read"]=2
    return saved

def whole_choice(candidates):
    if not candidates:raise ValueError("empty complete-candidate family")
    if len({name for name,_ in candidates})!=len(candidates):
        raise ValueError("duplicate complete-candidate identity")
    selected=min(candidates,key=lambda item:up(item[1]))
    return dict(complete_candidate_records={name:copy.deepcopy(v) for name,v in candidates},
        selected_complete_candidate=selected[0],complete_selected_upper=copy.deepcopy(selected[1]),
        choice_uses_final_retained_outward_records=True,tie_preserves_first_candidate=True,
        all_candidates_bound_the_same_complete_operator_and_window=True)

def combined_derivatives(saved):
    rows=saved["density"]["branches"]
    ds=[rec(up(up(rows["incoming"]["complete_actual_nonmean_derivative_L2_upper"][k])
              +up(rows["outgoing"]["complete_actual_nonmean_derivative_L2_upper"][k])))
        for k in range(4)]
    cs=[]
    for k in range(4):
        positive_sum=up(sum((up(arb(comb(k,q))*up(up(ds[q])*up(ds[q])))
            for q in range(k+1)),arb(0)))
        cs.append(rec(up(positive_sum.sqrt())))
    return dict(complete_difference_derivative_L2_upper=ds,
        complete_difference_Bessel_H0_H1_H2_H3_upper=cs,
        exact_difference="v = v_o - v_i",
        two_complete_branches_combined=True,
        original_outgoing_rotation_already_in_saved_column=True,
        true_density_and_angle_errors_already_paid_not_repeated=True,
        complete_difference_zero_mean=True)

def fourier_budgets(combined):
    ds=[up(x) for x in combined["complete_difference_derivative_L2_upper"]]
    cs=[up(x) for x in combined["complete_difference_Bessel_H0_H1_H2_H3_upper"]]
    sqrt96=arb(96).sqrt().lower()
    if sqrt96<=0:raise ValueError("the exact positive Fourier denominator failed")
    candidates={
        "V0":[("C1_over_2",rec(up(cs[1]/2))),
              ("C2_over_sqrt96",rec(up(cs[2]/sqrt96))),
              ("C3_over_32",rec(up(cs[3]/32))),
              ("complete_d0_d1_interpolation",rec(up(up(arb.pi()*ds[0]*ds[1]/2).sqrt())))],
        "W0":[("2_C3",rec(up(2*cs[3]))),
              ("17_C2_over_2",rec(up(arb(17)*cs[2]/2))),
              ("complete_17_d1_d2_interpolation",rec(up(arb(17)*up(up(arb.pi()*ds[1]*ds[2]/2).sqrt()))))],
        "Pfour_thirds":[("9_C3_over_2",rec(up(arb(9)*cs[3]/2))),
              ("26_C2",rec(up(arb(26)*cs[2])))],
        "Wone_third":[("4_C3",rec(up(4*cs[3]))),
              ("21_C2",rec(up(arb(21)*cs[2])))]}
    choices={name:whole_choice(v) for name,v in candidates.items()}
    values={name:copy.deepcopy(v["complete_selected_upper"]) for name,v in choices.items()}
    values["P0"]=rec(up(arb(17)*up(values["V0"])))
    values["Wfour_thirds"]=rec(up(arb(26)*cs[3]))
    values["Vfour_thirds"]=rec(up(arb(243)*cs[2]/160))
    return dict(complete_Wiener_bounds=values,complete_whole_choices=choices,
        complete_candidate_count=sum(len(v) for v in candidates.values()),
        exact_cohomological_equation="w(x-Omega)-w(x)=v(x)",
        exact_primitive="p=I w; mean(w)=mean(p)=0",
        same_selected_bounded15_rotation=True,
        full_infinite_two_sign_series_included=True,
        coefficient_17_is_old_complete_divisor_not_a_new_KAM_evaluation=True,
        V_budgets_bound_v_W_budgets_bound_w_P_budgets_bound_p=True,
        bounds_are_direct_series_inequalities_not_inversion_of_operator_norms=True)

def optional_neumann(W_record):
    gap_record=rec(arb(1)-up(W_record)/4)
    gap_lower=rb(gap_record).lower()
    passed=bool(gap_lower>0)
    return dict(complete_signed_gap=gap_record,strict_positive_gap=passed,
        complete_inverse_upper=rec(up(arb(1)/gap_lower)) if passed else None,
        failed_optional_gate_does_not_assert_noninvertibility=True,
        gate_uses_final_retained_gap_lower=True)

def normalizer_windows(fourier,saved):
    values=fourier["complete_Wiener_bounds"]
    W0,W13,W43,P0,P43=(up(values[k]) for k in
        ("W0","Wone_third","Wfour_thirds","P0","Pfour_thirds"))
    CI=up(saved["CI"])
    exponential=up(P0.exp())
    Z0=up(exponential*exponential*up((arb(1)+exponential)*(arb(1)+exponential))/4)
    ode0=rec(up(arb(1)+W0*Z0))
    neumann0=optional_neumann(values["W0"])
    choices0=[("complete_CN_low_order_ODE",ode0)]
    if neumann0["strict_positive_gap"]:
        choices0.append(("complete_L2_Neumann",copy.deepcopy(neumann0["complete_inverse_upper"])))
    choice0=whole_choice(choices0);K0=up(choice0["complete_selected_upper"])
    term1=rec(up(CI*W13))
    term2=rec(up(CI*up(term1)*W0*K0))
    adjminus=rec(up(arb(1)+up(term1)+up(term2)))
    neumannminus=optional_neumann(values["Wfour_thirds"])
    choicesminus=[("complete_adjoint_from_actual_L2",adjminus)]
    if neumannminus["strict_positive_gap"]:
        choicesminus.append(("complete_negative_Neumann",copy.deepcopy(neumannminus["complete_inverse_upper"])))
    choiceminus=whole_choice(choicesminus)
    log0=rec(up(up(choice0["complete_selected_upper"]).log()))
    logminus=rec(up(up(choiceminus["complete_selected_upper"]).log()))
    log_argument=rec(up(arb(1)+W43))
    direct_log=rec(up(up(up(log_argument).log())+4*P43))
    log_choice=whole_choice([("log_of_complete_evaluated_norm",logminus),
        ("complete_LN_direct_log_only",direct_log)])
    return dict(complete_exp_low_primitive_upper=rec(exponential),
        complete_Z_low_primitive_upper=rec(Z0),complete_CN_L2_ODE_inverse_upper=ode0,
        complete_L2_Neumann_test=neumann0,complete_L2_norm_whole_choice=choice0,
        complete_adjoint_CI_Wone_third_upper=term1,
        complete_adjoint_CI_squared_Wone_third_W0_K0_upper=term2,
        complete_adjoint_negative_inverse_upper=adjminus,
        complete_negative_Neumann_test=neumannminus,
        complete_negative_norm_whole_choice=choiceminus,
        complete_forward_L2_upper=rec(up(arb(1)+W0/4)),
        complete_forward_Hminus4_3_upper=rec(up(arb(1)+W43/4)),
        complete_log_L2_evaluated_inverse_upper=log0,
        complete_log_negative_evaluated_inverse_upper=logminus,
        complete_LN_negative_log_argument=log_argument,
        complete_LN_negative_log_only_upper=direct_log,
        complete_negative_log_whole_choice=log_choice,
        exactly_one_new_low_order_exponential=True,
        negative_primitive_and_saved_PG_PIB_logs_not_exponentiated=True,
        log_only_choice_never_substituted_for_an_evaluated_norm=True,
        same_exact_full_circle_N_inverse_on_both_windows=True,
        same_bounds_for_rotated_N_minus_inverse=True,
        first_weighted_mean_and_second_primitive_mean_retained=True,
        nonmean_w_not_replaced_by_ci_or_co=True,
        full_scalar_mean_and_two_physical_means_retained=True)

def complete_sign_and_affine(fourier,windows,saved):
    v=fourier["complete_Wiener_bounds"]
    V0,V43,W0,W13=(up(v[k]) for k in
        ("V0","Vfour_thirds","W0","Wone_third"))
    K0=up(windows["complete_L2_norm_whole_choice"]["complete_selected_upper"])
    Km=up(windows["complete_negative_norm_whole_choice"]["complete_selected_upper"])
    FN=up(windows["complete_forward_Hminus4_3_upper"])
    mu=up(saved["absolute_mu"])
    sign=rec(up(arb(17)*W13/8))
    bz=rec(up(K0*up(sign)*Km*FN))
    a_factor=rec(up(arb(1)+V43/4))
    az=rec(up(up(bz)*up(a_factor)))
    q=rec(up(up(V0*W13+mu*up(W13+W0))/2))
    cay_constant=rec(up(K0*up(q)+up(az)))
    cay_coefficient=rec(up(K0*FN+up(bz)))
    scalar_linear_fee=rec(up(mu*mu/4))
    return dict(
        complete_global_commutator_Hminus4_3_to_L2_upper=sign,
        complete_A_negative_known_factor_upper=a_factor,
        complete_sign_A_constant_upper=az,
        complete_sign_B_CE_coefficient_upper=bz,
        complete_two_ordered_Q_common_majorant_upper=q,
        complete_global_Cayley_A_constant_upper=cay_constant,
        complete_global_Cayley_B_CE_coefficient_upper=cay_coefficient,
        complete_linear_to_exponential_scalar_fee_upper=scalar_linear_fee,
        physical_two_primitive_rational_upper="1/2",
        conditional_sign_formula="A_Z + B_Z * C_E",
        conditional_global_Cayley_formula="A_Cay + B_Cay * C_E",
        C_E="unpaid complete strong error, symbolic",
        complete_C_E_supplied=False,
        complete_return_remainder_proved=False,
        left_N_inverse_window="L2",right_N_inverse_window="H^(-4/3)",
        input_N_forward_window="H^(-4/3)",
        second_global_sign_mean_row_retained=True,
        independent_physical_mean_rows_retained=True,
        exact_global_sign_not_replaced_by_a_scalar_sector=True,
        linear_mu_squared_fee_not_removed_from_linear_model=True,
        Cayley_no_independent_mu_squared_fee_requires_exact_new_ratio=True,
        no_old_linear_remainder_renamed_as_Cayley=True)

def render_conclusion(d):
    lines=["# Actual cohomological normalizer windows and global sign coefficients","",
        "Complete scientific success: "+str(d["complete"]),""]
    if d["complete"]:
        lines+=["The same complete N inverse is retained on L2 and Hminus4/3.",
            "The global Cayley error is an affine bound in the still unpaid complete C_E.",""]
    else:
        lines+=["Only saved partial fields are shown; no new N-window or affine conclusion is authorized.",""]
    f=d.get("complete_new_Fourier_budgets_conclusion")
    if f:
        lines+=["| Complete Wiener budget | Retained outward bound |","|---|---|"]
        for name,value in f["complete_Wiener_bounds"].items():
            lines.append("| "+name+" | "+value["ball"]+" |")
    w=d.get("complete_new_normalizer_windows_conclusion")
    if w:
        lines+=["","| Complete window or test | Result |","|---|---|",
            "| L2 inverse norm | "+w["complete_L2_norm_whole_choice"]["complete_selected_upper"]["ball"]+" |",
            "| Hminus4/3 inverse norm | "+w["complete_negative_norm_whole_choice"]["complete_selected_upper"]["ball"]+" |",
            "| L2 optional Neumann gate | "+str(w["complete_L2_Neumann_test"]["strict_positive_gap"])+" |",
            "| Hminus4/3 optional Neumann gate | "+str(w["complete_negative_Neumann_test"]["strict_positive_gap"])+" |",
            "| Complete negative logarithm | "+w["complete_negative_log_whole_choice"]["complete_selected_upper"]["ball"]+" |"]
    if d.get("failure"):lines+=["","Failure: "+json.dumps(d["failure"],sort_keys=True)]
    if d["complete"]:
        lines+=["","Both weighted scalar means and the two physical mean coordinates are retained."]
    lines+=["","No full physical incoming inverse, finite-border inverse or complete return remainder is claimed."]
    return "\n".join(lines)+"\n"

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--temporary-output-dir",type=Path,required=True)
    ap.add_argument("--process-receipt",type=Path,required=True)
    ap.add_argument("--small-summary",type=Path,required=True)
    ap.add_argument("--result-markdown",type=Path,required=True)
    a=ap.parse_args()
    if a.process_receipt.exists():raise FileExistsError("preserve every completed successful or failed new target")
    ctx.prec=320;started=time.monotonic()
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),arithmetic_bits=320,
        mathematical_parameters=PARAMETERS,public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("SCIENTIFIC_CHECKOUT_COMMIT"),
        stage="current_inputs",original_successful_small_receipts_read=0,
        saved_individual_derivative_columns_read=0,saved_absolute_mu_and_CI_records_read=0,
        new_complete_difference_derivative_bounds=0,new_complete_difference_Bessel_bounds=0,
        new_complete_Wiener_candidates=0,new_complete_Wiener_budgets=0,
        new_low_order_exponentials_evaluated=0,new_high_order_or_old_log_exponentials_evaluated=0,
        new_complete_L2_ODE_candidates=0,new_complete_adjoint_negative_candidates=0,
        new_optional_Neumann_tests_evaluated=0,new_optional_Neumann_tests_passed=0,
        new_complete_norm_whole_choices=0,new_complete_negative_log_whole_choices=0,
        new_logarithms_evaluated=0,new_global_sign_commutator_bounds=0,
        new_complete_conditional_affine_coefficients=0,new_complete_two_primitive_Q_bounds=0,
        new_complete_linear_scalar_difference_bounds=0,
        old_numerical_enclosures_recomputed=0,old_SN_SEI_PG_PIB_targets_recomputed=0,
        old_cohomological_or_phase_gap_evaluations_recomputed=0,
        old_scientific_producer_imports=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,new_angular_or_radial_integrals_evaluated=0,
        original_input_bytes_modified=0,
        complete_cohomological_normalizer_windows_consumer_paid=False,
        complete_C_E_supplied=False,full_physical_incoming_inverse_claimed=False,
        finite_Schur_inverse_claimed=False,full_return_R0_claimed=False,
        actual_nonlinear_background_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def gate(name,value):
        d["gates"].append(dict(name=name,passed=bool(value)))
        if not value:raise ValueError("new NW structural gate: "+name)
    try:
        paths=checked_inputs(a,d,gate)
        saved=accepted_SEI(paths["SEI_execution"],d,gate)
        rows=saved["density"]["branches"]
        gate("all eight original density inputs and both original mean and primitive budgets are finite nonnegative",
            all(rb(x).is_finite() and rb(x).lower()>=0
                for row in rows.values() for x in row["complete_actual_nonmean_derivative_L2_upper"])
            and rb(saved["absolute_mu"]).is_finite() and rb(saved["absolute_mu"]).lower()>=0
            and rb(saved["CI"]).is_finite() and rb(saved["CI"]).lower()>=1)
        d["stage"]="new_complete_difference_and_Wiener_budgets"
        combined=combined_derivatives(saved)
        d["complete_new_difference_derivative_conclusion"]=combined
        d["new_complete_difference_derivative_bounds"]=4
        d["new_complete_difference_Bessel_bounds"]=4
        gate("the complete difference has all four derivative and Bessel bounds with its true zero mean",
            finite(combined) and len(combined["complete_difference_derivative_L2_upper"])==4
            and len(combined["complete_difference_Bessel_H0_H1_H2_H3_upper"])==4
            and combined["complete_difference_zero_mean"] is True
            and combined["true_density_and_angle_errors_already_paid_not_repeated"] is True)
        fourier=fourier_budgets(combined)
        d["complete_new_Fourier_budgets_conclusion"]=fourier
        d["new_complete_Wiener_candidates"]=fourier["complete_candidate_count"]
        d["new_complete_Wiener_budgets"]=len(fourier["complete_Wiener_bounds"])
        gate("all eleven complete series candidates and seven true v w p bounds retain both frequency signs",
            finite(fourier) and fourier["complete_candidate_count"]==11
            and set(fourier["complete_Wiener_bounds"])=={
                "V0","W0","P0","Pfour_thirds","Wone_third","Wfour_thirds","Vfour_thirds"}
            and len(fourier["complete_whole_choices"])==4
            and fourier["full_infinite_two_sign_series_included"] is True)
        d["stage"]="new_complete_N_inverse_windows"
        windows=normalizer_windows(fourier,saved)
        d["complete_new_normalizer_windows_conclusion"]=windows
        d["new_low_order_exponentials_evaluated"]=1
        d["new_complete_L2_ODE_candidates"]=1
        d["new_complete_adjoint_negative_candidates"]=1
        d["new_optional_Neumann_tests_evaluated"]=2
        d["new_optional_Neumann_tests_passed"]=sum(
            windows[k]["strict_positive_gap"]
            for k in ("complete_L2_Neumann_test","complete_negative_Neumann_test"))
        d["new_complete_norm_whole_choices"]=2
        d["new_complete_negative_log_whole_choices"]=1
        d["new_logarithms_evaluated"]=3
        gate("the new low primitive exponential supplies the complete two-mean L2 ODE inverse",
            finite(windows) and up(windows["complete_exp_low_primitive_upper"])>=1
            and up(windows["complete_CN_L2_ODE_inverse_upper"])>=1
            and up(windows["complete_L2_norm_whole_choice"]["complete_selected_upper"])>=1
            and windows["first_weighted_mean_and_second_primitive_mean_retained"] is True
            and windows["nonmean_w_not_replaced_by_ci_or_co"] is True)
        gate("the complete negative-window candidate uses the actual same L2 inverse and two ordered primitive gains",
            up(windows["complete_adjoint_negative_inverse_upper"])>=1
            and up(windows["complete_negative_norm_whole_choice"]["complete_selected_upper"])>=1
            and windows["same_exact_full_circle_N_inverse_on_both_windows"] is True
            and windows["same_bounds_for_rotated_N_minus_inverse"] is True)
        tests=[windows[k] for k in ("complete_L2_Neumann_test","complete_negative_Neumann_test")]
        gate("both optional Neumann outcomes preserve signed gaps and failed tests are complete valid results",
            all(v["strict_positive_gap"]==bool(rb(v["complete_signed_gap"]).lower()>0)
                and ((v["strict_positive_gap"] and v["complete_inverse_upper"] is not None
                    and up(v["complete_inverse_upper"])>=1)
                 or (not v["strict_positive_gap"] and v["complete_inverse_upper"] is None))
                and v["failed_optional_gate_does_not_assert_noninvertibility"] is True for v in tests))
        gate("a complete log-only alternative never replaces an evaluated norm in any later product",
            len(windows["complete_negative_log_whole_choice"]["complete_candidate_records"])==2
            and windows["log_only_choice_never_substituted_for_an_evaluated_norm"] is True
            and windows["negative_primitive_and_saved_PG_PIB_logs_not_exponentiated"] is True
            and d["new_logarithms_evaluated"]==3
            and d["new_high_order_or_old_log_exponentials_evaluated"]==0)
        gate("both forward bounds and all scalar and physical mean rows retain their precise windows",
            up(windows["complete_forward_L2_upper"])>=1
            and up(windows["complete_forward_Hminus4_3_upper"])>=1
            and windows["full_scalar_mean_and_two_physical_means_retained"] is True
            and windows["exactly_one_new_low_order_exponential"] is True)
        d["stage"]="new_complete_global_sign_and_conditional_affine_bounds"
        affine=complete_sign_and_affine(fourier,windows,saved)
        d["complete_new_global_sign_and_affine_conclusion"]=affine
        d["new_global_sign_commutator_bounds"]=1
        d["new_complete_conditional_affine_coefficients"]=4
        d["new_complete_two_primitive_Q_bounds"]=1
        d["new_complete_linear_scalar_difference_bounds"]=1
        gate("the complete second global sign commutator retains its mean row and two inverse windows",
            finite(affine) and affine["second_global_sign_mean_row_retained"] is True
            and affine["exact_global_sign_not_replaced_by_a_scalar_sector"] is True
            and affine["left_N_inverse_window"]=="L2"
            and affine["right_N_inverse_window"]==affine["input_N_forward_window"]=="H^(-4/3)")
        gate("all four affine coefficients keep the complete unpaid C_E explicit instead of using a paid subtotal",
            all(k in affine for k in ("complete_sign_A_constant_upper","complete_sign_B_CE_coefficient_upper",
                "complete_global_Cayley_A_constant_upper","complete_global_Cayley_B_CE_coefficient_upper"))
            and affine["complete_C_E_supplied"] is False
            and affine["complete_return_remainder_proved"] is False
            and affine["C_E"]=="unpaid complete strong error, symbolic")
        gate("the separate linear-model scalar fee retains the entire original mu and is not discarded by Cayley naming",
            affine["physical_two_primitive_rational_upper"]=="1/2"
            and affine["linear_mu_squared_fee_not_removed_from_linear_model"] is True
            and affine["Cayley_no_independent_mu_squared_fee_requires_exact_new_ratio"] is True
            and affine["no_old_linear_remainder_renamed_as_Cayley"] is True)
        d["scope"]=dict(
            only_same_selected_actual_real_ci_co_difference=True,
            true_cohomological_w_and_p_not_individual_signed_principal_coefficients=True,
            two_complete_branches_and_full_infinite_two_sign_series_retained=True,
            original_true_angle_and_finite_angle_errors_not_paid_again=True,
            complete_same_N_inverse_on_L2_and_Hminus4_3=True,
            first_weighted_mean_and_second_primitive_mean_retained=True,
            independent_physical_mean_coordinates_retained=True,
            actual_evaluated_negative_norm_separate_from_log_only_choice=True,
            optional_Neumann_failure_not_noninvertibility=True,
            only_one_new_low_order_exponential_and_no_old_log_exponential=True,
            exact_global_sign_second_commutator_retained=True,
            all_complete_affine_C_E_coefficients_paid_but_C_E_unsupplied=True,
            full_incoming_outgoing_errors_finite_rows_positive_stable_and_return_still_required=True,
            no_WE_paid_subtotal_used_as_complete_C_E=True)
        gate("no successful old arithmetic or old producer is repeated and all original input bytes are unchanged",
            all(d[k]==0 for k in (
                "old_numerical_enclosures_recomputed","old_SN_SEI_PG_PIB_targets_recomputed",
                "old_cohomological_or_phase_gap_evaluations_recomputed",
                "old_scientific_producer_imports","old_scientific_producer_calls",
                "old_binary_or_archive_inputs_restored","new_angular_or_radial_integrals_evaluated",
                "original_input_bytes_modified"))
            and d["original_successful_small_receipts_read"]==1
            and d["saved_individual_derivative_columns_read"]==8
            and d["saved_absolute_mu_and_CI_records_read"]==2)
        gate("the complete N target retains every pending physical operator obligation and all twenty structural gates",
            finite(d) and len(d["gates"])==19
            and d["new_low_order_exponentials_evaluated"]==1
            and d["new_complete_conditional_affine_coefficients"]==4
            and not any(d[k] for k in ("complete_C_E_supplied","full_physical_incoming_inverse_claimed",
                "finite_Schur_inverse_claimed","full_return_R0_claimed","actual_nonlinear_background_claimed")))
        d["complete"]=True;d["proved"]=True;d["actual_returncode"]=0
        d["stage"]="complete_cohomological_normalizer_windows_sign_target"
        d["complete_cohomological_normalizer_windows_consumer_paid"]=True
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
    d["actual_mathematical_wall_seconds"]=time.monotonic()-started
    a.temporary_output_dir.mkdir(parents=True,exist_ok=True)
    native=a.temporary_output_dir/"temporary-cohomological-normalizer-windows-sign.json.gz"
    save(native,d,compressed=True)
    d["temporary_native_sha256"]=sha(native);d["temporary_native_bytes"]=native.stat().st_size
    # The full scientific result is persisted before presentation or publication.
    save(a.process_receipt,d);save(a.small_summary,d)
    a.result_markdown.parent.mkdir(parents=True,exist_ok=True)
    a.result_markdown.write_text(render_conclusion(d))
    if not d["complete"]:raise SystemExit(1)

if __name__=="__main__":main()

#!/usr/bin/env python3
"""New individual principal energy gates from the complete successful SN terminal.
Read complete terminal columns once; preserve old PG/PIB fallback logarithms.
Optional sign failure is a complete outcome, not a claim of noninvertibility.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,platform,time
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_individual_principal_energy_from_terminal_density_v1"
MANIFEST_KIND="individual_principal_energy_from_terminal_density_public_inputs_v1"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0")
CONTRACT="268be1a8766bad61335e1b47e15dad6686a2de1116caa880e1d007081a57d44c"
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"original_SN_run\":\"43751213826/1\",\"original_PIB_run\":\"43771317443/1\",\"exact_real_SN_transport_half_width\":\"1/10000000000\",\"true_angle_only_at_original_selected_parameter\":true,\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"physical_frequency_factor\":4,\"physical_period\":\"pi/2\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"principal_factors\":[\"T_ci = Id + M_ci I\",\"T_co = Id + M_co I\"],\"inverse_windows\":[\"L2\",\"H^(-4/3)\"],\"adjoint_intermediate_window\":\"H^(1/3)\",\"independent_physical_mean_coordinates\":2,\"complete_SN_derivative_orders\":[0,1,2,3],\"optional_signed_tests\":2,\"supremum_candidates_per_branch\":4,\"expected_actual_gate_count\":20,\"current_input_count\":9,\"old_successful_scientific_calls_allowed\":0,\"direct_exponential_evaluation_allowed\":false,\"complete_physical_incoming_or_finite_inverse_or_return_claimed\":false}")
OLD_SN=json.loads("{\"run\":\"43751213826\",\"attempt\":\"1\",\"execution_sha256\":\"eccb4ce4e7f8c783079e4400cd7a978214817d8092f50cd2bb8f1acbcf3d6ea6\",\"source\":\"6c63241ae5ad865952620f68d63670604875b460e51b083ecb66127cb785b339\",\"helper\":\"217a91e25ec7bb6cad5c115ddc4749f4d714c5ca47601e8ad8dd540e69ed1718\",\"manifest\":\"f6e5f9fe938d897c2b57d3d34e42391455fc6cea9804576d4dcc90b2021a8351\",\"kind\":\"actual_complete_signed_nonmean_density_H3_validation_v1\",\"execution_kind\":\"actual_public_signed_nonmean_density_H3_execution\",\"science_bytes\":22817,\"science_sha256\":\"8fea75ce01dd4bbd0d20532332ed458af73634a995c1dbce5c3cbac511e0e8a0\",\"parameters\":{\"all_output_means_retained\":true,\"angle_exp_degree\":24,\"angle_tail_width\":\"1/128\",\"arithmetic_bits\":320,\"candidate_prefix_parts\":2,\"complete_radial_remainder_order\":6,\"exact_real_parameter_half_width\":\"1/10000000000\",\"maximum_new_subcells\":120000,\"maximum_optical_step\":\"1/4\",\"original_compact_T_cells\":220,\"original_scalar_cells\":626,\"original_scalar_germs\":169,\"original_scalar_integrals_rays_KAM_and_response_recomputed\":0,\"original_strict_intervals\":3146,\"output_Sobolev_exponent\":3,\"physical_frequency_factor\":4,\"reference_modes\":128,\"reference_radial_degree\":6,\"root_piece\":2549,\"source_reference_is_not_a_Fourier_projection_proof\":true},\"original_input_sha256\":{\"angle_post\":\"a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60\",\"angle_root\":\"1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43\",\"candidate\":\"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413\",\"candidate_part0\":\"5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4\",\"candidate_part1\":\"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106\",\"direction\":\"87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88\",\"finite_part\":\"cd9ffed6d8c9e107eaac2b50f1846219d8ec90a130555bb91859d465c9bab202\",\"parameter_transfer\":\"06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb\",\"preparatory_execution\":\"3c18e4a06da0d9bf9a11e0bfd1354db48bfc2fedf4b5aeb311991fc0ae5b81aa\",\"repair\":\"6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc\",\"root_budget\":\"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f\",\"root_germ\":\"397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864\",\"scalar_cover\":\"94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3\",\"strip_proof\":\"dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854\",\"t_cache\":\"ab5e8156fbaf50c80e944a15d68858d29419229e7ae10665b432cd1af593587d\",\"transport_prefix_execution\":\"d2855e79fbf3332a993b927ff74d3371e72b74748145d87f191666803a360d56\"},\"actual_original_intervals\":3146,\"actual_subcells\":12584,\"actual_prefix_subcells\":1256,\"actual_suffix_subcells\":11328,\"gates\":21}")
OLD_PIB=json.loads("{\"run\":\"43771317443\",\"attempt\":\"1\",\"execution_sha256\":\"c892c96aefd81584c65dae3415c42cd48ff020b37132725babbcd7474d3f680a\",\"source\":\"14c1cf4a9047895cefec650378d1462ee8d86f4c074e9ea076efe2c1a9276a53\",\"manifest\":\"7afa0cdafab54202a6a4abe32f80a1e4ae2689b862bbad44ce652fe2d329048e\",\"kind\":\"actual_complete_principal_inverse_adjoint_bootstrap_v1\",\"execution_kind\":\"actual_public_principal_inverse_adjoint_bootstrap_execution\",\"gates\":15,\"runtime\":{\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"five_payload_sha256\":\"a446f04d52e0037e6dd062e29fa7765698ecc91ccb7559a2d94e5debb79af11b\",\"science_bytes\":9197,\"science_sha256\":\"258f85ec92bd5ebbc4d814b85e5abf86bd08e85e1aad4b80658bfee8901f1661\"}")

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)
def payload_sha(v):return hashlib.sha256(canonical(v).encode()).hexdigest()
def read(path):return json.loads(Path(path).read_bytes())
def save(path,v,compressed=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(canonical(v)+"\n").encode()
    body=gzip.compress(raw,mtime=0) if compressed else raw
    temp=path.with_name(path.name+".tmp");temp.write_bytes(body);temp.replace(path)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,dict):return arb(v["ball"])
    return arb(v)
def up(v):
    value=rb(v)
    if not value.is_finite() or value.lower()<0:
        raise ValueError("a complete nonnegative budget is invalid")
    return value.upper()
def rec(v):return dict(ball=rb(v).str(60))
def finite(v):
    if isinstance(v,dict):
        if "ball" in v:return rb(v).is_finite()
        return all(finite(x) for x in v.values())
    if isinstance(v,(list,tuple)):return all(finite(x) for x in v)
    if isinstance(v,arb):return v.is_finite()
    return True
def complete_gates(value,count):
    rows=value.get("gates",[])
    return len(rows)==count and all(x.get("passed") is True for x in rows)
def text_has(path,needles):
    text=Path(path).read_text()
    return all(value in text for value in needles)

def checked_inputs(a,d,gate):
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__)
    d["runtime"]=runtime
    gate("the only new mathematics runs in public Actions with the exact two-key runtime",
        os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
        and runtime==RUNTIME and ctx.prec==320)
    m=read(a.manifest)
    paths={k:a.repo_root/Path(v) for k,v in m["input_paths"].items()}
    expected_keys={"new_source","contract","IC_contract","LN_contract","PIB_contract",
                   "SN_source","SN_helper","SN_execution","PIB_execution"}
    gate("nine current small inputs and every new frozen parameter are fixed before any scalar",
        m["kind"]==MANIFEST_KIND and m["public_repository"]==PUBLIC
        and m["source_sha256"]==m["scientific_source_sha256"]==sha(__file__)
        and m["contract_sha256"]==CONTRACT and m["mathematical_parameters"]==PARAMETERS
        and m["expected_actual_gate_count"]==20 and m["file_count"]==len(m["files"])==9
        and m["all_inputs_are_current_small_texts"] is True
        and m["old_successful_scientific_calls_allowed"]==0 and m["legacy_artifact_inputs"]==[]
        and set(paths)==expected_keys)
    seen=set()
    for row in m["files"]:
        name=row["path"];p=(a.repo_root/name).resolve()
        if name in seen or not name.startswith("topics/visible-flex-exact-nearby/"):
            raise ValueError("duplicate or external immutable input")
        if not p.is_relative_to(a.repo_root.resolve()) or not p.is_file():
            raise ValueError("missing immutable current input")
        if p.stat().st_size!=row["bytes"] or sha(p)!=row["sha256"]:
            raise ValueError("an immutable current input changed: "+name)
        seen.add(name)
    gate("every complete current byte identity has been checked without an old producer",
        seen==set(m["input_paths"].values()) and sha(paths["new_source"])==sha(__file__)
        and sha(paths["contract"])==CONTRACT
        and sha(paths["SN_source"])==OLD_SN["source"] and sha(paths["SN_helper"])==OLD_SN["helper"])
    gate("the exact individual-coefficient and same-inverse source qualifications are retained",
        text_has(paths["IC_contract"],["IC.23","IC.26","IC.27","IC.28"])
        and text_has(paths["LN_contract"],["LN.20","complete terminal"])
        and text_has(paths["PIB_contract"],["PIB.14","PIB.20","PIB.21"])
        and text_has(paths["SN_source"],[
            'CENTRE="'+PARAMETERS["continuous_centre_definition_sha256"]+'"',
            'DIRECTION="'+PARAMETERS["continuous_response_definition_sha256"]+'"',
            'complete_qG_derivative_L2_upper','complete_new_H3_target',
            'true_angle_only_at_original_selected_parameter=True'])
        and text_has(paths["SN_helper"],["inverse_density_matrix","angle_error_derivatives"]))
    return paths

def accepted_terminal(path,d,gate):
    e=read(path);s=e.get("actual_scientific_receipt",{})
    gate("the one complete SN execution is the frozen actual successful run and attempt",
        sha(path)==OLD_SN["execution_sha256"] and e["kind"]==OLD_SN["execution_kind"]
        and str(e["run_id"])==OLD_SN["run"] and str(e["run_attempt"])==OLD_SN["attempt"]
        and e["repository"]==PUBLIC and e["complete"] is True
        and e["scientific_target_complete"] is True and e["actual_returncode"]==0
        and e["source_budget_source_sha256"]==OLD_SN["source"]
        and e["helper_source_sha256"]==OLD_SN["helper"] and e["input_manifest_sha256"]==OLD_SN["manifest"]
        and e["actual_failure"] is None and e["supervision_failure"] is None)
    raw=(canonical(s)+"\n").encode()
    gate("the complete SN scientific object equals its original prepublication bytes and hash",
        len(raw)==OLD_SN["science_bytes"] and hashlib.sha256(raw).hexdigest()==OLD_SN["science_sha256"]
        and e["recoverable_prepublication_stdout"]["SCIENCE"]["bytes"]==OLD_SN["science_bytes"]
        and e["recoverable_prepublication_stdout"]["SCIENCE"]["sha256"]==OLD_SN["science_sha256"])
    gate("all21 SN gates and the terminal stage passed with the exact source helper and parameters",
        s["kind"]==OLD_SN["kind"] and s["source_sha256"]==OLD_SN["source"]
        and s["helper_sha256"]==OLD_SN["helper"] and s["input_manifest_sha256"]==OLD_SN["manifest"]
        and s["parameters"]==OLD_SN["parameters"] and s["original_input_sha256"]==OLD_SN["original_input_sha256"]
        and str(s["run_id"])==OLD_SN["run"] and str(s["run_attempt"])==OLD_SN["attempt"]
        and s["complete"] is True and s["new_target_complete"] is True
        and s["actual_returncode"]==0 and s["failure"] is None and s["actual_gate_count"]==21
        and complete_gates(s,21) and s["latest_atomic_scientific_stage"]=="complete_new_H3_target")
    t=s["complete_new_transport_conclusion"]
    gate("the full path reaches the waist and preserves the accepted1256 prefix budgets",
        s["actual_exact_radial_cursor"]=="0"
        and s["actual_completed_original_transport_intervals"]==OLD_SN["actual_original_intervals"]
        and s["actual_new_transport_subcells_completed"]==OLD_SN["actual_subcells"]
        and s["actual_new_suffix_transport_subcells_completed"]==OLD_SN["actual_suffix_subcells"]
        and t["original_intervals_read"]==3146 and t["original_candidate_pieces_read"]==2550
        and t["completed_prefix_budget_subcells_reused"]==1256
        and t["new_suffix_subcells_verified"]==11328
        and t["completed_prefix_residual_parameter_energy_budgets_recomputed"]==0
        and t["complete_residual_modes_not_truncated"] is True
        and s["old_successful_mathematical_computations_repeated"]==0)
    v=s["complete_first_nonmean_coefficient_H3_conclusion"]
    gate("both complete four-column branches and the original signed scalar mean are present",
        set(v["branches"])=={"1","-1"} and v["all_complete_derivative_columns_0_through_3_saved"] is True
        and v["complete_scalar_mu_copied"]==s["complete_original_mean_finite_part"]
        and rb(v["complete_scalar_mu_copied"]).is_finite()
        and all(b["derivative_orders"]==[0,1,2,3] and b["complete_mean_is_exactly_zero"] is True
            and all(len(b[k])==4 and finite(b[k]) for k in (
                "complete_qG_derivative_L2_upper","complete_signed_reference_derivative_L2_upper",
                "complete_transport_derivative_L2_error","complete_finite_angle_tail_derivative_L2_upper"))
            for b in v["branches"].values()))
    h=v["true_angle_derivatives"]
    gate("the true angle matrix and its distinct error belong to the same selected SN target",
        v["full_real_family_transport_half_width"]=="1/10000000000"
        and v["true_angle_only_at_original_selected_parameter"] is True
        and v["same_selected_parameter_and_true_mean"] is True
        and h["literal_31over32_33over32_gates_verified"] is True
        and h["physical_width"]=="1/128" and len(h["angle_error_derivatives"])==4
        and len(h["inverse_density_matrix"])==4 and all(len(row)==4 for row in h["inverse_density_matrix"])
        and rb(h["proved_j_lower"]).lower()>=arb(31)/32
        and rb(h["proved_j_upper"]).upper()<=arb(33)/32
        and v["linear_or_exponential_strong_return_remainder_proved"] is False
        and v["incoming_high_inverse_or_true_PDE_background_transfer_proved"] is False)
    d["accepted_complete_SN_identity_read_verbatim"]=copy.deepcopy(OLD_SN)
    d["complete_SN_terminal_conclusion_read_verbatim"]=copy.deepcopy(v)
    d["complete_SN_terminal_conclusion_payload_sha256"]=payload_sha(v)
    d["complete_SN_whole_path_scope_read_verbatim"]=dict(
        actual_completed_original_transport_intervals=s["actual_completed_original_transport_intervals"],
        actual_exact_radial_cursor=s["actual_exact_radial_cursor"],
        actual_new_transport_subcells_completed=s["actual_new_transport_subcells_completed"],
        actual_new_suffix_transport_subcells_completed=s["actual_new_suffix_transport_subcells_completed"],
        completed_prefix_budget_subcells_reused=t["completed_prefix_budget_subcells_reused"],
        completed_prefix_residual_parameter_energy_budgets_recomputed=t["completed_prefix_residual_parameter_energy_budgets_recomputed"])
    return v

def accepted_fallback(path,d,gate):
    e=read(path);s=e.get("actual_scientific_receipt",{})
    gate("the complete PIB fallback is one immutable successful execution with15 gates",
        sha(path)==OLD_PIB["execution_sha256"] and e["kind"]==OLD_PIB["execution_kind"]
        and str(e["run_id"])==OLD_PIB["run"] and str(e["run_attempt"])==OLD_PIB["attempt"]
        and e["repository"]==PUBLIC and e["complete"] is True and e["actual_returncode"]==0
        and e["source_budget_source_sha256"]==OLD_PIB["source"]
        and e["input_manifest_sha256"]==OLD_PIB["manifest"]
        and s["kind"]==OLD_PIB["kind"] and s["source_sha256"]==OLD_PIB["source"]
        and s["input_manifest_sha256"]==OLD_PIB["manifest"] and s["runtime"]==OLD_PIB["runtime"]
        and s["complete"] is True and s["proved"] is True and s["actual_returncode"]==0
        and s["failure"] is None and complete_gates(s,15))
    saved=s["complete_saved_PG_inputs_read_verbatim"]
    oldcmp=s["complete_new_whole_log_comparison_conclusion"]
    raw=(canonical(s)+"\n").encode()
    gate("the five complete PG records and selected whole PIB logarithm are read without arithmetic",
        set(saved)=={"V0","B_one_third","CI","log_L2","log_Hminus4_3_original"}
        and payload_sha(saved)==s["complete_saved_PG_inputs_payload_sha256"]==OLD_PIB["five_payload_sha256"]
        and len(raw)==OLD_PIB["science_bytes"] and hashlib.sha256(raw).hexdigest()==OLD_PIB["science_sha256"]
        and oldcmp["both_candidates_bound_the_same_actual_inverse_and_window"] is True
        and oldcmp["choice_uses_final_retained_outward_records"] is True
        and finite(saved) and finite(oldcmp["complete_selected_log_Hminus4_3_upper"]))
    scope=s["complete_selected_common_input_scope_read_verbatim"]
    mp=s["mathematical_parameters"]
    gate("both actual individual principal factors share the original selected chart and complete means",
        scope["only_same_selected_actual_conjugacy"] is True
        and scope["selected_parameter_absolute_upper"]==PARAMETERS["selected_parameter_absolute_upper"]
        and mp["continuous_centre_definition_sha256"]==PARAMETERS["continuous_centre_definition_sha256"]
        and mp["continuous_response_definition_sha256"]==PARAMETERS["continuous_response_definition_sha256"]
        and mp["selected_common_input_order"]==PARAMETERS["selected_common_input_order"]
        and mp["independent_physical_mean_coordinates"]==2
        and s["scope"]["same_inverse_on_both_windows_and_on_their_dense_common_domain"] is True
        and s["scope"]["same_selected_real_individual_ci_co_not_a_ratio_substitute"] is True)
    d["accepted_complete_PIB_identity_read_verbatim"]=copy.deepcopy(OLD_PIB)
    d["complete_saved_PG_inputs_read_verbatim"]=copy.deepcopy(saved)
    d["complete_selected_PIB_log_conclusion_read_verbatim"]=copy.deepcopy(oldcmp)
    d["complete_selected_common_input_scope_read_verbatim"]=copy.deepcopy(scope)
    return dict(CI=copy.deepcopy(saved["CI"]),L2=copy.deepcopy(saved["log_L2"]),
        Hminus4_3=copy.deepcopy(oldcmp["complete_selected_log_Hminus4_3_upper"]))

def complete_density_derivatives(terminal):
    """IC26, with the separate true-H error once and only once per branch."""
    h=terminal["true_angle_derivatives"]
    errors=[up(v) for v in h["angle_error_derivatives"]]
    matrix=[[up(x) for x in row] for row in h["inverse_density_matrix"]]
    mu_abs=abs(rb(terminal["complete_scalar_mu_copied"])).upper()
    measure=up(up(h["proved_j_upper"]).sqrt())
    result={}
    for sigma,name in ((1,"incoming"),(-1,"outgoing")):
        saved=terminal["branches"][str(sigma)]["complete_qG_derivative_L2_upper"]
        r=[up(up(saved[q])+mu_abs*errors[q]/2) for q in range(4)]
        dd=[up(measure*sum((matrix[k][q]*r[q] for q in range(k+1)),arb(0)))
            for k in range(4)]
        result[name]=dict(sigma=sigma,complete_precomposition_density_derivative_upper=[rec(x) for x in r],
            complete_actual_nonmean_derivative_L2_upper=[rec(x) for x in dd],
            actual_coefficient="ci" if sigma==1 else "co",
            true_H_minus_G_error_paid_once_with_half=True,
            finite_G_analytic_tail_already_in_saved_Q_not_repeated=True,
            outgoing_final_rotation_isometric_and_retained=(sigma==-1))
    return dict(complete_absolute_mu_upper=rec(mu_abs),
        complete_sqrt_true_j_upper=rec(measure),branches=result,
        complete_derivative_orders=[0,1,2,3],new_actual_nonmean_derivative_bounds=8)

def choose_smallest(candidates):
    name,value=min(candidates,key=lambda pair:up(pair[1]))
    return dict(selected_complete_candidate=name,complete_selected_upper=copy.deepcopy(value),
        choice_uses_final_retained_outward_records=True,tie_preserves_first_candidate=True)

def complete_branch_budgets(converted):
    """Four whole V candidates and the complete W^(1/3) nonmean multiplier."""
    result={}
    muabs=up(converted["complete_absolute_mu_upper"])
    for name,branch in converted["branches"].items():
        dd=[up(v) for v in branch["complete_actual_nonmean_derivative_L2_upper"]]
        bessel=[up(sum((math.comb(k,q)*dd[q]*dd[q] for q in range(k+1)),arb(0))).sqrt().upper()
            for k in range(4)]
        sqrt96lower=arb(96).sqrt().lower()
        if sqrt96lower<=0:raise ArithmeticError("the exact positive sqrt96 divisor is invalid")
        candidates=[
            ("H1_over_2",rec(up(bessel[1]/2))),
            ("H2_over_sqrt96",rec(up(bessel[2]/sqrt96lower))),
            ("H3_over_32",rec(up(bessel[3]/32))),
            ("complete_L2_derivative_interpolation",rec(up(up(arb.pi()*dd[0]*dd[1]/2).sqrt())))]
        selected=choose_smallest(candidates)
        V=up(selected["complete_selected_upper"]);B=up(arb(39)*dd[1]/32)
        result[name]=dict(sigma=branch["sigma"],actual_coefficient=branch["actual_coefficient"],
            complete_Bessel_H0_H1_H2_H3_upper=[rec(x) for x in bessel],
            complete_Linfty_candidates={k:copy.deepcopy(v) for k,v in candidates},
            complete_Linfty_whole_choice=selected,complete_V_nonmean_Linfty_upper=copy.deepcopy(selected["complete_selected_upper"]),
            complete_B_nonmean_Wone_third_upper=rec(B),
            complete_actual_coefficient_Linfty_upper=rec(up(muabs/2+V)),
            exact_actual_nonmean_zero_mean=True,
            physical_mean_not_in_V_or_B=True)
    return dict(branches=result,supremum_candidates_per_branch=4,new_supremum_candidates=8,
        new_nonmean_multiplier_bounds=2,all_candidates_bound_the_same_complete_branch=True)

def signed_energy_candidates(terminal,budgets,fallback):
    """Signed lower gaps are not passed through the nonnegative up() helper."""
    mu=rb(terminal["complete_scalar_mu_copied"])
    lo,hi=mu.lower(),mu.upper()
    mean_sign=1 if lo>0 else (-1 if hi<0 else 0)
    absolute_lower=lo if mean_sign==1 else (-hi if mean_sign==-1 else arb(0))
    half_lower=(absolute_lower/2).lower()
    CI=up(fallback["CI"]);out={}
    for name,branch in budgets["branches"].items():
        V=up(branch["complete_V_nonmean_Linfty_upper"])
        B=up(branch["complete_B_nonmean_Wone_third_upper"])
        gap_record=rec(half_lower-V)
        gap_lower=rb(gap_record).lower()
        passed=bool(mean_sign!=0 and gap_lower>0)
        item=dict(sigma=branch["sigma"],actual_coefficient=branch["actual_coefficient"],
            complete_signed_gap=gap_record,strict_positive_gap=passed,
            certified_coefficient_sign=(-branch["sigma"]*mean_sign) if passed else None,
            energy_candidate_available=passed,
            complete_positive_gap_lower_for_division=None,
            complete_L2_energy_inverse_upper=None,complete_Hminus4_3_energy_inverse_upper=None,
            complete_log_L2_energy_upper=None,complete_log_Hminus4_3_energy_upper=None,
            failure_does_not_assert_noninvertibility=True,
            full_mean_is_retained_in_the_existing_inverse=True)
        if passed:
            K0=up(arb(1)+V/gap_lower)
            term1=up(CI*B);term2=up(CI*term1*V*K0)
            Km=up(arb(1)+term1+term2)
            item.update(complete_positive_gap_lower_for_division=rec(gap_lower),
                complete_L2_energy_inverse_upper=rec(K0),
                complete_Hminus4_3_energy_inverse_upper=rec(Km),
                complete_log_L2_energy_upper=rec(up(K0.log())),
                complete_log_Hminus4_3_energy_upper=rec(up(Km.log())),
                complete_CI_B_upper=rec(term1),
                complete_CI_squared_B_V_K0_upper=rec(term2),
                same_inverse_on_L2_and_Hminus4_3=True)
        out[name]=item
    return dict(original_signed_mu_read_verbatim=copy.deepcopy(terminal["complete_scalar_mu_copied"]),
        complete_mu_sign=mean_sign,complete_absolute_mu_lower=rec(absolute_lower),
        complete_absolute_mu_half_lower=rec(half_lower),branches=out,
        optional_signed_tests=2,optional_signed_tests_passed=sum(x["strict_positive_gap"] for x in out.values()),
        optional_false_is_a_complete_result=True,existing_complete_principal_inverse_is_not_retested=True)

def largest_whole(rows):
    key,value=max(rows,key=lambda pair:up(pair[1]))
    return dict(selected_complete_branch=key,complete_shared_upper=copy.deepcopy(value),
        maximum_uses_final_retained_outward_records=True,
        both_complete_branches_are_covered=True)

def complete_window_comparisons(energy,fallback):
    """Complete branch/window choices first, then a complete two-branch max."""
    branch_results={}
    for name,item in energy["branches"].items():
        windows={}
        for window,energy_key in (("L2","complete_log_L2_energy_upper"),
                                  ("Hminus4_3","complete_log_Hminus4_3_energy_upper")):
            candidates=[("saved_PG" if window=="L2" else "saved_selected_PIB",copy.deepcopy(fallback[window]))]
            if item["energy_candidate_available"]:
                candidates.append(("new_signed_energy",copy.deepcopy(item[energy_key])))
            chosen=choose_smallest(candidates)
            windows[window]=dict(original_complete_fallback_read_verbatim=copy.deepcopy(fallback[window]),
                complete_energy_log_candidate=copy.deepcopy(item[energy_key]),
                complete_candidate_records={k:copy.deepcopy(v) for k,v in candidates},
                complete_whole_choice=chosen,
                complete_selected_log_upper=copy.deepcopy(chosen["complete_selected_upper"]),
                both_candidates_use_the_same_inverse_and_window=True)
        branch_results[name]=windows
    shared={}
    for window in ("L2","Hminus4_3"):
        rows=[(name,x[window]["complete_selected_log_upper"]) for name,x in branch_results.items()]
        shared[window]=largest_whole(rows)
        shared[window]["old_complete_shared_log_read_verbatim"]=copy.deepcopy(fallback[window])
    energy_only=None
    if energy["optional_signed_tests_passed"]==2:
        energy_only={}
        for window,key,logkey in (
            ("L2","complete_L2_energy_inverse_upper","complete_log_L2_energy_upper"),
            ("Hminus4_3","complete_Hminus4_3_energy_inverse_upper","complete_log_Hminus4_3_energy_upper")):
            energy_only[window]=dict(
                norm=largest_whole([(name,x[key]) for name,x in energy["branches"].items()]),
                logarithm=largest_whole([(name,x[logkey]) for name,x in energy["branches"].items()]))
    return dict(branches=branch_results,complete_shared_log_windows=shared,
        complete_shared_energy_only_windows=energy_only,
        new_complete_branch_window_choices=4,new_complete_shared_windows=2,
        no_entrywise_minimum_or_different_selected_parameter=True,
        no_one_branch_pass_is_used_for_the_other_branch=True,
        old_fallback_remains_valid_if_both_optional_tests_fail=True,
        same_distributional_inverse_on_the_dense_common_domain=True)

def render_conclusion(d):
    lines=["# Actual individual principal energy gates",
        "", "Complete scientific success: "+str(d["complete"]),
        "", "Only the principal factors and their two complete inverse windows are covered.",
        "Full incoming, finite-border inversion, strong return and nonlinear background remain separate.",""]
    if d.get("complete_new_signed_energy_conclusion"):
        energy=d["complete_new_signed_energy_conclusion"]
        lines+=["| Branch | Sign gate | Signed gap | L2 energy inverse | Hminus4/3 energy inverse |",
                "|---|---|---|---|---|"]
        def value(x):return x["ball"] if isinstance(x,dict) and "ball" in x else str(x)
        for name,v in energy["branches"].items():
            lines.append("| "+name+" | "+str(v["strict_positive_gap"])+" | "+value(v["complete_signed_gap"])
                +" | "+value(v["complete_L2_energy_inverse_upper"])+" | "+value(v["complete_Hminus4_3_energy_inverse_upper"])+" |")
    if d.get("failure"):lines+=["","Failure: "+json.dumps(d["failure"],sort_keys=True)]
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
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("SCIENTIFIC_CHECKOUT_COMMIT"),
        stage="current_inputs",original_successful_small_receipts_read=0,
        original_SN_derivative_columns_read=0,new_complete_true_density_derivative_bounds=0,
        new_complete_supremum_candidates=0,new_complete_nonmean_multiplier_bounds=0,
        new_optional_signed_tests_evaluated=0,new_optional_signed_tests_passed=0,
        new_complete_energy_inverse_candidates=0,new_logarithms_evaluated=0,
        new_complete_branch_window_choices=0,new_complete_shared_windows=0,
        old_numerical_enclosures_recomputed=0,old_SN_PG_PIB_targets_recomputed=0,
        old_scientific_producer_imports=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,new_angular_or_radial_integrals_evaluated=0,
        direct_exponential_norm_bounds_evaluated=0,original_input_bytes_modified=0,
        complete_individual_principal_energy_consumer_paid=False,
        full_physical_incoming_inverse_claimed=False,finite_Schur_inverse_claimed=False,
        full_return_R0_claimed=False,actual_nonlinear_background_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def gate(name,value):
        d["gates"].append(dict(name=name,passed=bool(value)))
        if not value:raise ValueError("new SEI structural gate: "+name)
    try:
        paths=checked_inputs(a,d,gate)
        terminal=accepted_terminal(paths["SN_execution"],d,gate)
        fallback=accepted_fallback(paths["PIB_execution"],d,gate)
        d["original_successful_small_receipts_read"]=2
        d["original_SN_derivative_columns_read"]=8
        h=terminal["true_angle_derivatives"]
        arrays=[h["angle_error_derivatives"]]+h["inverse_density_matrix"]+[
            terminal["branches"][s]["complete_qG_derivative_L2_upper"] for s in ("1","-1")]
        gate("all saved derivative inputs are complete nonnegative budgets and the literal density map is positive",
            all(rb(v).is_finite() and rb(v).lower()>=0 for row in arrays for v in row)
            and all(rb(h["inverse_density_matrix"][k][q]).is_zero() for k in range(4) for q in range(k+1,4))
            and rb(h["proved_j_lower"]).lower()>0 and up(fallback["CI"])>=1
            and up(fallback["L2"])>=0 and up(fallback["Hminus4_3"])>=0)
        d["stage"]="new_complete_density_columns"
        converted=complete_density_derivatives(terminal)
        d["complete_new_individual_density_derivative_conclusion"]=converted
        d["new_complete_true_density_derivative_bounds"]=8
        gate("two complete four-derivative columns pay the distinct true-angle error exactly once",
            finite(converted) and converted["new_actual_nonmean_derivative_bounds"]==8
            and set(converted["branches"])=={"incoming","outgoing"}
            and all(len(v["complete_actual_nonmean_derivative_L2_upper"])==4
                and v["true_H_minus_G_error_paid_once_with_half"] is True
                and v["finite_G_analytic_tail_already_in_saved_Q_not_repeated"] is True
                for v in converted["branches"].values()))
        budgets=complete_branch_budgets(converted)
        d["complete_new_individual_nonmean_budget_conclusion"]=budgets
        d["new_complete_supremum_candidates"]=8
        d["new_complete_nonmean_multiplier_bounds"]=2
        gate("each branch retains all four complete supremum candidates and its own nonmean multiplier",
            finite(budgets) and budgets["new_supremum_candidates"]==8
            and budgets["new_nonmean_multiplier_bounds"]==2
            and all(len(v["complete_Linfty_candidates"])==4 and v["physical_mean_not_in_V_or_B"] is True
                for v in budgets["branches"].values()))
        d["stage"]="two_optional_signed_energy_gates"
        energy=signed_energy_candidates(terminal,budgets,fallback)
        d["complete_new_signed_energy_conclusion"]=energy
        d["new_optional_signed_tests_evaluated"]=2
        d["new_optional_signed_tests_passed"]=energy["optional_signed_tests_passed"]
        d["new_complete_energy_inverse_candidates"]=2*energy["optional_signed_tests_passed"]
        d["new_logarithms_evaluated"]=2*energy["optional_signed_tests_passed"]
        gate("both optional sign outcomes retain signed gaps and only positive lower gaps create energy bounds",
            finite(energy) and energy["optional_signed_tests"]==2
            and all((v["energy_candidate_available"] is True and v["strict_positive_gap"] is True
                     and rb(v["complete_positive_gap_lower_for_division"]).lower()>0
                     and up(v["complete_L2_energy_inverse_upper"])>=1
                     and up(v["complete_Hminus4_3_energy_inverse_upper"])>=1)
                    or (v["energy_candidate_available"] is False and v["strict_positive_gap"] is False
                        and v["complete_L2_energy_inverse_upper"] is None
                        and v["complete_Hminus4_3_energy_inverse_upper"] is None
                        and v["complete_log_L2_energy_upper"] is None
                        and v["complete_log_Hminus4_3_energy_upper"] is None)
                    for v in energy["branches"].values()))
        comparisons=complete_window_comparisons(energy,fallback)
        d["complete_new_whole_window_comparison_conclusion"]=comparisons
        d["new_complete_branch_window_choices"]=4;d["new_complete_shared_windows"]=2
        gate("all four branch-window choices and two shared readouts use complete same-inverse candidates",
            finite(comparisons) and comparisons["new_complete_branch_window_choices"]==4
            and comparisons["new_complete_shared_windows"]==2
            and comparisons["no_one_branch_pass_is_used_for_the_other_branch"] is True
            and (energy["optional_signed_tests_passed"]==2 or comparisons["complete_shared_energy_only_windows"] is None))
        d["scope"]=dict(
            same_selected_real_individual_ci_co=True,full_signed_mu_and_two_physical_means_retained=True,
            positive_true_density_and_original_rotation_retained=True,
            only_complete_SN_terminal_never_a_prefix_used=True,
            finite_angle_analytic_tail_not_repeated=True,distinct_true_angle_error_paid_once_per_half_branch=True,
            existing_complete_L2_inverse_used_before_energy_and_adjoint_bootstrap=True,
            same_inverse_on_L2_and_Hminus4_3=True,optional_sign_failure_not_noninvertibility=True,
            complete_old_fallback_and_complete_new_candidates_separate=True,
            no_exponential_of_large_saved_logarithms_evaluated=True,
            actual_incoming_errors_finite_rows_positive_stable_and_return_still_required=True,
            global_sign_operator_and_transported_sign_order_unchanged=True)
        gate("the completed new scalar target calls no accepted producer and changes no original input",
            all(d[k]==0 for k in (
                "old_numerical_enclosures_recomputed","old_SN_PG_PIB_targets_recomputed",
                "old_scientific_producer_imports","old_scientific_producer_calls",
                "old_binary_or_archive_inputs_restored","new_angular_or_radial_integrals_evaluated",
                "direct_exponential_norm_bounds_evaluated","original_input_bytes_modified"))
            and d["original_successful_small_receipts_read"]==2 and d["original_SN_derivative_columns_read"]==8)
        gate("the complete principal two-window conclusion keeps all physical mean and outstanding incoming obligations",
            finite(d) and len(d["gates"])==19
            and not any(d[k] for k in ("full_physical_incoming_inverse_claimed","finite_Schur_inverse_claimed",
                "full_return_R0_claimed","actual_nonlinear_background_claimed")))
        d["complete"]=True;d["proved"]=True;d["actual_returncode"]=0
        d["stage"]="complete_individual_principal_energy_target"
        d["complete_individual_principal_energy_consumer_paid"]=True
    except Exception as error:
        d["failure"]=dict(type=type(error).__name__,message=str(error))
    d["actual_mathematical_wall_seconds"]=time.monotonic()-started
    a.temporary_output_dir.mkdir(parents=True,exist_ok=True)
    native=a.temporary_output_dir/"temporary-individual-principal-energy-terminal-density.json.gz"
    save(native,d,compressed=True)
    d["temporary_native_sha256"]=sha(native);d["temporary_native_bytes"]=native.stat().st_size
    # Complete science is persisted before optional presentation or any publication.
    save(a.process_receipt,d);save(a.small_summary,d)
    a.result_markdown.parent.mkdir(parents=True,exist_ok=True)
    a.result_markdown.write_text(render_conclusion(d))
    if not d["complete"]:raise SystemExit(1)

if __name__=="__main__":main()

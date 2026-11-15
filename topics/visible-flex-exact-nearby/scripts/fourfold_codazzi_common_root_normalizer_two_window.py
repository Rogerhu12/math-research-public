#!/usr/bin/env python3
"""New complete common root normalizer from two completed small records."""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.metadata
import json
import os
import platform
import time
import traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_common_root_normalizer_two_window.py"
KIND="actual_common_root_normalizer_two_window_v1"
MANIFEST_KIND="common_root_normalizer_two_window_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=14
PINNED={"wl_execution":"936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d","fa_science":"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2","tf_contract":"652a9a2c2a9e0ccce1b07adae8848837ba579bec63d6ba5da21989a24b1bf5a3","metric_contract":"92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635","wl_contract":"e2e9d6d4dc98c8f0b2d9c6c5cc7700a3389d228c39470736f3a8706dccbd192e","fa_contract":"24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af","fa_algorithm":"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954","pf_contract":"5856c8cf5fac8c75997a6e3d8c9aba1ad88cb136d1ae184985164d1745aab026","ic_contract":"4164e4a7a10db651654cf63b7ecf7772fc1ba2cb966da4f9347711156301ddee"}
PARAMETERS={"arithmetic_bits":320,"runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"exact_real_delta_radius":"1/100000000","fixed_intrinsic_parameter":"eta_0","continuous_centre_definition_sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47","continuous_response_definition_sha256":"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04","exact_strict_cut":"76285779072683/320000000000000","exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"exact_metric_support":["1/20","9/50"],"original_WL_parameter_radius":"1/10000000000","chosen_complete_state_A0":{"centre":"7","response":"19"},"physical_frequency":"n=4|j|","root_coefficient_degree":192,"original_root_coefficient":"F_star=beta_star*u_star*v_star/eta_star","root_cutoff_rule":"smallest power of two J>=256 with J>=4*F_A_upper","required_root_cutoff":"J>=max(192,97,ceil(4*F_A_upper))","complete_windows":["L2","H^(-4/3)"],"independent_physical_means":2,"eta_lower_scope":"original full complex coefficient domain c[em], including the root","old_fold_majorants_stage_sha256":"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144","original_input_order":"L_sigma T_F_inverse; no factor commutation","finite_original_support_offset":191,"finite_rows_after_right_inverse_are_not_asserted_finite_input":True,"two_primitive_intermediate_window":"H^(-1/3)","complete_finite_fee_retained":True,"missing_C_sigma_or_E_sigma_supplied":False,"old_successful_producer_calls":0,"old_native_binary_or_archive_restored":0,"expected_gate_count":14,"full_incoming_finite_Schur_or_actual_solution_claimed":False}
EXPECTED={"wl_execution":{"run":"43749764738","gates":18,"kind":"actual_complete_waist_lifting_from_saved_positive_algorithm_v1","source":"d6764c570b935ed760425b10aeead6dea20e406fa0a0e606c1e61ad0c027d3b6","manifest":"70c8488c51d5e930b333108fd6ee0d091bd270cf5720871e813b53da13c12e43"},"fa_science":{"run":"43763658978","gates":24,"kind":"actual_complete_free_Airy_first_omitted_cut_scalars_v1","source":"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954","manifest":"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b"}}

def canonical(x):
    return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode("utf-8")
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def q(x):
    x=Fraction(x)
    return arb(x.numerator)/x.denominator
def box(x):
    if isinstance(x,dict):
        if "lower" in x and "upper" in x:
            y=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
        elif "ball" in x:y=arb(x["ball"])
        else:raise ValueError("saved scalar has no complete directed representation")
    else:y=arb(str(x))
    if not y.is_finite():raise ValueError("nonfinite saved scalar")
    return y
def up(x):
    y=box(x) if isinstance(x,dict) else arb(x)
    if not y.is_finite():raise ValueError("nonfinite directed upper")
    return y.upper()
def positive_lower(x):
    y=box(x).lower()
    if not y>0:raise ValueError("required full saved positive lower bound failed")
    return y
def nonnegative_upper(x):
    y=up(x)
    if not y>=0:raise ValueError("required nonnegative upper bound failed")
    return y
def record(x):
    y=arb(x)
    if not y.is_finite():raise ValueError("nonfinite new scalar")
    return {"ball":y.str(72)}
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("common root normalizer gate failed: "+name)
def successful(x,info):
    return (x.get("kind")==info["kind"] and x.get("complete") is True
        and x.get("proved") is True and x.get("actual_returncode")==0
        and x.get("failure") is None and str(x.get("run_id"))==info["run"]
        and str(x.get("run_attempt"))=="1"
        and x.get("source_sha256")==info["source"]
        and x.get("input_manifest_sha256")==info["manifest"]
        and len(x.get("gates",[]))==info["gates"]
        and all(z.get("passed") is True for z in x["gates"]))
def receipt(path,execution):
    raw=read(path)
    if execution:
        if (raw.get("complete") is not True or raw.get("actual_returncode")!=0
            or raw.get("actual_failure") is not None):
            raise ValueError("original wrapper did not complete")
        return raw,raw["actual_scientific_receipt"]
    return None,raw


def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),
            "python_flint":importlib.metadata.version("python-flint")}
    gate(doc,"public pinned runtime and320-bit directed scalar arithmetic",
         actual==RUNTIME and a.bits==320 and ctx.prec==320
         and os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==PUBLIC)
    doc["runtime"]=actual
    m=read(a.manifest)
    paths={role:Path(getattr(a,role)) for role in PINNED}
    gate(doc,"current-only closure source parameters and every immutable small input",
         sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
         and m.get("public_repository")==PUBLIC
         and m.get("source_sha256")==sha(__file__)
         and m.get("parameters")==PARAMETERS
         and m.get("mathematical_input_sha256")==PINNED
         and m.get("expected_actual_gate_count")==GATE_COUNT
         and all(sha(paths[k])==v for k,v in PINNED.items()))
    ew,wl=receipt(paths["wl_execution"],True)
    gate(doc,"WL completed original eighteen-gate full positive algorithm receipt",
         successful(wl,EXPECTED["wl_execution"])
         and ew.get("source_budget_source_sha256")==wl["source_sha256"]
         and wl.get("runtime")==RUNTIME)
    wo=wl["complete_original_input_conclusion"]
    wp=wl["complete_positive_product_conclusion"]
    gate(doc,"WL positive beta product and full mean complete7/19 keep their original smaller radius",
         wo.get("background_definition_sha256")==PARAMETERS["continuous_centre_definition_sha256"]
         and wo.get("direction_definition_sha256")==PARAMETERS["continuous_response_definition_sha256"]
         and wo.get("complete_core_exact_measure")=="9/10"
         and wo.get("complete_original_rows")==7721
         and wo.get("complete_original_parts")==40
         and wo.get("compact_support")==PARAMETERS["exact_metric_support"]
         and wo.get("chosen_global_constants")=={
             "background_pair_A0":"7","background_pair_angle_A0":"6",
             "response_pair_A0":"19","response_pair_angle_A0":"83"}
         and wl["mathematical_parameters"]["exact_parameter_half_width"]
             ==PARAMETERS["original_WL_parameter_radius"]
         and wl["mathematical_parameters"].get("full_even_mean_retained") is True
         and wp.get("same_original_positive_algorithm_lower_summands_used") is True
         and wp.get("no_abstract_operator_norm_reverse_inference") is True
         and wp.get("B_star_scope")=="absolute beta times max(1,absolute K_delta), uniformly on the whole core")
    _,fa=receipt(paths["fa_science"],False)
    gate(doc,"FA2 completed original twenty-four-gate full complex coefficient readout",
         successful(fa,EXPECTED["fa_science"])
         and fa.get("runtime")==dict(RUNTIME,arithmetic_bits=320)
         and fa.get("complete_free_cut_strong_bound_proved") is True
         and fa["mathematical_parameters"].get("exact_real_delta_radius")==PARAMETERS["exact_real_delta_radius"]
         and fa["mathematical_parameters"].get("fixed_intrinsic_parameter")=="eta_0"
         and fa["mathematical_parameters"].get("exact_strict_cut")==PARAMETERS["exact_strict_cut"]
         and fa["mathematical_parameters"].get("exact_root_interval")==PARAMETERS["exact_root_interval"]
         and fa["mathematical_parameters"].get("complete_physical_means_and_intermediate_projection_ranks_retained") is True)
    domain=fa["complete_new_cut_domain_conclusion"]
    rr=fa["complete_saved_cut_receiver_conclusion"]["RR_ng_q_and_means_read_verbatim"]
    root=rr["root_mean_value_q_bounds"]
    algorithm=paths["fa_algorithm"].read_text()
    gate(doc,"eta lower comes from the original full coefficient domain c[em] and not cut-only row790",
         fa["input_sha256"].get("old_fold_majorants_stage")==PARAMETERS["old_fold_majorants_stage_sha256"]
         and fa["source_sha256"]==PINNED["fa_algorithm"]
         and fa["mathematical_parameters"].get("exact_fold_radius")=="3/8000"
         and fa["mathematical_parameters"].get("exact_fold_strip")=="3/128"
         and fa["mathematical_parameters"].get("exact_coefficient_strip")=="1/32"
         and root.get("whole_segment_in_one_original_germ") is True
         and rr.get("both_mean_coordinates_retained") is True
         and 'em=positive_lower(c["em"],"original full complex eta lower")' in algorithm
         and '"complete_eta_full_complex_lower":em' in algorithm
         and "complete_eta_full_complex_lower" in domain)
    rc=Fraction(PARAMETERS["exact_strict_cut"])
    rlo,rhi=map(Fraction,PARAMETERS["exact_root_interval"])
    texts={k:paths[k].read_text() for k in PINNED if k.endswith("contract")}
    required={"tf_contract":["TF.7","TF.11","TF.13","TF.15","TF.18","TF.20"],
        "metric_contract":["D.2","[1/20,9/50]"],
        "wl_contract":["WL.2","WL.8"],
        "fa_contract":["FA.21","FA.28"],
        "pf_contract":["PF.15","PF.20a"],
        "ic_contract":["IC.3","IC.4","IC.9","IC.11"]}
    gate(doc,"root support degree192 and original ordered finite and mean identities are pinned",
         Fraction(9,50)<rc<rlo<=rhi<Fraction(9,10)
         and all(all(token in texts[k] for token in tokens) for k,tokens in required.items()))
    doc["copied_complete_input_objects"]={
        "WL_original_input_conclusion":copy.deepcopy(wo),
        "WL_complete_positive_product_conclusion":copy.deepcopy(wp),
        "WL_original_parameters":copy.deepcopy(wl["mathematical_parameters"]),
        "FA_complete_new_cut_domain_conclusion":copy.deepcopy(domain),
        "FA_complete_root_mean_value_q_bounds":copy.deepcopy(root),
        "FA_original_parameters":copy.deepcopy(fa["mathematical_parameters"]),
        "FA_original_fold_stage_sha256":fa["input_sha256"]["old_fold_majorants_stage"]}
    doc["complete_original_receipt_identities"]={
        k:dict(v,actual_gate_count=len(s["gates"]),all_actual_gates_passed=True)
        for k,v,s in [("wl_execution",EXPECTED["wl_execution"],wl),
                      ("fa_science",EXPECTED["fa_science"],fa)]}
    doc["input_sha256"]=copy.deepcopy(PINNED)
    doc["input_manifest_sha256"]=a.manifest_sha
    doc["public_repository"]=PUBLIC
    doc["arithmetic_bits"]=a.bits
    return paths,dict(wp=wp,domain=domain)

def scalar_bounds(v,doc):
    B=nonnegative_upper(v["wp"]["B_star"])
    em=positive_lower(v["domain"]["complete_eta_full_complex_lower"])
    gate(doc,"the saved beta product and full-domain eta lower are valid directed endpoints",
         B>=0 and em>0)
    M=up(q(7)+q(19)*q(PARAMETERS["exact_real_delta_radius"]))
    FA=up(B*M*M/em)
    gate(doc,"the complete root coefficient including its mean has the new Wiener bound",
         M>0 and FA>=0 and PARAMETERS["root_coefficient_degree"]==192)
    # Integer doubling uses only the new outward F_A. No floating ceil is used.
    J=256
    doublings=0
    while not q(J)>=4*FA:
        J*=2
        doublings+=1
    gate(doc,"the recorded dyadic integer satisfies the full exact root cutoff inequality",
         J>=256 and J>=192 and J>=97 and (J&(J-1))==0 and q(J)>=4*FA)
    ratio=up(1+q(192)/J)
    mneg=up(FA*ratio**q(Fraction(4,3)))
    mthird=up(FA*ratio**q(Fraction(1,3)))
    theta0=up(FA/(4*J))
    thetaneg=up(mneg/(4*J))
    gap0=(1-theta0).lower()
    gapneg=(1-thetaneg).lower()
    gate(doc,"both strict Neumann gaps are positive for the same compressed operator",
         gap0>0 and gapneg>0 and theta0>=0 and thetaneg>=0)
    inv0=up(1/gap0)
    invneg=up(1/gapneg)
    forward0=up(1+theta0)
    forwardneg=up(1+thetaneg)
    gate(doc,"the complete theta bounds imply the rational two-window inverse and forward bounds",
         ratio<=2 and theta0<=q(Fraction(1,16))
         and thetaneg<q(Fraction(3,16)) and 16<27)
    N=J+PARAMETERS["finite_original_support_offset"]
    lamJ=up((q(1)+q(4*J)**2).sqrt())
    lamN=up((q(1)+q(4*N)**2).sqrt())
    CI=up(q(17).sqrt()/4)
    alpha=up(lamJ**q(Fraction(4,3))/(4*J)**2)
    two_before=up(alpha*mthird)
    two_after=up(two_before*invneg)
    finite_before=up(2*CI*FA*lamN**q(Fraction(1,3)))
    finite_after=up(finite_before*invneg)
    gate(doc,"complete finite dual rows and two-primitive costs retain the true middle window and right order",
         N==J+191 and all(x>=0 for x in (
             alpha,mthird,two_before,two_after,finite_before,finite_after))
         and PARAMETERS["two_primitive_intermediate_window"]=="H^(-1/3)"
         and PARAMETERS["independent_physical_means"]==2
         and PARAMETERS["finite_rows_after_right_inverse_are_not_asserted_finite_input"] is True
         and PARAMETERS["missing_C_sigma_or_E_sigma_supplied"] is False)
    doc["complete_new_root_coefficient_conclusion"]={
        "complete_state_M_upper":record(M),
        "complete_root_F_A0_upper":record(FA),
        "complete_WL_B_star_used_verbatim":copy.deepcopy(v["wp"]["B_star"]),
        "complete_original_eta_lower_used_verbatim":copy.deepcopy(v["domain"]["complete_eta_full_complex_lower"]),
        "exact_full_family_delta_radius":PARAMETERS["exact_real_delta_radius"],
        "angular_degree":192,"root_mean_and_both_Fourier_signs_retained":True,
        "old_WL_global_parameter_fee_not_extended":True,
        "original_full_complex_eta_domain_includes_root":True,
        "cut_only_row790_eta_not_used":True,"second_alpha_not_applied":True,
        "abstract_operator_upper_not_inverted":True}
    doc["complete_new_root_normalizer_conclusion"]={
        "actual_J_F":J,"exact_cutoff_rule":PARAMETERS["root_cutoff_rule"],
        "dyadic_doublings_from256":doublings,
        "complete_high_high_weight_ratio_upper":record(ratio),
        "complete_high_high_Hminus4_3_multiplier_upper":record(mneg),
        "complete_high_high_Hminus1_3_multiplier_upper":record(mthird),
        "complete_theta_L2_upper":record(theta0),
        "complete_theta_Hminus4_3_upper":record(thetaneg),
        "complete_gap_L2_lower":record(gap0),
        "complete_gap_Hminus4_3_lower":record(gapneg),
        "complete_inverse_L2_upper":record(inv0),
        "complete_inverse_Hminus4_3_upper":record(invneg),
        "complete_forward_L2_upper":record(forward0),
        "complete_forward_Hminus4_3_upper":record(forwardneg),
        "exact_universal_theta_L2_upper":"1/16",
        "exact_strict_universal_theta_Hminus4_3_upper":"3/16",
        "exact_universal_inverse_L2_upper":"16/15",
        "exact_universal_inverse_Hminus4_3_upper":"16/13",
        "exact_universal_forward_L2_upper":"17/16",
        "exact_universal_forward_Hminus4_3_upper":"19/16",
        "same_inverse_on_both_windows":True,
        "below_J_F_and_independent_mean_ports_are_identity":True,
        "root_cutoff_is_not_moving_Js_or_principal_angle_cutoff":True,
        "finite_original_input_and_output_support_abs_j":N,
        "right_transformed_finite_rows_keep_actual_dual_norms":True,
        "right_transformed_finite_input_support_not_claimed":True}
    doc["complete_new_strong_scalar_factors"]={
        "complete_alpha_J_upper":record(alpha),
        "complete_two_primitive_left_multiplier_fee_before_right_inverse":record(two_before),
        "complete_two_primitive_left_multiplier_fee_after_right_inverse":record(two_after),
        "complete_finite_map_fee_before_right_inverse":record(finite_before),
        "complete_finite_map_fee_after_right_inverse":record(finite_after),
        "two_primitive_fee_requires_separate_complete_tilde_C_supremum":True,
        "finite_fee_is_one_complete_branch_fee_with_full_mean":True,
        "exact_order":"(E_sigma-M_tildeC_sigma I A_F) T_F_inverse + F_J T_F_inverse",
        "complete_E_sigma_or_C_sigma_not_inferred":True,
        "finite_rank_is_not_a_finite_inverse":True}

def run(a,doc):
    ctx.prec=a.bits
    paths,v=checked_inputs(a,doc)
    scalar_bounds(v,doc)
    gate(doc,"all fourteen gates preserve complete original inputs and zero old scientific calls",
         len(doc["gates"])==13 and all(g["passed"] is True for g in doc["gates"])
         and all(sha(paths[k])==val for k,val in PINNED.items()))
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("complete gate inventory changed")
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_common_root_normalizer_proved=True,
        original_completed_scientific_receipts_read=2,
        new_complete_root_coefficient_bound_count=1,
        new_complete_chosen_root_cutoff_count=1,
        new_complete_inverse_window_count=2,
        old_WL_FA_fold_state_root_or_ray_calls=0,
        old_binary_archive_or_native_restored=0,old_scientific_source_imports=0,
        original_input_bytes_modified=False,new_recomputable_arrays_persisted=False,
        independent_physical_mean_coordinates=2,
        full_incoming_inverse_proved=False,finite_Schur_inverse_proved=False,
        actual_nonlinear_background_proved=False,final_surface_proved=False)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    for role in PINNED:p.add_argument("--"+role.replace("_","-"),type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every existing complete orpartial conclusion")
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,
       failure=None,gates=[],source_sha256=sha(__file__),parameters=PARAMETERS,
       public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
       run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
       workflow_event_commit=os.environ.get("GITHUB_SHA"),
       actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"))
    try:run(a,doc)
    except Exception as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(error_type=type(error).__name__,message=str(error)))
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
    raw=canonical(doc)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    temp=a.out.with_name(a.out.name+".partial");temp.write_bytes(raw);temp.replace(a.out)
    print("COMMON_ROOT_NORMALIZER_TWO_WINDOW_SCIENTIFIC_RESULT_BEGIN",flush=True)
    print(json.dumps(dict(bytes=len(raw),sha256=sha_bytes(raw)),sort_keys=True),flush=True)
    print(raw.decode(),end="",flush=True)
    print("COMMON_ROOT_NORMALIZER_TWO_WINDOW_SCIENTIFIC_RESULT_END",flush=True)
    if len(raw)>30000:raise ValueError("saved complete root normalizer science exceeds30000bytes")
    return doc["actual_returncode"]

if __name__=="__main__":raise SystemExit(main())
